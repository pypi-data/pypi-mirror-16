/* Generated code for Python source for module 'isbnlib.dev.helpers'
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

/* The _module_isbnlib$dev$helpers is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_isbnlib$dev$helpers;
PyDictObject *moduledict_isbnlib$dev$helpers;

/* The module constants used, if any. */
extern PyObject *const_str_plain_ShelveCache;
extern PyObject *const_str_plain_cwdfiles;
extern PyObject *const_str_plain__fmt;
static PyObject *const_str_digest_a04280aa4373856c6f7034f11cf85039;
extern PyObject *const_str_plain__helpers;
extern PyObject *const_str_plain__fmtbib;
extern PyObject *const_str_plain__fmts;
extern PyObject *const_str_plain_unicode_to_utf8tex;
static PyObject *const_str_digest_6bc8f21944525d31f2f284d9c304a331;
static PyObject *const_tuple_str_plain_ShelveCache_tuple;
extern PyObject *const_str_plain_normalize_space;
extern PyObject *const_tuple_str_plain_IMCache_tuple;
extern PyObject *const_str_plain___doc__;
static PyObject *const_str_plain_fmtbib;
extern PyObject *const_str_plain_IMCache;
extern PyObject *const_str_plain_parse_placeholders;
extern PyObject *const_str_plain_File;
extern PyObject *const_str_plain__shelvecache;
static PyObject *const_tuple_str_plain_File_str_plain_cwdfiles_tuple;
static PyObject *const_str_digest_bbbfe708029c3d49e071376fb0e1e69c;
static PyObject *const_str_plain_fmts;
extern PyObject *const_str_plain___file__;
extern PyObject *const_str_plain_last_first;
extern PyObject *const_str_plain_helpers;
static PyObject *const_str_plain_to_utf8tex;
extern PyObject *const_int_pos_2;
extern PyObject *const_str_plain__imcache;
extern PyObject *const_int_pos_1;
extern PyObject *const_str_plain_cutoff_tokens;
extern PyObject *const_tuple_empty;
extern PyObject *const_str_plain___all__;
extern PyObject *const_str_plain__files;
extern PyObject *const_str_plain_fake_isbn;
static PyObject *const_list_905a6f64020d3e808189fac5f460f115_list;
extern PyObject *const_str_plain_in_virtual;
static PyObject *const_tuple_str_plain_unicode_to_utf8tex_tuple;
static PyObject *const_tuple_str_plain__fmtbib_str_plain__fmts_tuple;
static PyObject *const_tuple_b5001b926881eaf10b4aa334560c946c_tuple;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_digest_a04280aa4373856c6f7034f11cf85039 = UNSTREAM_STRING( &constant_bin[ 534464 ], 24, 0 );
    const_str_digest_6bc8f21944525d31f2f284d9c304a331 = UNSTREAM_STRING( &constant_bin[ 534488 ], 22, 0 );
    const_tuple_str_plain_ShelveCache_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_ShelveCache_tuple, 0, const_str_plain_ShelveCache ); Py_INCREF( const_str_plain_ShelveCache );
    const_str_plain_fmtbib = UNSTREAM_STRING( &constant_bin[ 534510 ], 6, 1 );
    const_tuple_str_plain_File_str_plain_cwdfiles_tuple = PyTuple_New( 2 );
    PyTuple_SET_ITEM( const_tuple_str_plain_File_str_plain_cwdfiles_tuple, 0, const_str_plain_File ); Py_INCREF( const_str_plain_File );
    PyTuple_SET_ITEM( const_tuple_str_plain_File_str_plain_cwdfiles_tuple, 1, const_str_plain_cwdfiles ); Py_INCREF( const_str_plain_cwdfiles );
    const_str_digest_bbbfe708029c3d49e071376fb0e1e69c = UNSTREAM_STRING( &constant_bin[ 534516 ], 19, 0 );
    const_str_plain_fmts = UNSTREAM_STRING( &constant_bin[ 534535 ], 4, 1 );
    const_str_plain_to_utf8tex = UNSTREAM_STRING( &constant_bin[ 534539 ], 10, 1 );
    const_list_905a6f64020d3e808189fac5f460f115_list = PyList_New( 13 );
    PyList_SET_ITEM( const_list_905a6f64020d3e808189fac5f460f115_list, 0, const_str_plain_File ); Py_INCREF( const_str_plain_File );
    PyList_SET_ITEM( const_list_905a6f64020d3e808189fac5f460f115_list, 1, const_str_plain_IMCache ); Py_INCREF( const_str_plain_IMCache );
    PyList_SET_ITEM( const_list_905a6f64020d3e808189fac5f460f115_list, 2, const_str_plain_ShelveCache ); Py_INCREF( const_str_plain_ShelveCache );
    PyList_SET_ITEM( const_list_905a6f64020d3e808189fac5f460f115_list, 3, const_str_plain_cutoff_tokens ); Py_INCREF( const_str_plain_cutoff_tokens );
    PyList_SET_ITEM( const_list_905a6f64020d3e808189fac5f460f115_list, 4, const_str_plain_cwdfiles ); Py_INCREF( const_str_plain_cwdfiles );
    PyList_SET_ITEM( const_list_905a6f64020d3e808189fac5f460f115_list, 5, const_str_plain_fmtbib ); Py_INCREF( const_str_plain_fmtbib );
    PyList_SET_ITEM( const_list_905a6f64020d3e808189fac5f460f115_list, 6, const_str_plain_fmts ); Py_INCREF( const_str_plain_fmts );
    PyList_SET_ITEM( const_list_905a6f64020d3e808189fac5f460f115_list, 7, const_str_plain_in_virtual ); Py_INCREF( const_str_plain_in_virtual );
    PyList_SET_ITEM( const_list_905a6f64020d3e808189fac5f460f115_list, 8, const_str_plain_last_first ); Py_INCREF( const_str_plain_last_first );
    PyList_SET_ITEM( const_list_905a6f64020d3e808189fac5f460f115_list, 9, const_str_plain_normalize_space ); Py_INCREF( const_str_plain_normalize_space );
    PyList_SET_ITEM( const_list_905a6f64020d3e808189fac5f460f115_list, 10, const_str_plain_parse_placeholders ); Py_INCREF( const_str_plain_parse_placeholders );
    PyList_SET_ITEM( const_list_905a6f64020d3e808189fac5f460f115_list, 11, const_str_plain_to_utf8tex ); Py_INCREF( const_str_plain_to_utf8tex );
    PyList_SET_ITEM( const_list_905a6f64020d3e808189fac5f460f115_list, 12, const_str_plain_fake_isbn ); Py_INCREF( const_str_plain_fake_isbn );
    const_tuple_str_plain_unicode_to_utf8tex_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_unicode_to_utf8tex_tuple, 0, const_str_plain_unicode_to_utf8tex ); Py_INCREF( const_str_plain_unicode_to_utf8tex );
    const_tuple_str_plain__fmtbib_str_plain__fmts_tuple = PyTuple_New( 2 );
    PyTuple_SET_ITEM( const_tuple_str_plain__fmtbib_str_plain__fmts_tuple, 0, const_str_plain__fmtbib ); Py_INCREF( const_str_plain__fmtbib );
    PyTuple_SET_ITEM( const_tuple_str_plain__fmtbib_str_plain__fmts_tuple, 1, const_str_plain__fmts ); Py_INCREF( const_str_plain__fmts );
    const_tuple_b5001b926881eaf10b4aa334560c946c_tuple = PyTuple_New( 6 );
    PyTuple_SET_ITEM( const_tuple_b5001b926881eaf10b4aa334560c946c_tuple, 0, const_str_plain_cutoff_tokens ); Py_INCREF( const_str_plain_cutoff_tokens );
    PyTuple_SET_ITEM( const_tuple_b5001b926881eaf10b4aa334560c946c_tuple, 1, const_str_plain_fake_isbn ); Py_INCREF( const_str_plain_fake_isbn );
    PyTuple_SET_ITEM( const_tuple_b5001b926881eaf10b4aa334560c946c_tuple, 2, const_str_plain_in_virtual ); Py_INCREF( const_str_plain_in_virtual );
    PyTuple_SET_ITEM( const_tuple_b5001b926881eaf10b4aa334560c946c_tuple, 3, const_str_plain_last_first ); Py_INCREF( const_str_plain_last_first );
    PyTuple_SET_ITEM( const_tuple_b5001b926881eaf10b4aa334560c946c_tuple, 4, const_str_plain_normalize_space ); Py_INCREF( const_str_plain_normalize_space );
    PyTuple_SET_ITEM( const_tuple_b5001b926881eaf10b4aa334560c946c_tuple, 5, const_str_plain_parse_placeholders ); Py_INCREF( const_str_plain_parse_placeholders );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_isbnlib$dev$helpers( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_081fdd44c3144c8f1da1d8bdf0016ebd;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_6bc8f21944525d31f2f284d9c304a331 );
    codeobj_081fdd44c3144c8f1da1d8bdf0016ebd = MAKE_CODEOBJ( module_filename_obj, const_str_plain_helpers, 1, const_tuple_empty, 0, CO_NOFREE );
}

