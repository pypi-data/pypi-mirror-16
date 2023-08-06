
#include <Python.h>
#include <stddef.h>

/* this block of #ifs should be kept exactly identical between
   c/_cffi_backend.c, cffi/vengine_cpy.py, cffi/vengine_gen.py */
#if defined(_MSC_VER)
# include <malloc.h>   /* for alloca() */
# if _MSC_VER < 1600   /* MSVC < 2010 */
   typedef __int8 int8_t;
   typedef __int16 int16_t;
   typedef __int32 int32_t;
   typedef __int64 int64_t;
   typedef unsigned __int8 uint8_t;
   typedef unsigned __int16 uint16_t;
   typedef unsigned __int32 uint32_t;
   typedef unsigned __int64 uint64_t;
   typedef __int8 int_least8_t;
   typedef __int16 int_least16_t;
   typedef __int32 int_least32_t;
   typedef __int64 int_least64_t;
   typedef unsigned __int8 uint_least8_t;
   typedef unsigned __int16 uint_least16_t;
   typedef unsigned __int32 uint_least32_t;
   typedef unsigned __int64 uint_least64_t;
   typedef __int8 int_fast8_t;
   typedef __int16 int_fast16_t;
   typedef __int32 int_fast32_t;
   typedef __int64 int_fast64_t;
   typedef unsigned __int8 uint_fast8_t;
   typedef unsigned __int16 uint_fast16_t;
   typedef unsigned __int32 uint_fast32_t;
   typedef unsigned __int64 uint_fast64_t;
   typedef __int64 intmax_t;
   typedef unsigned __int64 uintmax_t;
# else
#  include <stdint.h>
# endif
# if _MSC_VER < 1800   /* MSVC < 2013 */
   typedef unsigned char _Bool;
# endif
#else
# include <stdint.h>
# if (defined (__SVR4) && defined (__sun)) || defined(_AIX)
#  include <alloca.h>
# endif
#endif

#if PY_MAJOR_VERSION < 3
# undef PyCapsule_CheckExact
# undef PyCapsule_GetPointer
# define PyCapsule_CheckExact(capsule) (PyCObject_Check(capsule))
# define PyCapsule_GetPointer(capsule, name) \
    (PyCObject_AsVoidPtr(capsule))
#endif

#if PY_MAJOR_VERSION >= 3
# define PyInt_FromLong PyLong_FromLong
#endif

#define _cffi_from_c_double PyFloat_FromDouble
#define _cffi_from_c_float PyFloat_FromDouble
#define _cffi_from_c_long PyInt_FromLong
#define _cffi_from_c_ulong PyLong_FromUnsignedLong
#define _cffi_from_c_longlong PyLong_FromLongLong
#define _cffi_from_c_ulonglong PyLong_FromUnsignedLongLong

#define _cffi_to_c_double PyFloat_AsDouble
#define _cffi_to_c_float PyFloat_AsDouble

#define _cffi_from_c_int_const(x)                                        \
    (((x) > 0) ?                                                         \
        ((unsigned long long)(x) <= (unsigned long long)LONG_MAX) ?      \
            PyInt_FromLong((long)(x)) :                                  \
            PyLong_FromUnsignedLongLong((unsigned long long)(x)) :       \
        ((long long)(x) >= (long long)LONG_MIN) ?                        \
            PyInt_FromLong((long)(x)) :                                  \
            PyLong_FromLongLong((long long)(x)))

#define _cffi_from_c_int(x, type)                                        \
    (((type)-1) > 0 ? /* unsigned */                                     \
        (sizeof(type) < sizeof(long) ?                                   \
            PyInt_FromLong((long)x) :                                    \
         sizeof(type) == sizeof(long) ?                                  \
            PyLong_FromUnsignedLong((unsigned long)x) :                  \
            PyLong_FromUnsignedLongLong((unsigned long long)x)) :        \
        (sizeof(type) <= sizeof(long) ?                                  \
            PyInt_FromLong((long)x) :                                    \
            PyLong_FromLongLong((long long)x)))

