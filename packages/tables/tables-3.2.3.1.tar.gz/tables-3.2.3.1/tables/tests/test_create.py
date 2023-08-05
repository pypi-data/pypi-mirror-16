# -*- coding: utf-8 -*-

"""This test unit checks object creation funtions, like open_file,
create_table, create_array or create_group.

It also checks:

- name identifiers in tree objects
- title character limit for objects (255)
- limit in number in table fields (255)

"""

from __future__ import print_function
import os
import sys
import hashlib
import tempfile
import warnings
from distutils.version import LooseVersion

import numpy

import tables
from tables import (
    Group, Leaf, Table, Array, hdf5_version, Filters,
    StringAtom, Int16Atom, Int64Atom, Float32Atom, Float64Atom,
    Col, StringCol, IntCol, Int16Col, FloatCol, Float32Col,
)
from tables.parameters import MAX_COLUMNS
from tables.hdf5extension import HAVE_DIRECT_DRIVER, HAVE_WINDOWS_DRIVER
from tables.utils import quantize
from tables.tests import common
from tables.tests.common import unittest
from tables.tests.common import PyTablesTestCase as TestCase


hdf5_version = LooseVersion(hdf5_version)


class Record(tables.IsDescription):
    var1 = StringCol(itemsize=4)  # 4-character String
    var2 = IntCol()               # integer
    var3 = Int16Col()             # short integer
    var4 = FloatCol()             # double (double-precision)
    var5 = Float32Col()           # float  (single-precision)


class CreateTestCase(common.TempFileMixin, TestCase):
    title = "This is the table title"
    expectedrows = 100
    maxshort = 2 ** 15
    maxint = 2147483648   # (2 ** 31)
    compress = 0

    def setUp(self):
        super(CreateTestCase, self).setUp()

        # Create an instance of HDF5 Table
        self.root = self.h5file.root

        # Create a table object
        self.table = self.h5file.create_table(self.root, 'atable',
                                              Record, "Table title")
        # Create an array object
        self.array = self.h5file.create_array(self.root, 'anarray',
                                              [1], "Array title")
        # Create a group object
        self.group = self.h5file.create_group(self.root, 'agroup',
                                              "Group title")

    def test00_isClass(self):
        """Testing table creation."""

        self.assertTrue(isinstance(self.table, Table))
        self.assertTrue(isinstance(self.array, Array))
        self.assertTrue(isinstance(self.array, Leaf))
        self.assertTrue(isinstance(self.group, Group))

    def test01_overwriteNode(self):
        """Checking protection against node overwriting."""

        try:
            self.array = self.h5file.create_array(self.root, 'anarray',
                                                  [1], "Array title")
        except tables.NodeError:
            if common.verbose:
                (type, value, traceback) = sys.exc_info()
                print("\nGreat!, the next NameError was catched!")
                print(value)
        else:
            self.fail("expected a tables.NodeError")

    def test02_syntaxname(self):
        """Checking syntax in object tree names."""

        with self.assertWarns(tables.NaturalNameWarning):
            self.array = self.h5file.create_array(self.root, ' array',
                                                  [1], "Array title")

        # another name error
        with self.assertWarns(tables.NaturalNameWarning):
            self.array = self.h5file.create_array(self.root, '$array',
                                                  [1], "Array title")

        # Finally, test a reserved word
        with self.assertWarns(tables.NaturalNameWarning):
            self.array = self.h5file.create_array(self.root, 'for',
                                                  [1], "Array title")

    def test03a_titleAttr(self):
        """Checking the self.title attr in nodes."""

        # Close the opened file to destroy the object tree
        self._reopen()

        # Now, test that self.title exists and is correct in all the nodes
        self.assertEqual(self.h5file.root.agroup._v_title, "Group title")
        self.assertEqual(self.h5file.root.atable.title, "Table title")
        self.assertEqual(self.h5file.root.anarray.title, "Array title")

    def test03b_titleLength(self):
        """Checking large title character length limit (1023)"""

        titlelength = 1023
        # Try to put a very long title on a group object
        group = self.h5file.create_group(self.root, 'group', "t" * titlelength)
        self.assertEqual(group._v_title, "t" * titlelength)
        self.assertEqual(group._f_getattr('TITLE'), "t" * titlelength)

        # Now, try with a table object
        table = self.h5file.create_table(self.root, 'table',
                                         Record, "t" * titlelength)
        self.assertEqual(table.title, "t" * titlelength)
        self.assertEqual(table.get_attr("TITLE"), "t" * titlelength)

        # Finally, try with an Array object
        arr = self.h5file.create_array(self.root, 'arr',
                                       [1], "t" * titlelength)
        self.assertEqual(arr.title, "t" * titlelength)
        self.assertEqual(arr.get_attr("TITLE"), "t" * titlelength)

    def test04_maxFields(self):
        """Checking a large number of fields in tables"""

        # The number of fields for a table
        varnumber = MAX_COLUMNS

        varnames = []
        for i in range(varnumber):
            varnames.append('int%d' % i)

        # Build a dictionary with the types as values and varnames as keys
        recordDict = {}
        i = 0
        for varname in varnames:
            recordDict[varname] = Col.from_type("int32", dflt=1, pos=i)
            i += 1
        # Append this entry to indicate the alignment!
        recordDict['_v_align'] = "="
        table = self.h5file.create_table(self.root, 'table',
                                         recordDict, "MetaRecord instance")
        row = table.row
        listrows = []
        # Write 10 records
        for j in range(10):
            rowlist = []
            for i in range(len(table.colnames)):
                row[varnames[i]] = i * j
                rowlist.append(i * j)

            row.append()
            listrows.append(tuple(rowlist))

        # write data on disk
        table.flush()

        # Read all the data as a list
        listout = table.read().tolist()

        # Compare the input rowlist and output row list. They should
        # be equal.
        if common.verbose:
            print("Original row list:", listrows[-1])
            print("Retrieved row list:", listout[-1])
        self.assertEqual(listrows, listout)

    # The next limitation has been released. A warning is still there, though
    def test05_maxFieldsExceeded(self):
        """Checking an excess of the maximum number of fields in tables"""

        # The number of fields for a table
        varnumber = MAX_COLUMNS + 1

        varnames = []
        for i in range(varnumber):
            varnames.append('int%d' % i)

        # Build a dictionary with the types as values and varnames as keys
        recordDict = {}
        i = 0
        for varname in varnames:
            recordDict[varname] = Col.from_type("int32", dflt=1)
            i += 1

        # Now, create a table with this record object
        # This way of creating node objects has been deprecated
        # table = Table(recordDict, "MetaRecord instance")

        # Attach the table to object tree
        warnings.filterwarnings("error", category=tables.PerformanceWarning)
        # Here, a tables.PerformanceWarning should be raised!
        try:
            self.h5file.create_table(self.root, 'table',
                                     recordDict, "MetaRecord instance")
        except tables.PerformanceWarning:
            if common.verbose:
                (type, value, traceback) = sys.exc_info()
                print("\nGreat!, the next PerformanceWarning was catched!")
                print(value)
        else:
            self.fail("expected an tables.PerformanceWarning")
        # Reset the warning
        warnings.filterwarnings("default", category=tables.PerformanceWarning)

    # The next limitation has been released
    def _test06_maxColumnNameLengthExceeded(self):
        """Checking an excess (256) of the maximum length in column names"""

        # Build a dictionary with the types as values and varnames as keys
        recordDict = {}
        recordDict["a" * 255] = IntCol(dflt=1)
        recordDict["b" * 256] = IntCol(dflt=1)  # Should trigger a ValueError

        # Now, create a table with this record object
        # This way of creating node objects has been deprecated
        table = Table(recordDict, "MetaRecord instance")
        self.assertTrue(table is not None)

        # Attach the table to object tree
        # Here, ValueError should be raised!
        with self.assertRaises(ValueError):
            self.h5file.create_table(self.root, 'table',
                                     recordDict, "MetaRecord instance")

    def test06_noMaxColumnNameLength(self):
        """Checking unlimited length in column names"""

        # Build a dictionary with the types as values and varnames as keys
        recordDict = {}
        recordDict["a" * 255] = IntCol(dflt=1, pos=0)
        recordDict["b" * 1024] = IntCol(dflt=1, pos=1)  # Should work well

        # Attach the table to object tree
        # Here, IndexError should be raised!
        table = self.h5file.create_table(self.root, 'table',
                                         recordDict, "MetaRecord instance")
        self.assertEqual(table.colnames[0], "a" * 255)
        self.assertEqual(table.colnames[1], "b" * 1024)


class Record2(tables.IsDescription):
    var1 = StringCol(itemsize=4)  # 4-character String
    var2 = IntCol()               # integer
    var3 = Int16Col()             # short integer


