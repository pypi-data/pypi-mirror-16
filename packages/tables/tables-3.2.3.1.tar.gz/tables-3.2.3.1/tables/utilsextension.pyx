# -*- coding: utf-8 -*-

########################################################################
#
# License: BSD
# Created: May 20, 2005
# Author:  Francesc Alted - faltet@pytables.com
#
# $Id$
#
########################################################################

"""Cython utilities for PyTables and HDF5 library."""

import sys
import warnings

try:
  import zlib
  zlib_imported = True
except ImportError:
  zlib_imported = False

import numpy

from tables.description import Description, Col
from tables.misc.enum import Enum
from tables.exceptions import HDF5ExtError
from tables.atom import Atom, EnumAtom

from tables.utils import check_file_access
from tables._past import previous_api

from cpython cimport PY_MAJOR_VERSION
from libc.stdio cimport stderr
from libc.stdlib cimport malloc, free
from libc.string cimport strchr, strcmp, strncmp, strlen
from cpython.bytes cimport PyBytes_Check, PyBytes_FromStringAndSize
from cpython.unicode cimport PyUnicode_DecodeUTF8, PyUnicode_Check

from numpy cimport (import_array, ndarray, dtype,
  npy_int64, PyArray_DescrFromType, npy_intp,
  NPY_BOOL, NPY_STRING, NPY_INT8, NPY_INT16, NPY_INT32, NPY_INT64,
  NPY_UINT8, NPY_UINT16, NPY_UINT32, NPY_UINT64, NPY_FLOAT16, NPY_FLOAT32,
  NPY_FLOAT64, NPY_COMPLEX64, NPY_COMPLEX128)

from definitions cimport (H5ARRAYget_info, H5ARRAYget_ndims,
  H5ATTRfind_attribute, H5ATTRget_attribute_string, H5D_CHUNKED,
  H5D_layout_t, H5Dclose, H5Dget_type, H5Dopen, H5E_DEFAULT,
  H5E_WALK_DOWNWARD, H5E_auto_t, H5E_error_t, H5E_walk_t, H5Eget_msg,
  H5Eprint, H5Eset_auto, H5Ewalk, H5F_ACC_RDONLY, H5Fclose, H5Fis_hdf5,
  H5Fopen, H5Gclose, H5Gopen, H5P_DEFAULT, H5T_ARRAY, H5T_BITFIELD,
  H5T_COMPOUND, H5T_CSET_ASCII, H5T_CSET_UTF8, H5T_C_S1, H5T_DIR_DEFAULT,
  H5T_ENUM, H5T_FLOAT, H5T_IEEE_F32BE, H5T_IEEE_F32LE, H5T_IEEE_F64BE,
  H5T_IEEE_F64LE, H5T_INTEGER, H5T_NATIVE_DOUBLE, H5T_NATIVE_LDOUBLE,
  H5T_NO_CLASS, H5T_OPAQUE,
  H5T_ORDER_BE, H5T_ORDER_LE, H5T_REFERENCE, H5T_STD_B8BE, H5T_STD_B8LE,
  H5T_STD_I16BE, H5T_STD_I16LE, H5T_STD_I32BE, H5T_STD_I32LE, H5T_STD_I64BE,
  H5T_STD_I64LE, H5T_STD_I8BE, H5T_STD_I8LE, H5T_STD_U16BE, H5T_STD_U16LE,
  H5T_STD_U32BE, H5T_STD_U32LE, H5T_STD_U64BE, H5T_STD_U64LE, H5T_STD_U8BE,
  H5T_STD_U8LE, H5T_STRING, H5T_TIME, H5T_UNIX_D32BE, H5T_UNIX_D32LE,
  H5T_UNIX_D64BE, H5T_UNIX_D64LE, H5T_VLEN, H5T_class_t, H5T_sign_t,
  H5Tarray_create, H5Tclose, H5Tcopy, H5Tcreate, H5Tenum_create,
  H5Tenum_insert, H5Tget_array_dims, H5Tget_array_ndims, H5Tget_class,
  H5Tget_member_name, H5Tget_member_type, H5Tget_member_value,
  H5Tget_native_type, H5Tget_nmembers, H5Tget_offset, H5Tget_order,
  H5Tget_precision, H5Tget_sign, H5Tget_size, H5Tget_super, H5Tinsert,
  H5Tis_variable_str, H5Tpack, H5Tset_precision, H5Tset_size, H5Tvlen_create,
  H5Zunregister, FILTER_BLOSC,
  PyArray_Scalar, create_ieee_complex128, create_ieee_complex64,
  create_ieee_float16, create_ieee_complex192, create_ieee_complex256,
  get_len_of_range, get_order, herr_t, hid_t, hsize_t,
  hssize_t, htri_t, is_complex, register_blosc, set_order,
  pt_H5free_memory)


# Platform-dependent types
if sys.byteorder == "little":
  platform_byteorder = H5T_ORDER_LE
  # Standard types, independent of the byteorder
  H5T_STD_B8   = H5T_STD_B8LE
  H5T_STD_I8   = H5T_STD_I8LE
  H5T_STD_I16  = H5T_STD_I16LE
  H5T_STD_I32  = H5T_STD_I32LE
  H5T_STD_I64  = H5T_STD_I64LE
  H5T_STD_U8   = H5T_STD_U8LE
  H5T_STD_U16  = H5T_STD_U16LE
  H5T_STD_U32  = H5T_STD_U32LE
  H5T_STD_U64  = H5T_STD_U64LE
  H5T_IEEE_F32 = H5T_IEEE_F32LE
  H5T_IEEE_F64 = H5T_IEEE_F64LE
  H5T_UNIX_D32  = H5T_UNIX_D32LE
  H5T_UNIX_D64  = H5T_UNIX_D64LE
else:  # sys.byteorder == "big"
  platform_byteorder = H5T_ORDER_BE
  # Standard types, independent of the byteorder
  H5T_STD_B8   = H5T_STD_B8BE
  H5T_STD_I8   = H5T_STD_I8BE
  H5T_STD_I16  = H5T_STD_I16BE
  H5T_STD_I32  = H5T_STD_I32BE
  H5T_STD_I64  = H5T_STD_I64BE
  H5T_STD_U8   = H5T_STD_U8BE
  H5T_STD_U16  = H5T_STD_U16BE
  H5T_STD_U32  = H5T_STD_U32BE
  H5T_STD_U64  = H5T_STD_U64BE
  H5T_IEEE_F32 = H5T_IEEE_F32BE
  H5T_IEEE_F64 = H5T_IEEE_F64BE
  H5T_UNIX_D32  = H5T_UNIX_D32BE
  H5T_UNIX_D64  = H5T_UNIX_D64BE


#----------------------------------------------------------------------------

# Conversion from PyTables string types to HDF5 native types
# List only types that are susceptible of changing byteorder
# (complex & enumerated types are special and should not be listed here)
pttype_to_hdf5 = {
  'int8'   : H5T_STD_I8,   'uint8'  : H5T_STD_U8,
  'int16'  : H5T_STD_I16,  'uint16' : H5T_STD_U16,
  'int32'  : H5T_STD_I32,  'uint32' : H5T_STD_U32,
  'int64'  : H5T_STD_I64,  'uint64' : H5T_STD_U64,
  'float32': H5T_IEEE_F32, 'float64': H5T_IEEE_F64,
  'float96': H5T_NATIVE_LDOUBLE, 'float128': H5T_NATIVE_LDOUBLE,
  'time32' : H5T_UNIX_D32, 'time64' : H5T_UNIX_D64,
}

# Special cases whose byteorder cannot be directly changed
pt_special_kinds = ['complex', 'string', 'enum', 'bool']

# Conversion table from NumPy extended codes prefixes to PyTables kinds
npext_prefixes_to_ptkinds = {
  "S": "string",
  "b": "bool",
  "i": "int",
  "u": "uint",
  "f": "float",
  "c": "complex",
  "t": "time",
  "e": "enum",
}

# Names of HDF5 classes
hdf5_class_to_string = {
  H5T_NO_CLASS  : 'H5T_NO_CLASS',
  H5T_INTEGER   : 'H5T_INTEGER',
  H5T_FLOAT     : 'H5T_FLOAT',
  H5T_TIME      : 'H5T_TIME',
  H5T_STRING    : 'H5T_STRING',
  H5T_BITFIELD  : 'H5T_BITFIELD',
  H5T_OPAQUE    : 'H5T_OPAQUE',
  H5T_COMPOUND  : 'H5T_COMPOUND',
  H5T_REFERENCE : 'H5T_REFERENCE',
  H5T_ENUM      : 'H5T_ENUM',
  H5T_VLEN      : 'H5T_VLEN',
  H5T_ARRAY     : 'H5T_ARRAY',
}


# Depprecated API
PTTypeToHDF5 = pttype_to_hdf5
PTSpecialKinds = pt_special_kinds
NPExtPrefixesToPTKinds = npext_prefixes_to_ptkinds
HDF5ClassToString = hdf5_class_to_string


from numpy import typeDict
cdef int have_float16 = ("float16" in typeDict)


#----------------------------------------------------------------------

# External declarations


# PyTables helper routines.
cdef extern from "utils.h":

  int getLibrary(char *libname) nogil
  object _getTablesVersion()
  #object getZLIBVersionInfo()
  object getHDF5VersionInfo()
  object get_filter_names( hid_t loc_id, char *dset_name)

  H5T_class_t getHDF5ClassID(hid_t loc_id, char *name, H5D_layout_t *layout,
                             hid_t *type_id, hid_t *dataset_id) nogil


# Functions from Blosc
cdef extern from "blosc.h" nogil:
  void blosc_init()
  int blosc_set_nthreads(int nthreads)
  char* blosc_list_compressors()
  int blosc_compcode_to_compname(int compcode, char **compname)
  int blosc_get_complib_info(char *compname, char **complib, char **version)


# @TODO: use the c_string_type and c_string_encoding global directives
#        (new in cython 0.19)
cdef str cstr_to_pystr(const_char* cstring):
  if PY_MAJOR_VERSION > 2:
    pystring = PyUnicode_DecodeUTF8(cstring, strlen(cstring), NULL)
  else:
    pystring = bytes(<char*>cstring)

  return pystring


#----------------------------------------------------------------------
# Initialization code

# The NumPy API requires this function to be called before
# using any NumPy facilities in an extension module.
import_array()

# NaN-aware sorting with NaN as the greatest element
# numpy.isNaN only takes floats, this should work for strings too
cpdef nan_aware_lt(a, b): return a < b or (b != b and a == a)
cpdef nan_aware_le(a, b): return a <= b or b != b
cpdef nan_aware_gt(a, b): return a > b or (a != a and b == b)
cpdef nan_aware_ge(a, b): return a >= b or a != a

def bisect_left(a, x, int lo=0):
  """Return the index where to insert item x in list a, assuming a is sorted.

  The return value i is such that all e in a[:i] have e < x, and all e in
  a[i:] have e >= x.  So if x already appears in the list, i points just
  before the leftmost x already there.

  """

  cdef int mid, hi = len(a)

  lo = 0
  while lo < hi:
    mid = (lo+hi)/2
    if nan_aware_lt(a[mid], x): lo = mid+1
    else: hi = mid
  return lo

def bisect_right(a, x, int lo=0):
  """Return the index where to insert item x in list a, assuming a is sorted.

  The return value i is such that all e in a[:i] have e <= x, and all e in
  a[i:] have e > x.  So if x already appears in the list, i points just
  beyond the rightmost x already there.

  """

  cdef int mid, hi = len(a)

  lo = 0
  while lo < hi:
    mid = (lo+hi)/2
    if nan_aware_lt(x, a[mid]): hi = mid
    else: lo = mid+1
  return lo

cdef register_blosc_():
  cdef char *version
  cdef char *date

  register_blosc(&version, &date)
  compinfo = (version, date)
  free(version)
  free(date)
  if sys.version_info[0] > 2:
    return compinfo[0].decode('ascii'), compinfo[1].decode('ascii')
  else:
    return compinfo

blosc_version = register_blosc_()

# Old versions (<1.4) of the blosc compression library
# rely on unaligned memory access, so they are not functional on some
# platforms (see https://github.com/FrancescAlted/blosc/issues/3 and
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=661286).
# This function has been written by Julian Taylor <jtaylor@ubuntu.com>.
def _arch_without_blosc():
  import platform
  arch = platform.machine().lower()
  for a in ("arm", "sparc", "mips", "aarch64"):
    if a in arch:
      return True
  return False

if blosc_version and blosc_version < ('1', '4') and _arch_without_blosc():
  # Only use bloc compressor on platforms that actually support it.
  H5Zunregister(FILTER_BLOSC)
  blosc_version = None
else:
  blosc_init()  # from 1.2 on, Blosc library must be initialized


# Important: Blosc calls that modifies global variables in Blosc must be
# called from the same extension where Blosc is registered in HDF5.
def set_blosc_max_threads(nthreads):
  """set_blosc_max_threads(nthreads)

  Set the maximum number of threads that Blosc can use.

  This actually overrides the :data:`tables.parameters.MAX_BLOSC_THREADS`
  setting in :mod:`tables.parameters`, so the new value will be effective until
  this function is called again or a new file with a different
  :data:`tables.parameters.MAX_BLOSC_THREADS` value is specified.

  Returns the previous setting for maximum threads.

  """

  return blosc_set_nthreads(nthreads)


setBloscMaxThreads = previous_api(set_blosc_max_threads)


if sys.platform == "win32":
  # We need a different approach in Windows, because it complains when
  # trying to import the extension that is linked with a dynamic library
  # that is not installed in the system.

  # Initialize & register lzo
  if getLibrary("lzo2") == 0 or getLibrary("lzo1") == 0:
    import tables._comp_lzo
    lzo_version = tables._comp_lzo.register_()
  else:
    lzo_version = None

  # Initialize & register bzip2
  if getLibrary("bzip2") == 0 or getLibrary("libbz2") == 0:
    import tables._comp_bzip2
    bzip2_version = tables._comp_bzip2.register_()
  else:
    bzip2_version = None

else:  # Unix systems
  # Initialize & register lzo
  try:
    import tables._comp_lzo
    lzo_version = tables._comp_lzo.register_()
  except ImportError:
    lzo_version = None

  # Initialize & register bzip2
  try:
    import tables._comp_bzip2
    bzip2_version = tables._comp_bzip2.register_()
  except ImportError:
    bzip2_version = None


# End of initialization code
#---------------------------------------------------------------------

# Error handling helpers
# XXX: silence warning about incompatible pointer types
#ctypedef H5E_error_t* const_H5E_error_t_ptr "const H5E_error_t*"
cdef herr_t e_walk_cb(unsigned n, H5E_error_t *err, void *data) with gil:
    cdef object bt = <object>data   # list
    #cdef char major_msg[256]
    #cdef char minor_msg[256]
    #cdef ssize_t msg_len

    if err == NULL:
        return -1

    #msg_len = H5Eget_msg(err.maj_num, NULL, major_msg, 256)
    #if msg_len < 0:
    #    major_msg[0] = '\0'

    #msg_len = H5Eget_msg(err.min_num, NULL, minor_msg, 256)
    #if msg_len < 0:
    #    minor_msg[0] = '\0'

    #msg = "%s (MAJOR: %s, MINOR: %s)" % (
    #                bytes(<char*>err.desc).decode('utf-8'),
    #                bytes(<char*>major_msg).decode('utf-8'),
    #                bytes(<char*>minor_msg).decode('utf-8'))

    msg = bytes(<char*>err.desc).decode('utf-8')

    bt.append((
        bytes(<char*>err.file_name).decode('utf-8'),
        err.line,
        bytes(<char*>err.func_name).decode('utf-8'),
        msg,
    ))

    return 0


def _dump_h5_backtrace():
    cdef object bt = []

    if H5Ewalk(H5E_DEFAULT, H5E_WALK_DOWNWARD, e_walk_cb, <void*>bt) < 0:
        return None

    return bt


# Initialization of the _dump_h5_backtrace method of HDF5ExtError.
# The unusual machinery is needed in order to avoid cirdular dependencies
# between modules.
HDF5ExtError._dump_h5_backtrace = _dump_h5_backtrace


def silence_hdf5_messages(silence=True):
    """silence_hdf5_messages(silence=True)

    Silence (or re-enable) messages from the HDF5 C library.

    The *silence* parameter can be used control the behaviour and reset
    the standard HDF5 logging.

    .. versionadded:: 2.4

    """
    cdef herr_t err
    if silence:
        err = H5Eset_auto(H5E_DEFAULT, NULL, NULL)
    else:
        err = H5Eset_auto(H5E_DEFAULT, <H5E_auto_t>H5Eprint, stderr)
    if err < 0:
        raise HDF5ExtError("unable to configure HDF5 internal error handling")


silenceHDF5Messages = previous_api(silence_hdf5_messages)


# Disable automatic HDF5 error logging
silence_hdf5_messages()


def _broken_hdf5_long_double():
    # HDF5 < 1.8.12 has a bug that prevents correct identification of the
    # long double data type when the code is built with gcc 4.8.
    # See also: http://hdf-forum.184993.n3.nabble.com/Issues-with-H5T-NATIVE-LDOUBLE-tt4026450.html

    return H5Tget_order(H5T_NATIVE_DOUBLE) != H5Tget_order(H5T_NATIVE_LDOUBLE)


# Helper functions
cdef hsize_t *malloc_dims(object pdims):
  """Return a malloced hsize_t dims from a python pdims."""

  cdef int i, rank
  cdef hsize_t *dims

  dims = NULL
  rank = len(pdims)
  if rank > 0:
    dims = <hsize_t *>malloc(rank * sizeof(hsize_t))
    for i from 0 <= i < rank:
      dims[i] = pdims[i]
  return dims


cdef hid_t get_native_float_type(hid_t type_id) nogil:
  """Get a native type of an HDF5 float type.

  This functionn also handles half precision (float16) data type.

  """

  cdef hid_t  native_type_id
  cdef size_t precision

  precision = H5Tget_precision(type_id)

  if precision == 16 and have_float16:
    native_type_id = create_ieee_float16(NULL)
  else:
    native_type_id = H5Tget_native_type(type_id, H5T_DIR_DEFAULT)

  return native_type_id


# This is a re-implementation of a working H5Tget_native_type for nested
# compound types.  I should report the flaw to THG as soon as possible.
# F. Alted 2009-08-19
cdef hid_t get_nested_native_type(hid_t type_id) nogil:
  """Get a native nested type of an HDF5 type.

  In addition, it also recursively remove possible padding on type_id,
  i.e. it acts as a combination of H5Tget_native_type and H5Tpack.

  """

  cdef hid_t   tid, tid2
  cdef hid_t   member_type_id, native_type_id
  cdef hsize_t nfields
  cdef H5T_class_t class_id
  cdef size_t  offset, itemsize, itemsize1
  cdef char    *colname
  cdef int     i

  # Get the itemsize
  itemsize1 = H5Tget_size(type_id)
  # Build a new type container
  tid = H5Tcreate(H5T_COMPOUND, itemsize1)

  offset = 0
  # Get the number of members
  nfields = H5Tget_nmembers(type_id)
  # Iterate thru the members
  for i from 0 <= i < nfields:
    # Get the member name
    colname = H5Tget_member_name(type_id, i)
    # Get the member type
    member_type_id = H5Tget_member_type(type_id, i)
    # Get the HDF5 class
    class_id = H5Tget_class(member_type_id)
    if class_id == H5T_COMPOUND:
      native_tid = get_nested_native_type(member_type_id)
    else:
      if class_id == H5T_FLOAT:
        native_tid = get_native_float_type(member_type_id)
      else:
        native_tid = H5Tget_native_type(member_type_id, H5T_DIR_DEFAULT)
    H5Tinsert(tid, colname, offset, native_tid)
    itemsize = H5Tget_size(native_tid)
    offset = offset + itemsize
    # Release resources
    H5Tclose(native_tid)
    H5Tclose(member_type_id)
    pt_H5free_memory(colname)

  # Correct the type size in case the memory type size is less
  # than the type in-disk (probably due to reading native HDF5
  # files written with tools allowing field padding)
  if H5Tget_size(tid) > offset:
    H5Tset_size(tid, offset)

  return tid


# This routine is more complex than required because HDF5 1.6.x does
# not implement support for H5Tget_native_type with some types, like
# H5T_BITFIELD and probably others.  When 1.8.x would be a requisite,
# this can be simplified.
cdef hid_t get_native_type(hid_t type_id) nogil:
  """Get the native type of a HDF5 type."""

  cdef H5T_class_t class_id, super_class_id
  cdef hid_t native_type_id = 0, super_type_id, native_super_type_id
  cdef int rank
  cdef hsize_t *dims

  class_id = H5Tget_class(type_id)
  if class_id == H5T_COMPOUND:
    # XXX It turns out that HDF5 does not correctly implement
    # H5Tget_native_type on nested compounds types.  I should
    # report this to THG.
    #
    # *Note*: the next call *combines* the effect of H5Tget_native_type and
    # H5Tpack, and both effects are needed.  Have this in mind if you
    # ever wants to replace get_nested_native_type by native HDF5 calls.
    # F. Alted  2009-08-19
    return get_nested_native_type(type_id)

  elif class_id in (H5T_ARRAY, H5T_VLEN):
    # Get the array base component
    super_type_id = H5Tget_super(type_id)
    # Get the class
    super_class_id = H5Tget_class(super_type_id)
    if super_class_id == H5T_FLOAT:
        # replicate the logic of H5Tget_native_type for H5T_ARRAY and
        # H5T_VLEN taking into account extended floating point types
        # XXX: HDF5 error check
        native_super_type_id = get_native_float_type(super_type_id)
        H5Tclose(super_type_id)
        if class_id == H5T_ARRAY:
            rank = H5Tget_array_ndims(type_id)
            dims = <hsize_t *>malloc(rank * sizeof(hsize_t))
            H5Tget_array_dims(type_id, dims)
            native_type_id = H5Tarray_create(native_super_type_id, rank, dims)
            free(dims)
            H5Tclose(native_super_type_id)
            return native_type_id
        elif class_id == H5T_VLEN:
            native_type_id = H5Tvlen_create(native_super_type_id)
            H5Tclose(native_super_type_id)
            return native_type_id
    class_id = super_class_id
    H5Tclose(super_type_id)

  if class_id == H5T_FLOAT:
    native_type_id = get_native_float_type(type_id)
  elif class_id in (H5T_INTEGER, H5T_ENUM):
    native_type_id = H5Tget_native_type(type_id, H5T_DIR_DEFAULT)
  else:
    # Fixing the byteorder for other types shouldn't be needed.
    # More in particular, H5T_TIME is not managed yet by HDF5 and so this
    # has to be managed explicitely inside the PyTables extensions.
    # Regarding H5T_BITFIELD, well, I'm not sure if changing the byteorder
    # of this is a good idea at all.
    native_type_id = H5Tcopy(type_id)

  return native_type_id


def encode_filename(object filename):
  """Return the encoded filename in the filesystem encoding."""

  cdef bytes encname

  if isinstance(filename, (unicode, numpy.str_)):
#  if type(filename) is unicode:
    encoding = sys.getfilesystemencoding()
    encname = filename.encode(encoding, 'replace')
  else:
    encname = filename

  return encname


# Main functions
def is_hdf5_file(object filename):
  """is_hdf5_file(filename)

  Determine whether a file is in the HDF5 format.

  When successful, it returns a true value if the file is an HDF5
  file, false otherwise.  If there were problems identifying the file,
  an HDF5ExtError is raised.

  """

  # Check that the file exists and is readable.
  check_file_access(filename)

  # Encode the filename in case it is unicode
  encname = encode_filename(filename)

  ret = H5Fis_hdf5(encname)
  if ret < 0:
    raise HDF5ExtError("problems identifying file ``%s``" % (filename,))
  return ret > 0


isHDF5File = previous_api(is_hdf5_file)


def is_pytables_file(object filename):
  """is_pytables_file(filename)

  Determine whether a file is in the PyTables format.

  When successful, it returns the format version string if the file is a
  PyTables file, None otherwise.  If there were problems identifying the
  file, an HDF5ExtError is raised.

  """

  cdef hid_t file_id
  cdef object isptf = None  # A PYTABLES_FORMAT_VERSION attribute was not found

  if is_hdf5_file(filename):
    # Encode the filename in case it is unicode
    encname = encode_filename(filename)
    # The file exists and is HDF5, that's ok
    # Open it in read-only mode
    file_id = H5Fopen(encname, H5F_ACC_RDONLY, H5P_DEFAULT)
    isptf = read_f_attr(file_id, 'PYTABLES_FORMAT_VERSION')
    # Close the file
    H5Fclose(file_id)

    # system attributes should always be str
    if PY_MAJOR_VERSION < 3 and PyUnicode_Check(isptf):
        isptf = isptf.encode()
    elif PY_MAJOR_VERSION > 2 and PyBytes_Check(isptf):
        isptf = isptf.decode('utf-8')

  return isptf


isPyTablesFile = previous_api(is_pytables_file)


def get_hdf5_version():
  """Get the underlying HDF5 library version"""

  return getHDF5VersionInfo()[1]


getHDF5Version = previous_api(get_hdf5_version)


def get_pytables_version():
  """Return this extension version."""

  return _getTablesVersion()

getPyTablesVersion = previous_api(get_pytables_version)


def which_lib_version(str name):
  """which_lib_version(name)

  Get version information about a C library.

  If the library indicated by name is available, this function returns a
  3-tuple containing the major library version as an integer, its full version
  as a string, and the version date as a string. If the library is not
  available, None is returned.

  The currently supported library names are hdf5, zlib, lzo, bzip2, and blosc. If
  another name is given, a ValueError is raised.

  """

  cdef char *cname = NULL
  cdef bytes encoded_name

  encoded_name = name.encode('utf-8')
  # get the C pointer
  cname = encoded_name

  libnames = ('hdf5', 'zlib', 'lzo', 'bzip2', 'blosc')

  if strcmp(cname, "hdf5") == 0:
    binver, strver = getHDF5VersionInfo()
    return (binver, strver, None)     # Should be always available
  elif strcmp(cname, "zlib") == 0:
    if zlib_imported:
      return (1, zlib.ZLIB_VERSION, None)
  elif strcmp(cname, "lzo") == 0:
    if lzo_version:
      (lzo_version_string, lzo_version_date) = lzo_version
      return (lzo_version, lzo_version_string, lzo_version_date)
  elif strcmp(cname, "bzip2") == 0:
    if bzip2_version:
      (bzip2_version_string, bzip2_version_date) = bzip2_version
      return (bzip2_version, bzip2_version_string, bzip2_version_date)
  elif strncmp(cname, "blosc", 5) == 0:
    if blosc_version:
      (blosc_version_string, blosc_version_date) = blosc_version
      return (blosc_version, blosc_version_string, blosc_version_date)
  else:
    raise ValueError("asked version of unsupported library ``%s``; "
                     "supported library names are ``%s``" % (name, libnames))

  # A supported library was specified, but no version is available.
  return None


whichLibVersion = previous_api(which_lib_version)


# A function returning all the compressors supported by local Blosc
def blosc_compressor_list():
  """
  blosc_compressor_list()

  Returns a list of compressors available in the Blosc build.

  Parameters
  ----------
  None

  Returns
  -------
  out : list
      The list of names.
  """
  list_compr = blosc_list_compressors().decode()
  clist = [str(cname) for cname in list_compr.split(',')]
  return clist


# Convert compressor code to compressor name
def blosc_compcode_to_compname_(compcode):
  """
  blosc_compcode_to_compname()

  Returns the compressor name associated with compressor code.

  Parameters
  ----------
  None

  Returns
  -------
  out : string
      The name of the compressor.
  """
  cdef char *cname
  cdef object compname

  compname = b"unknown (report this to developers)"
  if blosc_compcode_to_compname(compcode, &cname) >= 0:
    compname = cname
  return compname.decode()


def blosc_get_complib_info_():
  """Get info from compression libraries included in the current build
  of blosc.

  Returns a mapping containing the compressor names as keys and the
  tuple (complib, version) as values.

  """

  cdef char *complib, *version

  cinfo = {}
  for name in blosc_list_compressors().split(b','):
    ret = blosc_get_complib_info(name, &complib, &version)
    if ret < 0:
      continue
    if isinstance(name, str):
      cinfo[name] = (complib, version)
    else:
      cinfo[name.decode()] = (complib.decode(), version.decode())
    free(complib)
    free(version)

  return cinfo


def which_class(hid_t loc_id, object name):
  """Detects a class ID using heuristics."""

  cdef H5T_class_t  class_id
  cdef H5D_layout_t layout
  cdef hsize_t      nfields
  cdef char         *field_name1
  cdef char         *field_name2
  cdef int          i
  cdef hid_t        type_id, dataset_id
  cdef object       classId
  cdef int          rank
  cdef hsize_t      *dims
  cdef hsize_t      *maxdims
  cdef char         byteorder[11]  # "irrelevant" fits easily here
  cdef bytes        encoded_name

  if isinstance(name, unicode):
      encoded_name = name.encode('utf-8')
  else:
      encoded_name = name

  classId = "UNSUPPORTED"  # default value
  # Get The HDF5 class for the datatype in this dataset
  class_id = getHDF5ClassID(loc_id, encoded_name, &layout, &type_id,
                            &dataset_id)
  # Check if this a dataset of supported classtype for ARRAY
  if  ((class_id == H5T_INTEGER)  or
       (class_id == H5T_FLOAT)    or
       (class_id == H5T_BITFIELD) or
       (class_id == H5T_TIME)     or
       (class_id == H5T_ENUM)     or
       (class_id == H5T_STRING)   or
       (class_id == H5T_ARRAY)):
    if layout == H5D_CHUNKED:
      if H5ARRAYget_ndims(dataset_id, &rank) < 0:
        raise HDF5ExtError("Problems getting ndims.")
      dims = <hsize_t *>malloc(rank * sizeof(hsize_t))
      maxdims = <hsize_t *>malloc(rank * sizeof(hsize_t))
      if H5ARRAYget_info(dataset_id, type_id, dims, maxdims,
                         &class_id, byteorder) < 0:
        raise HDF5ExtError("Unable to get array info.")
      classId = "CARRAY"
      # Check whether some dimension is enlargeable
      for i in range(rank):
        if maxdims[i] == -1:
          classId = "EARRAY"
          break
      free(<void *>dims)
      free(<void *>maxdims)
    else:
      classId = "ARRAY"

  elif class_id == H5T_COMPOUND:
    # check whether the type is complex or not
    iscomplex = False
    nfields = H5Tget_nmembers(type_id)
    if nfields == 2:
      field_name1 = H5Tget_member_name(type_id, 0)
      field_name2 = H5Tget_member_name(type_id, 1)
      # The pair ("r", "i") is for PyTables. ("real", "imag") for Octave.
      if ( (strcmp(field_name1, "real") == 0 and
            strcmp(field_name2, "imag") == 0) or
           (strcmp(field_name1, "r") == 0 and
            strcmp(field_name2, "i") == 0) ):
        iscomplex = True
      pt_H5free_memory(<void *>field_name1)
      pt_H5free_memory(<void *>field_name2)
    if layout == H5D_CHUNKED:
      if iscomplex:
        classId = "CARRAY"
      else:
        classId = "TABLE"
    else:  # Not chunked case
      # Octave saves complex arrays as non-chunked tables
      # with two fields: "real" and "imag"
      # Francesc Alted 2005-04-29
      # Get number of records
      if iscomplex:
        classId = "ARRAY"  # It is probably an Octave complex array
      else:
        # Added to support non-chunked tables
        classId = "TABLE"  # A test for supporting non-growable tables

  elif class_id == H5T_VLEN:
    if layout == H5D_CHUNKED:
      classId = "VLARRAY"

  # Release the datatype.
  H5Tclose(type_id)

  # Close the dataset.
  H5Dclose(dataset_id)

  # Fallback
  return classId


whichClass = previous_api(which_class)


def get_nested_field(recarray, fieldname):
  """Get the maybe nested field named `fieldname` from the `recarray`.

  The `fieldname` may be a simple field name or a nested field name
  with slah-separated components.

  """

  cdef bytes name = fieldname.encode('utf-8')
  try:
    if strchr(<char *>name, 47) != NULL:   # ord('/') == 47
      # It may be convenient to implement this way of descending nested
      # fields into the ``__getitem__()`` method of a subclass of
      # ``numpy.ndarray``.  -- ivb
      field = recarray
      for nfieldname in fieldname.split('/'):
        field = field[nfieldname]
    else:
      # Faster method for non-nested columns
      field = recarray[fieldname]
  except KeyError:
    raise KeyError("no such column: %s" % (fieldname,))
  return field


getNestedField = previous_api(get_nested_field)


def read_f_attr(hid_t file_id, str attr_name):
  """Read PyTables file attributes (i.e. in root group).

  Returns the value of the `attr_name` attribute in root group, or `None`
  if it does not exist.  This call cannot fail.

  """

  cdef size_t size
  cdef char *attr_value
  cdef int cset = H5T_CSET_ASCII
  cdef object retvalue
  cdef bytes encoded_attr_name
  cdef char *c_attr_name = NULL

  encoded_attr_name = attr_name.encode('utf-8')
  # Get the C pointer
  c_attr_name = encoded_attr_name

  attr_value = NULL
  retvalue = None
  # Check if attribute exists
  if H5ATTRfind_attribute(file_id, c_attr_name):
    # Read the attr_name attribute
    size = H5ATTRget_attribute_string(file_id, c_attr_name, &attr_value, &cset)
    if size == 0:
      if cset == H5T_CSET_UTF8:
        retvalue = numpy.unicode_(u'')
      else:
        retvalue = numpy.bytes_(b'')
    else:
      retvalue = <bytes>(attr_value).rstrip(b'\x00')
      if cset == H5T_CSET_UTF8:
        retvalue = retvalue.decode('utf-8')
        retvalue = numpy.str_(retvalue)
      else:
        retvalue = numpy.bytes_(retvalue)     # bytes

    # Important to release attr_value, because it has been malloc'ed!
    if attr_value:
      free(attr_value)

  return retvalue


def get_filters(parent_id, name):
  """Get a dictionary with the filter names and cd_values"""

  cdef bytes encoded_name

  encoded_name = name.encode('utf-8')

  return get_filter_names(parent_id, encoded_name)


getFilters = previous_api(get_filters)


# This is used by several <Leaf>._convert_types() methods.
def get_type_enum(hid_t h5type):
  """_getTypeEnum(h5type) -> hid_t

  Get the native HDF5 enumerated type of `h5type`.

  If `h5type` is an enumerated type, it is returned.  If it is a
  variable-length type with an enumerated base type, this is returned.  If it
  is a multi-dimensional type with an enumerated base type, this is returned.
  Else, a ``TypeError`` is raised.

  """

  cdef H5T_class_t typeClass
  cdef hid_t enumId, enumId2

  typeClass = H5Tget_class(h5type)
  if typeClass < 0:
    raise HDF5ExtError("failed to get class of HDF5 type")

  if typeClass == H5T_ENUM:
    # Get the native type (in order to do byteorder conversions automatically)
    enumId = H5Tget_native_type(h5type, H5T_DIR_DEFAULT)
  elif typeClass in (H5T_ARRAY, H5T_VLEN):
    # The field is multi-dimensional or variable length.
    enumId2 = H5Tget_super(h5type)
    enumId = get_type_enum(enumId2)
    H5Tclose(enumId2)
  else:
    raise TypeError(
      "enumerated values can not be stored using the given type")
  return enumId

getTypeEnum = previous_api(get_type_enum)


def enum_from_hdf5(hid_t enumId, str byteorder):
  """enum_from_hdf5(enumId) -> (Enum, npType)

  Convert an HDF5 enumerated type to a PyTables one.

  This function takes an HDF5 enumerated type and returns an `Enum`
  instance built from that, and the NumPy type used to encode it.

  """

  cdef hid_t  baseId
  cdef int    nelems, npenum, i
  cdef void   *rbuf
  cdef char   *ename
  cdef ndarray npvalue
  cdef object dtype
  cdef str pyename

  # Find the base type of the enumerated type, and get the atom
  baseId = H5Tget_super(enumId)
  atom = atom_from_hdf5_type(baseId)
  H5Tclose(baseId)
  if atom.kind not in ('int', 'uint'):
    raise NotImplementedError("sorry, only integer concrete values are "
                              "supported at this moment")

  dtype = atom.dtype
  npvalue = numpy.array((0,), dtype=dtype)
  rbuf = npvalue.data

  # Get the name and value of each of the members
  # and put the pair in `enumDict`.
  enumDict = {}

  nelems = H5Tget_nmembers(enumId)
  if enumId < 0:
    raise HDF5ExtError(
      "failed to get element count of HDF5 enumerated type")

  for i from 0 <= i < nelems:
    ename = H5Tget_member_name(enumId, i)
    if ename == NULL:
      raise HDF5ExtError(
        "failed to get element name from HDF5 enumerated type")

    pyename = cstr_to_pystr(ename)

    pt_H5free_memory(ename)

    if H5Tget_member_value(enumId, i, rbuf) < 0:
      raise HDF5ExtError(
        "failed to get element value from HDF5 enumerated type")

    enumDict[pyename] = npvalue[0]  # converted to NumPy scalar

  # Build an enumerated type from `enumDict` and return it.
  return Enum(enumDict), dtype


enumFromHDF5 = previous_api(enum_from_hdf5)


def enum_to_hdf5(object enum_atom, str byteorder):
  """Convert a PyTables enumerated type to an HDF5 one.

  This function creates an HDF5 enumerated type from the information
  contained in `enumAtom` (an ``Atom`` object), with the specified
  `byteorder` (a string).  The resulting HDF5 enumerated type is
  returned.

  """

  cdef bytes   name
  cdef hid_t   base_id, enum_id
  cdef long    bytestride, i
  cdef void    *rbuffer
  cdef void    *rbuf
  cdef ndarray values
  cdef object  base_atom

  # Get the base HDF5 type and create the enumerated type.
  base_atom = Atom.from_dtype(enum_atom.dtype.base)
  base_id = atom_to_hdf5_type(base_atom, byteorder)

  try:
    enum_id = H5Tenum_create(base_id)
    if enum_id < 0:
      raise HDF5ExtError("failed to create HDF5 enumerated type")
  finally:
    if H5Tclose(base_id) < 0:
      raise HDF5ExtError("failed to close HDF5 base type")

  # Set the name and value of each of the members.
  names = enum_atom._names
  values = enum_atom._values
  bytestride = values.strides[0]
  rbuffer = values.data

  i = names.index(enum_atom._defname)
  idx = list(range(len(names)))
  idx.pop(i)
  idx.insert(0, i)

  for i in idx:
    name = names[i].encode('utf-8')
    rbuf = <void *>(<char *>rbuffer + bytestride * i)
    if H5Tenum_insert(enum_id, name, rbuf) < 0:
      e = HDF5ExtError("failed to insert value into HDF5 enumerated type")
      if H5Tclose(enum_id) < 0:
        raise HDF5ExtError("failed to close HDF5 enumerated type")
      raise e

  # Return the new, open HDF5 enumerated type.
  return enum_id


enumToHDF5 = previous_api(enum_to_hdf5)


def atom_to_hdf5_type(atom, str byteorder):
  cdef hid_t   tid = -1
  cdef hsize_t *dims = NULL
  cdef bytes   encoded_byteorder
  cdef char    *cbyteorder = NULL

  encoded_byteorder = byteorder.encode('utf-8')
  # Get the C pointer
  cbyteorder = encoded_byteorder

  # Create the base HDF5 type
  if atom.type in pttype_to_hdf5:
    tid = H5Tcopy(pttype_to_hdf5[atom.type])
    # Fix the byteorder
    if atom.kind != 'time':
      set_order(tid, cbyteorder)
  elif atom.type == 'float16':
    tid = create_ieee_float16(cbyteorder)
  elif atom.kind in pt_special_kinds:
    # Special cases (the byteorder doesn't need to be fixed afterwards)
    if atom.type == 'complex64':
      tid = create_ieee_complex64(cbyteorder)
    elif atom.type == 'complex128':
      tid = create_ieee_complex128(cbyteorder)
    elif atom.type == 'complex192':
      tid = create_ieee_complex192(cbyteorder)
    elif atom.type == 'complex256':
      tid = create_ieee_complex256(cbyteorder)
    elif atom.kind == 'string':
      tid = H5Tcopy(H5T_C_S1);
      H5Tset_size(tid, atom.itemsize)
    elif atom.kind == 'bool':
      tid = H5Tcopy(H5T_STD_B8);
    elif atom.kind == 'enum':
      tid = enum_to_hdf5(atom, byteorder)
  else:
    raise TypeError("Invalid type for atom %s" % (atom,))
  # Create an H5T_ARRAY in case of non-scalar atoms
  if atom.shape != ():
    dims = malloc_dims(atom.shape)
    tid2 = H5Tarray_create(tid, len(atom.shape), dims)
    free(dims)
    H5Tclose(tid)
    tid = tid2

  return tid


AtomToHDF5Type = previous_api(atom_to_hdf5_type)


def load_enum(hid_t type_id):
  """load_enum() -> (Enum, npType)

  Load the enumerated HDF5 type associated with this type_id.

  It returns an `Enum` instance built from that, and the
  NumPy type used to encode it.

  """

  cdef hid_t enumId
  cdef char c_byteorder[11]  # "irrelevant" fits well here
  cdef str byteorder

  # Get the enumerated type
  enumId = get_type_enum(type_id)

  # Get the byteorder
  get_order(type_id, c_byteorder)
  byteorder = cstr_to_pystr(c_byteorder)
  # Get the Enum and NumPy types and close the HDF5 type.
  try:
    return enum_from_hdf5(enumId, byteorder)
  finally:
    # (Yes, the ``finally`` clause *is* executed.)
    if H5Tclose(enumId) < 0:
      raise HDF5ExtError("failed to close HDF5 enumerated type")


loadEnum = previous_api(load_enum)


def hdf5_to_np_nested_type(hid_t type_id):
  """Given a HDF5 `type_id`, return a dtype string representation of it."""

  cdef hid_t   member_type_id
  cdef hsize_t nfields
  cdef int     i
  cdef char    *c_colname
  cdef H5T_class_t class_id
  cdef object  desc
  cdef str     colname

  desc = {}
  # Get the number of members
  nfields = H5Tget_nmembers(type_id)
  # Iterate thru the members
  for i from 0 <= i < nfields:
    # Get the member name
    c_colname = H5Tget_member_name(type_id, i)
    colname = cstr_to_pystr(c_colname)

    # Get the member type
    member_type_id = H5Tget_member_type(type_id, i)

    # Get the HDF5 class
    class_id = H5Tget_class(member_type_id)
    if class_id == H5T_COMPOUND and not is_complex(member_type_id):
      desc[colname] = hdf5_to_np_nested_type(member_type_id)
      desc[colname]["_v_pos"] = i  # Remember the position
    else:
      atom = atom_from_hdf5_type(member_type_id, pure_numpy_types=True)
      desc[colname] = Col.from_atom(atom, pos=i)

    # Release resources
    H5Tclose(member_type_id)
    pt_H5free_memory(c_colname)

  return desc