// The module function declarations.


// The module function definitions.



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_isbnlib$dev$helpers =
{
    PyModuleDef_HEAD_INIT,
    "isbnlib.dev.helpers",   /* m_name */
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

MOD_INIT_DECL( isbnlib$dev$helpers )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_isbnlib$dev$helpers );
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

    // puts( "in initisbnlib$dev$helpers" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_isbnlib$dev$helpers = Py_InitModule4(
        "isbnlib.dev.helpers",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_isbnlib$dev$helpers = PyModule_Create( &mdef_isbnlib$dev$helpers );
#endif

    moduledict_isbnlib$dev$helpers = (PyDictObject *)((PyModuleObject *)module_isbnlib$dev$helpers)->md_dict;

    CHECK_OBJECT( module_isbnlib$dev$helpers );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_digest_bbbfe708029c3d49e071376fb0e1e69c, module_isbnlib$dev$helpers );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_isbnlib$dev$helpers );

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
    PyFrameObject *frame_module;


    // Module code.
    tmp_assign_source_1 = const_str_digest_a04280aa4373856c6f7034f11cf85039;
    UPDATE_STRING_DICT0( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    // Frame without reuse.
    frame_module = MAKE_MODULE_FRAME( codeobj_081fdd44c3144c8f1da1d8bdf0016ebd, module_isbnlib$dev$helpers );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_module );
    assert( Py_REFCNT( frame_module ) == 1 );