#define _cffi_to_c_int(o, type)                                          \
    (sizeof(type) == 1 ? (((type)-1) > 0 ? (type)_cffi_to_c_u8(o)        \
                                         : (type)_cffi_to_c_i8(o)) :     \
     sizeof(type) == 2 ? (((type)-1) > 0 ? (type)_cffi_to_c_u16(o)       \
                                         : (type)_cffi_to_c_i16(o)) :    \
     sizeof(type) == 4 ? (((type)-1) > 0 ? (type)_cffi_to_c_u32(o)       \
                                         : (type)_cffi_to_c_i32(o)) :    \
     sizeof(type) == 8 ? (((type)-1) > 0 ? (type)_cffi_to_c_u64(o)       \
                                         : (type)_cffi_to_c_i64(o)) :    \
     (Py_FatalError("unsupported size for type " #type), (type)0))

#define _cffi_to_c_i8                                                    \
                 ((int(*)(PyObject *))_cffi_exports[1])
#define _cffi_to_c_u8                                                    \
                 ((int(*)(PyObject *))_cffi_exports[2])
#define _cffi_to_c_i16                                                   \
                 ((int(*)(PyObject *))_cffi_exports[3])
#define _cffi_to_c_u16                                                   \
                 ((int(*)(PyObject *))_cffi_exports[4])
#define _cffi_to_c_i32                                                   \
                 ((int(*)(PyObject *))_cffi_exports[5])
#define _cffi_to_c_u32                                                   \
                 ((unsigned int(*)(PyObject *))_cffi_exports[6])
#define _cffi_to_c_i64                                                   \
                 ((long long(*)(PyObject *))_cffi_exports[7])
#define _cffi_to_c_u64                                                   \
                 ((unsigned long long(*)(PyObject *))_cffi_exports[8])
#define _cffi_to_c_char                                                  \
                 ((int(*)(PyObject *))_cffi_exports[9])
#define _cffi_from_c_pointer                                             \
    ((PyObject *(*)(char *, CTypeDescrObject *))_cffi_exports[10])
#define _cffi_to_c_pointer                                               \
    ((char *(*)(PyObject *, CTypeDescrObject *))_cffi_exports[11])
#define _cffi_get_struct_layout                                          \
    ((PyObject *(*)(Py_ssize_t[]))_cffi_exports[12])
#define _cffi_restore_errno                                              \
    ((void(*)(void))_cffi_exports[13])
#define _cffi_save_errno                                                 \
    ((void(*)(void))_cffi_exports[14])
#define _cffi_from_c_char                                                \
    ((PyObject *(*)(char))_cffi_exports[15])
#define _cffi_from_c_deref                                               \
    ((PyObject *(*)(char *, CTypeDescrObject *))_cffi_exports[16])
#define _cffi_to_c                                                       \
    ((int(*)(char *, CTypeDescrObject *, PyObject *))_cffi_exports[17])
#define _cffi_from_c_struct                                              \
    ((PyObject *(*)(char *, CTypeDescrObject *))_cffi_exports[18])
#define _cffi_to_c_wchar_t                                               \
    ((wchar_t(*)(PyObject *))_cffi_exports[19])
#define _cffi_from_c_wchar_t                                             \
    ((PyObject *(*)(wchar_t))_cffi_exports[20])
#define _cffi_to_c_long_double                                           \
    ((long double(*)(PyObject *))_cffi_exports[21])
#define _cffi_to_c__Bool                                                 \
    ((_Bool(*)(PyObject *))_cffi_exports[22])
#define _cffi_prepare_pointer_call_argument                              \
    ((Py_ssize_t(*)(CTypeDescrObject *, PyObject *, char **))_cffi_exports[23])
#define _cffi_convert_array_from_object                                  \
    ((int(*)(char *, CTypeDescrObject *, PyObject *))_cffi_exports[24])
#define _CFFI_NUM_EXPORTS 25

typedef struct _ctypedescr CTypeDescrObject;

static void *_cffi_exports[_CFFI_NUM_EXPORTS];
static PyObject *_cffi_types, *_cffi_VerificationError;

static int _cffi_setup_custom(PyObject *lib);   /* forward */

static PyObject *_cffi_setup(PyObject *self, PyObject *args)
{
    PyObject *library;
    int was_alive = (_cffi_types != NULL);
    (void)self; /* unused */
    if (!PyArg_ParseTuple(args, "OOO", &_cffi_types, &_cffi_VerificationError,
                                       &library))
        return NULL;
    Py_INCREF(_cffi_types);
    Py_INCREF(_cffi_VerificationError);
    if (_cffi_setup_custom(library) < 0)
        return NULL;
    return PyBool_FromLong(was_alive);
}

static int _cffi_init(void)
{
    PyObject *module, *c_api_object = NULL;

    module = PyImport_ImportModule("_cffi_backend");
    if (module == NULL)
        goto failure;

    c_api_object = PyObject_GetAttrString(module, "_C_API");
    if (c_api_object == NULL)
        goto failure;
    if (!PyCapsule_CheckExact(c_api_object)) {
        PyErr_SetNone(PyExc_ImportError);
        goto failure;
    }
    memcpy(_cffi_exports, PyCapsule_GetPointer(c_api_object, "cffi"),
           _CFFI_NUM_EXPORTS * sizeof(void *));

    Py_DECREF(module);
    Py_DECREF(c_api_object);
    return 0;

  failure:
    Py_XDECREF(module);
    Py_XDECREF(c_api_object);
    return -1;
}

#define _cffi_type(num) ((CTypeDescrObject *)PyList_GET_ITEM(_cffi_types, num))

/**********/



    #include <stdio.h>
    #include <unistd.h>
    #include <sys/types.h>
    #include <sys/socket.h>
    #include <netinet/in.h>
    #include "include/ebtables.h"
    #include "include/ebtables_u.h"

    unsigned int OPT_KERNELDATA = 0x800;

    void ebt_early_init_once(void);
    

static PyObject *
_cffi_f_do_command(PyObject *self, PyObject *args)
{
  int x0;
  char * * x1;
  int x2;
  struct ebt_u_replace * x3;
  Py_ssize_t datasize;
  int result;
  PyObject *arg0;
  PyObject *arg1;
  PyObject *arg2;
  PyObject *arg3;

  if (!PyArg_ParseTuple(args, "OOOO:do_command", &arg0, &arg1, &arg2, &arg3))
    return NULL;

  x0 = _cffi_to_c_int(arg0, int);
  if (x0 == (int)-1 && PyErr_Occurred())
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(0), arg1, (char **)&x1);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x1 = alloca((size_t)datasize);
    memset((void *)x1, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x1, _cffi_type(0), arg1) < 0)
      return NULL;
  }

  x2 = _cffi_to_c_int(arg2, int);
  if (x2 == (int)-1 && PyErr_Occurred())
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(1), arg3, (char **)&x3);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x3 = alloca((size_t)datasize);
    memset((void *)x3, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x3, _cffi_type(1), arg3) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = do_command(x0, x1, x2, x3); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_ebt_cleanup_replace(PyObject *self, PyObject *arg0)
{
  struct ebt_u_replace * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(1), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(1), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { ebt_cleanup_replace(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_ebt_deliver_table(PyObject *self, PyObject *arg0)
{
  struct ebt_u_replace * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(1), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(1), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { ebt_deliver_table(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_ebt_early_init_once(PyObject *self, PyObject *noarg)
{

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { ebt_early_init_once(); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  (void)noarg; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_ebt_get_kernel_table(PyObject *self, PyObject *args)
{
  struct ebt_u_replace * x0;
  int x1;
  Py_ssize_t datasize;
  int result;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:ebt_get_kernel_table", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(1), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(1), arg0) < 0)
      return NULL;
  }

  x1 = _cffi_to_c_int(arg1, int);
  if (x1 == (int)-1 && PyErr_Occurred())
    return NULL;

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = ebt_get_kernel_table(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_int(result, int);
}

static PyObject *
_cffi_f_ebt_reinit_extensions(PyObject *self, PyObject *noarg)
{

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { ebt_reinit_extensions(); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  (void)noarg; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_free(PyObject *self, PyObject *arg0)
{
  void * x0;
  Py_ssize_t datasize;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(3), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(3), arg0) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { free(x0); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject *
_cffi_f_strcpy(PyObject *self, PyObject *args)
{
  char * x0;
  char const * x1;
  Py_ssize_t datasize;
  char * result;
  PyObject *arg0;
  PyObject *arg1;

  if (!PyArg_ParseTuple(args, "OO:strcpy", &arg0, &arg1))
    return NULL;

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(4), arg0, (char **)&x0);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x0 = alloca((size_t)datasize);
    memset((void *)x0, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x0, _cffi_type(4), arg0) < 0)
      return NULL;
  }

  datasize = _cffi_prepare_pointer_call_argument(
      _cffi_type(5), arg1, (char **)&x1);
  if (datasize != 0) {
    if (datasize < 0)
      return NULL;
    x1 = alloca((size_t)datasize);
    memset((void *)x1, 0, (size_t)datasize);
    if (_cffi_convert_array_from_object((char *)x1, _cffi_type(5), arg1) < 0)
      return NULL;
  }

  Py_BEGIN_ALLOW_THREADS
  _cffi_restore_errno();
  { result = strcpy(x0, x1); }
  _cffi_save_errno();
  Py_END_ALLOW_THREADS

  (void)self; /* unused */
  return _cffi_from_c_pointer((char *)result, _cffi_type(4));
}

static int _cffi_const_EBT_TABLE_MAXNAMELEN(PyObject *lib)
{
  PyObject *o;
  int res;
  if ((EBT_TABLE_MAXNAMELEN) <= 0 || (unsigned long)(EBT_TABLE_MAXNAMELEN) != 32UL) {
    char buf[64];
    if ((EBT_TABLE_MAXNAMELEN) <= 0)
        snprintf(buf, 63, "%ld", (long)(EBT_TABLE_MAXNAMELEN));
    else
        snprintf(buf, 63, "%lu", (unsigned long)(EBT_TABLE_MAXNAMELEN));
    PyErr_Format(_cffi_VerificationError,
                 "%s%s has the real value %s, not %s",
                 "", "EBT_TABLE_MAXNAMELEN", buf, "32");
    return -1;
  }
  o = _cffi_from_c_int_const(EBT_TABLE_MAXNAMELEN);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "EBT_TABLE_MAXNAMELEN", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return ((void)lib,0);
}

static int _cffi_const_ERRORMSG_MAXLEN(PyObject *lib)
{
  PyObject *o;
  int res;
  if ((ERRORMSG_MAXLEN) <= 0 || (unsigned long)(ERRORMSG_MAXLEN) != 128UL) {
    char buf[64];
    if ((ERRORMSG_MAXLEN) <= 0)
        snprintf(buf, 63, "%ld", (long)(ERRORMSG_MAXLEN));
    else
        snprintf(buf, 63, "%lu", (unsigned long)(ERRORMSG_MAXLEN));
    PyErr_Format(_cffi_VerificationError,
                 "%s%s has the real value %s, not %s",
                 "", "ERRORMSG_MAXLEN", buf, "128");
    return -1;
  }
  o = _cffi_from_c_int_const(ERRORMSG_MAXLEN);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "ERRORMSG_MAXLEN", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_EBT_TABLE_MAXNAMELEN(lib);
}

static int _cffi_const_EXEC_STYLE_DAEMON(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(EXEC_STYLE_DAEMON);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "EXEC_STYLE_DAEMON", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_ERRORMSG_MAXLEN(lib);
}

static int _cffi_const_EXEC_STYLE_PRG(PyObject *lib)
{
  PyObject *o;
  int res;
  o = _cffi_from_c_int_const(EXEC_STYLE_PRG);
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "EXEC_STYLE_PRG", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_EXEC_STYLE_DAEMON(lib);
}

static void _cffi_check_struct_ebt_u_replace(struct ebt_u_replace *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { char(*tmp)[32] = &p->name; (void)tmp; }
  { struct ebt_u_entries * * *tmp = &p->chains; (void)tmp; }
  { struct ebt_cntchanges * *tmp = &p->cc; (void)tmp; }
  (void)((p->flags) << 1);
  { char *tmp = &p->command; (void)tmp; }
}
static PyObject *
_cffi_layout_struct_ebt_u_replace(PyObject *self, PyObject *noarg)
{
  struct _cffi_aligncheck { char x; struct ebt_u_replace y; };
  static Py_ssize_t nums[] = {
    sizeof(struct ebt_u_replace),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct ebt_u_replace, name),
    sizeof(((struct ebt_u_replace *)0)->name),
    offsetof(struct ebt_u_replace, chains),
    sizeof(((struct ebt_u_replace *)0)->chains),
    offsetof(struct ebt_u_replace, cc),
    sizeof(((struct ebt_u_replace *)0)->cc),
    offsetof(struct ebt_u_replace, flags),
    sizeof(((struct ebt_u_replace *)0)->flags),
    offsetof(struct ebt_u_replace, command),
    sizeof(((struct ebt_u_replace *)0)->command),
    -1
  };
  (void)self; /* unused */
  (void)noarg; /* unused */
  return _cffi_get_struct_layout(nums);
  /* the next line is not executed, but compiled */
  _cffi_check_struct_ebt_u_replace(0);
}

static int _cffi_var_OPT_KERNELDATA(PyObject *lib)
{
  PyObject *o;
  int res;
  unsigned int * i;
  i = (&OPT_KERNELDATA);
  o = _cffi_from_c_pointer((char *)i, _cffi_type(6));
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "OPT_KERNELDATA", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_EXEC_STYLE_PRG(lib);
}

static int _cffi_const_ebt_errormsg(PyObject *lib)
{
  PyObject *o;
  int res;
  char * i;
  i = (ebt_errormsg);
  o = _cffi_from_c_pointer((char *)i, _cffi_type(4));
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "ebt_errormsg", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_var_OPT_KERNELDATA(lib);
}

static int _cffi_var_ebt_silent(PyObject *lib)
{
  PyObject *o;
  int res;
  int * i;
  i = (&ebt_silent);
  o = _cffi_from_c_pointer((char *)i, _cffi_type(7));
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "ebt_silent", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_const_ebt_errormsg(lib);
}

static int _cffi_var_optarg(PyObject *lib)
{
  PyObject *o;
  int res;
  char * * i;
  i = (&optarg);
  o = _cffi_from_c_pointer((char *)i, _cffi_type(0));
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "optarg", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_var_ebt_silent(lib);
}

static int _cffi_var_optind(PyObject *lib)
{
  PyObject *o;
  int res;
  int * i;
  i = (&optind);
  o = _cffi_from_c_pointer((char *)i, _cffi_type(7));
  if (o == NULL)
    return -1;
  res = PyObject_SetAttrString(lib, "optind", o);
  Py_DECREF(o);
  if (res < 0)
    return -1;
  return _cffi_var_optarg(lib);
}

static int _cffi_setup_custom(PyObject *lib)
{
  return _cffi_var_optind(lib);
}

static PyMethodDef _cffi_methods[] = {
  {"do_command", _cffi_f_do_command, METH_VARARGS, NULL},
  {"ebt_cleanup_replace", _cffi_f_ebt_cleanup_replace, METH_O, NULL},
  {"ebt_deliver_table", _cffi_f_ebt_deliver_table, METH_O, NULL},
  {"ebt_early_init_once", _cffi_f_ebt_early_init_once, METH_NOARGS, NULL},
  {"ebt_get_kernel_table", _cffi_f_ebt_get_kernel_table, METH_VARARGS, NULL},
  {"ebt_reinit_extensions", _cffi_f_ebt_reinit_extensions, METH_NOARGS, NULL},
  {"free", _cffi_f_free, METH_O, NULL},
  {"strcpy", _cffi_f_strcpy, METH_VARARGS, NULL},
  {"_cffi_layout_struct_ebt_u_replace", _cffi_layout_struct_ebt_u_replace, METH_NOARGS, NULL},
  {"_cffi_setup", _cffi_setup, METH_VARARGS, NULL},
  {NULL, NULL, 0, NULL}    /* Sentinel */
};

#if PY_MAJOR_VERSION >= 3

static struct PyModuleDef _cffi_module_def = {
  PyModuleDef_HEAD_INIT,
  "ebtables_c19823a81fcabf0305de42c5319650a0583eaa2d",
  NULL,
  -1,
  _cffi_methods,
  NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC
PyInit_ebtables_c19823a81fcabf0305de42c5319650a0583eaa2d(void)
{
  PyObject *lib;
  lib = PyModule_Create(&_cffi_module_def);
  if (lib == NULL)
    return NULL;
  if (((void)lib,0) < 0 || _cffi_init() < 0) {
    Py_DECREF(lib);
    return NULL;
  }
  return lib;
}

#else

PyMODINIT_FUNC
initebtables_c19823a81fcabf0305de42c5319650a0583eaa2d(void)
{
  PyObject *lib;
  lib = Py_InitModule("ebtables_c19823a81fcabf0305de42c5319650a0583eaa2d", _cffi_methods);
  if (lib == NULL)
    return;
  if (((void)lib,0) < 0 || _cffi_init() < 0)
    return;
  return;
}

#endif
