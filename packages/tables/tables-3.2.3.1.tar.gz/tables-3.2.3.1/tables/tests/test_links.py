# -*- coding: utf-8 -*-

########################################################################
#
# License: BSD
# Created: 2009-11-24
# Author: Francesc Alted - faltet@pytables.org
#
# $Id$
#
########################################################################

"""Test module for diferent kind of links under PyTables."""

from __future__ import print_function
import os
import re
import tempfile

import tables
from tables.tests import common
from tables.tests.common import unittest
from tables.tests.common import PyTablesTestCase as TestCase


# Test for hard links
class HardLinkTestCase(common.TempFileMixin, TestCase):

    def setUp(self):
        super(HardLinkTestCase, self).setUp()
        self._createFile()

    def _createFile(self):
        self.h5file.create_array('/', 'arr1', [1, 2])
        group1 = self.h5file.create_group('/', 'group1')
        arr2 = self.h5file.create_array(group1, 'arr2', [1, 2, 3])
        lgroup1 = self.h5file.create_hard_link('/', 'lgroup1', '/group1')
        self.assertTrue(lgroup1 is not None)
        larr1 = self.h5file.create_hard_link(group1, 'larr1', '/arr1')
        self.assertTrue(larr1 is not None)
        larr2 = self.h5file.create_hard_link('/', 'larr2', arr2)
        self.assertTrue(larr2 is not None)

    def test00_create(self):
        """Creating hard links."""

        self._checkEqualityGroup(self.h5file.root.group1,
                                 self.h5file.root.lgroup1,
                                 hardlink=True)
        self._checkEqualityLeaf(self.h5file.root.arr1,
                                self.h5file.root.group1.larr1,
                                hardlink=True)
        self._checkEqualityLeaf(self.h5file.root.lgroup1.arr2,
                                self.h5file.root.larr2,
                                hardlink=True)

    def test01_open(self):
        """Opening a file with hard links."""

        self._reopen()
        self._checkEqualityGroup(self.h5file.root.group1,
                                 self.h5file.root.lgroup1,
                                 hardlink=True)
        self._checkEqualityLeaf(self.h5file.root.arr1,
                                self.h5file.root.group1.larr1,
                                hardlink=True)
        self._checkEqualityLeaf(self.h5file.root.lgroup1.arr2,
                                self.h5file.root.larr2,
                                hardlink=True)

    def test02_removeLeaf(self):
        """Removing a hard link to a Leaf."""

        # First delete the initial link
        self.h5file.root.arr1.remove()
        self.assertTrue('/arr1' not in self.h5file)
        # The second link should still be there
        if common.verbose:
            print("Remaining link:", self.h5file.root.group1.larr1)
        self.assertTrue('/group1/larr1' in self.h5file)
        # Remove the second link
        self.h5file.root.group1.larr1.remove()
        self.assertTrue('/group1/larr1' not in self.h5file)

    def test03_removeGroup(self):
        """Removing a hard link to a Group."""

        if common.verbose:
            print("Original object tree:", self.h5file)
        # First delete the initial link
        self.h5file.root.group1._f_remove(force=True)
        self.assertTrue('/group1' not in self.h5file)
        # The second link should still be there
        if common.verbose:
            print("Remaining link:", self.h5file.root.lgroup1)
            print("Object tree:", self.h5file)
        self.assertTrue('/lgroup1' in self.h5file)
        # Remove the second link
        self.h5file.root.lgroup1._g_remove(recursive=True)
        self.assertTrue('/lgroup1' not in self.h5file)
        if common.verbose:
            print("Final object tree:", self.h5file)


# Test for soft links
class SoftLinkTestCase(common.TempFileMixin, TestCase):

    def setUp(self):
        super(SoftLinkTestCase, self).setUp()
        self._createFile()

    def _createFile(self):
        self.h5file.create_array('/', 'arr1', [1, 2])
        group1 = self.h5file.create_group('/', 'group1')
        arr2 = self.h5file.create_array(group1, 'arr2', [1, 2, 3])
        lgroup1 = self.h5file.create_soft_link('/', 'lgroup1', '/group1')
        self.assertTrue(lgroup1 is not None)
        larr1 = self.h5file.create_soft_link(group1, 'larr1', '/arr1')
        self.assertTrue(larr1 is not None)
        larr2 = self.h5file.create_soft_link('/', 'larr2', arr2)
        self.assertTrue(larr2 is not None)

    def test00_create(self):
        """Creating soft links."""

        self._checkEqualityGroup(self.h5file.root.group1,
                                 self.h5file.root.lgroup1())
        self._checkEqualityLeaf(self.h5file.root.arr1,
                                self.h5file.root.group1.larr1())
        self._checkEqualityLeaf(self.h5file.root.lgroup1().arr2,
                                self.h5file.root.larr2())

    def test01_open(self):
        """Opening a file with soft links."""

        self._reopen()
        self._checkEqualityGroup(self.h5file.root.group1,
                                 self.h5file.root.lgroup1())
        self._checkEqualityLeaf(self.h5file.root.arr1,
                                self.h5file.root.group1.larr1())
        self._checkEqualityLeaf(self.h5file.root.lgroup1().arr2,
                                self.h5file.root.larr2())

    def test02_remove(self):
        """Removing a soft link."""

        # First delete the referred link
        self.h5file.root.arr1.remove()
        self.assertTrue('/arr1' not in self.h5file)
        # The soft link should still be there (but dangling)
        if common.verbose:
            print("Dangling link:", self.h5file.root.group1.larr1)
        self.assertTrue('/group1/larr1' in self.h5file)
        # Remove the soft link itself
        self.h5file.root.group1.larr1.remove()
        self.assertTrue('/group1/larr1' not in self.h5file)

    def test03_copy(self):
        """Copying a soft link."""

        # Copy the link into another location
        root = self.h5file.root
        lgroup1 = root.lgroup1
        lgroup2 = lgroup1.copy('/', 'lgroup2')
        self.assertTrue('/lgroup1' in self.h5file)
        self.assertTrue('/lgroup2' in self.h5file)
        self.assertTrue('lgroup2' in root._v_children)
        self.assertTrue('lgroup2' in root._v_links)
        if common.verbose:
            print("Copied link:", lgroup2)
        # Remove the first link
        lgroup1.remove()
        self._checkEqualityGroup(self.h5file.root.group1,
                                 self.h5file.root.lgroup2())

    def test03_overwrite(self):
        """Overwrite a soft link."""

        # Copy the link into another location
        root = self.h5file.root
        lgroup1 = root.lgroup1
        lgroup2 = lgroup1.copy('/', 'lgroup2')
        lgroup2 = lgroup1.copy('/', 'lgroup2', overwrite=True)
        self.assertTrue('/lgroup1' in self.h5file)
        self.assertTrue('/lgroup2' in self.h5file)
        self.assertTrue('lgroup2' in root._v_children)
        self.assertTrue('lgroup2' in root._v_links)
        if common.verbose:
            print("Copied link:", lgroup2)
        # Remove the first link
        lgroup1.remove()
        self._checkEqualityGroup(self.h5file.root.group1,
                                 self.h5file.root.lgroup2())

    def test04_move(self):
        """Moving a soft link."""

        # Move the link into another location
        lgroup1 = self.h5file.root.lgroup1
        group2 = self.h5file.create_group('/', 'group2')
        lgroup1.move(group2, 'lgroup2')
        lgroup2 = self.h5file.root.group2.lgroup2
        if common.verbose:
            print("Moved link:", lgroup2)
        self.assertTrue('/lgroup1' not in self.h5file)
        self.assertTrue('/group2/lgroup2' in self.h5file)
        self._checkEqualityGroup(self.h5file.root.group1,
                                 self.h5file.root.group2.lgroup2())

    def test05_rename(self):
        """Renaming a soft link."""

        # Rename the link
        lgroup1 = self.h5file.root.lgroup1
        lgroup1.rename('lgroup2')
        lgroup2 = self.h5file.root.lgroup2
        if common.verbose:
            print("Moved link:", lgroup2)
        self.assertTrue('/lgroup1' not in self.h5file)
        self.assertTrue('/lgroup2' in self.h5file)
        self._checkEqualityGroup(self.h5file.root.group1,
                                 self.h5file.root.lgroup2())

    def test06a_relative_path(self):
        """Using soft links with relative paths."""

        # Create new group
        self.h5file.create_group('/group1', 'group3')
        # ... and relative link
        lgroup3 = self.h5file.create_soft_link(
            '/group1', 'lgroup3', 'group3')
        if common.verbose:
            print("Relative path link:", lgroup3)
        self.assertTrue('/group1/lgroup3' in self.h5file)
        self._checkEqualityGroup(self.h5file.root.group1.group3,
                                 self.h5file.root.group1.lgroup3())

    def test06b_relative_path(self):
        """Using soft links with relative paths (./ version)"""

        # Create new group
        self.h5file.create_group('/group1', 'group3')
        # ... and relative link
        lgroup3 = self.h5file.create_soft_link(
            '/group1', 'lgroup3', './group3')
        if common.verbose:
            print("Relative path link:", lgroup3)
        self.assertTrue('/group1/lgroup3' in self.h5file)
        self._checkEqualityGroup(self.h5file.root.group1.group3,
                                 self.h5file.root.group1.lgroup3())

    def test07_walkNodes(self):
        """Checking `walk_nodes` with `classname` option."""

        links = [node._v_pathname for node in
                 self.h5file.walk_nodes('/', classname="Link")]
        if common.verbose:
            print("detected links (classname='Link'):", links)
        self.assertEqual(links, ['/larr2', '/lgroup1', '/group1/larr1'])
        links = [node._v_pathname for node in
                 self.h5file.walk_nodes('/', classname="SoftLink")]
        if common.verbose:
            print("detected links (classname='SoftLink'):", links)
        self.assertEqual(links, ['/larr2', '/lgroup1', '/group1/larr1'])

    def test08__v_links(self):
        """Checking `Group._v_links`."""

        links = [node for node in self.h5file.root._v_links]
        if common.verbose:
            print("detected links (under root):", links)
        self.assertEqual(len(links), 2)
        links = [node for node in self.h5file.root.group1._v_links]
        if common.verbose:
            print("detected links (under /group1):", links)
        self.assertEqual(links, ['larr1'])

    def test09_link_to_link(self):
        """Checking linked links."""

        # Create a link to another existing link
        lgroup2 = self.h5file.create_soft_link(
            '/', 'lgroup2', '/lgroup1')
        # Dereference it once:
        self.assertTrue(lgroup2() is self.h5file.get_node('/lgroup1'))
        if common.verbose:
            print("First dereference is correct:", lgroup2())
        # Dereference it twice:
        self.assertTrue(lgroup2()() is self.h5file.get_node('/group1'))
        if common.verbose:
            print("Second dereference is correct:", lgroup2()())

    def test10_copy_link_to_file(self):
        """Checking copying a link to another file."""

        fname = tempfile.mktemp(".h5")
        h5f = tables.open_file(fname, "a")
        h5f.create_array('/', 'arr1', [1, 2])
        h5f.create_group('/', 'group1')
        lgroup1 = self.h5file.root.lgroup1
        lgroup1_ = lgroup1.copy(h5f.root, 'lgroup1')
        self.assertTrue('/lgroup1' in self.h5file)
        self.assertTrue('/lgroup1' in h5f)
        self.assertTrue(lgroup1_ in h5f)
        if common.verbose:
            print("Copied link:", lgroup1_, 'in:', lgroup1_._v_file.filename)
        h5f.close()
        os.remove(fname)

    def test11_direct_attribute_access(self):
        """Check direct get/set attributes via link-->target.attribute"""

        larr1 = self.h5file.get_node('/lgroup1/larr1')
        arr1 = self.h5file.get_node('/arr1')
        # get
        self.assertTrue(larr1.shape == (2,))
        self.assertTrue(larr1[:] == [1, 2])
        # set
        larr1[0] = -1
        self.assertTrue(arr1[:] == [-1, 2])

    def test12_access_child_node_attributes(self):
        """Check get/set attributes via link-->target.child.attribute"""

        lgroup1 = self.h5file.get_node('/lgroup1')
        arr2 = self.h5file.get_node('/group1/arr2')
        # get child attribute
        self.assertTrue(lgroup1.arr2[:] == [1, 2, 3])
        # set child attribute
        lgroup1.arr2[0] = -1
        self.assertTrue(arr2[:] == [-1, 2, 3])

    def test13_direct_attribute_access_via_chained_softlinks(self):
        """Check get/set access via link2-->link1-->target.child.attribute"""

        lgroup1 = self.h5file.get_node('/lgroup1')
        arr2 = self.h5file.get_node('/group1/arr2')
        # multiple chained links
        l_lgroup1 = self.h5file.create_soft_link('/', 'l_lgroup1', '/lgroup1')
        # get child attribute
        self.assertTrue(l_lgroup1.arr2[:] == [1, 2, 3])
        # set child attribute
        l_lgroup1.arr2[0] = -1
        self.assertTrue(arr2[:] == [-1, 2, 3])

    def test14_child_of_softlink_to_group(self):
        """Create an array whose parent is a softlink to another group"""

        group1 = self.h5file.get_node('/group1')
        lgroup1 = self.h5file.get_node('/lgroup1')
        new_arr = self.h5file.create_array(lgroup1, 'new_arr', obj=[1, 2, 3])
        new_arr2 = self.h5file.get_node('/group1/new_arr')
        self.assertTrue(new_arr2[:] == [1, 2, 3])

    def test_str(self):
        s = str(self.h5file)
        self.assertEqual(len(re.findall('\(SoftLink\)', s)), 3)
        self.assertEqual(len(re.findall('\(dangling\)', s)), 0)

    def test_str_with_dangling_link(self):
        self.h5file.root.group1.arr2.remove()
        s = str(self.h5file)
        self.assertEqual(len(re.findall('\(SoftLink\)', s)), 3)
        self.assertEqual(len(re.findall('\(dangling\)', s)), 1)