class FiltersTreeTestCase(common.TempFileMixin, TestCase):
    title = "A title"
    nrows = 10

    def setUp(self):
        super(FiltersTreeTestCase, self).setUp()
        self.populateFile()

    def populateFile(self):
        group = self.h5file.root
        # Create a tree with three levels of depth
        for j in range(5):
            # Create a table
            table = self.h5file.create_table(group, 'table1', Record2,
                                             title=self.title,
                                             filters=None)
            # Get the record object associated with the new table
            d = table.row
            # Fill the table
            for i in xrange(self.nrows):
                d['var1'] = '%04d' % (self.nrows - i)
                d['var2'] = i
                d['var3'] = i * 2
                d.append()      # This injects the Record values
            # Flush the buffer for this table
            table.flush()

            # Create a couple of arrays in each group
            var1List = [x['var1'] for x in table.iterrows()]
            var3List = [x['var3'] for x in table.iterrows()]

            self.h5file.create_array(group, 'array1', var1List, "col 1")
            self.h5file.create_array(group, 'array2', var3List, "col 3")

            # Create a couple of EArrays as well
            ea1 = self.h5file.create_earray(group, 'earray1',
                                            StringAtom(itemsize=4), (0,),
                                            "col 1")
            ea2 = self.h5file.create_earray(group, 'earray2',
                                            Int16Atom(), (0,), "col 3")
            # And fill them with some values
            ea1.append(var1List)
            ea2.append(var3List)

            # Finally a couple of VLArrays too
            vla1 = self.h5file.create_vlarray(group, 'vlarray1',
                                              StringAtom(itemsize=4), "col 1")
            vla2 = self.h5file.create_vlarray(group, 'vlarray2',
                                              Int16Atom(), "col 3")
            # And fill them with some values
            vla1.append(var1List)
            vla2.append(var3List)

            # Create a new group (descendant of group)
            if j == 1:  # The second level
                group2 = self.h5file.create_group(group, 'group' + str(j),
                                                  filters=self.gfilters)
            elif j == 2:  # third level
                group2 = self.h5file.create_group(group, 'group' + str(j))
            else:   # The rest of levels
                group2 = self.h5file.create_group(group, 'group' + str(j),
                                                  filters=self.filters)
            # Iterate over this new group (group2)
            group = group2

    def test00_checkFilters(self):
        """Checking inheritance of filters on trees (open file version)"""

        if common.verbose:
            print('\n', '-=' * 30)
            print("Running %s.test00_checkFilters..." %
                  self.__class__.__name__)

        # First level check
        if common.verbose:
            print("Test filter:", repr(self.filters))
            print("Filters in file:", repr(self.h5file.filters))

        if self.filters is None:
            filters = Filters()
        else:
            filters = self.filters
        self.assertEqual(repr(filters), repr(self.h5file.filters))

        # The next nodes have to have the same filter properties as
        # self.filters
        nodelist = [
            '/table1', '/group0/earray1', '/group0/vlarray1', '/group0',
        ]
        for node in nodelist:
            obj = self.h5file.get_node(node)
            if isinstance(obj, Group):
                self.assertEqual(repr(filters), repr(obj._v_filters))
            else:
                self.assertEqual(repr(filters), repr(obj.filters))

        # Second and third level check
        group1 = self.h5file.root.group0.group1
        if self.gfilters is None:
            if self.filters is None:
                gfilters = Filters()
            else:
                gfilters = self.filters
        else:
            gfilters = self.gfilters
        if common.verbose:
            print("Test gfilter:", repr(gfilters))
            print("Filters in file:", repr(group1._v_filters))

        self.assertEqual(repr(gfilters), repr(group1._v_filters))

        # The next nodes have to have the same filter properties as
        # gfilters
        nodelist = [
            '/group0/group1', '/group0/group1/earray1',
            '/group0/group1/vlarray1',
            '/group0/group1/table1', '/group0/group1/group2/table1',
        ]
        for node in nodelist:
            obj = self.h5file.get_node(node)
            if isinstance(obj, Group):
                self.assertEqual(repr(gfilters), repr(obj._v_filters))
            else:
                self.assertEqual(repr(gfilters), repr(obj.filters))

        # Fourth and fifth level check
        if self.filters is None:
            # If None, the filters are inherited!
            if self.gfilters is None:
                filters = Filters()
            else:
                filters = self.gfilters
        else:
            filters = self.filters
        group3 = self.h5file.root.group0.group1.group2.group3
        if common.verbose:
            print("Test filter:", repr(filters))
            print("Filters in file:", repr(group3._v_filters))

        self.assertEqual(repr(filters), repr(group3._v_filters))

        # The next nodes have to have the same filter properties as
        # self.filter
        nodelist = [
            '/group0/group1/group2/group3',
            '/group0/group1/group2/group3/earray1',
            '/group0/group1/group2/group3/vlarray1',
            '/group0/group1/group2/group3/table1',
            '/group0/group1/group2/group3/group4',
        ]
        for node in nodelist:
            obj = self.h5file.get_node(node)
            if isinstance(obj, Group):
                self.assertEqual(repr(filters), repr(obj._v_filters))
            else:
                self.assertEqual(repr(filters), repr(obj.filters))

        # Checking the special case for Arrays in which the compression
        # should always be the empty Filter()
        # The next nodes have to have the same filter properties as
        # Filter()
        nodelist = [
            '/array1',
            '/group0/array1',
            '/group0/group1/array1',
            '/group0/group1/group2/array1',
            '/group0/group1/group2/group3/array1',
        ]
        for node in nodelist:
            obj = self.h5file.get_node(node)
            self.assertEqual(repr(Filters()), repr(obj.filters))

    def test01_checkFilters(self):
        """Checking inheritance of filters on trees (close file version)"""

        if common.verbose:
            print('\n', '-=' * 30)
            print("Running %s.test01_checkFilters..." %
                  self.__class__.__name__)

        # Close the file
        self._reopen()

        # First level check
        if self.filters is None:
            filters = Filters()
        else:
            filters = self.filters
        if common.verbose:
            print("Test filter:", repr(filters))
            print("Filters in file:", repr(self.h5file.filters))

        self.assertEqual(repr(filters), repr(self.h5file.filters))

        # The next nodes have to have the same filter properties as
        # self.filters
        nodelist = [
            '/table1', '/group0/earray1', '/group0/vlarray1', '/group0',
        ]
        for node in nodelist:
            object_ = self.h5file.get_node(node)
            if isinstance(object_, Group):
                self.assertEqual(repr(filters), repr(object_._v_filters))
            else:
                self.assertEqual(repr(filters), repr(object_.filters))

        # Second and third level check
        group1 = self.h5file.root.group0.group1
        if self.gfilters is None:
            if self.filters is None:
                gfilters = Filters()
            else:
                gfilters = self.filters
        else:
            gfilters = self.gfilters
        if common.verbose:
            print("Test filter:", repr(gfilters))
            print("Filters in file:", repr(group1._v_filters))

        self.assertEqual(repr(gfilters), repr(group1._v_filters))

        # The next nodes have to have the same filter properties as
        # gfilters
        nodelist = [
            '/group0/group1', '/group0/group1/earray1',
            '/group0/group1/vlarray1',
            '/group0/group1/table1', '/group0/group1/group2/table1',
        ]
        for node in nodelist:
            object_ = self.h5file.get_node(node)
            if isinstance(object_, Group):
                self.assertEqual(repr(gfilters), repr(object_._v_filters))
            else:
                self.assertEqual(repr(gfilters), repr(object_.filters))

        # Fourth and fifth level check
        if self.filters is None:
            if self.gfilters is None:
                filters = Filters()
            else:
                filters = self.gfilters
        else:
            filters = self.filters
        group3 = self.h5file.root.group0.group1.group2.group3
        if common.verbose:
            print("Test filter:", repr(filters))
            print("Filters in file:", repr(group3._v_filters))

        repr(filters) == repr(group3._v_filters)
        # The next nodes have to have the same filter properties as
        # self.filters
        nodelist = [
            '/group0/group1/group2/group3',
            '/group0/group1/group2/group3/earray1',
            '/group0/group1/group2/group3/vlarray1',
            '/group0/group1/group2/group3/table1',
            '/group0/group1/group2/group3/group4',
        ]
        for node in nodelist:
            obj = self.h5file.get_node(node)
            if isinstance(obj, Group):
                self.assertEqual(repr(filters), repr(obj._v_filters))
            else:
                self.assertEqual(repr(filters), repr(obj.filters))

        # Checking the special case for Arrays in which the compression
        # should always be the empty Filter()
        # The next nodes have to have the same filter properties as
        # Filter()
        nodelist = [
            '/array1',
            '/group0/array1',
            '/group0/group1/array1',
            '/group0/group1/group2/array1',
            '/group0/group1/group2/group3/array1',
        ]
        for node in nodelist:
            obj = self.h5file.get_node(node)
            self.assertEqual(repr(Filters()), repr(obj.filters))


class FiltersCase1(FiltersTreeTestCase):
    filters = Filters()
    gfilters = Filters(complevel=1)
    open_kwargs = dict(filters=filters)


@unittest.skipIf(not common.bzip2_avail,
                 'BZIP2 compression library not available')
class FiltersCase2(FiltersTreeTestCase):
    filters = Filters(complevel=1, complib="bzip2")
    gfilters = Filters(complevel=1)
    open_kwargs = dict(filters=filters)


@unittest.skipIf(not common.lzo_avail, 'LZO compression library not available')
class FiltersCase3(FiltersTreeTestCase):
    filters = Filters(shuffle=True, complib="zlib")
    gfilters = Filters(complevel=1, shuffle=False, complib="lzo")
    open_kwargs = dict(filters=filters)


class FiltersCase4(FiltersTreeTestCase):
    filters = Filters(shuffle=True)
    gfilters = Filters(complevel=1, shuffle=False)
    open_kwargs = dict(filters=filters)


class FiltersCase5(FiltersTreeTestCase):
    filters = Filters(fletcher32=True)
    gfilters = Filters(complevel=1, shuffle=False)
    open_kwargs = dict(filters=filters)


class FiltersCase6(FiltersTreeTestCase):
    filters = None
    gfilters = Filters(complevel=1, shuffle=False)
    open_kwargs = dict(filters=filters)


class FiltersCase7(FiltersTreeTestCase):
    filters = Filters(complevel=1)
    gfilters = None
    open_kwargs = dict(filters=filters)


class FiltersCase8(FiltersTreeTestCase):
    filters = None
    gfilters = None
    open_kwargs = dict(filters=filters)


@unittest.skipIf(not common.bzip2_avail,
                 'BZIP2 compression library not available')
class FiltersCase9(FiltersTreeTestCase):
    filters = Filters(shuffle=True, complib="zlib")
    gfilters = Filters(complevel=5, shuffle=True, complib="bzip2")
    open_kwargs = dict(filters=filters)


@unittest.skipIf(not common.blosc_avail,
                 'BLOSC compression library not available')
class FiltersCase10(FiltersTreeTestCase):
    filters = Filters(shuffle=False, complevel=1, complib="blosc")
    gfilters = Filters(complevel=5, shuffle=True, complib="blosc")
    open_kwargs = dict(filters=filters)


@unittest.skipIf(not common.blosc_avail,
                 'BLOSC compression library not available')
class FiltersCaseBloscBloscLZ(FiltersTreeTestCase):
    filters = Filters(shuffle=False, complevel=1, complib="blosc:blosclz")
    gfilters = Filters(complevel=5, shuffle=True, complib="blosc:blosclz")
    open_kwargs = dict(filters=filters)


@unittest.skipIf(not common.blosc_avail,
                 'BLOSC compression library not available')
@unittest.skipIf('lz4' not in tables.blosc_compressor_list(), 'lz4 required')
class FiltersCaseBloscLZ4(FiltersTreeTestCase):
    filters = Filters(shuffle=False, complevel=1, complib="blosc:lz4")
    gfilters = Filters(complevel=5, shuffle=True, complib="blosc:lz4")
    open_kwargs = dict(filters=filters)


@unittest.skipIf(not common.blosc_avail,
                 'BLOSC compression library not available')
@unittest.skipIf('lz4' not in tables.blosc_compressor_list(), 'lz4 required')
class FiltersCaseBloscLZ4HC(FiltersTreeTestCase):
    filters = Filters(shuffle=False, complevel=1, complib="blosc:lz4hc")
    gfilters = Filters(complevel=5, shuffle=True, complib="blosc:lz4hc")
    open_kwargs = dict(filters=filters)


@unittest.skipIf(not common.blosc_avail,
                 'BLOSC compression library not available')
@unittest.skipIf('snappy' not in tables.blosc_compressor_list(),
                 'snappy required')
class FiltersCaseBloscSnappy(FiltersTreeTestCase):
    filters = Filters(shuffle=False, complevel=1, complib="blosc:snappy")
    gfilters = Filters(complevel=5, shuffle=True, complib="blosc:snappy")
    open_kwargs = dict(filters=filters)


@unittest.skipIf(not common.blosc_avail,
                 'BLOSC compression library not available')
@unittest.skipIf('zlib' not in tables.blosc_compressor_list(), 'zlib required')
class FiltersCaseBloscZlib(FiltersTreeTestCase):
    filters = Filters(shuffle=False, complevel=1, complib="blosc:zlib")
    gfilters = Filters(complevel=5, shuffle=True, complib="blosc:zlib")
    open_kwargs = dict(filters=filters)