HDF5ToNPNestedType = previous_api(hdf5_to_np_nested_type)


def hdf5_to_np_ext_type(hid_t type_id, pure_numpy_types=True, atom=False):
  """Map the atomic HDF5 type to a string repr of NumPy extended codes.

  If `pure_numpy_types` is true, detected HDF5 types that does not match pure
  NumPy types will raise a ``TypeError`` exception.  If not, HDF5 types like
  TIME, VLEN or ENUM are passed through.

  If `atom` is true, the resulting repr is meant for atoms.  If not, the
  result is meant for attributes.

  Returns the string repr of type and its shape.  The exception is for
  compounds types, that returns a NumPy dtype and shape instead.

  """

  cdef H5T_sign_t  sign
  cdef hid_t       super_type_id, native_type_id
  cdef H5T_class_t class_id
  cdef size_t      itemsize
  cdef object      stype, shape, shape2
  cdef hsize_t     *dims

  # default shape
  shape = ()
  # Get the HDF5 class
  class_id = H5Tget_class(type_id)
  # Get the itemsize
  itemsize = H5Tget_size(type_id)

  if class_id == H5T_BITFIELD:
    stype = "b1"
  elif class_id == H5T_INTEGER:
    # Get the sign
    sign = H5Tget_sign(type_id)
    if (sign > 0):
      stype = "i%s" % itemsize
    else:
      stype = "u%s" % itemsize
  elif class_id == H5T_FLOAT:
    stype = "f%s" % itemsize
  elif class_id ==  H5T_COMPOUND:
    if is_complex(type_id):
      stype = "c%s" % itemsize
    else:
      if atom:
        raise TypeError("the HDF5 class ``%s`` is not supported yet"
                        % hdf5_class_to_string[class_id])
      # Recursively remove possible padding on type_id.
      native_type_id = get_nested_native_type(type_id)
      desc = Description(hdf5_to_np_nested_type(native_type_id))
      # stype here is not exactly a string, but the NumPy dtype factory
      # will deal with this.
      stype = desc._v_dtype
      H5Tclose(native_type_id)
  elif class_id == H5T_STRING:
    if H5Tis_variable_str(type_id):
      raise TypeError("variable length strings are not supported yet")
    stype = "S%s" % itemsize
  elif class_id == H5T_TIME:
    if pure_numpy_types:
      raise TypeError("the HDF5 class ``%s`` is not supported yet"
                      % hdf5_class_to_string[class_id])
    stype = "t%s" % itemsize
  elif class_id == H5T_ENUM:
    if pure_numpy_types:
      raise TypeError("the HDF5 class ``%s`` is not supported yet"
                      % hdf5_class_to_string[class_id])
    stype = "e"
  elif class_id == H5T_VLEN:
    if pure_numpy_types:
      raise TypeError("the HDF5 class ``%s`` is not supported yet"
                      % hdf5_class_to_string[class_id])
    # Get the variable length base component
    super_type_id = H5Tget_super(type_id)
    # Find the super member format
    stype, shape = hdf5_to_np_ext_type(super_type_id, pure_numpy_types)
    # Release resources
    H5Tclose(super_type_id)
  elif class_id == H5T_ARRAY:
    # Get the array base component
    super_type_id = H5Tget_super(type_id)
    # Find the super member format
    stype, shape2 = hdf5_to_np_ext_type(super_type_id, pure_numpy_types)
    # Get shape
    shape = []
    ndims = H5Tget_array_ndims(type_id)
    dims = <hsize_t *>malloc(ndims * sizeof(hsize_t))
    H5Tget_array_dims(type_id, dims)
    for i from 0 <= i < ndims:
      shape.append(<int>dims[i])  # cast to avoid long representation (i.e. 2L)
    shape = tuple(shape)
    # Release resources
    free(dims)
    H5Tclose(super_type_id)
  else:
    # Other types are not supported yet
    raise TypeError("the HDF5 class ``%s`` is not supported yet"
                    % hdf5_class_to_string[class_id])

  return stype, shape


HDF5ToNPExtType = previous_api(hdf5_to_np_ext_type)


def atom_from_hdf5_type(hid_t type_id, pure_numpy_types=False):
  """Get an atom from a type_id.

  See `hdf5_to_np_ext_type` for an explanation of the `pure_numpy_types`
  parameter.

  """

  cdef object stype, shape, atom_, sctype, tsize, kind
  cdef object dflt, base, enum_, nptype

  stype, shape = hdf5_to_np_ext_type(type_id, pure_numpy_types, atom=True)
  # Create the Atom
  if stype == 'e':
    (enum_, nptype) = load_enum(type_id)
    # Take one of the names as the default in the enumeration.
    dflt = next(iter(enum_))[0]
    base = Atom.from_dtype(nptype)
    atom_ = EnumAtom(enum_, dflt, base, shape=shape)
  else:
    kind = npext_prefixes_to_ptkinds[stype[0]]
    tsize = int(stype[1:])
    atom_ = Atom.from_kind(kind, tsize, shape=shape)

  return atom_


AtomFromHDF5Type = previous_api(atom_from_hdf5_type)


def create_nested_type(object desc, str byteorder):
  """Create a nested type based on a description and return an HDF5 type."""

  cdef hid_t tid, tid2
  cdef size_t offset
  cdef bytes encoded_name

  tid = H5Tcreate(H5T_COMPOUND, desc._v_itemsize)
  if tid < 0:
    return -1

  offset = 0
  for k in desc._v_names:
    obj = desc._v_colobjects[k]
    if isinstance(obj, Description):
      tid2 = create_nested_type(obj, byteorder)
    else:
      tid2 = atom_to_hdf5_type(obj, byteorder)
    encoded_name = k.encode('utf-8')
    H5Tinsert(tid, encoded_name, offset, tid2)
    offset = offset + desc._v_dtype[k].itemsize
    # Release resources
    H5Tclose(tid2)

  return tid


createNestedType = previous_api(create_nested_type)


## Local Variables:
## mode: python
## py-indent-offset: 2
## tab-width: 2
## fill-column: 78
## End:
