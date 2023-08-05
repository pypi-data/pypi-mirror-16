#pragma once

#include <string.h>
#include "debugConfig.h"

#ifdef __cplusplus
#define EXTERNC extern "C"
#else
#define EXTERNC
#endif

#ifdef USE_PYTHON
EXTERNC  PyObject *
hdlConvertor_parse(PyObject *self, PyObject *args, PyObject *keywds);
PyMODINIT_FUNC PyInit_hdlConvertor(void);
#endif