#if PYTHON_VERSION >= 340
    frame_module->f_executing += 1;
#endif

    // Framed code:
    tmp_import_globals_1 = ((PyModuleObject *)module_isbnlib$dev$helpers)->md_dict;
    frame_module->f_lineno = 6;
    tmp_import_name_from_1 = IMPORT_MODULE( const_str_plain__imcache, tmp_import_globals_1, tmp_import_globals_1, const_tuple_str_plain_IMCache_tuple, const_int_pos_2 );
    if ( tmp_import_name_from_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 6;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_3 = IMPORT_NAME( tmp_import_name_from_1, const_str_plain_IMCache );
    Py_DECREF( tmp_import_name_from_1 );
    if ( tmp_assign_source_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 6;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain_IMCache, tmp_assign_source_3 );
    tmp_import_globals_2 = ((PyModuleObject *)module_isbnlib$dev$helpers)->md_dict;
    frame_module->f_lineno = 7;
    tmp_import_name_from_2 = IMPORT_MODULE( const_str_plain__files, tmp_import_globals_2, tmp_import_globals_2, const_tuple_str_plain_File_str_plain_cwdfiles_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 7;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_4 = IMPORT_NAME( tmp_import_name_from_2, const_str_plain_File );
    Py_DECREF( tmp_import_name_from_2 );
    if ( tmp_assign_source_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 7;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain_File, tmp_assign_source_4 );
    tmp_import_globals_3 = ((PyModuleObject *)module_isbnlib$dev$helpers)->md_dict;
    frame_module->f_lineno = 7;
    tmp_import_name_from_3 = IMPORT_MODULE( const_str_plain__files, tmp_import_globals_3, tmp_import_globals_3, const_tuple_str_plain_File_str_plain_cwdfiles_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 7;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_5 = IMPORT_NAME( tmp_import_name_from_3, const_str_plain_cwdfiles );
    Py_DECREF( tmp_import_name_from_3 );
    if ( tmp_assign_source_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 7;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain_cwdfiles, tmp_assign_source_5 );
    tmp_import_globals_4 = ((PyModuleObject *)module_isbnlib$dev$helpers)->md_dict;
    frame_module->f_lineno = 8;
    tmp_import_name_from_4 = IMPORT_MODULE( const_str_plain__fmt, tmp_import_globals_4, tmp_import_globals_4, const_tuple_str_plain__fmtbib_str_plain__fmts_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 8;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_6 = IMPORT_NAME( tmp_import_name_from_4, const_str_plain__fmtbib );
    Py_DECREF( tmp_import_name_from_4 );
    if ( tmp_assign_source_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 8;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain__fmtbib, tmp_assign_source_6 );
    tmp_import_globals_5 = ((PyModuleObject *)module_isbnlib$dev$helpers)->md_dict;
    frame_module->f_lineno = 8;
    tmp_import_name_from_5 = IMPORT_MODULE( const_str_plain__fmt, tmp_import_globals_5, tmp_import_globals_5, const_tuple_str_plain__fmtbib_str_plain__fmts_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 8;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_7 = IMPORT_NAME( tmp_import_name_from_5, const_str_plain__fmts );
    Py_DECREF( tmp_import_name_from_5 );
    if ( tmp_assign_source_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 8;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain__fmts, tmp_assign_source_7 );
    tmp_import_globals_6 = ((PyModuleObject *)module_isbnlib$dev$helpers)->md_dict;
    frame_module->f_lineno = 9;
    tmp_import_name_from_6 = IMPORT_MODULE( const_str_plain__helpers, tmp_import_globals_6, tmp_import_globals_6, const_tuple_str_plain_unicode_to_utf8tex_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 9;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_8 = IMPORT_NAME( tmp_import_name_from_6, const_str_plain_unicode_to_utf8tex );
    Py_DECREF( tmp_import_name_from_6 );
    if ( tmp_assign_source_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 9;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain_to_utf8tex, tmp_assign_source_8 );
    tmp_import_globals_7 = ((PyModuleObject *)module_isbnlib$dev$helpers)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_7 = IMPORT_MODULE( const_str_plain__helpers, tmp_import_globals_7, tmp_import_globals_7, const_tuple_b5001b926881eaf10b4aa334560c946c_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_9 = IMPORT_NAME( tmp_import_name_from_7, const_str_plain_cutoff_tokens );
    Py_DECREF( tmp_import_name_from_7 );
    if ( tmp_assign_source_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain_cutoff_tokens, tmp_assign_source_9 );
    tmp_import_globals_8 = ((PyModuleObject *)module_isbnlib$dev$helpers)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_8 = IMPORT_MODULE( const_str_plain__helpers, tmp_import_globals_8, tmp_import_globals_8, const_tuple_b5001b926881eaf10b4aa334560c946c_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_10 = IMPORT_NAME( tmp_import_name_from_8, const_str_plain_fake_isbn );
    Py_DECREF( tmp_import_name_from_8 );
    if ( tmp_assign_source_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain_fake_isbn, tmp_assign_source_10 );
    tmp_import_globals_9 = ((PyModuleObject *)module_isbnlib$dev$helpers)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_9 = IMPORT_MODULE( const_str_plain__helpers, tmp_import_globals_9, tmp_import_globals_9, const_tuple_b5001b926881eaf10b4aa334560c946c_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_11 = IMPORT_NAME( tmp_import_name_from_9, const_str_plain_in_virtual );
    Py_DECREF( tmp_import_name_from_9 );
    if ( tmp_assign_source_11 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain_in_virtual, tmp_assign_source_11 );
    tmp_import_globals_10 = ((PyModuleObject *)module_isbnlib$dev$helpers)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_10 = IMPORT_MODULE( const_str_plain__helpers, tmp_import_globals_10, tmp_import_globals_10, const_tuple_b5001b926881eaf10b4aa334560c946c_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_12 = IMPORT_NAME( tmp_import_name_from_10, const_str_plain_last_first );
    Py_DECREF( tmp_import_name_from_10 );
    if ( tmp_assign_source_12 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain_last_first, tmp_assign_source_12 );
    tmp_import_globals_11 = ((PyModuleObject *)module_isbnlib$dev$helpers)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_11 = IMPORT_MODULE( const_str_plain__helpers, tmp_import_globals_11, tmp_import_globals_11, const_tuple_b5001b926881eaf10b4aa334560c946c_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_11 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_13 = IMPORT_NAME( tmp_import_name_from_11, const_str_plain_normalize_space );
    Py_DECREF( tmp_import_name_from_11 );
    if ( tmp_assign_source_13 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain_normalize_space, tmp_assign_source_13 );
    tmp_import_globals_12 = ((PyModuleObject *)module_isbnlib$dev$helpers)->md_dict;
    frame_module->f_lineno = 10;
    tmp_import_name_from_12 = IMPORT_MODULE( const_str_plain__helpers, tmp_import_globals_12, tmp_import_globals_12, const_tuple_b5001b926881eaf10b4aa334560c946c_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_12 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_14 = IMPORT_NAME( tmp_import_name_from_12, const_str_plain_parse_placeholders );
    Py_DECREF( tmp_import_name_from_12 );
    if ( tmp_assign_source_14 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 10;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain_parse_placeholders, tmp_assign_source_14 );
    tmp_import_globals_13 = ((PyModuleObject *)module_isbnlib$dev$helpers)->md_dict;
    frame_module->f_lineno = 12;
    tmp_import_name_from_13 = IMPORT_MODULE( const_str_plain__shelvecache, tmp_import_globals_13, tmp_import_globals_13, const_tuple_str_plain_ShelveCache_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_13 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 12;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_15 = IMPORT_NAME( tmp_import_name_from_13, const_str_plain_ShelveCache );
    Py_DECREF( tmp_import_name_from_13 );
    if ( tmp_assign_source_15 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 12;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain_ShelveCache, tmp_assign_source_15 );
    tmp_assign_source_16 = GET_STRING_DICT_VALUE( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain__fmtbib );

    if (unlikely( tmp_assign_source_16 == NULL ))
    {
        tmp_assign_source_16 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__fmtbib );
    }

    if ( tmp_assign_source_16 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "_fmtbib" );
        exception_tb = NULL;

        exception_lineno = 16;
        goto frame_exception_exit_1;
    }

    UPDATE_STRING_DICT0( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain_fmtbib, tmp_assign_source_16 );
    tmp_assign_source_17 = GET_STRING_DICT_VALUE( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain__fmts );

    if (unlikely( tmp_assign_source_17 == NULL ))
    {
        tmp_assign_source_17 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__fmts );
    }

    if ( tmp_assign_source_17 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "_fmts" );
        exception_tb = NULL;

        exception_lineno = 17;
        goto frame_exception_exit_1;
    }

    UPDATE_STRING_DICT0( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain_fmts, tmp_assign_source_17 );

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
    tmp_assign_source_18 = LIST_COPY( const_list_905a6f64020d3e808189fac5f460f115_list );
    UPDATE_STRING_DICT1( moduledict_isbnlib$dev$helpers, (Nuitka_StringObject *)const_str_plain___all__, tmp_assign_source_18 );

    return MOD_RETURN_VALUE( module_isbnlib$dev$helpers );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