# Test for external links
@unittest.skipIf(tables.file._FILE_OPEN_POLICY == 'strict',
                 'FILE_OPEN_POLICY = "strict"')
class ExternalLinkTestCase(common.TempFileMixin, TestCase):

    def setUp(self):
        super(ExternalLinkTestCase, self).setUp()

        self.extfname = tempfile.mktemp(".h5")
        self.exth5file = tables.open_file(self.extfname, "w")
        self._createFile()

    def tearDown(self):
        """Remove ``extfname``."""

        extfname = self.extfname
        self.exth5file.close()
        super(ExternalLinkTestCase, self).tearDown()

        #open_files = tables.file._open_files
        #if self.extfname in open_files:
        #    #assert False
        #    for handler in open_files.get_handlers_by_name(self.extfname):
        #        handler.close()

        os.remove(extfname)   # comment this for debugging purposes only

    def _createFile(self):
        self.h5file.create_array('/', 'arr1', [1, 2])
        group1 = self.h5file.create_group('/', 'group1')
        self.h5file.create_array(group1, 'arr2', [1, 2, 3])

        # The external file
        extarr1 = self.exth5file.create_array('/', 'arr1', [1, 2])
        self.assertTrue(extarr1 is not None)
        extgroup1 = self.exth5file.create_group('/', 'group1')
        extarr2 = self.exth5file.create_array(extgroup1, 'arr2', [1, 2, 3])

        # Create external links
        lgroup1 = self.h5file.create_external_link(
            '/', 'lgroup1', '%s:/group1' % self.extfname)
        self.assertTrue(lgroup1 is not None)
        larr1 = self.h5file.create_external_link(
            group1, 'larr1', '%s:/arr1' % self.extfname)
        self.assertTrue(larr1 is not None)
        larr2 = self.h5file.create_external_link('/', 'larr2', extarr2)
        self.assertTrue(larr2 is not None)

        # Re-open the external file in 'r'ead-only mode
        self.exth5file.close()
        self.exth5file = tables.open_file(self.extfname, "r")

    def test00_create(self):
        """Creating soft links."""

        self._checkEqualityGroup(self.exth5file.root.group1,
                                 self.h5file.root.lgroup1())
        self._checkEqualityLeaf(self.exth5file.root.arr1,
                                self.h5file.root.group1.larr1())
        self._checkEqualityLeaf(self.h5file.root.lgroup1().arr2,
                                self.h5file.root.larr2())

    def test01_open(self):
        """Opening a file with soft links."""

        self._reopen()
        self._checkEqualityGroup(self.exth5file.root.group1,
                                 self.h5file.root.lgroup1())
        self._checkEqualityLeaf(self.exth5file.root.arr1,
                                self.h5file.root.group1.larr1())
        self._checkEqualityLeaf(self.h5file.root.lgroup1().arr2,
                                self.h5file.root.larr2())

    def test02_remove(self):
        """Removing an external link."""

        # Re-open the external file in 'a'ppend mode
        self.exth5file.close()
        self.exth5file = tables.open_file(self.extfname, "a")

        # First delete the referred link
        self.exth5file.root.arr1.remove()
        self.assertTrue('/arr1' not in self.exth5file)

        # The external link should still be there (but dangling)
        if common.verbose:
            print("Dangling link:", self.h5file.root.group1.larr1)
        self.assertTrue('/group1/larr1' in self.h5file)

        # Remove the external link itself
        self.h5file.root.group1.larr1.remove()
        self.assertTrue('/group1/larr1' not in self.h5file)

    def test03_copy(self):
        """Copying an external link."""

        # Copy the link into another location
        root = self.h5file.root
        lgroup1 = root.lgroup1
        lgroup2 = lgroup1.copy('/', 'lgroup2')
        self.assertTrue('/lgroup1' in self.h5file)
        self.assertTrue('/lgroup2' in self.h5file)
        self.assertTrue('lgroup2' in root._v_children)
        self.assertTrue('lgroup2' in root._v_links)
        if common.verbose:
            print("Copied link:", lgroup2)

        # Remove the first link
        lgroup1.remove()
        self._checkEqualityGroup(self.exth5file.root.group1,
                                 self.h5file.root.lgroup2())

    def test03_overwrite(self):
        """Overwrite an external link."""

        # Copy the link into another location
        root = self.h5file.root
        lgroup1 = root.lgroup1
        lgroup2 = lgroup1.copy('/', 'lgroup2')
        lgroup2 = lgroup1.copy('/', 'lgroup2', overwrite=True)
        self.assertTrue('/lgroup1' in self.h5file)
        self.assertTrue('/lgroup2' in self.h5file)
        self.assertTrue('lgroup2' in root._v_children)
        self.assertTrue('lgroup2' in root._v_links)
        if common.verbose:
            print("Copied link:", lgroup2)

        # Remove the first link
        lgroup1.remove()
        self._checkEqualityGroup(self.exth5file.root.group1,
                                 self.h5file.root.lgroup2())

    def test04_move(self):
        """Moving an external link."""

        # Move the link into another location
        lgroup1 = self.h5file.root.lgroup1
        group2 = self.h5file.create_group('/', 'group2')
        lgroup1.move(group2, 'lgroup2')
        lgroup2 = self.h5file.root.group2.lgroup2
        if common.verbose:
            print("Moved link:", lgroup2)
        self.assertTrue('/lgroup1' not in self.h5file)
        self.assertTrue('/group2/lgroup2' in self.h5file)
        self._checkEqualityGroup(self.exth5file.root.group1,
                                 self.h5file.root.group2.lgroup2())

    def test05_rename(self):
        """Renaming an external link."""

        # Rename the link
        lgroup1 = self.h5file.root.lgroup1
        lgroup1.rename('lgroup2')
        lgroup2 = self.h5file.root.lgroup2
        if common.verbose:
            print("Moved link:", lgroup2)
        self.assertTrue('/lgroup1' not in self.h5file)
        self.assertTrue('/lgroup2' in self.h5file)
        self._checkEqualityGroup(self.exth5file.root.group1,
                                 self.h5file.root.lgroup2())

    def test07_walkNodes(self):
        """Checking `walk_nodes` with `classname` option."""

        # Create a new soft link
        self.h5file.create_soft_link('/group1', 'lgroup3', './group3')
        links = [node._v_pathname for node in
                 self.h5file.walk_nodes('/', classname="Link")]
        if common.verbose:
            print("detected links (classname='Link'):", links)
        self.assertEqual(links, ['/larr2', '/lgroup1',
                                 '/group1/larr1', '/group1/lgroup3'])
        links = [node._v_pathname for node in
                 self.h5file.walk_nodes('/', classname="ExternalLink")]
        if common.verbose:
            print("detected links (classname='ExternalLink'):", links)
        self.assertEqual(links, ['/larr2', '/lgroup1', '/group1/larr1'])

    def test08__v_links(self):
        """Checking `Group._v_links`."""

        links = [node for node in self.h5file.root._v_links]
        if common.verbose:
            print("detected links (under root):", links)
        self.assertEqual(len(links), 2)
        links = [node for node in self.h5file.root.group1._v_links]
        if common.verbose:
            print("detected links (under /group1):", links)
        self.assertEqual(links, ['larr1'])

    def test09_umount(self):
        """Checking `umount()` method."""

        link = self.h5file.root.lgroup1
        self.assertTrue(link.extfile is None)

        # Dereference a external node (and hence, 'mount' a file)
        enode = link()
        self.assertTrue(enode is not None)
        self.assertTrue(link.extfile is not None)

        # Umount the link
        link.umount()
        self.assertTrue(link.extfile is None)

    def test10_copy_link_to_file(self):
        """Checking copying a link to another file."""

        h5fname2 = tempfile.mktemp(".h5")
        try:
            with tables.open_file(h5fname2, "a") as h5file2:
                h5file2.create_array('/', 'arr1', [1, 2])
                h5file2.create_group('/', 'group1')
                lgroup1 = self.h5file.root.lgroup1
                lgroup1_ = lgroup1.copy(h5file2.root, 'lgroup1')
                self.assertTrue('/lgroup1' in self.h5file)
                self.assertTrue('/lgroup1' in h5file2)
                self.assertTrue(lgroup1_ in h5file2)
                if common.verbose:
                    print("Copied link:", lgroup1_, 'in:',
                          lgroup1_._v_file.filename)
        finally:
            if os.path.exists(h5fname2):
                os.remove(h5fname2)


def suite():
    """Return a test suite consisting of all the test cases in the module."""

    theSuite = unittest.TestSuite()
    niter = 1
    # common.heavy = 1  # uncomment this only for testing purposes

    for i in range(niter):
        theSuite.addTest(unittest.makeSuite(HardLinkTestCase))
        theSuite.addTest(unittest.makeSuite(SoftLinkTestCase))
        theSuite.addTest(unittest.makeSuite(ExternalLinkTestCase))

    return theSuite


if __name__ == '__main__':
    import sys
    common.parse_argv(sys.argv)
    common.print_versions()
    unittest.main(defaultTest='suite')


## Local Variables:
## mode: python
## py-indent-offset: 4
## tab-width: 4
## fill-column: 72
## End:
