/* Generated code for Python source for module 'isbnlib'
 * created by Nuitka version 0.5.21.1
 *
 * This code is in part copyright 2016 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.hpp"

#include "__helpers.hpp"

/* The _module_isbnlib is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_isbnlib;
PyDictObject *moduledict_isbnlib;

/* The module constants used, if any. */
extern PyObject *const_tuple_str_plain_config_tuple;
static PyObject *const_str_plain__nh;
extern PyObject *const_str_plain_GTIN13;
static PyObject *const_tuple_str_plain_RDDATE_tuple;
extern PyObject *const_str_plain_clean;
extern PyObject *const_str_plain_RDDATE;
extern PyObject *const_str_plain_EAN13;
extern PyObject *const_str_plain_RE_ISBN13;
extern PyObject *const_str_plain_emit;
extern PyObject *const_int_neg_1;
extern PyObject *const_str_plain_PluginNotLoadedError;
extern PyObject *const_str_plain_logging;
extern PyObject *const_str_plain__goom;
extern PyObject *const_str_plain_quiet_errors;
extern PyObject *const_str_plain_NullHandler;
extern PyObject *const_str_plain_query;
extern PyObject *const_str_plain_get_isbnlike;
extern PyObject *const_dict_empty;
static PyObject *const_tuple_2dd54363478e7f9167cad677209d7435_tuple;
extern PyObject *const_str_plain_ISBNLibException;
extern PyObject *const_str_plain_notisbn;
extern PyObject *const_str_plain_ren;
static PyObject *const_str_plain_ISBN13;
extern PyObject *const_str_plain_NotRecognizedServiceError;
extern PyObject *const_str_plain_info;
extern PyObject *const_str_digest_260aecc1c2bfc603c94e52a492c0caa3;
static PyObject *const_str_plain__logging;
extern PyObject *const_str_plain_cover;
extern PyObject *const_str_plain_RE_LOOSE;
extern PyObject *const_str_plain_config;
extern PyObject *const_str_plain_meta;
extern PyObject *const_str_plain___path__;
extern PyObject *const_str_plain_doi;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain_RE_STRICT;
extern PyObject *const_str_plain_addHandler;
extern PyObject *const_str_plain_mask;
extern PyObject *const_str_plain_getLogger;
extern PyObject *const_tuple_empty;
extern PyObject *const_str_plain___all__;
extern PyObject *const_str_plain_doi2tex;
extern PyObject *const_tuple_str_plain_query_tuple;
static PyObject *const_str_digest_ed2f8d97f44c0eec471ecabd377f988a;
extern PyObject *const_str_plain_get_canonical_isbn;
extern PyObject *const_str_plain___file__;
extern PyObject *const_str_plain___version__;
static PyObject *const_tuple_str_plain_doi2tex_tuple;
extern PyObject *const_str_plain_RE_NORMAL;
static PyObject *const_tuple_2c00889c4f9ce4e4a90373868d3bdd45_tuple;
extern PyObject *const_str_plain_self;
extern PyObject *const_str_plain__ext;
extern PyObject *const_str_plain_isbnlib;
static PyObject *const_str_digest_54d96c8010d214731f1dcae8dde8f9de;
extern PyObject *const_str_plain_canonical;
extern PyObject *const_int_pos_1;
extern PyObject *const_str_empty;
extern PyObject *const_str_plain__doitotex;
static PyObject *const_str_digest_db1c32457a7ae665e53016b13b232e0a;
static PyObject *const_str_plain___support__;
extern PyObject *const_str_plain_Handler;
static PyObject *const_tuple_str_plain_isbnlib_tuple;
extern PyObject *const_str_plain___module__;
extern PyObject *const_str_plain_isbn_from_words;
extern PyObject *const_str_plain__core;
extern PyObject *const_tuple_str_plain_self_str_plain_record_tuple;
extern PyObject *const_str_plain___metaclass__;
extern PyObject *const_str_plain_dirname;
extern PyObject *const_str_plain_ean13;
extern PyObject *const_str_plain_to_isbn10;
extern PyObject *const_str_plain_to_isbn13;
static PyObject *const_str_plain_goom;
extern PyObject *const_str_plain_is_isbn10;
extern PyObject *const_str_plain_editions;
extern PyObject *const_str_plain_is_isbn13;
extern PyObject *const_str_plain__exceptions;
static PyObject *const_str_digest_edb993cc5666e55721eb806e6f8ef908;
extern PyObject *const_str_plain_RE_ISBN10;
static PyObject *const_tuple_1ec9a5d983a97d17880bfb27bf3aef6c_tuple;
extern PyObject *const_str_plain_desc;
static PyObject *const_tuple_722c64b73b5d104c10f748431666f687_tuple;
extern PyObject *const_str_plain_record;
extern PyObject *const_str_plain_NotValidISBNError;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_plain__nh = UNSTREAM_STRING( &constant_bin[ 427166 ], 3, 1 );
    const_tuple_str_plain_RDDATE_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_RDDATE_tuple, 0, const_str_plain_RDDATE ); Py_INCREF( const_str_plain_RDDATE );
    const_tuple_2dd54363478e7f9167cad677209d7435_tuple = PyTuple_New( 16 );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 0, const_str_plain_is_isbn10 ); Py_INCREF( const_str_plain_is_isbn10 );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 1, const_str_plain_is_isbn13 ); Py_INCREF( const_str_plain_is_isbn13 );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 2, const_str_plain_to_isbn10 ); Py_INCREF( const_str_plain_to_isbn10 );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 3, const_str_plain_to_isbn13 ); Py_INCREF( const_str_plain_to_isbn13 );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 4, const_str_plain_clean ); Py_INCREF( const_str_plain_clean );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 5, const_str_plain_canonical ); Py_INCREF( const_str_plain_canonical );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 6, const_str_plain_notisbn ); Py_INCREF( const_str_plain_notisbn );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 7, const_str_plain_get_isbnlike ); Py_INCREF( const_str_plain_get_isbnlike );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 8, const_str_plain_get_canonical_isbn ); Py_INCREF( const_str_plain_get_canonical_isbn );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 9, const_str_plain_GTIN13 ); Py_INCREF( const_str_plain_GTIN13 );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 10, const_str_plain_EAN13 ); Py_INCREF( const_str_plain_EAN13 );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 11, const_str_plain_RE_ISBN10 ); Py_INCREF( const_str_plain_RE_ISBN10 );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 12, const_str_plain_RE_ISBN13 ); Py_INCREF( const_str_plain_RE_ISBN13 );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 13, const_str_plain_RE_LOOSE ); Py_INCREF( const_str_plain_RE_LOOSE );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 14, const_str_plain_RE_NORMAL ); Py_INCREF( const_str_plain_RE_NORMAL );
    PyTuple_SET_ITEM( const_tuple_2dd54363478e7f9167cad677209d7435_tuple, 15, const_str_plain_RE_STRICT ); Py_INCREF( const_str_plain_RE_STRICT );
    const_str_plain_ISBN13 = UNSTREAM_STRING( &constant_bin[ 427169 ], 6, 1 );
    const_str_plain__logging = UNSTREAM_STRING( &constant_bin[ 427175 ], 8, 1 );
    const_str_digest_ed2f8d97f44c0eec471ecabd377f988a = UNSTREAM_STRING( &constant_bin[ 427183 ], 82, 0 );
    const_tuple_str_plain_doi2tex_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_doi2tex_tuple, 0, const_str_plain_doi2tex ); Py_INCREF( const_str_plain_doi2tex );
    const_tuple_2c00889c4f9ce4e4a90373868d3bdd45_tuple = PyMarshal_ReadObjectFromString( (char *)&constant_bin[ 427265 ], 453 );
    const_str_digest_54d96c8010d214731f1dcae8dde8f9de = UNSTREAM_STRING( &constant_bin[ 427718 ], 41, 0 );
    const_str_digest_db1c32457a7ae665e53016b13b232e0a = UNSTREAM_STRING( &constant_bin[ 427759 ], 19, 0 );
    const_str_plain___support__ = UNSTREAM_STRING( &constant_bin[ 427550 ], 11, 1 );
    const_tuple_str_plain_isbnlib_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_isbnlib_tuple, 0, const_str_plain_isbnlib ); Py_INCREF( const_str_plain_isbnlib );
    const_str_plain_goom = UNSTREAM_STRING( &constant_bin[ 427691 ], 4, 1 );
    const_str_digest_edb993cc5666e55721eb806e6f8ef908 = UNSTREAM_STRING( &constant_bin[ 427778 ], 5, 0 );
    const_tuple_1ec9a5d983a97d17880bfb27bf3aef6c_tuple = PyTuple_New( 5 );
    PyTuple_SET_ITEM( const_tuple_1ec9a5d983a97d17880bfb27bf3aef6c_tuple, 0, const_str_plain_quiet_errors ); Py_INCREF( const_str_plain_quiet_errors );
    PyTuple_SET_ITEM( const_tuple_1ec9a5d983a97d17880bfb27bf3aef6c_tuple, 1, const_str_plain_ISBNLibException ); Py_INCREF( const_str_plain_ISBNLibException );
    PyTuple_SET_ITEM( const_tuple_1ec9a5d983a97d17880bfb27bf3aef6c_tuple, 2, const_str_plain_NotRecognizedServiceError ); Py_INCREF( const_str_plain_NotRecognizedServiceError );
    PyTuple_SET_ITEM( const_tuple_1ec9a5d983a97d17880bfb27bf3aef6c_tuple, 3, const_str_plain_NotValidISBNError ); Py_INCREF( const_str_plain_NotValidISBNError );
    PyTuple_SET_ITEM( const_tuple_1ec9a5d983a97d17880bfb27bf3aef6c_tuple, 4, const_str_plain_PluginNotLoadedError ); Py_INCREF( const_str_plain_PluginNotLoadedError );
    const_tuple_722c64b73b5d104c10f748431666f687_tuple = PyTuple_New( 9 );
    PyTuple_SET_ITEM( const_tuple_722c64b73b5d104c10f748431666f687_tuple, 0, const_str_plain_cover ); Py_INCREF( const_str_plain_cover );
    PyTuple_SET_ITEM( const_tuple_722c64b73b5d104c10f748431666f687_tuple, 1, const_str_plain_desc ); Py_INCREF( const_str_plain_desc );
    PyTuple_SET_ITEM( const_tuple_722c64b73b5d104c10f748431666f687_tuple, 2, const_str_plain_mask ); Py_INCREF( const_str_plain_mask );
    PyTuple_SET_ITEM( const_tuple_722c64b73b5d104c10f748431666f687_tuple, 3, const_str_plain_meta ); Py_INCREF( const_str_plain_meta );
    PyTuple_SET_ITEM( const_tuple_722c64b73b5d104c10f748431666f687_tuple, 4, const_str_plain_info ); Py_INCREF( const_str_plain_info );
    PyTuple_SET_ITEM( const_tuple_722c64b73b5d104c10f748431666f687_tuple, 5, const_str_plain_editions ); Py_INCREF( const_str_plain_editions );
    PyTuple_SET_ITEM( const_tuple_722c64b73b5d104c10f748431666f687_tuple, 6, const_str_plain_isbn_from_words ); Py_INCREF( const_str_plain_isbn_from_words );
    PyTuple_SET_ITEM( const_tuple_722c64b73b5d104c10f748431666f687_tuple, 7, const_str_plain_doi ); Py_INCREF( const_str_plain_doi );
    PyTuple_SET_ITEM( const_tuple_722c64b73b5d104c10f748431666f687_tuple, 8, const_str_plain_ren ); Py_INCREF( const_str_plain_ren );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_isbnlib( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_69acea11e19376c3d337b88291f85fcc;
static PyCodeObject *codeobj_d1b2314efce60764444d7489e8e584e3;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_db1c32457a7ae665e53016b13b232e0a );
    codeobj_69acea11e19376c3d337b88291f85fcc = MAKE_CODEOBJ( module_filename_obj, const_str_plain_emit, 20, const_tuple_str_plain_self_str_plain_record_tuple, 2, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_d1b2314efce60764444d7489e8e584e3 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_isbnlib, 1, const_tuple_empty, 0, CO_NOFREE );
}