class CopyGroupTestCase(common.TempFileMixin, TestCase):
    title = "A title"
    nrows = 10

    def setUp(self):
        super(CopyGroupTestCase, self).setUp()

        # Create a temporary file
        self.h5fname2 = tempfile.mktemp(".h5")

        # Create the destination
        self.h5file2 = tables.open_file(self.h5fname2, "w")
        self.populateFile()

    def populateFile(self):
        group = self.h5file.root
        # Add some user attrs:
        group._v_attrs.attr1 = "an string for root group"
        group._v_attrs.attr2 = 124
        # Create a tree
        for j in range(5):
            for i in range(2):
                # Create a new group (brother of group)
                group2 = self.h5file.create_group(group, 'bgroup' + str(i),
                                                  filters=None)

                # Create a table
                table = self.h5file.create_table(group2, 'table1', Record2,
                                                 title=self.title,
                                                 filters=None)
                # Get the record object associated with the new table
                d = table.row
                # Fill the table
                for i in xrange(self.nrows):
                    d['var1'] = '%04d' % (self.nrows - i)
                    d['var2'] = i
                    d['var3'] = i * 2
                    d.append()      # This injects the Record values
                # Flush the buffer for this table
                table.flush()

                # Add some user attrs:
                table.attrs.attr1 = "an string"
                table.attrs.attr2 = 234

                # Create a couple of arrays in each group
                var1List = [x['var1'] for x in table.iterrows()]
                var3List = [x['var3'] for x in table.iterrows()]

                self.h5file.create_array(group2, 'array1', var1List, "col 1")
                self.h5file.create_array(group2, 'array2', var3List, "col 3")

                # Create a couple of EArrays as well
                ea1 = self.h5file.create_earray(group2, 'earray1',
                                                StringAtom(itemsize=4), (0,),
                                                "col 1")
                ea2 = self.h5file.create_earray(group2, 'earray2',
                                                Int16Atom(), (0,), "col 3")
                # Add some user attrs:
                ea1.attrs.attr1 = "an string for earray"
                ea2.attrs.attr2 = 123
                # And fill them with some values
                ea1.append(var1List)
                ea2.append(var3List)

            # Create a new group (descendant of group)
            group3 = self.h5file.create_group(group, 'group' + str(j),
                                              filters=None)
            # Iterate over this new group (group3)
            group = group3
            # Add some user attrs:
            group._v_attrs.attr1 = "an string for group"
            group._v_attrs.attr2 = 124

    def tearDown(self):
        # Close the file
        if self.h5file2.isopen:
            self.h5file2.close()
        os.remove(self.h5fname2)

        super(CopyGroupTestCase, self).tearDown()

    def test00_nonRecursive(self):
        """Checking non-recursive copy of a Group"""

        if common.verbose:
            print('\n', '-=' * 30)
            print("Running %s.test00_nonRecursive..." %
                  self.__class__.__name__)

        # Copy a group non-recursively
        srcgroup = self.h5file.root.group0.group1
        #srcgroup._f_copy_children(self.h5file2.root, recursive=False,
        #                          filters=self.filters)
        self.h5file.copy_children(srcgroup, self.h5file2.root,
                                  recursive=False, filters=self.filters)
        if self.close:
            # Close the destination file
            self.h5file2.close()
            # And open it again
            self.h5file2 = tables.open_file(self.h5fname2, "r")

        # Check that the copy has been done correctly
        dstgroup = self.h5file2.root
        nodelist1 = srcgroup._v_children.keys()
        nodelist2 = dstgroup._v_children.keys()
        # Sort the lists
        nodelist1.sort()
        nodelist2.sort()
        if common.verbose:
            print("The origin node list -->", nodelist1)
            print("The copied node list -->", nodelist2)
        self.assertEqual(srcgroup._v_nchildren, dstgroup._v_nchildren)
        self.assertEqual(nodelist1, nodelist2)

    def test01_nonRecursiveAttrs(self):
        """Checking non-recursive copy of a Group (attributes copied)"""

        if common.verbose:
            print('\n', '-=' * 30)
            print(("Running %s.test01_nonRecursiveAttrs..." %
                   self.__class__.__name__))

        # Copy a group non-recursively with attrs
        srcgroup = self.h5file.root.group0.group1
        srcgroup._f_copy_children(self.h5file2.root,
                                  recursive=False,
                                  filters=self.filters,
                                  copyuserattrs=1)
        if self.close:
            # Close the destination file
            self.h5file2.close()
            # And open it again
            self.h5file2 = tables.open_file(self.h5fname2, "r")

        # Check that the copy has been done correctly
        dstgroup = self.h5file2.root
        for srcnode in srcgroup:
            dstnode = getattr(dstgroup, srcnode._v_name)
            if isinstance(srcnode, Group):
                srcattrs = srcnode._v_attrs
                srcattrskeys = srcattrs._f_list("all")
                dstattrs = dstnode._v_attrs
                dstattrskeys = dstattrs._f_list("all")
            else:
                srcattrs = srcnode.attrs
                srcattrskeys = srcattrs._f_list("all")
                dstattrs = dstnode.attrs
                dstattrskeys = dstattrs._f_list("all")

            # Filters may differ, do not take into account
            if self.filters is not None:
                dstattrskeys.remove('FILTERS')

            # These lists should already be ordered
            if common.verbose:
                print("srcattrskeys for node %s: %s" % (srcnode._v_name,
                                                        srcattrskeys))
                print("dstattrskeys for node %s: %s" % (dstnode._v_name,
                                                        dstattrskeys))
            self.assertEqual(srcattrskeys, dstattrskeys)
            if common.verbose:
                print("The attrs names has been copied correctly")

            # Now, for the contents of attributes
            for srcattrname in srcattrskeys:
                srcattrvalue = str(getattr(srcattrs, srcattrname))
                dstattrvalue = str(getattr(dstattrs, srcattrname))
                self.assertEqual(srcattrvalue, dstattrvalue)
            if self.filters is not None:
                self.assertEqual(dstattrs.FILTERS, self.filters)

            if common.verbose:
                print("The attrs contents has been copied correctly")

    def test02_Recursive(self):
        """Checking recursive copy of a Group"""

        if common.verbose:
            print('\n', '-=' * 30)
            print("Running %s.test02_Recursive..." % self.__class__.__name__)

        # Create the destination node
        group = self.h5file2.root
        for groupname in self.dstnode.split("/"):
            if groupname:
                group = self.h5file2.create_group(group, groupname)
        dstgroup = self.h5file2.get_node(self.dstnode)

        # Copy a group non-recursively
        srcgroup = self.h5file.get_node(self.srcnode)
        self.h5file.copy_children(srcgroup, dstgroup,
                                  recursive=True,
                                  filters=self.filters)
        lenSrcGroup = len(srcgroup._v_pathname)
        if lenSrcGroup == 1:
            lenSrcGroup = 0  # Case where srcgroup == "/"
        if self.close:
            # Close the destination file
            self.h5file2.close()
            # And open it again
            self.h5file2 = tables.open_file(self.h5fname2, "r")
            dstgroup = self.h5file2.get_node(self.dstnode)

        # Check that the copy has been done correctly
        lenDstGroup = len(dstgroup._v_pathname)
        if lenDstGroup == 1:
            lenDstGroup = 0  # Case where dstgroup == "/"
        first = 1
        nodelist1 = []
        for node in srcgroup._f_walknodes():
            if first:
                # skip the first group
                first = 0
                continue
            nodelist1.append(node._v_pathname[lenSrcGroup:])

        first = 1
        nodelist2 = []
        for node in dstgroup._f_walknodes():
            if first:
                # skip the first group
                first = 0
                continue
            nodelist2.append(node._v_pathname[lenDstGroup:])

        if common.verbose:
            print("The origin node list -->", nodelist1)
            print("The copied node list -->", nodelist2)
        self.assertEqual(nodelist1, nodelist2)

    def test03_RecursiveFilters(self):
        """Checking recursive copy of a Group (cheking Filters)"""

        if common.verbose:
            print('\n', '-=' * 30)
            print(("Running %s.test03_RecursiveFilters..." %
                   self.__class__.__name__))

        # Create the destination node
        group = self.h5file2.root
        for groupname in self.dstnode.split("/"):
            if groupname:
                group = self.h5file2.create_group(group, groupname)
        dstgroup = self.h5file2.get_node(self.dstnode)

        # Copy a group non-recursively
        srcgroup = self.h5file.get_node(self.srcnode)
        srcgroup._f_copy_children(dstgroup,
                                  recursive=True,
                                  filters=self.filters)
        lenSrcGroup = len(srcgroup._v_pathname)
        if lenSrcGroup == 1:
            lenSrcGroup = 0  # Case where srcgroup == "/"
        if self.close:
            # Close the destination file
            self.h5file2.close()
            # And open it again
            self.h5file2 = tables.open_file(self.h5fname2, "r")
            dstgroup = self.h5file2.get_node(self.dstnode)

        # Check that the copy has been done correctly
        lenDstGroup = len(dstgroup._v_pathname)
        if lenDstGroup == 1:
            lenDstGroup = 0  # Case where dstgroup == "/"
        first = 1
        nodelist1 = {}
        for node in srcgroup._f_walknodes():
            if first:
                # skip the first group
                first = 0
                continue
            nodelist1[node._v_name] = node._v_pathname[lenSrcGroup:]

        first = 1
        for node in dstgroup._f_walknodes():
            if first:
                # skip the first group
                first = 0
                continue
            if isinstance(node, Group):
                repr(node._v_filters) == repr(nodelist1[node._v_name])
            else:
                repr(node.filters) == repr(nodelist1[node._v_name])


class CopyGroupCase1(CopyGroupTestCase):
    close = 0
    filters = None
    srcnode = '/group0/group1'
    dstnode = '/'


class CopyGroupCase2(CopyGroupTestCase):
    close = 1
    filters = None
    srcnode = '/group0/group1'
    dstnode = '/'


class CopyGroupCase3(CopyGroupTestCase):
    close = 0
    filters = None
    srcnode = '/group0'
    dstnode = '/group2/group3'


class CopyGroupCase4(CopyGroupTestCase):
    close = 1
    filters = Filters(complevel=1)
    srcnode = '/group0'
    dstnode = '/group2/group3'


class CopyGroupCase5(CopyGroupTestCase):
    close = 0
    filters = Filters()
    srcnode = '/'
    dstnode = '/group2/group3'


class CopyGroupCase6(CopyGroupTestCase):
    close = 1
    filters = Filters(fletcher32=True)
    srcnode = '/group0'
    dstnode = '/group2/group3'


class CopyGroupCase7(CopyGroupTestCase):
    close = 0
    filters = Filters(complevel=1, shuffle=False)
    srcnode = '/'
    dstnode = '/'


@unittest.skipIf(not common.lzo_avail, 'LZO compression library not available')
class CopyGroupCase8(CopyGroupTestCase):
    close = 1
    filters = Filters(complevel=1, complib="lzo")
    srcnode = '/'
    dstnode = '/'


class CopyFileTestCase(common.TempFileMixin, TestCase):
    title = "A title"
    nrows = 10

    def setUp(self):
        super(CopyFileTestCase, self).setUp()

        # Create a temporary file
        self.h5fname2 = tempfile.mktemp(".h5")

        # Create the source file
        self.populateFile()

    def populateFile(self):
        group = self.h5file.root
        # Add some user attrs:
        group._v_attrs.attr1 = "an string for root group"
        group._v_attrs.attr2 = 124
        # Create a tree
        for j in range(5):
            for i in range(2):
                # Create a new group (brother of group)
                group2 = self.h5file.create_group(group, 'bgroup' + str(i),
                                                  filters=None)

                # Create a table
                table = self.h5file.create_table(group2, 'table1', Record2,
                                                 title=self.title,
                                                 filters=None)
                # Get the record object associated with the new table
                d = table.row
                # Fill the table
                for i in xrange(self.nrows):
                    d['var1'] = '%04d' % (self.nrows - i)
                    d['var2'] = i
                    d['var3'] = i * 2
                    d.append()      # This injects the Record values
                # Flush the buffer for this table
                table.flush()

                # Add some user attrs:
                table.attrs.attr1 = "an string"
                table.attrs.attr2 = 234

                # Create a couple of arrays in each group
                var1List = [x['var1'] for x in table.iterrows()]
                var3List = [x['var3'] for x in table.iterrows()]

                self.h5file.create_array(group2, 'array1', var1List, "col 1")
                self.h5file.create_array(group2, 'array2', var3List, "col 3")

                # Create a couple of EArrays as well
                ea1 = self.h5file.create_earray(group2, 'earray1',
                                                StringAtom(itemsize=4), (0,),
                                                "col 1")
                ea2 = self.h5file.create_earray(group2, 'earray2',
                                                Int16Atom(), (0,),
                                                "col 3")
                # Add some user attrs:
                ea1.attrs.attr1 = "an string for earray"
                ea2.attrs.attr2 = 123
                # And fill them with some values
                ea1.append(var1List)
                ea2.append(var3List)

            # Create a new group (descendant of group)
            group3 = self.h5file.create_group(group, 'group' + str(j),
                                              filters=None)
            # Iterate over this new group (group3)
            group = group3
            # Add some user attrs:
            group._v_attrs.attr1 = "an string for group"
            group._v_attrs.attr2 = 124

    def tearDown(self):
        # Close the file
        if hasattr(self, 'h5file2') and self.h5file2.isopen:
            self.h5file2.close()

        if hasattr(self, 'h5fname2') and os.path.exists(self.h5fname2):
            os.remove(self.h5fname2)

        super(CopyFileTestCase, self).tearDown()

    def test00_overwrite(self):
        """Checking copy of a File (overwriting file)"""

        if common.verbose:
            print('\n', '-=' * 30)
            print("Running %s.test00_overwrite..." % self.__class__.__name__)

        # Create a temporary file
        file2h = open(self.h5fname2, "w")
        file2h.close()

        # Copy the file to the destination
        self.h5file.copy_file(self.h5fname2, title=self.title,
                              overwrite=1,
                              copyuserattrs=0,
                              filters=None)

        # Close the original file, if needed
        if self.close:
            self._reopen()

        # ...and open the destination file
        self.h5file2 = tables.open_file(self.h5fname2, "r")

        # Check that the copy has been done correctly
        srcgroup = self.h5file.root
        dstgroup = self.h5file2.root
        nodelist1 = srcgroup._v_children.keys()
        nodelist2 = dstgroup._v_children.keys()
        # Sort the lists
        nodelist1.sort()
        nodelist2.sort()
        if common.verbose:
            print("The origin node list -->", nodelist1)
            print("The copied node list -->", nodelist2)
        self.assertEqual(srcgroup._v_nchildren, dstgroup._v_nchildren)
        self.assertEqual(nodelist1, nodelist2)
        self.assertEqual(self.h5file2.title, self.title)

    def test00a_srcdstequal(self):
        """Checking copy of a File (srcfile == dstfile)"""

        if common.verbose:
            print('\n', '-=' * 30)
            print("Running %s.test00a_srcdstequal..." %
                  self.__class__.__name__)

        # Copy the file to the destination
        self.assertRaises(IOError, self.h5file.copy_file, self.h5file.filename)

    def test00b_firstclass(self):
        """Checking copy of a File (first-class function)"""

        if common.verbose:
            print('\n', '-=' * 30)
            print("Running %s.test00b_firstclass..." % self.__class__.__name__)

        # Close the temporary file
        self.h5file.close()

        # Copy the file to the destination
        tables.copy_file(self.h5fname, self.h5fname2, title=self.title,
                         copyuserattrs=0, filters=None, overwrite=1)

        # ...and open the source and destination file
        self.h5file = tables.open_file(self.h5fname, "r")
        self.h5file2 = tables.open_file(self.h5fname2, "r")

        # Check that the copy has been done correctly
        srcgroup = self.h5file.root
        dstgroup = self.h5file2.root
        nodelist1 = srcgroup._v_children.keys()
        nodelist2 = dstgroup._v_children.keys()

        # Sort the lists
        nodelist1.sort()
        nodelist2.sort()
        if common.verbose:
            print("The origin node list -->", nodelist1)
            print("The copied node list -->", nodelist2)
        self.assertEqual(srcgroup._v_nchildren, dstgroup._v_nchildren)
        self.assertEqual(nodelist1, nodelist2)
        self.assertEqual(self.h5file2.title, self.title)

    def test01_copy(self):
        """Checking copy of a File (attributes not copied)"""

        if common.verbose:
            print('\n', '-=' * 30)
            print("Running %s.test01_copy..." % self.__class__.__name__)

        # Copy the file to the destination
        self.h5file.copy_file(self.h5fname2, title=self.title,
                              copyuserattrs=0,
                              filters=self.filters)

        # Close the original file, if needed
        if self.close:
            self._reopen()

        # ...and open the destination file
        self.h5file2 = tables.open_file(self.h5fname2, "r")

        # Check that the copy has been done correctly
        srcgroup = self.h5file.root
        dstgroup = self.h5file2.root
        nodelist1 = srcgroup._v_children.keys()
        nodelist2 = dstgroup._v_children.keys()

        # Sort the lists
        nodelist1.sort()
        nodelist2.sort()
        if common.verbose:
            print("The origin node list -->", nodelist1)
            print("The copied node list -->", nodelist2)
        self.assertEqual(srcgroup._v_nchildren, dstgroup._v_nchildren)
        self.assertEqual(nodelist1, nodelist2)
        # print("_v_attrnames-->", self.h5file2.root._v_attrs._v_attrnames)
        # print("--> <%s,%s>" % (self.h5file2.title, self.title))
        self.assertEqual(self.h5file2.title, self.title)

        # Check that user attributes has not been copied
        for srcnode in srcgroup:
            dstnode = getattr(dstgroup, srcnode._v_name)
            srcattrs = srcnode._v_attrs
            srcattrskeys = srcattrs._f_list("sys")
            dstattrs = dstnode._v_attrs
            dstattrskeys = dstattrs._f_list("all")

            # Filters may differ, do not take into account
            if self.filters is not None:
                dstattrskeys.remove('FILTERS')

            # These lists should already be ordered
            if common.verbose:
                print("srcattrskeys for node %s: %s" % (srcnode._v_name,
                                                        srcattrskeys))
                print("dstattrskeys for node %s: %s" % (dstnode._v_name,
                                                        dstattrskeys))
            self.assertEqual(srcattrskeys, dstattrskeys)
            if common.verbose:
                print("The attrs names has been copied correctly")

            # Now, for the contents of attributes
            for srcattrname in srcattrskeys:
                srcattrvalue = str(getattr(srcattrs, srcattrname))
                dstattrvalue = str(getattr(dstattrs, srcattrname))
                self.assertEqual(srcattrvalue, dstattrvalue)
            if self.filters is not None:
                self.assertEqual(dstattrs.FILTERS, self.filters)

            if common.verbose:
                print("The attrs contents has been copied correctly")

    def test02_Attrs(self):
        """Checking copy of a File (attributes copied)"""

        if common.verbose:
            print('\n', '-=' * 30)
            print("Running %s.test02_Attrs..." % self.__class__.__name__)

        # Copy the file to the destination
        self.h5file.copy_file(self.h5fname2, title=self.title,
                              copyuserattrs=1,
                              filters=self.filters)

        # Close the original file, if needed
        if self.close:
            self._reopen()

        # ...and open the destination file
        self.h5file2 = tables.open_file(self.h5fname2, "r")

        # Check that the copy has been done correctly
        srcgroup = self.h5file.root
        dstgroup = self.h5file2.root
        for srcnode in srcgroup:
            dstnode = getattr(dstgroup, srcnode._v_name)
            srcattrs = srcnode._v_attrs
            srcattrskeys = srcattrs._f_list("all")
            dstattrs = dstnode._v_attrs
            dstattrskeys = dstattrs._f_list("all")
            # These lists should already be ordered
            if common.verbose:
                print("srcattrskeys for node %s: %s" % (srcnode._v_name,
                                                        srcattrskeys))
                print("dstattrskeys for node %s: %s" % (dstnode._v_name,
                                                        dstattrskeys))

            # Filters may differ, do not take into account
            if self.filters is not None:
                dstattrskeys.remove('FILTERS')
            self.assertEqual(srcattrskeys, dstattrskeys)
            if common.verbose:
                print("The attrs names has been copied correctly")

            # Now, for the contents of attributes
            for srcattrname in srcattrskeys:
                srcattrvalue = str(getattr(srcattrs, srcattrname))
                dstattrvalue = str(getattr(dstattrs, srcattrname))
                self.assertEqual(srcattrvalue, dstattrvalue)
            if self.filters is not None:
                self.assertEqual(dstattrs.FILTERS, self.filters)

            if common.verbose:
                print("The attrs contents has been copied correctly")


class CopyFileCase1(CopyFileTestCase):
    close = 0
    title = "A new title"
    filters = None


class CopyFileCase2(CopyFileTestCase):
    close = 1
    title = "A new title"
    filters = None


class CopyFileCase3(CopyFileTestCase):
    close = 0
    title = "A new title"
    filters = Filters(complevel=1)


class CopyFileCase4(CopyFileTestCase):
    close = 1
    title = "A new title"
    filters = Filters(complevel=1)


class CopyFileCase5(CopyFileTestCase):
    close = 0
    title = "A new title"
    filters = Filters(fletcher32=True)


class CopyFileCase6(CopyFileTestCase):
    close = 1
    title = "A new title"
    filters = Filters(fletcher32=True)


class CopyFileCase7(CopyFileTestCase):
    close = 0
    title = "A new title"
    filters = Filters(complevel=1, complib="lzo")


class CopyFileCase8(CopyFileTestCase):
    close = 1
    title = "A new title"
    filters = Filters(complevel=1, complib="lzo")


class CopyFileCase10(common.TempFileMixin, TestCase):

    def test01_notoverwrite(self):
        """Checking copy of a File (checking not overwriting)"""

        if common.verbose:
            print('\n', '-=' * 30)
            print("Running %s.test01_notoverwrite..." %
                  self.__class__.__name__)

        # Create two empty files:
        self.h5fname2 = tempfile.mktemp(".h5")
        self.h5file2 = tables.open_file(self.h5fname2, "w")
        self.h5file2.close()  # close the second one

        try:
            # Copy the first into the second
            self.assertRaises(
                IOError, self.h5file.copy_file, self.h5fname2, overwrite=False)
        finally:
            # Delete files
            os.remove(self.h5fname2)


class GroupFiltersTestCase(common.TempFileMixin, TestCase):
    filters = tables.Filters(complevel=4)  # something non-default

    def setUp(self):
        super(GroupFiltersTestCase, self).setUp()

        atom, shape = tables.IntAtom(), (1, 1)
        create_group = self.h5file.create_group
        create_carray = self.h5file.create_carray

        create_group('/', 'implicit_no')
        create_group('/implicit_no', 'implicit_no')
        create_carray('/implicit_no/implicit_no', 'implicit_no',
                      atom=atom, shape=shape)
        create_carray('/implicit_no/implicit_no', 'explicit_no',
                      atom=atom, shape=shape, filters=tables.Filters())
        create_carray('/implicit_no/implicit_no', 'explicit_yes',
                      atom=atom, shape=shape, filters=self.filters)

        create_group('/', 'explicit_yes', filters=self.filters)
        create_group('/explicit_yes', 'implicit_yes')
        create_carray('/explicit_yes/implicit_yes', 'implicit_yes',
                      atom=atom, shape=shape)
        create_carray('/explicit_yes/implicit_yes', 'explicit_yes',
                      atom=atom, shape=shape, filters=self.filters)
        create_carray('/explicit_yes/implicit_yes', 'explicit_no',
                      atom=atom, shape=shape, filters=tables.Filters())

    def _check_filters(self, h5file, filters=None):
        for node in h5file:
            # Get node filters.
            if hasattr(node, 'filters'):
                node_filters = node.filters
            else:
                node_filters = node._v_filters

            # Compare to given filters.
            if filters is not None:
                self.assertEqual(node_filters, filters)
                return

            # Guess filters to compare to by node name.
            if node._v_name.endswith('_no'):
                self.assertEqual(
                    node_filters, tables.Filters(),
                    "node ``%s`` should have no filters" % node._v_pathname)
            elif node._v_name.endswith('_yes'):
                self.assertEqual(
                    node_filters, self.filters,
                    "node ``%s`` should have filters" % node._v_pathname)

    def test00_propagate(self):
        """Filters propagating to children."""

        self._check_filters(self.h5file)

    def _test_copyFile(self, filters=None):
        copyfname = tempfile.mktemp(suffix='.h5')
        try:
            self.h5file.copy_file(copyfname, filters=filters)
            try:
                copyf = tables.open_file(copyfname)
                self._check_filters(copyf, filters=filters)
            finally:
                copyf.close()
        finally:
            os.remove(copyfname)

    def test01_copyFile(self):
        """Keeping filters when copying a file."""

        self._test_copyFile()

    def test02_copyFile_override(self):
        """Overriding filters when copying a file."""

        self._test_copyFile(self.filters)

    def _test_change(self, pathname, change_filters, new_filters):
        group = self.h5file.get_node(pathname)

        # Check expected current filters.
        old_filters = tables.Filters()
        if pathname.endswith('_yes'):
            old_filters = self.filters
        self.assertEqual(group._v_filters, old_filters)

        # Change filters.
        change_filters(group)
        self.assertEqual(group._v_filters, new_filters)

        # Get and check changed filters.
        if self._reopen():
            group = self.h5file.get_node(pathname)
        self.assertEqual(group._v_filters, new_filters)

    def test03_change(self):
        """Changing the filters of a group."""

        def set_filters(group):
            group._v_filters = self.filters
        self._test_change('/', set_filters, self.filters)

    def test04_delete(self):
        """Deleting the filters of a group."""

        def del_filters(group):
            del group._v_filters
        self._test_change('/explicit_yes', del_filters, tables.Filters())


@unittest.skipIf(not common.blosc_avail, 'BLOSC not available')
class SetBloscMaxThreadsTestCase(common.TempFileMixin, TestCase):
    filters = tables.Filters(complevel=4, complib="blosc")

    def test00(self):
        """Checking set_blosc_max_threads()"""

        nthreads_old = tables.set_blosc_max_threads(4)
        if common.verbose:
            print("Previous max threads:", nthreads_old)
            print("Should be:", self.h5file.params['MAX_BLOSC_THREADS'])
        self.assertEqual(nthreads_old, self.h5file.params['MAX_BLOSC_THREADS'])
        self.h5file.create_carray('/', 'some_array',
                                  atom=tables.Int32Atom(), shape=(3, 3),
                                  filters = self.filters)
        nthreads_old = tables.set_blosc_max_threads(1)
        if common.verbose:
            print("Previous max threads:", nthreads_old)
            print("Should be:", 4)
        self.assertEqual(nthreads_old, 4)

    def test01(self):
        """Checking set_blosc_max_threads() (re-open)"""

        nthreads_old = tables.set_blosc_max_threads(4)
        self.h5file.create_carray('/', 'some_array',
                                  atom=tables.Int32Atom(), shape=(3, 3),
                                  filters = self.filters)
        self._reopen()
        nthreads_old = tables.set_blosc_max_threads(4)
        if common.verbose:
            print("Previous max threads:", nthreads_old)
            print("Should be:", self.h5file.params['MAX_BLOSC_THREADS'])
        self.assertEqual(nthreads_old, self.h5file.params['MAX_BLOSC_THREADS'])


class FilterTestCase(TestCase):
    def test_filter_pack_type(self):
        self.assertEqual(type(Filters()._pack()), numpy.int64)

    @staticmethod
    def _hexl(n):
        if sys.version_info[0] > 2:
            return hex(int(n))
        else:
            return hex(long(n)).rstrip('L')

    def test_filter_pack_01(self):
        filter_ = Filters()
        self.assertEqual(self._hexl(filter_._pack()), '0x0')

    def test_filter_pack_02(self):
        filter_ = Filters(1, shuffle=False)
        self.assertEqual(self._hexl(filter_._pack()), '0x101')

    def test_filter_pack_03(self):
        filter_ = Filters(9, 'zlib', shuffle=True, fletcher32=True)
        self.assertEqual(self._hexl(filter_._pack()), '0x30109')

    def test_filter_pack_04(self):
        filter_ = Filters(1, shuffle=False, least_significant_digit=5)
        self.assertEqual(self._hexl(filter_._pack()), '0x5040101')

    def test_filter_unpack_01(self):
        filter_ = Filters._unpack(numpy.int64(0x0))
        self.assertFalse(filter_.shuffle)
        self.assertFalse(filter_.fletcher32)
        self.assertEqual(filter_.least_significant_digit, None)
        self.assertEqual(filter_.complevel, 0)
        self.assertEqual(filter_.complib, None)

    def test_filter_unpack_02(self):
        filter_ = Filters._unpack(numpy.int64(0x101))
        self.assertFalse(filter_.shuffle)
        self.assertFalse(filter_.fletcher32)
        self.assertEqual(filter_.least_significant_digit, None)
        self.assertEqual(filter_.complevel, 1)
        self.assertEqual(filter_.complib, 'zlib')

    def test_filter_unpack_03(self):
        filter_ = Filters._unpack(numpy.int64(0x30109))
        self.assertTrue(filter_.shuffle)
        self.assertTrue(filter_.fletcher32)
        self.assertEqual(filter_.least_significant_digit, None)
        self.assertEqual(filter_.complevel, 9)
        self.assertEqual(filter_.complib, 'zlib')

    def test_filter_unpack_04(self):
        filter_ = Filters._unpack(numpy.int64(0x5040101))
        self.assertFalse(filter_.shuffle)
        self.assertFalse(filter_.fletcher32)
        self.assertEqual(filter_.least_significant_digit, 5)
        self.assertEqual(filter_.complevel, 1)
        self.assertEqual(filter_.complib, 'zlib')


class DefaultDriverTestCase(common.TempFileMixin, TestCase):
    DRIVER = None
    DRIVER_PARAMS = {}
    open_kwargs = dict(driver=DRIVER, **DRIVER_PARAMS)

    def setUp(self):
        super(DefaultDriverTestCase, self).setUp()

        # Create an HDF5 file and contents
        root = self.h5file.root
        self.h5file.set_node_attr(root, "testattr", 41)
        self.h5file.create_array(root, "array", [1, 2], title="array")
        self.h5file.create_table(root, "table", {"var1": tables.IntCol()},
                                 title="table")

    def assertIsFile(self):
        self.assertTrue(os.path.isfile(self.h5fname))

    def test_newFile(self):
        self.assertTrue(isinstance(self.h5file, tables.File))
        self.assertIsFile()

    def test_readFile(self):
        self.h5file.close()
        self.h5file = None

        self.assertIsFile()

        # Open an existing HDF5 file
        self.h5file = tables.open_file(self.h5fname, mode="r",
                                       driver=self.DRIVER,
                                       **self.DRIVER_PARAMS)

        # check contents
        root = self.h5file.root

        self.assertEqual(self.h5file.get_node_attr(root, "testattr"), 41)

        self.assertTrue(isinstance(root.array, tables.Array))
        self.assertEqual(root.array._v_title, "array")

        self.assertTrue(isinstance(root.table, tables.Table))
        self.assertEqual(root.table._v_title, "table")
        self.assertTrue("var1" in root.table.colnames)
        self.assertEqual(root.table.cols.var1.dtype, tables.IntCol().dtype)

    def test_openFileA(self):
        self.h5file.close()
        self.h5file = None

        self.assertIsFile()

        # Open an existing HDF5 file in append mode
        self.h5file = tables.open_file(self.h5fname, mode="a",
                                       driver=self.DRIVER,
                                       **self.DRIVER_PARAMS)

        # check contents
        root = self.h5file.root

        self.assertEqual(self.h5file.get_node_attr(root, "testattr"), 41)

        self.assertTrue(isinstance(root.array, tables.Array))
        self.assertEqual(root.array._v_title, "array")

        self.assertTrue(isinstance(root.table, tables.Table))
        self.assertEqual(root.table._v_title, "table")
        self.assertTrue("var1" in root.table.colnames)
        self.assertEqual(root.table.cols.var1.dtype, tables.IntCol().dtype)

        # write new data
        root = self.h5file.root
        self.h5file.set_node_attr(root, "testattr2", 42)
        self.h5file.create_array(root, "array2", [1, 2], title="array2")
        self.h5file.create_table(root, "table2", {"var2": tables.FloatCol()},
                                 title="table2")

        # check contents
        self._reopen(mode="a", driver=self.DRIVER, **self.DRIVER_PARAMS)

        root = self.h5file.root

        self.assertEqual(self.h5file.get_node_attr(root, "testattr"), 41)
        self.assertEqual(self.h5file.get_node_attr(root, "testattr2"), 42)

        self.assertTrue(isinstance(root.array, tables.Array))
        self.assertEqual(root.array._v_title, "array")

        self.assertTrue(isinstance(root.array2, tables.Array))
        self.assertEqual(root.array2._v_title, "array2")

        self.assertTrue(isinstance(root.table, tables.Table))
        self.assertEqual(root.table._v_title, "table")
        self.assertTrue("var1" in root.table.colnames)
        self.assertEqual(root.table.cols.var1.dtype, tables.IntCol().dtype)

        self.assertTrue(isinstance(root.table2, tables.Table))
        self.assertEqual(root.table2._v_title, "table2")
        self.assertTrue("var2" in root.table2.colnames)
        self.assertEqual(root.table2.cols.var2.dtype, tables.FloatCol().dtype)

    def test_openFileRW(self):
        self.h5file.close()
        self.h5file = None

        self.assertIsFile()

        # Open an existing HDF5 file in append mode
        self.h5file = tables.open_file(self.h5fname, mode="r+",
                                       driver=self.DRIVER,
                                       **self.DRIVER_PARAMS)

        # check contents
        root = self.h5file.root

        self.assertEqual(self.h5file.get_node_attr(root, "testattr"), 41)

        self.assertTrue(isinstance(root.array, tables.Array))
        self.assertEqual(root.array._v_title, "array")

        self.assertTrue(isinstance(root.table, tables.Table))
        self.assertEqual(root.table._v_title, "table")
        self.assertTrue("var1" in root.table.colnames)
        self.assertEqual(root.table.cols.var1.dtype, tables.IntCol().dtype)

        # write new data
        self.h5file.set_node_attr(root, "testattr2", 42)
        self.h5file.create_array(root, "array2", [1, 2], title="array2")
        self.h5file.create_table(root, "table2", {"var2": tables.FloatCol()},
                                 title="table2")

        # check contents
        self._reopen(mode="r+", driver=self.DRIVER, **self.DRIVER_PARAMS)

        root = self.h5file.root

        self.assertEqual(self.h5file.get_node_attr(root, "testattr"), 41)
        self.assertEqual(self.h5file.get_node_attr(root, "testattr2"), 42)

        self.assertTrue(isinstance(root.array, tables.Array))
        self.assertEqual(root.array._v_title, "array")

        self.assertTrue(isinstance(root.array2, tables.Array))
        self.assertEqual(root.array2._v_title, "array2")

        self.assertTrue(isinstance(root.table, tables.Table))
        self.assertEqual(root.table._v_title, "table")
        self.assertTrue("var1" in root.table.colnames)
        self.assertEqual(root.table.cols.var1.dtype, tables.IntCol().dtype)

        self.assertTrue(isinstance(root.table2, tables.Table))
        self.assertEqual(root.table2._v_title, "table2")
        self.assertTrue("var2" in root.table2.colnames)
        self.assertEqual(root.table2.cols.var2.dtype, tables.FloatCol().dtype)


@unittest.skipIf(hdf5_version < "1.8.9", "requires HDF5 >= 1.8,9")
class Sec2DriverTestCase(DefaultDriverTestCase):
    DRIVER = "H5FD_SEC2"
    open_kwargs = dict(driver=DRIVER, **DefaultDriverTestCase.DRIVER_PARAMS)

    def test_get_file_image(self):
        image = self.h5file.get_file_image()
        self.assertTrue(len(image) > 0)
        if sys.version_info[0] < 3:
            self.assertEqual([ord(i) for i in image[
                             :4]], [137, 72, 68, 70])
        else:
            self.assertEqual([i for i in image[:4]], [137, 72, 68, 70])


@unittest.skipIf(hdf5_version < "1.8.9", "requires HDF5 >= 1.8,9")
class StdioDriverTestCase(DefaultDriverTestCase):
    DRIVER = "H5FD_STDIO"
    open_kwargs = dict(driver=DRIVER, **DefaultDriverTestCase.DRIVER_PARAMS)

    def test_get_file_image(self):
        image = self.h5file.get_file_image()
        self.assertTrue(len(image) > 0)
        if sys.version_info[0] < 3:
            self.assertEqual([ord(i) for i in image[
                             :4]], [137, 72, 68, 70])
        else:
            self.assertEqual([i for i in image[:4]], [137, 72, 68, 70])


@unittest.skipIf(hdf5_version < "1.8.9", "requires HDF5 >= 1.8,9")
class CoreDriverTestCase(DefaultDriverTestCase):
    DRIVER = "H5FD_CORE"
    open_kwargs = dict(driver=DRIVER, **DefaultDriverTestCase.DRIVER_PARAMS)

    def test_get_file_image(self):
        image = self.h5file.get_file_image()
        self.assertTrue(len(image) > 0)
        if sys.version_info[0] < 3:
            self.assertEqual([ord(i) for i in image[
                             :4]], [137, 72, 68, 70])
        else:
            self.assertEqual([i for i in image[:4]], [137, 72, 68, 70])


class CoreDriverNoBackingStoreTestCase(TestCase):
    DRIVER = "H5FD_CORE"

    def setUp(self):
        super(CoreDriverNoBackingStoreTestCase, self).setUp()

        self.h5fname = tempfile.mktemp(suffix=".h5")
        self.h5file = None

    def tearDown(self):
        if self.h5file:
            self.h5file.close()
        elif self.h5fname in tables.file._open_files:
            open_files = tables.file._open_files
            for h5file in open_files.get_handlers_by_name(self.h5fname):
                h5file.close()

        self.h5file = None
        if os.path.isfile(self.h5fname):
            os.remove(self.h5fname)

        super(CoreDriverNoBackingStoreTestCase, self).tearDown()

    def test_newFile(self):
        """Ensure that nothing is written to file."""

        self.assertFalse(os.path.isfile(self.h5fname))

        self.h5file = tables.open_file(self.h5fname, mode="w",
                                       driver=self.DRIVER,
                                       driver_core_backing_store=False)

        # Create an HDF5 file and contents
        root = self.h5file.root
        self.h5file.set_node_attr(root, "testattr", 41)
        self.h5file.create_array(root, "array", [1, 2], title="array")
        self.h5file.create_table(root, "table", {"var1": tables.IntCol()},
                                 title="table")
        self.h5file.close()     # flush

        self.assertFalse(os.path.isfile(self.h5fname))

    def test_readNewFileW(self):
        self.assertFalse(os.path.isfile(self.h5fname))

        # Create an HDF5 file and contents
        self.h5file = tables.open_file(self.h5fname, mode="w",
                                       driver=self.DRIVER,
                                       driver_core_backing_store=False)
        root = self.h5file.root
        self.h5file.set_node_attr(root, "testattr", 41)
        self.h5file.create_array(root, "array", [1, 2], title="array")
        self.h5file.create_table(root, "table", {"var1": tables.IntCol()},
                                 title="table")

        self.assertEqual(self.h5file.get_node_attr(root, "testattr"), 41)

        self.assertTrue(isinstance(root.array, tables.Array))
        self.assertEqual(root.array._v_title, "array")

        self.assertTrue(isinstance(root.table, tables.Table))
        self.assertEqual(root.table._v_title, "table")
        self.assertTrue("var1" in root.table.colnames)
        self.assertEqual(root.table.cols.var1.dtype, tables.IntCol().dtype)

        self.h5file.close()     # flush

        self.assertFalse(os.path.isfile(self.h5fname))

    def test_readNewFileA(self):
        self.assertFalse(os.path.isfile(self.h5fname))

        # Create an HDF5 file and contents
        self.h5file = tables.open_file(self.h5fname, mode="a",
                                       driver=self.DRIVER,
                                       driver_core_backing_store=False)
        root = self.h5file.root
        self.h5file.set_node_attr(root, "testattr", 41)
        self.h5file.create_array(root, "array", [1, 2], title="array")
        self.h5file.create_table(root, "table", {"var1": tables.IntCol()},
                                 title="table")

        self.assertEqual(self.h5file.get_node_attr(root, "testattr"), 41)

        self.assertTrue(isinstance(root.array, tables.Array))
        self.assertEqual(root.array._v_title, "array")

        self.assertTrue(isinstance(root.table, tables.Table))
        self.assertEqual(root.table._v_title, "table")
        self.assertTrue("var1" in root.table.colnames)
        self.assertEqual(root.table.cols.var1.dtype, tables.IntCol().dtype)

        self.h5file.close()     # flush

        self.assertFalse(os.path.isfile(self.h5fname))

    def test_openNewFileRW(self):
        self.assertFalse(os.path.isfile(self.h5fname))
        self.assertRaises(tables.HDF5ExtError,
                          tables.open_file, self.h5fname, mode="r+",
                          driver=self.DRIVER, driver_core_backing_store=False)

    def test_openNewFileR(self):
        self.assertFalse(os.path.isfile(self.h5fname))
        self.assertRaises(tables.HDF5ExtError,
                          tables.open_file, self.h5fname, mode="r",
                          driver=self.DRIVER, driver_core_backing_store=False)

    def _create_file(self, filename):
        h5file = tables.open_file(filename, mode="w")

        root = h5file.root
        h5file.set_node_attr(root, "testattr", 41)
        h5file.create_array(root, "array", [1, 2], title="array")
        h5file.create_table(root, "table", {"var1": tables.IntCol()},
                            title="table")

        h5file.close()

    def test_readFile(self):
        self._create_file(self.h5fname)
        self.assertTrue(os.path.isfile(self.h5fname))

        # Open an existing HDF5 file
        self.h5file = tables.open_file(self.h5fname, mode="r",
                                       driver=self.DRIVER,
                                       driver_core_backing_store=False)
        root = self.h5file.root

        self.assertEqual(self.h5file.get_node_attr(root, "testattr"), 41)

        self.assertTrue(isinstance(root.array, tables.Array))
        self.assertEqual(root.array._v_title, "array")

        self.assertTrue(isinstance(root.table, tables.Table))
        self.assertEqual(root.table._v_title, "table")
        self.assertTrue("var1" in root.table.colnames)
        self.assertEqual(root.table.cols.var1.dtype, tables.IntCol().dtype)

    def _get_digest(self, filename):
        md5 = hashlib.md5()
        fd = open(filename, 'rb')

        for data in fd:
            md5.update(data)

        fd.close()

        hexdigest = md5.hexdigest()

        return hexdigest

    def test_openFileA(self):
        self._create_file(self.h5fname)
        self.assertTrue(os.path.isfile(self.h5fname))

        # compute the file hash
        hexdigest = self._get_digest(self.h5fname)

        # Open an existing HDF5 file in append mode
        self.h5file = tables.open_file(self.h5fname, mode="a",
                                       driver=self.DRIVER,
                                       driver_core_backing_store=False)

        # check contents
        root = self.h5file.root

        self.assertEqual(self.h5file.get_node_attr(root, "testattr"), 41)

        self.assertTrue(isinstance(root.array, tables.Array))
        self.assertEqual(root.array._v_title, "array")

        self.assertTrue(isinstance(root.table, tables.Table))
        self.assertEqual(root.table._v_title, "table")
        self.assertTrue("var1" in root.table.colnames)
        self.assertEqual(root.table.cols.var1.dtype, tables.IntCol().dtype)

        # write new data
        root = self.h5file.root
        self.h5file.set_node_attr(root, "testattr2", 42)
        self.h5file.create_array(root, "array2", [1, 2], title="array2")
        self.h5file.create_table(root, "table2", {"var2": tables.FloatCol()},
                                 title="table2")
        self.h5file.close()

        # ensure that there is no change on the file on disk
        self.assertEqual(hexdigest, self._get_digest(self.h5fname))

    def test_openFileRW(self):
        self._create_file(self.h5fname)
        self.assertTrue(os.path.isfile(self.h5fname))

        # compute the file hash
        hexdigest = self._get_digest(self.h5fname)

        # Open an existing HDF5 file in append mode
        self.h5file = tables.open_file(self.h5fname, mode="r+",
                                       driver=self.DRIVER,
                                       driver_core_backing_store=False)

        # check contents
        root = self.h5file.root

        self.assertEqual(self.h5file.get_node_attr(root, "testattr"), 41)

        self.assertTrue(isinstance(root.array, tables.Array))
        self.assertEqual(root.array._v_title, "array")

        self.assertTrue(isinstance(root.table, tables.Table))
        self.assertEqual(root.table._v_title, "table")
        self.assertTrue("var1" in root.table.colnames)
        self.assertEqual(root.table.cols.var1.dtype, tables.IntCol().dtype)

        # write new data
        root = self.h5file.root
        self.h5file.set_node_attr(root, "testattr2", 42)
        self.h5file.create_array(root, "array2", [1, 2], title="array2")
        self.h5file.create_table(root, "table2", {"var2": tables.FloatCol()},
                                 title="table2")
        self.h5file.close()

        # ensure that there is no change on the file on disk
        self.assertEqual(hexdigest, self._get_digest(self.h5fname))

    @unittest.skipIf(hdf5_version < "1.8.9", 'HDF5 >= "1.8.9" required')
    def test_get_file_image(self):
        self.h5file = tables.open_file(self.h5fname, mode="w",
                                       driver=self.DRIVER,
                                       driver_core_backing_store=False)
        root = self.h5file.root
        self.h5file.set_node_attr(root, "testattr", 41)
        self.h5file.create_array(root, "array", [1, 2], title="array")
        self.h5file.create_table(root, "table", {"var1": tables.IntCol()},
                                 title="table")

        image = self.h5file.get_file_image()

        self.assertTrue(len(image) > 0)
        if sys.version_info[0] < 3:
            self.assertEqual([ord(i) for i in image[
                             :4]], [137, 72, 68, 70])
        else:
            self.assertEqual([i for i in image[:4]], [137, 72, 68, 70])


class SplitDriverTestCase(DefaultDriverTestCase):
    DRIVER = "H5FD_SPLIT"
    DRIVER_PARAMS = {
        "driver_split_meta_ext": "-xm.h5",
        "driver_split_raw_ext": "-xr.h5",
    }
    open_kwargs = dict(driver=DRIVER, **DRIVER_PARAMS)

    def _getTempFileName(self):
        return tempfile.mktemp(prefix=self._getName())

    def setUp(self):
        super(SplitDriverTestCase, self).setUp()

        self.h5fnames = [self.h5fname + self.DRIVER_PARAMS[k] for k in
                         ("driver_split_meta_ext", "driver_split_raw_ext")]

    def tearDown(self):
        self.h5file.close()
        for fname in self.h5fnames:
            if os.path.isfile(fname):
                os.remove(fname)
        #super(SplitDriverTestCase, self).tearDown()
        TestCase.tearDown(self)

    def assertIsFile(self):
        for fname in self.h5fnames:
            self.assertTrue(os.path.isfile(fname))


class NotSpportedDriverTestCase(TestCase):
    DRIVER = None
    DRIVER_PARAMS = {}
    EXCEPTION = ValueError

    def setUp(self):
        super(NotSpportedDriverTestCase, self).setUp()
        self.h5fname = tempfile.mktemp(suffix=".h5")

    def tearDown(self):
        open_files = tables.file._open_files
        if self.h5fname in open_files:
            for h5file in open_files.get_handlers_by_name(self.h5fname):
                h5file.close()
        if os.path.exists(self.h5fname):
            os.remove(self.h5fname)
        super(NotSpportedDriverTestCase, self).tearDown()

    def test_newFile(self):
        self.assertRaises(self.EXCEPTION, tables.open_file, self.h5fname,
                          mode="w", driver=self.DRIVER, **self.DRIVER_PARAMS)
        self.assertFalse(os.path.isfile(self.h5fname))


if "H5FD_LOG" in tables.hdf5extension._supported_drivers:
    BaseLogDriverTestCase = DefaultDriverTestCase

else:
    BaseLogDriverTestCase = NotSpportedDriverTestCase


class LogDriverTestCase(BaseLogDriverTestCase):
    DRIVER = "H5FD_LOG"
    open_kwargs = dict(driver=DRIVER, **BaseLogDriverTestCase.DRIVER_PARAMS)

    def setUp(self):
        # local binding
        self.DRIVER_PARAMS = {
            "driver_log_file": tempfile.mktemp(suffix=".log")
        }

        super(LogDriverTestCase, self).setUp()

    def tearDown(self):
        if os.path.exists(self.DRIVER_PARAMS["driver_log_file"]):
            os.remove(self.DRIVER_PARAMS["driver_log_file"])
        super(LogDriverTestCase, self).tearDown()


if HAVE_DIRECT_DRIVER:
    class DirectDriverTestCase(DefaultDriverTestCase):
        DRIVER = "H5FD_DIRECT"
        open_kwargs = dict(
            driver=DRIVER, **DefaultDriverTestCase.DRIVER_PARAMS
        )

else:
    class DirectDriverTestCase(NotSpportedDriverTestCase):
        DRIVER = "H5FD_DIRECT"
        EXCEPTION = RuntimeError


if HAVE_WINDOWS_DRIVER:
    class WindowsDriverTestCase(DefaultDriverTestCase):
        DRIVER = "H5FD_WINDOWS"
        open_kwargs = dict(
            driver=DRIVER, **DefaultDriverTestCase.DRIVER_PARAMS
        )

else:
    class WindowsDriverTestCase(NotSpportedDriverTestCase):
        DRIVER = "H5FD_WINDOWS"
        EXCEPTION = RuntimeError


class FamilyDriverTestCase(NotSpportedDriverTestCase):
    DRIVER = "H5FD_FAMILY"


class MultiDriverTestCase(NotSpportedDriverTestCase):
    DRIVER = "H5FD_MULTI"


class MpioDriverTestCase(NotSpportedDriverTestCase):
    DRIVER = "H5FD_MPIO"


class MpiPosixDriverTestCase(NotSpportedDriverTestCase):
    DRIVER = "H5FD_MPIPOSIX"


class StreamDriverTestCase(NotSpportedDriverTestCase):
    DRIVER = "H5FD_STREAM"


@unittest.skipIf(hdf5_version < "1.8.9", 'HDF5 >= "1.8.9" required')
class InMemoryCoreDriverTestCase(TestCase):
    DRIVER = "H5FD_CORE"

    def setUp(self):
        super(InMemoryCoreDriverTestCase, self).setUp()
        self.h5fname = tempfile.mktemp(".h5")
        self.h5file = None

    def tearDown(self):
        if self.h5file:
            self.h5file.close()
        self.h5file = None

        if os.path.isfile(self.h5fname):
            os.remove(self.h5fname)
        super(InMemoryCoreDriverTestCase, self).tearDown()

    def _create_image(self, filename="in-memory", title="Title", mode='w'):
        h5file = tables.open_file(filename, mode=mode, title=title,
                                  driver=self.DRIVER,
                                  driver_core_backing_store=0)

        try:
            h5file.create_array(h5file.root, 'array', [1, 2], title="Array")
            h5file.create_table(h5file.root, 'table', {
                                'var1': IntCol()}, "Table")
            h5file.root._v_attrs.testattr = 41

            image = h5file.get_file_image()
        finally:
            h5file.close()

        return image

    def test_newFileW(self):
        image = self._create_image(self.h5fname, mode='w')
        self.assertTrue(len(image) > 0)
        if sys.version_info[0] < 3:
            self.assertEqual([ord(i) for i in image[:4]], [137, 72, 68, 70])
        else:
            self.assertEqual([i for i in image[:4]], [137, 72, 68, 70])
        self.assertFalse(os.path.exists(self.h5fname))

    def test_newFileA(self):
        image = self._create_image(self.h5fname, mode='a')
        self.assertTrue(len(image) > 0)
        if sys.version_info[0] < 3:
            self.assertEqual([ord(i) for i in image[:4]], [137, 72, 68, 70])
        else:
            self.assertEqual([i for i in image[:4]], [137, 72, 68, 70])
        self.assertFalse(os.path.exists(self.h5fname))

    def test_openFileR(self):
        image = self._create_image(self.h5fname)
        self.assertFalse(os.path.exists(self.h5fname))

        # Open an existing file
        self.h5file = tables.open_file(self.h5fname, mode="r",
                                       driver=self.DRIVER,
                                       driver_core_image=image,
                                       driver_core_backing_store=0)

        # Get the CLASS attribute of the arr object
        self.assertTrue(hasattr(self.h5file.root._v_attrs, "TITLE"))
        self.assertEqual(self.h5file.get_node_attr("/", "TITLE"), "Title")
        self.assertTrue(hasattr(self.h5file.root._v_attrs, "testattr"))
        self.assertEqual(self.h5file.get_node_attr("/", "testattr"), 41)
        self.assertTrue(hasattr(self.h5file.root, "array"))
        self.assertEqual(self.h5file.get_node_attr("/array", "TITLE"), "Array")
        self.assertTrue(hasattr(self.h5file.root, "table"))
        self.assertEqual(self.h5file.get_node_attr("/table", "TITLE"), "Table")
        self.assertEqual(self.h5file.root.array.read(), [1, 2])

    def test_openFileRW(self):
        image = self._create_image(self.h5fname)
        self.assertFalse(os.path.exists(self.h5fname))

        # Open an existing file
        self.h5file = tables.open_file(self.h5fname, mode="r+",
                                       driver=self.DRIVER,
                                       driver_core_image=image,
                                       driver_core_backing_store=0)

        # Get the CLASS attribute of the arr object
        self.assertTrue(hasattr(self.h5file.root._v_attrs, "TITLE"))
        self.assertEqual(self.h5file.get_node_attr("/", "TITLE"), "Title")
        self.assertTrue(hasattr(self.h5file.root._v_attrs, "testattr"))
        self.assertEqual(self.h5file.get_node_attr("/", "testattr"), 41)
        self.assertTrue(hasattr(self.h5file.root, "array"))
        self.assertEqual(self.h5file.get_node_attr("/array", "TITLE"), "Array")
        self.assertTrue(hasattr(self.h5file.root, "table"))
        self.assertEqual(self.h5file.get_node_attr("/table", "TITLE"), "Table")
        self.assertEqual(self.h5file.root.array.read(), [1, 2])

        self.h5file.create_array(self.h5file.root, 'array2', range(10000),
                                 title="Array2")
        self.h5file.root._v_attrs.testattr2 = 42

        self.h5file.close()

        self.assertFalse(os.path.exists(self.h5fname))

    def test_openFileRW_update(self):
        filename = tempfile.mktemp(".h5")
        image1 = self._create_image(filename)
        self.assertFalse(os.path.exists(self.h5fname))

        # Open an existing file
        self.h5file = tables.open_file(self.h5fname, mode="r+",
                                       driver=self.DRIVER,
                                       driver_core_image=image1,
                                       driver_core_backing_store=0)

        # Get the CLASS attribute of the arr object
        self.assertTrue(hasattr(self.h5file.root._v_attrs, "TITLE"))
        self.assertEqual(self.h5file.get_node_attr("/", "TITLE"), "Title")
        self.assertTrue(hasattr(self.h5file.root._v_attrs, "testattr"))
        self.assertEqual(self.h5file.get_node_attr("/", "testattr"), 41)
        self.assertTrue(hasattr(self.h5file.root, "array"))
        self.assertEqual(self.h5file.get_node_attr("/array", "TITLE"), "Array")
        self.assertTrue(hasattr(self.h5file.root, "table"))
        self.assertEqual(self.h5file.get_node_attr("/table", "TITLE"), "Table")
        self.assertEqual(self.h5file.root.array.read(), [1, 2])

        data = range(2 * tables.parameters.DRIVER_CORE_INCREMENT)
        self.h5file.create_array(self.h5file.root, 'array2', data,
                                 title="Array2")
        self.h5file.root._v_attrs.testattr2 = 42

        image2 = self.h5file.get_file_image()

        self.h5file.close()

        self.assertFalse(os.path.exists(self.h5fname))

        self.assertNotEqual(len(image1), len(image2))
        self.assertNotEqual(image1, image2)

        # Open an existing file
        self.h5file = tables.open_file(self.h5fname, mode="r",
                                       driver=self.DRIVER,
                                       driver_core_image=image2,
                                       driver_core_backing_store=0)

        # Get the CLASS attribute of the arr object
        self.assertTrue(hasattr(self.h5file.root._v_attrs, "TITLE"))
        self.assertEqual(self.h5file.get_node_attr("/", "TITLE"), "Title")
        self.assertTrue(hasattr(self.h5file.root._v_attrs, "testattr"))
        self.assertEqual(self.h5file.get_node_attr("/", "testattr"), 41)
        self.assertTrue(hasattr(self.h5file.root, "array"))
        self.assertEqual(self.h5file.get_node_attr("/array", "TITLE"), "Array")
        self.assertTrue(hasattr(self.h5file.root, "table"))
        self.assertEqual(self.h5file.get_node_attr("/table", "TITLE"), "Table")
        self.assertEqual(self.h5file.root.array.read(), [1, 2])

        self.assertTrue(hasattr(self.h5file.root._v_attrs, "testattr2"))
        self.assertEqual(self.h5file.get_node_attr("/", "testattr2"), 42)
        self.assertTrue(hasattr(self.h5file.root, "array2"))
        self.assertEqual(self.h5file.get_node_attr(
            "/array2", "TITLE"), "Array2")
        self.assertEqual(self.h5file.root.array2.read(), data)

        self.h5file.close()

        self.assertFalse(os.path.exists(self.h5fname))

    def test_openFileA(self):
        image = self._create_image(self.h5fname)
        self.assertFalse(os.path.exists(self.h5fname))

        # Open an existing file
        self.h5file = tables.open_file(self.h5fname, mode="a",
                                       driver=self.DRIVER,
                                       driver_core_image=image,
                                       driver_core_backing_store=0)

        # Get the CLASS attribute of the arr object
        self.assertTrue(hasattr(self.h5file.root._v_attrs, "TITLE"))
        self.assertEqual(self.h5file.get_node_attr("/", "TITLE"), "Title")
        self.assertTrue(hasattr(self.h5file.root._v_attrs, "testattr"))
        self.assertEqual(self.h5file.get_node_attr("/", "testattr"), 41)
        self.assertTrue(hasattr(self.h5file.root, "array"))
        self.assertEqual(self.h5file.get_node_attr("/array", "TITLE"), "Array")
        self.assertTrue(hasattr(self.h5file.root, "table"))
        self.assertEqual(self.h5file.get_node_attr("/table", "TITLE"), "Table")
        self.assertEqual(self.h5file.root.array.read(), [1, 2])

        self.h5file.close()

        self.assertFalse(os.path.exists(self.h5fname))

    def test_openFileA_update(self):
        h5fname = tempfile.mktemp(".h5")
        image1 = self._create_image(h5fname)
        self.assertFalse(os.path.exists(self.h5fname))

        # Open an existing file
        self.h5file = tables.open_file(self.h5fname, mode="a",
                                       driver=self.DRIVER,
                                       driver_core_image=image1,
                                       driver_core_backing_store=0)

        # Get the CLASS attribute of the arr object
        self.assertTrue(hasattr(self.h5file.root._v_attrs, "TITLE"))
        self.assertEqual(self.h5file.get_node_attr("/", "TITLE"), "Title")
        self.assertTrue(hasattr(self.h5file.root._v_attrs, "testattr"))
        self.assertEqual(self.h5file.get_node_attr("/", "testattr"), 41)
        self.assertTrue(hasattr(self.h5file.root, "array"))
        self.assertEqual(self.h5file.get_node_attr("/array", "TITLE"), "Array")
        self.assertTrue(hasattr(self.h5file.root, "table"))
        self.assertEqual(self.h5file.get_node_attr("/table", "TITLE"), "Table")
        self.assertEqual(self.h5file.root.array.read(), [1, 2])

        data = range(2 * tables.parameters.DRIVER_CORE_INCREMENT)
        self.h5file.create_array(self.h5file.root, 'array2', data,
                                 title="Array2")
        self.h5file.root._v_attrs.testattr2 = 42

        image2 = self.h5file.get_file_image()

        self.h5file.close()

        self.assertFalse(os.path.exists(self.h5fname))

        self.assertNotEqual(len(image1), len(image2))
        self.assertNotEqual(image1, image2)

        # Open an existing file
        self.h5file = tables.open_file(self.h5fname, mode="r",
                                       driver=self.DRIVER,
                                       driver_core_image=image2,
                                       driver_core_backing_store=0)

        # Get the CLASS attribute of the arr object
        self.assertTrue(hasattr(self.h5file.root._v_attrs, "TITLE"))
        self.assertEqual(self.h5file.get_node_attr("/", "TITLE"), "Title")
        self.assertTrue(hasattr(self.h5file.root._v_attrs, "testattr"))
        self.assertEqual(self.h5file.get_node_attr("/", "testattr"), 41)
        self.assertTrue(hasattr(self.h5file.root, "array"))
        self.assertEqual(self.h5file.get_node_attr("/array", "TITLE"), "Array")
        self.assertTrue(hasattr(self.h5file.root, "table"))
        self.assertEqual(self.h5file.get_node_attr("/table", "TITLE"), "Table")
        self.assertEqual(self.h5file.root.array.read(), [1, 2])

        self.assertTrue(hasattr(self.h5file.root._v_attrs, "testattr2"))
        self.assertEqual(self.h5file.get_node_attr("/", "testattr2"), 42)
        self.assertTrue(hasattr(self.h5file.root, "array2"))
        self.assertEqual(self.h5file.get_node_attr(
            "/array2", "TITLE"), "Array2")
        self.assertEqual(self.h5file.root.array2.read(), data)

        self.h5file.close()

        self.assertFalse(os.path.exists(self.h5fname))

    def test_str(self):
        self.h5file = tables.open_file(self.h5fname, mode="w", title="Title",
                                       driver=self.DRIVER,
                                       driver_core_backing_store=0)

        self.h5file.create_array(self.h5file.root, 'array', [1, 2],
                                 title="Array")
        self.h5file.create_table(self.h5file.root, 'table', {'var1': IntCol()},
                                 "Table")
        self.h5file.root._v_attrs.testattr = 41

        # ensure that the __str__ method works even if there is no phisical
        # file on disk (in which case the os.stat operation for date retrieval
        # fails)
        self.assertTrue(str(self.h5file) is not None)

        self.h5file.close()
        self.assertFalse(os.path.exists(self.h5fname))


