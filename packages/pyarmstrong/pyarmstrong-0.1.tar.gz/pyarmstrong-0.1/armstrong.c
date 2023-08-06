#include <Python.h>
#include <stdio.h>
#include <math.h>

static PyObject *pyisarmstrong(PyObject *self, PyObject *args){

  long number, originalNumber, remainder=0, result = 0, n = 0;
  PyObject *pyresult; 
  if(!PyArg_ParseTuple(args,"l", &number)){
    return NULL;
  }

  originalNumber = number;
  while (originalNumber != 0){
    originalNumber /= 10;
    ++n;
  }

  originalNumber = number;
  while (originalNumber != 0){
    remainder = originalNumber%10;
    result += pow(remainder, n);
    originalNumber /= 10;
  }

  if(result == number)
    pyresult = Py_True;
  else
    pyresult = Py_False;
  Py_INCREF(pyresult);
  return pyresult;
}

static PyMethodDef ArmstrongMethods[] = {
  {"isarmstrong", pyisarmstrong , METH_VARARGS, "Checks if a number is an armstrong number."},
  { NULL, NULL, 0, NULL}
};

static struct PyModuleDef armstrongmodule = {
  PyModuleDef_HEAD_INIT,
  "pyarmstrong",          
  "A module for checking armstrong numbers.",  
  -1,                
  ArmstrongMethods       
};

PyMODINIT_FUNC PyInit_pyarmstrong(void) {
  return PyModule_Create(&armstrongmodule);
}
