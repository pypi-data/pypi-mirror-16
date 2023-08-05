/* Generated code for Python source for module 'isbnlib.dev'
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

/* The _module_isbnlib$dev is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_isbnlib$dev;
PyDictObject *moduledict_isbnlib$dev;

/* The module constants used, if any. */
extern PyObject *const_str_plain_WEBService;
static PyObject *const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple;
extern PyObject *const_int_pos_1;
extern PyObject *const_str_plain_ISBNLibHTTPError;
static PyObject *const_str_plain_ISBNToolsURLError;
extern PyObject *const_str_plain_dev;
extern PyObject *const_str_plain_ServiceIsDownError;
extern PyObject *const_str_empty;
extern PyObject *const_str_plain_DataWrongShapeError;
extern PyObject *const_str_plain_NotValidMetadataError;
static PyObject *const_str_plain_ISBNToolsDevException;
static PyObject *const_tuple_str_plain_WEBService_tuple;
extern PyObject *const_str_plain_vias;
static PyObject *const_tuple_43825479620781d3a694764e6071a520_tuple;
extern PyObject *const_str_plain_RecordMappingError;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain_webservice;
static PyObject *const_tuple_str_plain_WEBQuery_tuple;
extern PyObject *const_str_plain_webquery;
extern PyObject *const_tuple_empty;
extern PyObject *const_str_plain_Metadata;
extern PyObject *const_str_plain_DataNotFoundAtServiceError;
extern PyObject *const_str_plain_NoDataForSelectorError;
extern PyObject *const_str_plain___file__;
extern PyObject *const_str_plain_helpers;
static PyObject *const_tuple_str_plain_bouth23_str_plain_helpers_str_plain_vias_tuple;
extern PyObject *const_str_plain_ISBNLibDevException;
static PyObject *const_str_digest_4214ea3c004a2b4b1e63a9fb3e2ea544;
extern PyObject *const_str_plain__data;
extern PyObject *const_str_plain_ISBNLibURLError;
extern PyObject *const_str_plain___path__;
extern PyObject *const_str_plain___all__;
extern PyObject *const_str_plain_bouth23;
extern PyObject *const_str_plain_dirname;
extern PyObject *const_str_plain_WEBQuery;
static PyObject *const_str_digest_e0f2d70d53159315274056bdaf6b6d09;
static PyObject *const_tuple_str_plain_Metadata_str_plain_stdmeta_tuple;
extern PyObject *const_str_plain__exceptions;
static PyObject *const_str_plain_ISBNToolsHTTPError;
extern PyObject *const_str_plain_stdmeta;
extern PyObject *const_str_plain_NoAPIKeyError;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple = PyTuple_New( 10 );
    PyTuple_SET_ITEM( const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, 0, const_str_plain_DataNotFoundAtServiceError ); Py_INCREF( const_str_plain_DataNotFoundAtServiceError );
    PyTuple_SET_ITEM( const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, 1, const_str_plain_DataWrongShapeError ); Py_INCREF( const_str_plain_DataWrongShapeError );
    PyTuple_SET_ITEM( const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, 2, const_str_plain_ISBNLibDevException ); Py_INCREF( const_str_plain_ISBNLibDevException );
    PyTuple_SET_ITEM( const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, 3, const_str_plain_ISBNLibHTTPError ); Py_INCREF( const_str_plain_ISBNLibHTTPError );
    PyTuple_SET_ITEM( const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, 4, const_str_plain_ISBNLibURLError ); Py_INCREF( const_str_plain_ISBNLibURLError );
    PyTuple_SET_ITEM( const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, 5, const_str_plain_NoAPIKeyError ); Py_INCREF( const_str_plain_NoAPIKeyError );
    PyTuple_SET_ITEM( const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, 6, const_str_plain_NoDataForSelectorError ); Py_INCREF( const_str_plain_NoDataForSelectorError );
    PyTuple_SET_ITEM( const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, 7, const_str_plain_NotValidMetadataError ); Py_INCREF( const_str_plain_NotValidMetadataError );
    PyTuple_SET_ITEM( const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, 8, const_str_plain_RecordMappingError ); Py_INCREF( const_str_plain_RecordMappingError );
    PyTuple_SET_ITEM( const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, 9, const_str_plain_ServiceIsDownError ); Py_INCREF( const_str_plain_ServiceIsDownError );
    const_str_plain_ISBNToolsURLError = UNSTREAM_STRING( &constant_bin[ 528054 ], 17, 1 );
    const_str_plain_ISBNToolsDevException = UNSTREAM_STRING( &constant_bin[ 528071 ], 21, 1 );
    const_tuple_str_plain_WEBService_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_WEBService_tuple, 0, const_str_plain_WEBService ); Py_INCREF( const_str_plain_WEBService );
    const_tuple_43825479620781d3a694764e6071a520_tuple = PyMarshal_ReadObjectFromString( (char *)&constant_bin[ 528092 ], 399 );
    const_tuple_str_plain_WEBQuery_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_WEBQuery_tuple, 0, const_str_plain_WEBQuery ); Py_INCREF( const_str_plain_WEBQuery );
    const_tuple_str_plain_bouth23_str_plain_helpers_str_plain_vias_tuple = PyTuple_New( 3 );
    PyTuple_SET_ITEM( const_tuple_str_plain_bouth23_str_plain_helpers_str_plain_vias_tuple, 0, const_str_plain_bouth23 ); Py_INCREF( const_str_plain_bouth23 );
    PyTuple_SET_ITEM( const_tuple_str_plain_bouth23_str_plain_helpers_str_plain_vias_tuple, 1, const_str_plain_helpers ); Py_INCREF( const_str_plain_helpers );
    PyTuple_SET_ITEM( const_tuple_str_plain_bouth23_str_plain_helpers_str_plain_vias_tuple, 2, const_str_plain_vias ); Py_INCREF( const_str_plain_vias );
    const_str_digest_4214ea3c004a2b4b1e63a9fb3e2ea544 = UNSTREAM_STRING( &constant_bin[ 528491 ], 23, 0 );
    const_str_digest_e0f2d70d53159315274056bdaf6b6d09 = UNSTREAM_STRING( &constant_bin[ 528514 ], 11, 0 );
    const_tuple_str_plain_Metadata_str_plain_stdmeta_tuple = PyTuple_New( 2 );
    PyTuple_SET_ITEM( const_tuple_str_plain_Metadata_str_plain_stdmeta_tuple, 0, const_str_plain_Metadata ); Py_INCREF( const_str_plain_Metadata );
    PyTuple_SET_ITEM( const_tuple_str_plain_Metadata_str_plain_stdmeta_tuple, 1, const_str_plain_stdmeta ); Py_INCREF( const_str_plain_stdmeta );
    const_str_plain_ISBNToolsHTTPError = UNSTREAM_STRING( &constant_bin[ 528152 ], 18, 1 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_isbnlib$dev( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_dd57f9fcab0d6f5b90cf39cce605a556;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_4214ea3c004a2b4b1e63a9fb3e2ea544 );
    codeobj_dd57f9fcab0d6f5b90cf39cce605a556 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_dev, 1, const_tuple_empty, 0, CO_NOFREE );
}

// The module function declarations.


// The module function definitions.



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_isbnlib$dev =
{
    PyModuleDef_HEAD_INIT,
    "isbnlib.dev",   /* m_name */
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

MOD_INIT_DECL( isbnlib$dev )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_isbnlib$dev );
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

    // puts( "in initisbnlib$dev" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_isbnlib$dev = Py_InitModule4(
        "isbnlib.dev",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_isbnlib$dev = PyModule_Create( &mdef_isbnlib$dev );
#endif

    moduledict_isbnlib$dev = (PyDictObject *)((PyModuleObject *)module_isbnlib$dev)->md_dict;

    CHECK_OBJECT( module_isbnlib$dev );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_digest_e0f2d70d53159315274056bdaf6b6d09, module_isbnlib$dev );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_isbnlib$dev );

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
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *tmp_args_element_name_1;
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
    PyObject *tmp_called_name_1;
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
    PyObject *tmp_list_element_1;
    PyObject *tmp_source_name_1;
    PyFrameObject *frame_module;


    // Module code.
    tmp_assign_source_1 = Py_None;
    UPDATE_STRING_DICT0( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    // Frame without reuse.
    frame_module = MAKE_MODULE_FRAME( codeobj_dd57f9fcab0d6f5b90cf39cce605a556, module_isbnlib$dev );

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
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain___path__, tmp_assign_source_3 );
    tmp_import_globals_1 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 2;
    tmp_import_name_from_1 = IMPORT_MODULE( const_str_empty, tmp_import_globals_1, tmp_import_globals_1, const_tuple_str_plain_bouth23_str_plain_helpers_str_plain_vias_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 2;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_4 = IMPORT_NAME( tmp_import_name_from_1, const_str_plain_bouth23 );
    Py_DECREF( tmp_import_name_from_1 );
    if ( tmp_assign_source_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 2;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_bouth23, tmp_assign_source_4 );
    tmp_import_globals_2 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 2;
    tmp_import_name_from_2 = IMPORT_MODULE( const_str_empty, tmp_import_globals_2, tmp_import_globals_2, const_tuple_str_plain_bouth23_str_plain_helpers_str_plain_vias_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 2;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_5 = IMPORT_NAME( tmp_import_name_from_2, const_str_plain_helpers );
    Py_DECREF( tmp_import_name_from_2 );
    if ( tmp_assign_source_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 2;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_helpers, tmp_assign_source_5 );
    tmp_import_globals_3 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 2;
    tmp_import_name_from_3 = IMPORT_MODULE( const_str_empty, tmp_import_globals_3, tmp_import_globals_3, const_tuple_str_plain_bouth23_str_plain_helpers_str_plain_vias_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 2;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_6 = IMPORT_NAME( tmp_import_name_from_3, const_str_plain_vias );
    Py_DECREF( tmp_import_name_from_3 );
    if ( tmp_assign_source_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 2;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_vias, tmp_assign_source_6 );
    tmp_import_globals_4 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 3;
    tmp_import_name_from_4 = IMPORT_MODULE( const_str_plain__data, tmp_import_globals_4, tmp_import_globals_4, const_tuple_str_plain_Metadata_str_plain_stdmeta_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 3;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_7 = IMPORT_NAME( tmp_import_name_from_4, const_str_plain_Metadata );
    Py_DECREF( tmp_import_name_from_4 );
    if ( tmp_assign_source_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 3;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_Metadata, tmp_assign_source_7 );
    tmp_import_globals_5 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 3;
    tmp_import_name_from_5 = IMPORT_MODULE( const_str_plain__data, tmp_import_globals_5, tmp_import_globals_5, const_tuple_str_plain_Metadata_str_plain_stdmeta_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 3;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_8 = IMPORT_NAME( tmp_import_name_from_5, const_str_plain_stdmeta );
    Py_DECREF( tmp_import_name_from_5 );
    if ( tmp_assign_source_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 3;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_stdmeta, tmp_assign_source_8 );
    tmp_import_globals_6 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 4;
    tmp_import_name_from_6 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_6, tmp_import_globals_6, const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_9 = IMPORT_NAME( tmp_import_name_from_6, const_str_plain_DataNotFoundAtServiceError );
    Py_DECREF( tmp_import_name_from_6 );
    if ( tmp_assign_source_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_DataNotFoundAtServiceError, tmp_assign_source_9 );
    tmp_import_globals_7 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 4;
    tmp_import_name_from_7 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_7, tmp_import_globals_7, const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_10 = IMPORT_NAME( tmp_import_name_from_7, const_str_plain_DataWrongShapeError );
    Py_DECREF( tmp_import_name_from_7 );
    if ( tmp_assign_source_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_DataWrongShapeError, tmp_assign_source_10 );
    tmp_import_globals_8 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 4;
    tmp_import_name_from_8 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_8, tmp_import_globals_8, const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_11 = IMPORT_NAME( tmp_import_name_from_8, const_str_plain_ISBNLibDevException );
    Py_DECREF( tmp_import_name_from_8 );
    if ( tmp_assign_source_11 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_ISBNLibDevException, tmp_assign_source_11 );
    tmp_import_globals_9 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 4;
    tmp_import_name_from_9 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_9, tmp_import_globals_9, const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_12 = IMPORT_NAME( tmp_import_name_from_9, const_str_plain_ISBNLibHTTPError );
    Py_DECREF( tmp_import_name_from_9 );
    if ( tmp_assign_source_12 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_ISBNLibHTTPError, tmp_assign_source_12 );
    tmp_import_globals_10 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 4;
    tmp_import_name_from_10 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_10, tmp_import_globals_10, const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_13 = IMPORT_NAME( tmp_import_name_from_10, const_str_plain_ISBNLibURLError );
    Py_DECREF( tmp_import_name_from_10 );
    if ( tmp_assign_source_13 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_ISBNLibURLError, tmp_assign_source_13 );
    tmp_import_globals_11 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 4;
    tmp_import_name_from_11 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_11, tmp_import_globals_11, const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_11 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_14 = IMPORT_NAME( tmp_import_name_from_11, const_str_plain_NoAPIKeyError );
    Py_DECREF( tmp_import_name_from_11 );
    if ( tmp_assign_source_14 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_NoAPIKeyError, tmp_assign_source_14 );
    tmp_import_globals_12 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 4;
    tmp_import_name_from_12 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_12, tmp_import_globals_12, const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_12 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_15 = IMPORT_NAME( tmp_import_name_from_12, const_str_plain_NoDataForSelectorError );
    Py_DECREF( tmp_import_name_from_12 );
    if ( tmp_assign_source_15 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_NoDataForSelectorError, tmp_assign_source_15 );
    tmp_import_globals_13 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 4;
    tmp_import_name_from_13 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_13, tmp_import_globals_13, const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_13 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_16 = IMPORT_NAME( tmp_import_name_from_13, const_str_plain_NotValidMetadataError );
    Py_DECREF( tmp_import_name_from_13 );
    if ( tmp_assign_source_16 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_NotValidMetadataError, tmp_assign_source_16 );
    tmp_import_globals_14 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 4;
    tmp_import_name_from_14 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_14, tmp_import_globals_14, const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_14 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_17 = IMPORT_NAME( tmp_import_name_from_14, const_str_plain_RecordMappingError );
    Py_DECREF( tmp_import_name_from_14 );
    if ( tmp_assign_source_17 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_RecordMappingError, tmp_assign_source_17 );
    tmp_import_globals_15 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 4;
    tmp_import_name_from_15 = IMPORT_MODULE( const_str_plain__exceptions, tmp_import_globals_15, tmp_import_globals_15, const_tuple_9b219dcc26176afa4cb7ab9e98ff56bd_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_15 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_18 = IMPORT_NAME( tmp_import_name_from_15, const_str_plain_ServiceIsDownError );
    Py_DECREF( tmp_import_name_from_15 );
    if ( tmp_assign_source_18 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_ServiceIsDownError, tmp_assign_source_18 );
    tmp_import_globals_16 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 8;
    tmp_import_name_from_16 = IMPORT_MODULE( const_str_plain_webquery, tmp_import_globals_16, tmp_import_globals_16, const_tuple_str_plain_WEBQuery_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_16 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 8;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_19 = IMPORT_NAME( tmp_import_name_from_16, const_str_plain_WEBQuery );
    Py_DECREF( tmp_import_name_from_16 );
    if ( tmp_assign_source_19 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 8;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_WEBQuery, tmp_assign_source_19 );
    tmp_import_globals_17 = ((PyModuleObject *)module_isbnlib$dev)->md_dict;
    frame_module->f_lineno = 9;
    tmp_import_name_from_17 = IMPORT_MODULE( const_str_plain_webservice, tmp_import_globals_17, tmp_import_globals_17, const_tuple_str_plain_WEBService_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_17 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 9;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_20 = IMPORT_NAME( tmp_import_name_from_17, const_str_plain_WEBService );
    Py_DECREF( tmp_import_name_from_17 );
    if ( tmp_assign_source_20 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 9;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_WEBService, tmp_assign_source_20 );
    tmp_assign_source_21 = GET_STRING_DICT_VALUE( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_ISBNLibDevException );

    if (unlikely( tmp_assign_source_21 == NULL ))
    {
        tmp_assign_source_21 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_ISBNLibDevException );
    }

    if ( tmp_assign_source_21 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "ISBNLibDevException" );
        exception_tb = NULL;

        exception_lineno = 12;
        goto frame_exception_exit_1;
    }

    UPDATE_STRING_DICT0( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_ISBNToolsDevException, tmp_assign_source_21 );
    tmp_assign_source_22 = GET_STRING_DICT_VALUE( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_ISBNLibHTTPError );

    if (unlikely( tmp_assign_source_22 == NULL ))
    {
        tmp_assign_source_22 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_ISBNLibHTTPError );
    }

    if ( tmp_assign_source_22 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "ISBNLibHTTPError" );
        exception_tb = NULL;

        exception_lineno = 13;
        goto frame_exception_exit_1;
    }

    UPDATE_STRING_DICT0( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_ISBNToolsHTTPError, tmp_assign_source_22 );
    tmp_assign_source_23 = GET_STRING_DICT_VALUE( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_ISBNLibURLError );

    if (unlikely( tmp_assign_source_23 == NULL ))
    {
        tmp_assign_source_23 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_ISBNLibURLError );
    }

    if ( tmp_assign_source_23 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "ISBNLibURLError" );
        exception_tb = NULL;

        exception_lineno = 14;
        goto frame_exception_exit_1;
    }

    UPDATE_STRING_DICT0( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain_ISBNToolsURLError, tmp_assign_source_23 );

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION( frame_module );
#endif
    popFrameStack();

    assertFrameObject( frame_module );
    Py_DECREF( frame_module );

    goto frame_no_exception_1;
    frame_exception_exit_1:;
#if 0
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
    tmp_assign_source_24 = const_tuple_43825479620781d3a694764e6071a520_tuple;
    UPDATE_STRING_DICT0( moduledict_isbnlib$dev, (Nuitka_StringObject *)const_str_plain___all__, tmp_assign_source_24 );

    return MOD_RETURN_VALUE( module_isbnlib$dev );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