class QuantizeTestCase(common.TempFileMixin, TestCase):
    mode = "w"
    title = "This is the table title"
    expectedrows = 10
    appendrows = 5

    def setUp(self):
        super(QuantizeTestCase, self).setUp()

        self.data = numpy.linspace(-5., 5., 41)
        self.randomdata = numpy.random.random_sample(1000000)
        self.randomints = numpy.random.random_integers(
            -1000000, 1000000, 1000000).astype('int64')

        self.populateFile()
        self.h5file.close()

        self.quantizeddata_0 = numpy.asarray(
            [-5.] * 2 + [-4.] * 5 + [-3.] * 3 + [-2.] * 5 + [-1.] * 3 +
            [0.] * 5 + [1.] * 3 + [2.] * 5 + [3.] * 3 + [4.] * 5 + [5.] * 2)
        self.quantizeddata_m1 = numpy.asarray(
            [-8.] * 4 + [0.] * 33 + [8.] * 4)

    def populateFile(self):
        root = self.h5file.root
        filters = Filters(complevel=1, complib="blosc",
                          least_significant_digit=1)
        ints = self.h5file.create_carray(root, "integers", Int64Atom(),
                                         (1000000,), filters=filters)
        ints[:] = self.randomints
        floats = self.h5file.create_carray(root, "floats", Float32Atom(),
                                           (1000000,), filters=filters)
        floats[:] = self.randomdata
        data1 = self.h5file.create_carray(root, "data1", Float64Atom(),
                                          (41,), filters=filters)
        data1[:] = self.data
        filters = Filters(complevel=1, complib="blosc",
                          least_significant_digit=0)
        data0 = self.h5file.create_carray(root, "data0", Float64Atom(),
                                          (41,), filters=filters)
        data0[:] = self.data
        filters = Filters(complevel=1, complib="blosc",
                          least_significant_digit=2)
        data2 = self.h5file.create_carray(root, "data2", Float64Atom(),
                                          (41,), filters=filters)
        data2[:] = self.data
        filters = Filters(complevel=1, complib="blosc",
                          least_significant_digit=-1)
        datam1 = self.h5file.create_carray(root, "datam1", Float64Atom(),
                                           (41,), filters=filters)
        datam1[:] = self.data

    def test00_quantizeData(self):
        """Checking the quantize() function."""

        quantized_0 = quantize(self.data, 0)
        quantized_1 = quantize(self.data, 1)
        quantized_2 = quantize(self.data, 2)
        quantized_m1 = quantize(self.data, -1)
        numpy.testing.assert_array_equal(quantized_0, self.quantizeddata_0)
        numpy.testing.assert_array_equal(quantized_1, self.data)
        numpy.testing.assert_array_equal(quantized_2, self.data)
        numpy.testing.assert_array_equal(quantized_m1, self.quantizeddata_m1)

    def test01_quantizeDataMaxError(self):
        """Checking the maximum error introduced by the quantize() function."""

        quantized_0 = quantize(self.randomdata, 0)
        quantized_1 = quantize(self.randomdata, 1)
        quantized_2 = quantize(self.randomdata, 2)
        quantized_m1 = quantize(self.randomdata, -1)

        # assertLess is new in Python 2.7
        #self.assertLess(numpy.abs(quantized_0 - self.randomdata).max(), 0.5)
        #self.assertLess(numpy.abs(quantized_1 - self.randomdata).max(), 0.05)
        #self.assertLess(numpy.abs(quantized_2 - self.randomdata).max(), 0.005)
        #self.assertLess(numpy.abs(quantized_m1 - self.randomdata).max(), 1.)

        self.assertTrue(numpy.abs(quantized_0 - self.randomdata).max() < 0.5)
        self.assertTrue(numpy.abs(quantized_1 - self.randomdata).max() < 0.05)
        self.assertTrue(numpy.abs(quantized_2 - self.randomdata).max() < 0.005)
        self.assertTrue(numpy.abs(quantized_m1 - self.randomdata).max() < 1.)

    def test02_array(self):
        """Checking quantized data as written to disk."""

        self.h5file = tables.open_file(self.h5fname, "r")
        numpy.testing.assert_array_equal(self.h5file.root.data1[:], self.data)
        numpy.testing.assert_array_equal(self.h5file.root.data2[:], self.data)
        numpy.testing.assert_array_equal(self.h5file.root.data0[:],
                                         self.quantizeddata_0)
        numpy.testing.assert_array_equal(self.h5file.root.datam1[:],
                                         self.quantizeddata_m1)
        numpy.testing.assert_array_equal(self.h5file.root.integers[:],
                                         self.randomints)
        self.assertEqual(self.h5file.root.integers[:].dtype,
                         self.randomints.dtype)

        # assertLess is new in Python 2.7
        #self.assertLess(
        #    numpy.abs(self.h5file.root.floats[:] - self.randomdata).max(),
        #    0.05
        #)
        self.assertTrue(
            numpy.abs(self.h5file.root.floats[:] - self.randomdata).max() <
            0.05
        )


def suite():
    import doctest

    theSuite = unittest.TestSuite()
    niter = 1
    # common.heavy = 1 # Uncomment this only for testing purposes!

    for i in range(niter):
        theSuite.addTest(unittest.makeSuite(FiltersCase1))
        theSuite.addTest(unittest.makeSuite(FiltersCase2))
        theSuite.addTest(unittest.makeSuite(FiltersCase10))
        theSuite.addTest(unittest.makeSuite(FiltersCaseBloscBloscLZ))
        theSuite.addTest(unittest.makeSuite(FiltersCaseBloscLZ4))
        theSuite.addTest(unittest.makeSuite(FiltersCaseBloscLZ4HC))
        theSuite.addTest(unittest.makeSuite(FiltersCaseBloscSnappy))
        theSuite.addTest(unittest.makeSuite(FiltersCaseBloscZlib))
        theSuite.addTest(unittest.makeSuite(CopyGroupCase1))
        theSuite.addTest(unittest.makeSuite(CopyGroupCase2))
        theSuite.addTest(unittest.makeSuite(CopyFileCase1))
        theSuite.addTest(unittest.makeSuite(CopyFileCase2))
        theSuite.addTest(unittest.makeSuite(GroupFiltersTestCase))
        theSuite.addTest(unittest.makeSuite(SetBloscMaxThreadsTestCase))
        theSuite.addTest(unittest.makeSuite(FilterTestCase))
        theSuite.addTest(doctest.DocTestSuite(tables.filters))

        theSuite.addTest(unittest.makeSuite(DefaultDriverTestCase))
        theSuite.addTest(unittest.makeSuite(Sec2DriverTestCase))
        theSuite.addTest(unittest.makeSuite(StdioDriverTestCase))
        theSuite.addTest(unittest.makeSuite(CoreDriverTestCase))
        theSuite.addTest(unittest.makeSuite(CoreDriverNoBackingStoreTestCase))
        theSuite.addTest(unittest.makeSuite(SplitDriverTestCase))

        theSuite.addTest(unittest.makeSuite(LogDriverTestCase))
        theSuite.addTest(unittest.makeSuite(DirectDriverTestCase))
        theSuite.addTest(unittest.makeSuite(WindowsDriverTestCase))

        theSuite.addTest(unittest.makeSuite(FamilyDriverTestCase))
        theSuite.addTest(unittest.makeSuite(MultiDriverTestCase))
        theSuite.addTest(unittest.makeSuite(MpioDriverTestCase))
        theSuite.addTest(unittest.makeSuite(MpiPosixDriverTestCase))
        theSuite.addTest(unittest.makeSuite(StreamDriverTestCase))
        theSuite.addTest(unittest.makeSuite(InMemoryCoreDriverTestCase))

        theSuite.addTest(unittest.makeSuite(QuantizeTestCase))

    if common.heavy:
        theSuite.addTest(unittest.makeSuite(CreateTestCase))
        theSuite.addTest(unittest.makeSuite(FiltersCase3))
        theSuite.addTest(unittest.makeSuite(FiltersCase4))
        theSuite.addTest(unittest.makeSuite(FiltersCase5))
        theSuite.addTest(unittest.makeSuite(FiltersCase6))
        theSuite.addTest(unittest.makeSuite(FiltersCase7))
        theSuite.addTest(unittest.makeSuite(FiltersCase8))
        theSuite.addTest(unittest.makeSuite(FiltersCase9))
        theSuite.addTest(unittest.makeSuite(CopyFileCase3))
        theSuite.addTest(unittest.makeSuite(CopyFileCase4))
        theSuite.addTest(unittest.makeSuite(CopyFileCase5))
        theSuite.addTest(unittest.makeSuite(CopyFileCase6))
        theSuite.addTest(unittest.makeSuite(CopyFileCase7))
        theSuite.addTest(unittest.makeSuite(CopyFileCase8))
        theSuite.addTest(unittest.makeSuite(CopyFileCase10))
        theSuite.addTest(unittest.makeSuite(CopyGroupCase3))
        theSuite.addTest(unittest.makeSuite(CopyGroupCase4))
        theSuite.addTest(unittest.makeSuite(CopyGroupCase5))
        theSuite.addTest(unittest.makeSuite(CopyGroupCase6))
        theSuite.addTest(unittest.makeSuite(CopyGroupCase7))
        theSuite.addTest(unittest.makeSuite(CopyGroupCase8))

    return theSuite


if __name__ == '__main__':
    common.parse_argv(sys.argv)
    common.print_versions()
    unittest.main(defaultTest='suite')