// The module function declarations.
NUITKA_LOCAL_MODULE PyObject *impl_class_1_NullHandler_of_isbnlib( PyObject **python_pars );


static PyObject *MAKE_FUNCTION_function_1_emit_of_class_1_NullHandler_of_isbnlib(  );


// The module function definitions.
NUITKA_LOCAL_MODULE PyObject *impl_class_1_NullHandler_of_isbnlib( PyObject **python_pars )
{
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
    assert(!had_error); // Do not enter inlined functions with error set.
#endif

    // Local variable declarations.
    PyObject *var___module__ = NULL;
    PyObject *var_emit = NULL;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_return_value;
    tmp_return_value = NULL;

    // Actual function code.
    tmp_assign_source_1 = const_str_plain_isbnlib;
    assert( var___module__ == NULL );
    Py_INCREF( tmp_assign_source_1 );
    var___module__ = tmp_assign_source_1;

    tmp_assign_source_2 = MAKE_FUNCTION_function_1_emit_of_class_1_NullHandler_of_isbnlib(  );
    assert( var_emit == NULL );
    var_emit = tmp_assign_source_2;

    // Tried code:
    tmp_return_value = PyDict_New();
    if ( var___module__ )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain___module__,
            var___module__
        );

        assert( res == 0 );
    }

    if ( var_emit )
    {
        int res = PyDict_SetItem(
            tmp_return_value,
            const_str_plain_emit,
            var_emit
        );

        assert( res == 0 );
    }

    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( class_1_NullHandler_of_isbnlib );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)var___module__ );
    Py_DECREF( var___module__ );
    var___module__ = NULL;

    CHECK_OBJECT( (PyObject *)var_emit );
    Py_DECREF( var_emit );
    var_emit = NULL;

    goto function_return_exit;
    // End of try:
    CHECK_OBJECT( (PyObject *)var___module__ );
    Py_DECREF( var___module__ );
    var___module__ = NULL;

    CHECK_OBJECT( (PyObject *)var_emit );
    Py_DECREF( var_emit );
    var_emit = NULL;


    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( class_1_NullHandler_of_isbnlib );
    return NULL;

    function_return_exit:

    CHECK_OBJECT( tmp_return_value );
    assert( had_error || !ERROR_OCCURRED() );
    return tmp_return_value;

}


static PyObject *impl_function_1_emit_of_class_1_NullHandler_of_isbnlib( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_self = python_pars[ 0 ];
    PyObject *par_record = python_pars[ 1 ];
    PyObject *tmp_return_value;
    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_1_emit_of_class_1_NullHandler_of_isbnlib );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_self );
    Py_DECREF( par_self );
    par_self = NULL;

    CHECK_OBJECT( (PyObject *)par_record );
    Py_DECREF( par_record );
    par_record = NULL;

    goto function_return_exit;
    // End of try:
    CHECK_OBJECT( (PyObject *)par_self );
    Py_DECREF( par_self );
    par_self = NULL;

    CHECK_OBJECT( (PyObject *)par_record );
    Py_DECREF( par_record );
    par_record = NULL;


    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_1_emit_of_class_1_NullHandler_of_isbnlib );
    return NULL;

    function_return_exit:

    CHECK_OBJECT( tmp_return_value );
    assert( had_error || !ERROR_OCCURRED() );
    return tmp_return_value;

}



static PyObject *MAKE_FUNCTION_function_1_emit_of_class_1_NullHandler_of_isbnlib(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_1_emit_of_class_1_NullHandler_of_isbnlib,
        const_str_plain_emit,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_69acea11e19376c3d337b88291f85fcc,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_isbnlib,
        Py_None
    );

    return result;
}



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_isbnlib =
{
    PyModuleDef_HEAD_INIT,
    "isbnlib",   /* m_name */
    NULL,                /* m_doc */
    -1,                  /* m_size */
    NULL,                /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#endif

#if PYTHON_VERSION >= 300
extern PyObject *metapath_based_loader;
#endif

// The exported interface to CPython. On import of the module, this function
// gets called. It has to have an exact function name, in cases it's a shared
// library export. This is hidden behind the MOD_INIT_DECL.

MOD_INIT_DECL( isbnlib )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_isbnlib );
    }
    else
    {
        _init_done = true;
    }
#endif

#ifdef _NUITKA_MODULE
    // In case of a stand alone extension module, need to call initialization
    // the init here because that's the first and only time we are going to get
    // called here.

    // Initialize the constant values used.
    _initBuiltinModule();
    createGlobalConstants();

    // Initialize the compiled types of Nuitka.
    PyType_Ready( &Nuitka_Generator_Type );
    PyType_Ready( &Nuitka_Function_Type );
    PyType_Ready( &Nuitka_Method_Type );
    PyType_Ready( &Nuitka_Frame_Type );
#if PYTHON_VERSION >= 350
    PyType_Ready( &Nuitka_Coroutine_Type );
    PyType_Ready( &Nuitka_CoroutineWrapper_Type );
#endif

#if PYTHON_VERSION < 300
    _initSlotCompare();
#endif
#if PYTHON_VERSION >= 270
    _initSlotIternext();
#endif

    patchBuiltinModule();
    patchTypeComparison();

    // Enable meta path based loader if not already done.
    setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 300
    patchInspectModule();
#endif

#endif

    createModuleConstants();
    createModuleCodeObjects();

    // puts( "in initisbnlib" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_isbnlib = Py_InitModule4(
        "isbnlib",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_isbnlib = PyModule_Create( &mdef_isbnlib );
#endif

    moduledict_isbnlib = (PyDictObject *)((PyModuleObject *)module_isbnlib)->md_dict;

    CHECK_OBJECT( module_isbnlib );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_plain_isbnlib, module_isbnlib );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_isbnlib );

    if ( PyDict_GetItem( module_dict, const_str_plain___builtins__ ) == NULL )
    {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then.
#if !defined(_NUITKA_EXE) || !0
        value = PyModule_GetDict( value );
#endif

#ifndef __NUITKA_NO_ASSERT__
        int res =
#endif
            PyDict_SetItem( module_dict, const_str_plain___builtins__, value );

        assert( res == 0 );
    }

#if PYTHON_VERSION >= 330
    PyDict_SetItem( module_dict, const_str_plain___loader__, metapath_based_loader );
#endif

    // Temp variables if any
    PyObject *tmp_class_creation_1__bases = NULL;
    PyObject *tmp_class_creation_1__class_dict = NULL;
    PyObject *tmp_class_creation_1__metaclass = NULL;
    PyObject *tmp_class_creation_1__class = NULL;
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *exception_keeper_type_2;
    PyObject *exception_keeper_value_2;
    PyTracebackObject *exception_keeper_tb_2;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_2;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_args_element_name_2;
    PyObject *tmp_args_element_name_3;
    PyObject *tmp_args_element_name_4;
    PyObject *tmp_args_element_name_5;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_assign_source_4;
    PyObject *tmp_assign_source_5;
    PyObject *tmp_assign_source_6;
    PyObject *tmp_assign_source_7;
    PyObject *tmp_assign_source_8;
    PyObject *tmp_assign_source_9;
    PyObject *tmp_assign_source_10;
    PyObject *tmp_assign_source_11;
    PyObject *tmp_assign_source_12;
    PyObject *tmp_assign_source_13;
    PyObject *tmp_assign_source_14;
    PyObject *tmp_assign_source_15;
    PyObject *tmp_assign_source_16;
    PyObject *tmp_assign_source_17;
    PyObject *tmp_assign_source_18;
    PyObject *tmp_assign_source_19;
    PyObject *tmp_assign_source_20;
    PyObject *tmp_assign_source_21;
    PyObject *tmp_assign_source_22;
    PyObject *tmp_assign_source_23;
    PyObject *tmp_assign_source_24;
    PyObject *tmp_assign_source_25;
    PyObject *tmp_assign_source_26;
    PyObject *tmp_assign_source_27;
    PyObject *tmp_assign_source_28;
    PyObject *tmp_assign_source_29;
    PyObject *tmp_assign_source_30;
    PyObject *tmp_assign_source_31;
    PyObject *tmp_assign_source_32;
    PyObject *tmp_assign_source_33;
    PyObject *tmp_assign_source_34;
    PyObject *tmp_assign_source_35;
    PyObject *tmp_assign_source_36;
    PyObject *tmp_assign_source_37;
    PyObject *tmp_assign_source_38;
    PyObject *tmp_assign_source_39;
    PyObject *tmp_assign_source_40;
    PyObject *tmp_assign_source_41;
    PyObject *tmp_assign_source_42;
    PyObject *tmp_assign_source_43;
    PyObject *tmp_assign_source_44;
    PyObject *tmp_assign_source_45;
    PyObject *tmp_assign_source_46;
    PyObject *tmp_assign_source_47;
    PyObject *tmp_assign_source_48;
    PyObject *tmp_assign_source_49;
    PyObject *tmp_assign_source_50;
    PyObject *tmp_bases_name_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_called_name_3;
    PyObject *tmp_called_name_4;
    PyObject *tmp_called_name_5;
    PyObject *tmp_called_name_6;
    int tmp_cmp_In_1;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_dict_name_1;
    PyObject *tmp_import_globals_1;
    PyObject *tmp_import_globals_2;
    PyObject *tmp_import_globals_3;
    PyObject *tmp_import_globals_4;
    PyObject *tmp_import_globals_5;
    PyObject *tmp_import_globals_6;
    PyObject *tmp_import_globals_7;
    PyObject *tmp_import_globals_8;
    PyObject *tmp_import_globals_9;
    PyObject *tmp_import_globals_10;
    PyObject *tmp_import_globals_11;
    PyObject *tmp_import_globals_12;
    PyObject *tmp_import_globals_13;
    PyObject *tmp_import_globals_14;
    PyObject *tmp_import_globals_15;
    PyObject *tmp_import_globals_16;
    PyObject *tmp_import_globals_17;
    PyObject *tmp_import_globals_18;
    PyObject *tmp_import_globals_19;
    PyObject *tmp_import_globals_20;
    PyObject *tmp_import_globals_21;
    PyObject *tmp_import_globals_22;
    PyObject *tmp_import_globals_23;
    PyObject *tmp_import_globals_24;
    PyObject *tmp_import_globals_25;
    PyObject *tmp_import_globals_26;
    PyObject *tmp_import_globals_27;
    PyObject *tmp_import_globals_28;
    PyObject *tmp_import_globals_29;
    PyObject *tmp_import_globals_30;
    PyObject *tmp_import_globals_31;
    PyObject *tmp_import_globals_32;
    PyObject *tmp_import_globals_33;
    PyObject *tmp_import_globals_34;
    PyObject *tmp_import_globals_35;
    PyObject *tmp_import_name_from_1;
    PyObject *tmp_import_name_from_2;
    PyObject *tmp_import_name_from_3;
    PyObject *tmp_import_name_from_4;
    PyObject *tmp_import_name_from_5;
    PyObject *tmp_import_name_from_6;
    PyObject *tmp_import_name_from_7;
    PyObject *tmp_import_name_from_8;
    PyObject *tmp_import_name_from_9;
    PyObject *tmp_import_name_from_10;
    PyObject *tmp_import_name_from_11;
    PyObject *tmp_import_name_from_12;
    PyObject *tmp_import_name_from_13;
    PyObject *tmp_import_name_from_14;
    PyObject *tmp_import_name_from_15;
    PyObject *tmp_import_name_from_16;
    PyObject *tmp_import_name_from_17;
    PyObject *tmp_import_name_from_18;
    PyObject *tmp_import_name_from_19;
    PyObject *tmp_import_name_from_20;
    PyObject *tmp_import_name_from_21;
    PyObject *tmp_import_name_from_22;
    PyObject *tmp_import_name_from_23;
    PyObject *tmp_import_name_from_24;
    PyObject *tmp_import_name_from_25;
    PyObject *tmp_import_name_from_26;
    PyObject *tmp_import_name_from_27;
    PyObject *tmp_import_name_from_28;
    PyObject *tmp_import_name_from_29;
    PyObject *tmp_import_name_from_30;
    PyObject *tmp_import_name_from_31;
    PyObject *tmp_import_name_from_32;
    PyObject *tmp_import_name_from_33;
    PyObject *tmp_import_name_from_34;
    PyObject *tmp_key_name_1;
    PyObject *tmp_list_element_1;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    PyObject *tmp_source_name_3;
    PyObject *tmp_source_name_4;
    PyObject *tmp_source_name_5;
    PyObject *tmp_tuple_element_1;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    PyFrameObject *frame_module;


    // Module code.
    tmp_assign_source_1 = const_str_digest_ed2f8d97f44c0eec471ecabd377f988a;
    UPDATE_STRING_DICT0( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    // Frame without reuse.
    frame_module = MAKE_MODULE_FRAME( codeobj_d1b2314efce60764444d7489e8e584e3, module_isbnlib );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_module );
    assert( Py_REFCNT( frame_module ) == 1 );

#if PYTHON_VERSION >= 340
    frame_module->f_executing += 1;
#endif

    // Framed code:
    tmp_assign_source_3 = PyList_New( 1 );
    tmp_source_name_1 = PyObject_GetAttrString(PyImport_ImportModule("os"), "path");
    if ( tmp_source_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_3 );


        goto frame_exception_exit_1;
    }
    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_dirname );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_3 );


        goto frame_exception_exit_1;
    }
    tmp_args_element_name_1 = module_filename_obj;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_list_element_1 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    Py_DECREF( tmp_called_name_1 );
    if ( tmp_list_element_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_3 );


        goto frame_exception_exit_1;
    }
    PyList_SET_ITEM( tmp_assign_source_3, 0, tmp_list_element_1 );
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain___path__, tmp_assign_source_3 );
    tmp_import_globals_1 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 8;
    tmp_assign_source_4 = IMPORT_MODULE( const_str_plain_logging, tmp_import_globals_1, tmp_import_globals_1, Py_None, const_int_neg_1 );
    if ( tmp_assign_source_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 8;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain__logging, tmp_assign_source_4 );
    tmp_import_globals_2 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_1 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_2, tmp_import_globals_2, const_tuple_1ec9a5d983a97d17880bfb27bf3aef6c_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_5 = IMPORT_NAME( tmp_import_name_from_1, const_str_plain_quiet_errors );
    Py_DECREF( tmp_import_name_from_1 );
    if ( tmp_assign_source_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_quiet_errors, tmp_assign_source_5 );
    tmp_import_globals_3 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_2 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_3, tmp_import_globals_3, const_tuple_1ec9a5d983a97d17880bfb27bf3aef6c_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_6 = IMPORT_NAME( tmp_import_name_from_2, const_str_plain_ISBNLibException );
    Py_DECREF( tmp_import_name_from_2 );
    if ( tmp_assign_source_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_ISBNLibException, tmp_assign_source_6 );
    tmp_import_globals_4 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_3 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_4, tmp_import_globals_4, const_tuple_1ec9a5d983a97d17880bfb27bf3aef6c_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_7 = IMPORT_NAME( tmp_import_name_from_3, const_str_plain_NotRecognizedServiceError );
    Py_DECREF( tmp_import_name_from_3 );
    if ( tmp_assign_source_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_NotRecognizedServiceError, tmp_assign_source_7 );
    tmp_import_globals_5 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_4 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_5, tmp_import_globals_5, const_tuple_1ec9a5d983a97d17880bfb27bf3aef6c_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_8 = IMPORT_NAME( tmp_import_name_from_4, const_str_plain_NotValidISBNError );
    Py_DECREF( tmp_import_name_from_4 );
    if ( tmp_assign_source_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_NotValidISBNError, tmp_assign_source_8 );
    tmp_import_globals_6 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_5 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_6, tmp_import_globals_6, const_tuple_1ec9a5d983a97d17880bfb27bf3aef6c_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_9 = IMPORT_NAME( tmp_import_name_from_5, const_str_plain_PluginNotLoadedError );
    Py_DECREF( tmp_import_name_from_5 );
    if ( tmp_assign_source_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_PluginNotLoadedError, tmp_assign_source_9 );
    // Tried code:
    tmp_source_name_2 = GET_STRING_DICT_VALUE( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain__logging );

    if (unlikely( tmp_source_name_2 == NULL ))
    {
        tmp_source_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__logging );
    }

    if ( tmp_source_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "_logging" );
        exception_tb = NULL;

        exception_lineno = 16;
        goto try_except_handler_1;
    }

    tmp_called_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_NullHandler );
    if ( tmp_called_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 16;
        goto try_except_handler_1;
    }
    frame_module->f_lineno = 16;
    tmp_assign_source_10 = CALL_FUNCTION_NO_ARGS( tmp_called_name_2 );
    Py_DECREF( tmp_called_name_2 );
    if ( tmp_assign_source_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 16;
        goto try_except_handler_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain__nh, tmp_assign_source_10 );
    goto try_end_1;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    // Preserve existing published exception.
    PRESERVE_FRAME_EXCEPTION( frame_module );
    if ( exception_keeper_tb_1 == NULL )
    {
        exception_keeper_tb_1 = MAKE_TRACEBACK( frame_module, exception_keeper_lineno_1 );
    }
    else if ( exception_keeper_lineno_1 != -1 )
    {
        exception_keeper_tb_1 = ADD_TRACEBACK( exception_keeper_tb_1, frame_module, exception_keeper_lineno_1 );
    }

    NORMALIZE_EXCEPTION( &exception_keeper_type_1, &exception_keeper_value_1, &exception_keeper_tb_1 );
    PUBLISH_EXCEPTION( &exception_keeper_type_1, &exception_keeper_value_1, &exception_keeper_tb_1 );
    // Tried code:
    tmp_assign_source_11 = PyTuple_New( 1 );
    tmp_source_name_3 = GET_STRING_DICT_VALUE( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain__logging );

    if (unlikely( tmp_source_name_3 == NULL ))
    {
        tmp_source_name_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__logging );
    }

    if ( tmp_source_name_3 == NULL )
    {
        Py_DECREF( tmp_assign_source_11 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "_logging" );
        exception_tb = NULL;

        exception_lineno = 19;
        goto try_except_handler_2;
    }

    tmp_tuple_element_1 = LOOKUP_ATTRIBUTE( tmp_source_name_3, const_str_plain_Handler );
    if ( tmp_tuple_element_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_assign_source_11 );

        exception_lineno = 19;
        goto try_except_handler_2;
    }
    PyTuple_SET_ITEM( tmp_assign_source_11, 0, tmp_tuple_element_1 );
    assert( tmp_class_creation_1__bases == NULL );
    tmp_class_creation_1__bases = tmp_assign_source_11;

    tmp_assign_source_12 = impl_class_1_NullHandler_of_isbnlib( NULL );
    assert( tmp_assign_source_12 != NULL );
    assert( tmp_class_creation_1__class_dict == NULL );
    tmp_class_creation_1__class_dict = tmp_assign_source_12;

    tmp_compare_left_1 = const_str_plain___metaclass__;
    tmp_compare_right_1 = tmp_class_creation_1__class_dict;

    tmp_cmp_In_1 = PySequence_Contains( tmp_compare_right_1, tmp_compare_left_1 );
    assert( !(tmp_cmp_In_1 == -1) );
    if ( tmp_cmp_In_1 == 1 )
    {
        goto condexpr_true_1;
    }
    else
    {
        goto condexpr_false_1;
    }
    condexpr_true_1:;
    tmp_dict_name_1 = tmp_class_creation_1__class_dict;

    tmp_key_name_1 = const_str_plain___metaclass__;
    tmp_assign_source_13 = DICT_GET_ITEM( tmp_dict_name_1, tmp_key_name_1 );
    if ( tmp_assign_source_13 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 19;
        goto try_except_handler_2;
    }
    goto condexpr_end_1;
    condexpr_false_1:;
    tmp_bases_name_1 = tmp_class_creation_1__bases;

    tmp_assign_source_13 = SELECT_METACLASS( tmp_bases_name_1, GET_STRING_DICT_VALUE( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain___metaclass__ ) );
    condexpr_end_1:;
    assert( tmp_class_creation_1__metaclass == NULL );
    tmp_class_creation_1__metaclass = tmp_assign_source_13;

    tmp_called_name_3 = tmp_class_creation_1__metaclass;

    tmp_args_element_name_2 = const_str_plain_NullHandler;
    tmp_args_element_name_3 = tmp_class_creation_1__bases;

    tmp_args_element_name_4 = tmp_class_creation_1__class_dict;

    frame_module->f_lineno = 19;
    {
        PyObject *call_args[] = { tmp_args_element_name_2, tmp_args_element_name_3, tmp_args_element_name_4 };
        tmp_assign_source_14 = CALL_FUNCTION_WITH_ARGS3( tmp_called_name_3, call_args );
    }

    if ( tmp_assign_source_14 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 19;
        goto try_except_handler_2;
    }
    assert( tmp_class_creation_1__class == NULL );
    tmp_class_creation_1__class = tmp_assign_source_14;

    goto try_end_2;
    // Exception handler code:
    try_except_handler_2:;
    exception_keeper_type_2 = exception_type;
    exception_keeper_value_2 = exception_value;
    exception_keeper_tb_2 = exception_tb;
    exception_keeper_lineno_2 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    Py_XDECREF( tmp_class_creation_1__bases );
    tmp_class_creation_1__bases = NULL;

    Py_XDECREF( tmp_class_creation_1__class_dict );
    tmp_class_creation_1__class_dict = NULL;

    Py_XDECREF( tmp_class_creation_1__metaclass );
    tmp_class_creation_1__metaclass = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_2;
    exception_value = exception_keeper_value_2;
    exception_tb = exception_keeper_tb_2;
    exception_lineno = exception_keeper_lineno_2;

    goto frame_exception_exit_1;
    // End of try:
    try_end_2:;
    tmp_assign_source_15 = tmp_class_creation_1__class;

    UPDATE_STRING_DICT0( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_NullHandler, tmp_assign_source_15 );
    CHECK_OBJECT( (PyObject *)tmp_class_creation_1__class );
    Py_DECREF( tmp_class_creation_1__class );
    tmp_class_creation_1__class = NULL;

    CHECK_OBJECT( (PyObject *)tmp_class_creation_1__bases );
    Py_DECREF( tmp_class_creation_1__bases );
    tmp_class_creation_1__bases = NULL;

    CHECK_OBJECT( (PyObject *)tmp_class_creation_1__class_dict );
    Py_DECREF( tmp_class_creation_1__class_dict );
    tmp_class_creation_1__class_dict = NULL;

    CHECK_OBJECT( (PyObject *)tmp_class_creation_1__metaclass );
    Py_DECREF( tmp_class_creation_1__metaclass );
    tmp_class_creation_1__metaclass = NULL;

    tmp_called_name_4 = GET_STRING_DICT_VALUE( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_NullHandler );

    if (unlikely( tmp_called_name_4 == NULL ))
    {
        tmp_called_name_4 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_NullHandler );
    }

    if ( tmp_called_name_4 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "NullHandler" );
        exception_tb = NULL;

        exception_lineno = 23;
        goto frame_exception_exit_1;
    }

    frame_module->f_lineno = 23;
    tmp_assign_source_16 = CALL_FUNCTION_NO_ARGS( tmp_called_name_4 );
    if ( tmp_assign_source_16 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 23;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain__nh, tmp_assign_source_16 );
    goto try_end_1;
    // exception handler codes exits in all cases
    NUITKA_CANNOT_GET_HERE( isbnlib );
    return MOD_RETURN_VALUE( NULL );
    // End of try:
    try_end_1:;
    tmp_source_name_5 = GET_STRING_DICT_VALUE( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain__logging );

    if (unlikely( tmp_source_name_5 == NULL ))
    {
        tmp_source_name_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__logging );
    }

    if ( tmp_source_name_5 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "_logging" );
        exception_tb = NULL;

        exception_lineno = 24;
        goto frame_exception_exit_1;
    }

    tmp_called_name_6 = LOOKUP_ATTRIBUTE( tmp_source_name_5, const_str_plain_getLogger );
    if ( tmp_called_name_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 24;
        goto frame_exception_exit_1;
    }
    frame_module->f_lineno = 24;
    tmp_source_name_4 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_6, &PyTuple_GET_ITEM( const_tuple_str_plain_isbnlib_tuple, 0 ) );

    Py_DECREF( tmp_called_name_6 );
    if ( tmp_source_name_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 24;
        goto frame_exception_exit_1;
    }
    tmp_called_name_5 = LOOKUP_ATTRIBUTE( tmp_source_name_4, const_str_plain_addHandler );
    Py_DECREF( tmp_source_name_4 );
    if ( tmp_called_name_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 24;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_5 = GET_STRING_DICT_VALUE( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain__nh );

    if (unlikely( tmp_args_element_name_5 == NULL ))
    {
        tmp_args_element_name_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__nh );
    }

    if ( tmp_args_element_name_5 == NULL )
    {
        Py_DECREF( tmp_called_name_5 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "_nh" );
        exception_tb = NULL;

        exception_lineno = 24;
        goto frame_exception_exit_1;
    }

    frame_module->f_lineno = 24;
    {
        PyObject *call_args[] = { tmp_args_element_name_5 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_5, call_args );
    }

    Py_DECREF( tmp_called_name_5 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 24;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_import_globals_7 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 27;
    tmp_import_name_from_6 = IMPORT_MODULE( const_str_empty, tmp_import_globals_7, tmp_import_globals_7, const_tuple_str_plain_config_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 27;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_17 = IMPORT_NAME( tmp_import_name_from_6, const_str_plain_config );
    Py_DECREF( tmp_import_name_from_6 );
    if ( tmp_assign_source_17 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 27;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_config, tmp_assign_source_17 );
    tmp_import_globals_8 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_7 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_8, tmp_import_globals_8, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_18 = IMPORT_NAME( tmp_import_name_from_7, const_str_plain_is_isbn10 );
    Py_DECREF( tmp_import_name_from_7 );
    if ( tmp_assign_source_18 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_is_isbn10, tmp_assign_source_18 );
    tmp_import_globals_9 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_8 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_9, tmp_import_globals_9, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_19 = IMPORT_NAME( tmp_import_name_from_8, const_str_plain_is_isbn13 );
    Py_DECREF( tmp_import_name_from_8 );
    if ( tmp_assign_source_19 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_is_isbn13, tmp_assign_source_19 );
    tmp_import_globals_10 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_9 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_10, tmp_import_globals_10, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_20 = IMPORT_NAME( tmp_import_name_from_9, const_str_plain_to_isbn10 );
    Py_DECREF( tmp_import_name_from_9 );
    if ( tmp_assign_source_20 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_to_isbn10, tmp_assign_source_20 );
    tmp_import_globals_11 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_10 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_11, tmp_import_globals_11, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_21 = IMPORT_NAME( tmp_import_name_from_10, const_str_plain_to_isbn13 );
    Py_DECREF( tmp_import_name_from_10 );
    if ( tmp_assign_source_21 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_to_isbn13, tmp_assign_source_21 );
    tmp_import_globals_12 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_11 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_12, tmp_import_globals_12, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_11 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_22 = IMPORT_NAME( tmp_import_name_from_11, const_str_plain_clean );
    Py_DECREF( tmp_import_name_from_11 );
    if ( tmp_assign_source_22 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_clean, tmp_assign_source_22 );
    tmp_import_globals_13 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_12 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_13, tmp_import_globals_13, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_12 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_23 = IMPORT_NAME( tmp_import_name_from_12, const_str_plain_canonical );
    Py_DECREF( tmp_import_name_from_12 );
    if ( tmp_assign_source_23 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_canonical, tmp_assign_source_23 );
    tmp_import_globals_14 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_13 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_14, tmp_import_globals_14, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_13 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_24 = IMPORT_NAME( tmp_import_name_from_13, const_str_plain_notisbn );
    Py_DECREF( tmp_import_name_from_13 );
    if ( tmp_assign_source_24 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_notisbn, tmp_assign_source_24 );
    tmp_import_globals_15 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_14 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_15, tmp_import_globals_15, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_14 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_25 = IMPORT_NAME( tmp_import_name_from_14, const_str_plain_get_isbnlike );
    Py_DECREF( tmp_import_name_from_14 );
    if ( tmp_assign_source_25 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_get_isbnlike, tmp_assign_source_25 );
    tmp_import_globals_16 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_15 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_16, tmp_import_globals_16, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_15 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_26 = IMPORT_NAME( tmp_import_name_from_15, const_str_plain_get_canonical_isbn );
    Py_DECREF( tmp_import_name_from_15 );
    if ( tmp_assign_source_26 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_get_canonical_isbn, tmp_assign_source_26 );
    tmp_import_globals_17 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_16 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_17, tmp_import_globals_17, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_16 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_27 = IMPORT_NAME( tmp_import_name_from_16, const_str_plain_GTIN13 );
    Py_DECREF( tmp_import_name_from_16 );
    if ( tmp_assign_source_27 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_GTIN13, tmp_assign_source_27 );
    tmp_import_globals_18 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_17 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_18, tmp_import_globals_18, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_17 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_28 = IMPORT_NAME( tmp_import_name_from_17, const_str_plain_EAN13 );
    Py_DECREF( tmp_import_name_from_17 );
    if ( tmp_assign_source_28 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_EAN13, tmp_assign_source_28 );
    tmp_import_globals_19 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_18 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_19, tmp_import_globals_19, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_18 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_29 = IMPORT_NAME( tmp_import_name_from_18, const_str_plain_RE_ISBN10 );
    Py_DECREF( tmp_import_name_from_18 );
    if ( tmp_assign_source_29 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_RE_ISBN10, tmp_assign_source_29 );
    tmp_import_globals_20 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_19 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_20, tmp_import_globals_20, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_19 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_30 = IMPORT_NAME( tmp_import_name_from_19, const_str_plain_RE_ISBN13 );
    Py_DECREF( tmp_import_name_from_19 );
    if ( tmp_assign_source_30 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_RE_ISBN13, tmp_assign_source_30 );
    tmp_import_globals_21 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_20 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_21, tmp_import_globals_21, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_20 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_31 = IMPORT_NAME( tmp_import_name_from_20, const_str_plain_RE_LOOSE );
    Py_DECREF( tmp_import_name_from_20 );
    if ( tmp_assign_source_31 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_RE_LOOSE, tmp_assign_source_31 );
    tmp_import_globals_22 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_21 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_22, tmp_import_globals_22, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_21 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_32 = IMPORT_NAME( tmp_import_name_from_21, const_str_plain_RE_NORMAL );
    Py_DECREF( tmp_import_name_from_21 );
    if ( tmp_assign_source_32 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_RE_NORMAL, tmp_assign_source_32 );
    tmp_import_globals_23 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 30;
    tmp_import_name_from_22 = IMPORT_MODULE( const_str_plain__core, tmp_import_globals_23, tmp_import_globals_23, const_tuple_2dd54363478e7f9167cad677209d7435_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_22 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_33 = IMPORT_NAME( tmp_import_name_from_22, const_str_plain_RE_STRICT );
    Py_DECREF( tmp_import_name_from_22 );
    if ( tmp_assign_source_33 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 30;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_RE_STRICT, tmp_assign_source_33 );
    tmp_import_globals_24 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 34;
    tmp_import_name_from_23 = IMPORT_MODULE( const_str_plain__ext, tmp_import_globals_24, tmp_import_globals_24, const_tuple_722c64b73b5d104c10f748431666f687_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_23 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_34 = IMPORT_NAME( tmp_import_name_from_23, const_str_plain_cover );
    Py_DECREF( tmp_import_name_from_23 );
    if ( tmp_assign_source_34 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_cover, tmp_assign_source_34 );
    tmp_import_globals_25 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 34;
    tmp_import_name_from_24 = IMPORT_MODULE( const_str_plain__ext, tmp_import_globals_25, tmp_import_globals_25, const_tuple_722c64b73b5d104c10f748431666f687_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_24 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_35 = IMPORT_NAME( tmp_import_name_from_24, const_str_plain_desc );
    Py_DECREF( tmp_import_name_from_24 );
    if ( tmp_assign_source_35 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_desc, tmp_assign_source_35 );
    tmp_import_globals_26 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 34;
    tmp_import_name_from_25 = IMPORT_MODULE( const_str_plain__ext, tmp_import_globals_26, tmp_import_globals_26, const_tuple_722c64b73b5d104c10f748431666f687_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_25 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_36 = IMPORT_NAME( tmp_import_name_from_25, const_str_plain_mask );
    Py_DECREF( tmp_import_name_from_25 );
    if ( tmp_assign_source_36 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_mask, tmp_assign_source_36 );
    tmp_import_globals_27 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 34;
    tmp_import_name_from_26 = IMPORT_MODULE( const_str_plain__ext, tmp_import_globals_27, tmp_import_globals_27, const_tuple_722c64b73b5d104c10f748431666f687_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_26 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_37 = IMPORT_NAME( tmp_import_name_from_26, const_str_plain_meta );
    Py_DECREF( tmp_import_name_from_26 );
    if ( tmp_assign_source_37 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_meta, tmp_assign_source_37 );
    tmp_import_globals_28 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 34;
    tmp_import_name_from_27 = IMPORT_MODULE( const_str_plain__ext, tmp_import_globals_28, tmp_import_globals_28, const_tuple_722c64b73b5d104c10f748431666f687_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_27 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_38 = IMPORT_NAME( tmp_import_name_from_27, const_str_plain_info );
    Py_DECREF( tmp_import_name_from_27 );
    if ( tmp_assign_source_38 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_info, tmp_assign_source_38 );
    tmp_import_globals_29 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 34;
    tmp_import_name_from_28 = IMPORT_MODULE( const_str_plain__ext, tmp_import_globals_29, tmp_import_globals_29, const_tuple_722c64b73b5d104c10f748431666f687_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_28 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_39 = IMPORT_NAME( tmp_import_name_from_28, const_str_plain_editions );
    Py_DECREF( tmp_import_name_from_28 );
    if ( tmp_assign_source_39 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_editions, tmp_assign_source_39 );
    tmp_import_globals_30 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 34;
    tmp_import_name_from_29 = IMPORT_MODULE( const_str_plain__ext, tmp_import_globals_30, tmp_import_globals_30, const_tuple_722c64b73b5d104c10f748431666f687_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_29 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_40 = IMPORT_NAME( tmp_import_name_from_29, const_str_plain_isbn_from_words );
    Py_DECREF( tmp_import_name_from_29 );
    if ( tmp_assign_source_40 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_isbn_from_words, tmp_assign_source_40 );
    tmp_import_globals_31 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 34;
    tmp_import_name_from_30 = IMPORT_MODULE( const_str_plain__ext, tmp_import_globals_31, tmp_import_globals_31, const_tuple_722c64b73b5d104c10f748431666f687_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_30 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_41 = IMPORT_NAME( tmp_import_name_from_30, const_str_plain_doi );
    Py_DECREF( tmp_import_name_from_30 );
    if ( tmp_assign_source_41 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_doi, tmp_assign_source_41 );
    tmp_import_globals_32 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 34;
    tmp_import_name_from_31 = IMPORT_MODULE( const_str_plain__ext, tmp_import_globals_32, tmp_import_globals_32, const_tuple_722c64b73b5d104c10f748431666f687_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_31 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_42 = IMPORT_NAME( tmp_import_name_from_31, const_str_plain_ren );
    Py_DECREF( tmp_import_name_from_31 );
    if ( tmp_assign_source_42 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_ren, tmp_assign_source_42 );
    tmp_import_globals_33 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 36;
    tmp_import_name_from_32 = IMPORT_MODULE( const_str_plain__goom, tmp_import_globals_33, tmp_import_globals_33, const_tuple_str_plain_query_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_32 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 36;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_43 = IMPORT_NAME( tmp_import_name_from_32, const_str_plain_query );
    Py_DECREF( tmp_import_name_from_32 );
    if ( tmp_assign_source_43 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 36;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_goom, tmp_assign_source_43 );
    tmp_import_globals_34 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 37;
    tmp_import_name_from_33 = IMPORT_MODULE( const_str_plain__doitotex, tmp_import_globals_34, tmp_import_globals_34, const_tuple_str_plain_doi2tex_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_33 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 37;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_44 = IMPORT_NAME( tmp_import_name_from_33, const_str_plain_doi2tex );
    Py_DECREF( tmp_import_name_from_33 );
    if ( tmp_assign_source_44 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 37;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_doi2tex, tmp_assign_source_44 );
    tmp_import_globals_35 = ((PyModuleObject *)module_isbnlib)->md_dict;
    frame_module->f_lineno = 40;
    tmp_import_name_from_34 = IMPORT_MODULE( const_str_digest_260aecc1c2bfc603c94e52a492c0caa3, tmp_import_globals_35, tmp_import_globals_35, const_tuple_str_plain_RDDATE_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_34 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 40;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_45 = IMPORT_NAME( tmp_import_name_from_34, const_str_plain_RDDATE );
    Py_DECREF( tmp_import_name_from_34 );
    if ( tmp_assign_source_45 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 40;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_RDDATE, tmp_assign_source_45 );
    tmp_assign_source_46 = GET_STRING_DICT_VALUE( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_EAN13 );

    if (unlikely( tmp_assign_source_46 == NULL ))
    {
        tmp_assign_source_46 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_EAN13 );
    }

    if ( tmp_assign_source_46 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "EAN13" );
        exception_tb = NULL;

        exception_lineno = 43;
        goto frame_exception_exit_1;
    }

    UPDATE_STRING_DICT0( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_ISBN13, tmp_assign_source_46 );
    tmp_assign_source_47 = GET_STRING_DICT_VALUE( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_EAN13 );

    if (unlikely( tmp_assign_source_47 == NULL ))
    {
        tmp_assign_source_47 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_EAN13 );
    }

    if ( tmp_assign_source_47 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "EAN13" );
        exception_tb = NULL;

        exception_lineno = 44;
        goto frame_exception_exit_1;
    }

    UPDATE_STRING_DICT0( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain_ean13, tmp_assign_source_47 );

    // Restore frame exception if necessary.
#if 1
    RESTORE_FRAME_EXCEPTION( frame_module );
#endif
    popFrameStack();

    assertFrameObject( frame_module );
    Py_DECREF( frame_module );

    goto frame_no_exception_1;
    frame_exception_exit_1:;
#if 1
    RESTORE_FRAME_EXCEPTION( frame_module );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( frame_module, exception_lineno );
    }
    else if ( exception_tb->tb_frame != frame_module )
    {
        PyTracebackObject *traceback_new = MAKE_TRACEBACK( frame_module, exception_lineno );
        traceback_new->tb_next = exception_tb;
        exception_tb = traceback_new;
    }

    // Put the previous frame back on top.
    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_module->f_executing -= 1;
#endif
    Py_DECREF( frame_module );

    // Return the error.
    goto module_exception_exit;
    frame_no_exception_1:;
    tmp_assign_source_48 = const_tuple_2c00889c4f9ce4e4a90373868d3bdd45_tuple;
    UPDATE_STRING_DICT0( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain___all__, tmp_assign_source_48 );
    tmp_assign_source_49 = const_str_digest_edb993cc5666e55721eb806e6f8ef908;
    UPDATE_STRING_DICT0( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain___version__, tmp_assign_source_49 );
    tmp_assign_source_50 = const_str_digest_54d96c8010d214731f1dcae8dde8f9de;
    UPDATE_STRING_DICT0( moduledict_isbnlib, (Nuitka_StringObject *)const_str_plain___support__, tmp_assign_source_50 );

    return MOD_RETURN_VALUE( module_isbnlib );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
