#include <Python.h>
#include <numpy/arrayobject.h>
#include "heron.h"
#include "segment.h"
#include "areas.h"
#include "intersection.h"
#include "generate.h"
#include "blocked.h"
#include "ephemeris.h"
#include "main.h"
#include "pyutil.h"
#include "blackbody.h"
#include <stdio.h>

static char module_docstring[] =
    "This module is used to calcuate the areas of geometric shapes";
static char web_docstring[] =
    "Calculate triangle area with only the lengths known.";
static char segment_docstring[] =
    "Calculate the area of a circle segment.";
static char quad_docstring[] =
    "Calculate the area of a circle segment.";

static PyObject *web_heron(PyObject *self, PyObject *args);
static PyObject *web_segment(PyObject *self, PyObject *args);
static PyObject *web_find_segment_area(PyObject *self, PyObject *args);
static PyObject *web_find_quad_area(PyObject *self, PyObject *args);
static PyObject *web_one_in_one_out(PyObject *self, PyObject *args);
static PyObject *web_circle_intersect(PyObject *self, PyObject *args);
static PyObject *web_line_intersect(PyObject *self, PyObject *args);
static PyObject *web_generate_planet(PyObject *self, PyObject *args);
static PyObject *web_blocked(PyObject *self, PyObject *args);
static PyObject *web_zhang_2016(PyObject *self, PyObject *args);
static PyObject *web_separation_of_centers(PyObject *self, PyObject *args);
static PyObject *web_lightcurve(PyObject *self, PyObject *args);

static PyMethodDef module_methods[] = {
    {"heron", web_heron, METH_VARARGS, web_docstring},
    {"segment", web_segment, METH_VARARGS, segment_docstring},
    {"find_segment_area", web_find_segment_area, METH_VARARGS, segment_docstring},
    {"find_quad_area", web_find_quad_area, METH_VARARGS, quad_docstring},
    {"one_in_one_out", web_one_in_one_out, METH_VARARGS, quad_docstring},
    {"circle_intersect", web_circle_intersect, METH_VARARGS, quad_docstring},
    {"line_intersect", web_line_intersect, METH_VARARGS, quad_docstring},
    {"generate_planet", web_generate_planet, METH_VARARGS, quad_docstring},
    {"blocked", web_blocked, METH_VARARGS, quad_docstring},
    {"zhang_2016", web_zhang_2016, METH_VARARGS, quad_docstring},
    {"separation_of_centers", web_separation_of_centers, METH_VARARGS, quad_docstring},
    {"lightcurve", web_lightcurve, METH_VARARGS, quad_docstring},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
#if PY_MAJOR_VERSION >= 3
PyInit__web(void)
#else
init_web(void)
#endif
{
	#if PY_MAJOR_VERSION >= 3
		PyObject *module;
		static struct PyModuleDef moduledef = {
			PyModuleDef_HEAD_INIT,
			"_web",             /* m_name */
			module_docstring,    /* m_doc */
			-1,                  /* m_size */
			module_methods,      /* m_methods */
			NULL,                /* m_reload */
			NULL,                /* m_traverse */
			NULL,                /* m_clear */
			NULL,                /* m_free */
		};
	#endif

	#if PY_MAJOR_VERSION >= 3
		module = PyModule_Create(&moduledef);
		if (!module)
			return NULL;
		/* Load `numpy` functionality. */
		import_array();
		return module;
	#else
	    PyObject *m = Py_InitModule3("_web", module_methods, module_docstring);
		if (m == NULL)
			return;
		/* Load `numpy` functionality. */
		import_array();
	#endif
}

static PyObject *web_heron(PyObject *self, PyObject *args)
{
    double a, b,c;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "ddd", &a, &b, &c))
        return NULL;

    /* Call the external C function to compute the area. */
    double area = heron(a,b,c);

    /* Build the output tuple */

    PyObject *ret = Py_BuildValue("d",area);
    return ret;
}

static PyObject *web_segment(PyObject *self, PyObject *args)
{
    double r, theta;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "dd", &r, &theta))
        return NULL;

    /* Call the external C function to compute the area. */
    double area = segment(r,theta);

    /* Build the output tuple */

    PyObject *ret = Py_BuildValue("d",area);
    return ret;
}

static PyObject *web_find_segment_area(PyObject *self, PyObject *args)
{
    double c1x,c2x,c1y,c2y,x2,y2,r2;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "ddddddd", &c1x, &c2x, &c1y, &c2y,&x2,&y2,&r2))
        return NULL;

    /* Call the external C function to compute the area. */

    double *c1 = malloc(sizeof(double) * 2);
    double *c2 = malloc(sizeof(double) * 2);

    c1[0] = c1x;
    c1[1] = c1y;
    c2[0] = c2x;
    c2[1] = c2y;

    double area = find_segment_area(c1,c2,x2,y2,r2);

    /* Build the output tuple */

    PyObject *ret = Py_BuildValue("d",area);
    return ret;
}

static PyObject *web_find_quad_area(PyObject *self, PyObject *args)
{
    PyObject *a_obj,*b_obj,*c_obj,*d_obj;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "OOOO", &a_obj, &b_obj,&c_obj,&d_obj))
        return NULL;

    /* Interpret the input objects as numpy arrays. */
    PyObject *a_array = PyArray_FROM_OTF(a_obj, NPY_DOUBLE, NPY_IN_ARRAY);
    PyObject *b_array = PyArray_FROM_OTF(b_obj, NPY_DOUBLE, NPY_IN_ARRAY);
    PyObject *c_array = PyArray_FROM_OTF(c_obj, NPY_DOUBLE, NPY_IN_ARRAY);
    PyObject *d_array = PyArray_FROM_OTF(d_obj, NPY_DOUBLE, NPY_IN_ARRAY);

    /* If that didn't work, throw an exception. */
    if (a_array == NULL || b_array == NULL || c_array == NULL || d_array == NULL) {
        Py_XDECREF(a_array);
        Py_XDECREF(b_array);
        Py_XDECREF(c_array);
        Py_XDECREF(d_array);
        return NULL;
    }

    /* Get pointers to the data as C-types. */
    double *a    = (double*)PyArray_DATA(a_array);
    double *b    = (double*)PyArray_DATA(b_array);
    double *c    = (double*)PyArray_DATA(c_array);
    double *d    = (double*)PyArray_DATA(d_array);

    /* Call the external C function to compute the area. */
    double area = find_quad_area(a,b,c,d);

    /* Build the output tuple */

    PyObject *ret = Py_BuildValue("d",area);
    return ret;
}

static PyObject *web_one_in_one_out(PyObject *self, PyObject *args)
{
    double r_inner,r_outer,r2,x2,y2;
    PyObject *c1_obj,*c2_obj,*e1_obj,*e2_obj;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "OOOOddddd", &c1_obj, &c2_obj,&e1_obj,&e2_obj,&r_inner,&r_outer,&r2,&x2,&y2))
        return NULL;

    /* Interpret the input objects as numpy arrays. */
    PyObject *c1_array = PyArray_FROM_OTF(c1_obj, NPY_DOUBLE, NPY_IN_ARRAY);
    PyObject *c2_array = PyArray_FROM_OTF(c2_obj, NPY_DOUBLE, NPY_IN_ARRAY);
    PyObject *e1_array = PyArray_FROM_OTF(e1_obj, NPY_DOUBLE, NPY_IN_ARRAY);
    PyObject *e2_array = PyArray_FROM_OTF(e2_obj, NPY_DOUBLE, NPY_IN_ARRAY);

    /* If that didn't work, throw an exception. */
    if (c1_array == NULL || c2_array == NULL || e1_array == NULL || e2_array == NULL) {
        Py_XDECREF(c1_array);
        Py_XDECREF(c2_array);
        Py_XDECREF(e1_array);
        Py_XDECREF(e2_array);
        return NULL;
    }

    /* Get pointers to the data as C-types. */
    double *c1    = (double*)PyArray_DATA(c1_array);
    double *c2    = (double*)PyArray_DATA(c2_array);
    double *e1    = (double*)PyArray_DATA(e1_array);
    double *e2    = (double*)PyArray_DATA(e2_array);

    /* Call the external C function to compute the area. */
    double area = one_in_one_out(c1,c2,e1,e2,r_inner,r_outer,r2,x2,y2);

    /* Build the output tuple */

    PyObject *ret = Py_BuildValue("d",area);
    return ret;
}

static PyObject *web_circle_intersect(PyObject *self, PyObject *args)
{
    double x1,y1,r1,x2,y2,r2;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "dddddd", &x1,&y1,&r1,&x2,&y2,&r2))
        return NULL;

    /* Call the external C function to compute the area. */
    double *intersect = circle_intersect(x1,y1,r1,x2,y2,r2);

    /* Build the output tuple */

    PyObject *ret = Py_BuildValue("[d,d,d,d]",intersect[0],intersect[1],intersect[2],intersect[3]);
    return ret;
}

static PyObject *web_line_intersect(PyObject *self, PyObject *args)
{
    double x1,y1,x2,y2,r2;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "ddddd", &x1,&y1,&x2,&y2,&r2))
        return NULL;

    /* Call the external C function to compute the area. */
    double *intersect = line_intersect(0,0,x1,y1,x2,y2,r2);

    /* Build the output tuple */

    PyObject *ret = Py_BuildValue("[d,d,d,d]",intersect[0],intersect[1],intersect[2],intersect[3]);
    return ret;
}

static PyObject *web_generate_planet(PyObject *self, PyObject *args)
{
    int n_layers,n_1,n_2;
    double xi,T_n,delta_T,lambda0,phi0,p_u1,p_u2;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "iddddddd", &n_layers,&xi,&T_n,&delta_T,&lambda0,&phi0,&p_u1,&p_u2))
        return NULL;

    /* Call the external C function to compute the area. */
    double **planet_struct = generate_planet(n_layers);

    map_model(planet_struct,n_layers,xi,T_n,delta_T,lambda0,phi0,p_u1,p_u2);

    /* Build the output tuple */

    n_1 =pow(n_layers,2);
    n_2=18;

    PyObject *pylist = Convert_2d_Array(planet_struct,n_1,n_2);

    /* Clean up. */
    free(planet_struct);

    return pylist;
}

static PyObject *web_blocked(PyObject *self, PyObject *args)
{
    int n_layers;
    double r2;
    PyObject *x_obj, *y_obj;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "iOOd", &n_layers,&x_obj,&y_obj,&r2))
        return NULL;

    PyObject *x_array = PyArray_FROM_OTF(x_obj, NPY_DOUBLE, NPY_IN_ARRAY);
    PyObject *y_array = PyArray_FROM_OTF(y_obj, NPY_DOUBLE, NPY_IN_ARRAY);

    /* If that didn't work, throw an exception. */
    if (x_array == NULL || y_array == NULL) {
        Py_XDECREF(x_array);
        Py_XDECREF(y_array);
        return NULL;
    }

    /* How many data points are there? */
    int N = (int)PyArray_DIM(x_array, 0);

    /* Get pointers to the data as C-types. */
    double *x2    = (double*)PyArray_DATA(x_array);
    double *y2    = (double*)PyArray_DATA(y_array);

    /* Call the external C function to compute the area. */
    double *output = call_blocked(n_layers,N,x2,y2,r2);

    PyObject *pylist = Convert_Big_Array(output,N);

    /* Clean up. */
    Py_DECREF(x_array);
    Py_DECREF(y_array);
    free(output);

    return pylist;
}

static PyObject *web_zhang_2016(PyObject *self, PyObject *args)
{
    double lat, lon, zeta, T_n, delta_T;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "ddddd", &lat, &lon, &zeta, &T_n, &delta_T))
        return NULL;

    /* Call the external C function to compute the area. */
    double output = zhang_2016(lat, lon, zeta, T_n, delta_T);

     PyObject *ret = Py_BuildValue("d",output);

    return ret;
}


static PyObject *web_separation_of_centers(PyObject *self, PyObject *args)
{
    double t,tc,per,a,inc,ecc,omega,a_rs,r2;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "ddddddddd", &t,&tc,&per,&a,&inc,&ecc,&omega,&a_rs,&r2))
        return NULL;

    /* Call the external C function to compute the area. */
    double *output = separation_of_centers(t,tc,per,a,inc,ecc,omega,a_rs,r2);

    PyObject *ret = Py_BuildValue("[d,d,d]",output[0],output[1],output[2]);

    return ret;
}

static PyObject *web_lightcurve(PyObject *self, PyObject *args)
{
    int n_layers;
    double tc,per,a,inc,ecc,omega,a_rs,rp,xi,T_n,delta_T,p_u1,p_u2,T_s;
    PyObject *t_obj;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "iOdddddddddddddd", &n_layers,&t_obj,&tc,&per,&a,&inc,&ecc,&omega,&a_rs,&rp,&xi,&T_n,&delta_T,&p_u1,&p_u2,&T_s))
        return NULL;

    PyObject *t_array = PyArray_FROM_OTF(t_obj, NPY_DOUBLE, NPY_IN_ARRAY);

    /* If that didn't work, throw an exception. */
    if (t_array == NULL) {
        Py_XDECREF(t_array);
        return NULL;
    }

    /* How many data points are there? */
    int N = (int)PyArray_DIM(t_array, 0);

    /* Get pointers to the data as C-types. */
    double *t2    = (double*)PyArray_DATA(t_array);

    /* Call the external C function to compute the area. */
    double *output = lightcurve(n_layers,N,t2,tc,per,a,inc,ecc,omega,a_rs,rp,xi,T_n,delta_T,p_u1,p_u2,T_s);

    PyObject *pylist = Convert_Big_Array(output,N);

    /* Clean up. */
    Py_DECREF(t_array);
    free(output);

    return pylist;
}