/* Generated code for Python source for module 'unittest'
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

/* The _module_unittest is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_unittest;
PyDictObject *moduledict_unittest;

/* The module constants used, if any. */
static PyObject *const_list_fd16d68eab66967073de98a58a3f21a0_list;
extern PyObject *const_str_plain_expectedFailure;
extern PyObject *const_str_plain_TestCase;
extern PyObject *const_str_plain_runner;
extern PyObject *const_int_pos_1;
static PyObject *const_tuple_str_plain_TestProgram_str_plain_main_tuple;
extern PyObject *const_str_plain_registerResult;
extern PyObject *const_str_plain_SkipTest;
extern PyObject *const_str_plain_suite;
extern PyObject *const_str_plain_installHandler;
extern PyObject *const_str_plain_TestResult;
static PyObject *const_str_digest_82e3f31a21f429b52167a610e614494b;
extern PyObject *const_str_plain_findTestCases;
extern PyObject *const_str_plain_unittest;
extern PyObject *const_str_plain_TextTestResult;
extern PyObject *const_str_plain_TestSuite;
static PyObject *const_tuple_str_plain_TextTestRunner_str_plain_TextTestResult_tuple;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain_skip;
extern PyObject *const_str_plain___all__;
extern PyObject *const_str_plain_skipUnless;
static PyObject *const_str_plain__TextTestResult;
static PyObject *const_str_digest_c5e495d14186af80bc8062138eaa1955;
extern PyObject *const_str_plain_getTestCaseNames;
extern PyObject *const_str_plain___file__;
static PyObject *const_tuple_61646aa3e725fac25d25edd5ff90e344_tuple;
extern PyObject *const_str_plain_extend;
extern PyObject *const_str_plain_removeResult;
extern PyObject *const_str_plain_loader;
extern PyObject *const_str_plain_result;
extern PyObject *const_str_plain_main;
extern PyObject *const_str_plain_case;
extern PyObject *const_str_plain___unittest;
extern PyObject *const_str_plain_removeHandler;
extern PyObject *const_tuple_empty;
extern PyObject *const_str_plain___path__;
extern PyObject *const_str_plain_signals;
extern PyObject *const_str_plain_defaultTestLoader;
extern PyObject *const_str_plain_TestLoader;
extern PyObject *const_str_plain_BaseTestSuite;
extern PyObject *const_str_plain_dirname;
static PyObject *const_tuple_str_plain_BaseTestSuite_str_plain_TestSuite_tuple;
static PyObject *const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple;
static PyObject *const_tuple_fc8c7e19e3ce48ab8190e98be8ffe351_tuple;
static PyObject *const_tuple_str_plain_TestResult_tuple;
extern PyObject *const_str_plain_TextTestRunner;
static PyObject *const_list_cbfdf307027060106ba3821db33dfd66_list;
extern PyObject *const_str_plain_skipIf;
extern PyObject *const_str_plain_makeSuite;
extern PyObject *const_str_plain_TestProgram;
extern PyObject *const_str_plain_FunctionTestCase;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_list_fd16d68eab66967073de98a58a3f21a0_list = PyList_New( 18 );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 0, const_str_plain_TestResult ); Py_INCREF( const_str_plain_TestResult );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 1, const_str_plain_TestCase ); Py_INCREF( const_str_plain_TestCase );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 2, const_str_plain_TestSuite ); Py_INCREF( const_str_plain_TestSuite );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 3, const_str_plain_TextTestRunner ); Py_INCREF( const_str_plain_TextTestRunner );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 4, const_str_plain_TestLoader ); Py_INCREF( const_str_plain_TestLoader );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 5, const_str_plain_FunctionTestCase ); Py_INCREF( const_str_plain_FunctionTestCase );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 6, const_str_plain_main ); Py_INCREF( const_str_plain_main );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 7, const_str_plain_defaultTestLoader ); Py_INCREF( const_str_plain_defaultTestLoader );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 8, const_str_plain_SkipTest ); Py_INCREF( const_str_plain_SkipTest );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 9, const_str_plain_skip ); Py_INCREF( const_str_plain_skip );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 10, const_str_plain_skipIf ); Py_INCREF( const_str_plain_skipIf );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 11, const_str_plain_skipUnless ); Py_INCREF( const_str_plain_skipUnless );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 12, const_str_plain_expectedFailure ); Py_INCREF( const_str_plain_expectedFailure );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 13, const_str_plain_TextTestResult ); Py_INCREF( const_str_plain_TextTestResult );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 14, const_str_plain_installHandler ); Py_INCREF( const_str_plain_installHandler );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 15, const_str_plain_registerResult ); Py_INCREF( const_str_plain_registerResult );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 16, const_str_plain_removeResult ); Py_INCREF( const_str_plain_removeResult );
    PyList_SET_ITEM( const_list_fd16d68eab66967073de98a58a3f21a0_list, 17, const_str_plain_removeHandler ); Py_INCREF( const_str_plain_removeHandler );
    const_tuple_str_plain_TestProgram_str_plain_main_tuple = PyTuple_New( 2 );
    PyTuple_SET_ITEM( const_tuple_str_plain_TestProgram_str_plain_main_tuple, 0, const_str_plain_TestProgram ); Py_INCREF( const_str_plain_TestProgram );
    PyTuple_SET_ITEM( const_tuple_str_plain_TestProgram_str_plain_main_tuple, 1, const_str_plain_main ); Py_INCREF( const_str_plain_main );
    const_str_digest_82e3f31a21f429b52167a610e614494b = UNSTREAM_STRING( &constant_bin[ 963087 ], 1715, 0 );
    const_tuple_str_plain_TextTestRunner_str_plain_TextTestResult_tuple = PyTuple_New( 2 );
    PyTuple_SET_ITEM( const_tuple_str_plain_TextTestRunner_str_plain_TextTestResult_tuple, 0, const_str_plain_TextTestRunner ); Py_INCREF( const_str_plain_TextTestRunner );
    PyTuple_SET_ITEM( const_tuple_str_plain_TextTestRunner_str_plain_TextTestResult_tuple, 1, const_str_plain_TextTestResult ); Py_INCREF( const_str_plain_TextTestResult );
    const_str_plain__TextTestResult = UNSTREAM_STRING( &constant_bin[ 964802 ], 15, 1 );
    const_str_digest_c5e495d14186af80bc8062138eaa1955 = UNSTREAM_STRING( &constant_bin[ 964817 ], 20, 0 );
    const_tuple_61646aa3e725fac25d25edd5ff90e344_tuple = PyTuple_New( 5 );
    PyTuple_SET_ITEM( const_tuple_61646aa3e725fac25d25edd5ff90e344_tuple, 0, const_str_plain_TestLoader ); Py_INCREF( const_str_plain_TestLoader );
    PyTuple_SET_ITEM( const_tuple_61646aa3e725fac25d25edd5ff90e344_tuple, 1, const_str_plain_defaultTestLoader ); Py_INCREF( const_str_plain_defaultTestLoader );
    PyTuple_SET_ITEM( const_tuple_61646aa3e725fac25d25edd5ff90e344_tuple, 2, const_str_plain_makeSuite ); Py_INCREF( const_str_plain_makeSuite );
    PyTuple_SET_ITEM( const_tuple_61646aa3e725fac25d25edd5ff90e344_tuple, 3, const_str_plain_getTestCaseNames ); Py_INCREF( const_str_plain_getTestCaseNames );
    PyTuple_SET_ITEM( const_tuple_61646aa3e725fac25d25edd5ff90e344_tuple, 4, const_str_plain_findTestCases ); Py_INCREF( const_str_plain_findTestCases );
    const_tuple_str_plain_BaseTestSuite_str_plain_TestSuite_tuple = PyTuple_New( 2 );
    PyTuple_SET_ITEM( const_tuple_str_plain_BaseTestSuite_str_plain_TestSuite_tuple, 0, const_str_plain_BaseTestSuite ); Py_INCREF( const_str_plain_BaseTestSuite );
    PyTuple_SET_ITEM( const_tuple_str_plain_BaseTestSuite_str_plain_TestSuite_tuple, 1, const_str_plain_TestSuite ); Py_INCREF( const_str_plain_TestSuite );
    const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple = PyTuple_New( 7 );
    PyTuple_SET_ITEM( const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple, 0, const_str_plain_TestCase ); Py_INCREF( const_str_plain_TestCase );
    PyTuple_SET_ITEM( const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple, 1, const_str_plain_FunctionTestCase ); Py_INCREF( const_str_plain_FunctionTestCase );
    PyTuple_SET_ITEM( const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple, 2, const_str_plain_SkipTest ); Py_INCREF( const_str_plain_SkipTest );
    PyTuple_SET_ITEM( const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple, 3, const_str_plain_skip ); Py_INCREF( const_str_plain_skip );
    PyTuple_SET_ITEM( const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple, 4, const_str_plain_skipIf ); Py_INCREF( const_str_plain_skipIf );
    PyTuple_SET_ITEM( const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple, 5, const_str_plain_skipUnless ); Py_INCREF( const_str_plain_skipUnless );
    PyTuple_SET_ITEM( const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple, 6, const_str_plain_expectedFailure ); Py_INCREF( const_str_plain_expectedFailure );
    const_tuple_fc8c7e19e3ce48ab8190e98be8ffe351_tuple = PyTuple_New( 4 );
    PyTuple_SET_ITEM( const_tuple_fc8c7e19e3ce48ab8190e98be8ffe351_tuple, 0, const_str_plain_installHandler ); Py_INCREF( const_str_plain_installHandler );
    PyTuple_SET_ITEM( const_tuple_fc8c7e19e3ce48ab8190e98be8ffe351_tuple, 1, const_str_plain_registerResult ); Py_INCREF( const_str_plain_registerResult );
    PyTuple_SET_ITEM( const_tuple_fc8c7e19e3ce48ab8190e98be8ffe351_tuple, 2, const_str_plain_removeResult ); Py_INCREF( const_str_plain_removeResult );
    PyTuple_SET_ITEM( const_tuple_fc8c7e19e3ce48ab8190e98be8ffe351_tuple, 3, const_str_plain_removeHandler ); Py_INCREF( const_str_plain_removeHandler );
    const_tuple_str_plain_TestResult_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_TestResult_tuple, 0, const_str_plain_TestResult ); Py_INCREF( const_str_plain_TestResult );
    const_list_cbfdf307027060106ba3821db33dfd66_list = PyList_New( 3 );
    PyList_SET_ITEM( const_list_cbfdf307027060106ba3821db33dfd66_list, 0, const_str_plain_getTestCaseNames ); Py_INCREF( const_str_plain_getTestCaseNames );
    PyList_SET_ITEM( const_list_cbfdf307027060106ba3821db33dfd66_list, 1, const_str_plain_makeSuite ); Py_INCREF( const_str_plain_makeSuite );
    PyList_SET_ITEM( const_list_cbfdf307027060106ba3821db33dfd66_list, 2, const_str_plain_findTestCases ); Py_INCREF( const_str_plain_findTestCases );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_unittest( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_97e97a9c23cd757a6586dba1ba403793;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_c5e495d14186af80bc8062138eaa1955 );
    codeobj_97e97a9c23cd757a6586dba1ba403793 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_unittest, 1, const_tuple_empty, 0, CO_NOFREE );
}

// The module function declarations.


// The module function definitions.



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_unittest =
{
    PyModuleDef_HEAD_INIT,
    "unittest",   /* m_name */
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

MOD_INIT_DECL( unittest )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_unittest );
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

    // puts( "in initunittest" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_unittest = Py_InitModule4(
        "unittest",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_unittest = PyModule_Create( &mdef_unittest );
#endif

    moduledict_unittest = (PyDictObject *)((PyModuleObject *)module_unittest)->md_dict;

    CHECK_OBJECT( module_unittest );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_plain_unittest, module_unittest );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_unittest );

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
    PyObject *tmp_assign_source_25;
    PyObject *tmp_assign_source_26;
    PyObject *tmp_assign_source_27;
    PyObject *tmp_assign_source_28;
    PyObject *tmp_assign_source_29;
    PyObject *tmp_call_arg_element_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
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
    PyObject *tmp_list_element_1;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    PyFrameObject *frame_module;


    // Module code.
    tmp_assign_source_1 = const_str_digest_82e3f31a21f429b52167a610e614494b;
    UPDATE_STRING_DICT0( moduledict_unittest, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_unittest, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    // Frame without reuse.
    frame_module = MAKE_MODULE_FRAME( codeobj_97e97a9c23cd757a6586dba1ba403793, module_unittest );

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
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain___path__, tmp_assign_source_3 );
    tmp_assign_source_4 = LIST_COPY( const_list_fd16d68eab66967073de98a58a3f21a0_list );
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain___all__, tmp_assign_source_4 );
    tmp_source_name_2 = GET_STRING_DICT_VALUE( moduledict_unittest, (Nuitka_StringObject *)const_str_plain___all__ );

    if (unlikely( tmp_source_name_2 == NULL ))
    {
        tmp_source_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain___all__ );
    }

    if ( tmp_source_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "__all__" );
        exception_tb = NULL;

        exception_lineno = 54;
        goto frame_exception_exit_1;
    }

    tmp_called_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_extend );
    if ( tmp_called_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 54;
        goto frame_exception_exit_1;
    }
    tmp_call_arg_element_1 = LIST_COPY( const_list_cbfdf307027060106ba3821db33dfd66_list );
    frame_module->f_lineno = 54;
    {
        PyObject *call_args[] = { tmp_call_arg_element_1 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_2, call_args );
    }

    Py_DECREF( tmp_called_name_2 );
    Py_DECREF( tmp_call_arg_element_1 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 54;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_assign_source_5 = Py_True;
    UPDATE_STRING_DICT0( moduledict_unittest, (Nuitka_StringObject *)const_str_plain___unittest, tmp_assign_source_5 );
    tmp_import_globals_1 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 58;
    tmp_import_name_from_1 = IMPORT_MODULE( const_str_plain_result, tmp_import_globals_1, tmp_import_globals_1, const_tuple_str_plain_TestResult_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 58;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_6 = IMPORT_NAME( tmp_import_name_from_1, const_str_plain_TestResult );
    Py_DECREF( tmp_import_name_from_1 );
    if ( tmp_assign_source_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 58;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_TestResult, tmp_assign_source_6 );
    tmp_import_globals_2 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 59;
    tmp_import_name_from_2 = IMPORT_MODULE( const_str_plain_case, tmp_import_globals_2, tmp_import_globals_2, const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_7 = IMPORT_NAME( tmp_import_name_from_2, const_str_plain_TestCase );
    Py_DECREF( tmp_import_name_from_2 );
    if ( tmp_assign_source_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_TestCase, tmp_assign_source_7 );
    tmp_import_globals_3 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 59;
    tmp_import_name_from_3 = IMPORT_MODULE( const_str_plain_case, tmp_import_globals_3, tmp_import_globals_3, const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_8 = IMPORT_NAME( tmp_import_name_from_3, const_str_plain_FunctionTestCase );
    Py_DECREF( tmp_import_name_from_3 );
    if ( tmp_assign_source_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_FunctionTestCase, tmp_assign_source_8 );
    tmp_import_globals_4 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 59;
    tmp_import_name_from_4 = IMPORT_MODULE( const_str_plain_case, tmp_import_globals_4, tmp_import_globals_4, const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_9 = IMPORT_NAME( tmp_import_name_from_4, const_str_plain_SkipTest );
    Py_DECREF( tmp_import_name_from_4 );
    if ( tmp_assign_source_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_SkipTest, tmp_assign_source_9 );
    tmp_import_globals_5 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 59;
    tmp_import_name_from_5 = IMPORT_MODULE( const_str_plain_case, tmp_import_globals_5, tmp_import_globals_5, const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_10 = IMPORT_NAME( tmp_import_name_from_5, const_str_plain_skip );
    Py_DECREF( tmp_import_name_from_5 );
    if ( tmp_assign_source_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_skip, tmp_assign_source_10 );
    tmp_import_globals_6 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 59;
    tmp_import_name_from_6 = IMPORT_MODULE( const_str_plain_case, tmp_import_globals_6, tmp_import_globals_6, const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_11 = IMPORT_NAME( tmp_import_name_from_6, const_str_plain_skipIf );
    Py_DECREF( tmp_import_name_from_6 );
    if ( tmp_assign_source_11 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_skipIf, tmp_assign_source_11 );
    tmp_import_globals_7 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 59;
    tmp_import_name_from_7 = IMPORT_MODULE( const_str_plain_case, tmp_import_globals_7, tmp_import_globals_7, const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_12 = IMPORT_NAME( tmp_import_name_from_7, const_str_plain_skipUnless );
    Py_DECREF( tmp_import_name_from_7 );
    if ( tmp_assign_source_12 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_skipUnless, tmp_assign_source_12 );
    tmp_import_globals_8 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 59;
    tmp_import_name_from_8 = IMPORT_MODULE( const_str_plain_case, tmp_import_globals_8, tmp_import_globals_8, const_tuple_27d43546aec0a862badd0f98608dc9b7_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_13 = IMPORT_NAME( tmp_import_name_from_8, const_str_plain_expectedFailure );
    Py_DECREF( tmp_import_name_from_8 );
    if ( tmp_assign_source_13 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_expectedFailure, tmp_assign_source_13 );
    tmp_import_globals_9 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 61;
    tmp_import_name_from_9 = IMPORT_MODULE( const_str_plain_suite, tmp_import_globals_9, tmp_import_globals_9, const_tuple_str_plain_BaseTestSuite_str_plain_TestSuite_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 61;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_14 = IMPORT_NAME( tmp_import_name_from_9, const_str_plain_BaseTestSuite );
    Py_DECREF( tmp_import_name_from_9 );
    if ( tmp_assign_source_14 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 61;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_BaseTestSuite, tmp_assign_source_14 );
    tmp_import_globals_10 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 61;
    tmp_import_name_from_10 = IMPORT_MODULE( const_str_plain_suite, tmp_import_globals_10, tmp_import_globals_10, const_tuple_str_plain_BaseTestSuite_str_plain_TestSuite_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 61;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_15 = IMPORT_NAME( tmp_import_name_from_10, const_str_plain_TestSuite );
    Py_DECREF( tmp_import_name_from_10 );
    if ( tmp_assign_source_15 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 61;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_TestSuite, tmp_assign_source_15 );
    tmp_import_globals_11 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 62;
    tmp_import_name_from_11 = IMPORT_MODULE( const_str_plain_loader, tmp_import_globals_11, tmp_import_globals_11, const_tuple_61646aa3e725fac25d25edd5ff90e344_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_11 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 62;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_16 = IMPORT_NAME( tmp_import_name_from_11, const_str_plain_TestLoader );
    Py_DECREF( tmp_import_name_from_11 );
    if ( tmp_assign_source_16 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 62;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_TestLoader, tmp_assign_source_16 );
    tmp_import_globals_12 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 62;
    tmp_import_name_from_12 = IMPORT_MODULE( const_str_plain_loader, tmp_import_globals_12, tmp_import_globals_12, const_tuple_61646aa3e725fac25d25edd5ff90e344_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_12 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 62;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_17 = IMPORT_NAME( tmp_import_name_from_12, const_str_plain_defaultTestLoader );
    Py_DECREF( tmp_import_name_from_12 );
    if ( tmp_assign_source_17 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 62;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_defaultTestLoader, tmp_assign_source_17 );
    tmp_import_globals_13 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 62;
    tmp_import_name_from_13 = IMPORT_MODULE( const_str_plain_loader, tmp_import_globals_13, tmp_import_globals_13, const_tuple_61646aa3e725fac25d25edd5ff90e344_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_13 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 62;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_18 = IMPORT_NAME( tmp_import_name_from_13, const_str_plain_makeSuite );
    Py_DECREF( tmp_import_name_from_13 );
    if ( tmp_assign_source_18 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 62;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_makeSuite, tmp_assign_source_18 );
    tmp_import_globals_14 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 62;
    tmp_import_name_from_14 = IMPORT_MODULE( const_str_plain_loader, tmp_import_globals_14, tmp_import_globals_14, const_tuple_61646aa3e725fac25d25edd5ff90e344_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_14 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 62;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_19 = IMPORT_NAME( tmp_import_name_from_14, const_str_plain_getTestCaseNames );
    Py_DECREF( tmp_import_name_from_14 );
    if ( tmp_assign_source_19 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 62;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_getTestCaseNames, tmp_assign_source_19 );
    tmp_import_globals_15 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 62;
    tmp_import_name_from_15 = IMPORT_MODULE( const_str_plain_loader, tmp_import_globals_15, tmp_import_globals_15, const_tuple_61646aa3e725fac25d25edd5ff90e344_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_15 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 62;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_20 = IMPORT_NAME( tmp_import_name_from_15, const_str_plain_findTestCases );
    Py_DECREF( tmp_import_name_from_15 );
    if ( tmp_assign_source_20 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 62;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_findTestCases, tmp_assign_source_20 );
    tmp_import_globals_16 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 64;
    tmp_import_name_from_16 = IMPORT_MODULE( const_str_plain_main, tmp_import_globals_16, tmp_import_globals_16, const_tuple_str_plain_TestProgram_str_plain_main_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_16 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 64;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_21 = IMPORT_NAME( tmp_import_name_from_16, const_str_plain_TestProgram );
    Py_DECREF( tmp_import_name_from_16 );
    if ( tmp_assign_source_21 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 64;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_TestProgram, tmp_assign_source_21 );
    tmp_import_globals_17 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 64;
    tmp_import_name_from_17 = IMPORT_MODULE( const_str_plain_main, tmp_import_globals_17, tmp_import_globals_17, const_tuple_str_plain_TestProgram_str_plain_main_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_17 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 64;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_22 = IMPORT_NAME( tmp_import_name_from_17, const_str_plain_main );
    Py_DECREF( tmp_import_name_from_17 );
    if ( tmp_assign_source_22 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 64;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_main, tmp_assign_source_22 );
    tmp_import_globals_18 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 65;
    tmp_import_name_from_18 = IMPORT_MODULE( const_str_plain_runner, tmp_import_globals_18, tmp_import_globals_18, const_tuple_str_plain_TextTestRunner_str_plain_TextTestResult_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_18 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 65;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_23 = IMPORT_NAME( tmp_import_name_from_18, const_str_plain_TextTestRunner );
    Py_DECREF( tmp_import_name_from_18 );
    if ( tmp_assign_source_23 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 65;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_TextTestRunner, tmp_assign_source_23 );
    tmp_import_globals_19 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 65;
    tmp_import_name_from_19 = IMPORT_MODULE( const_str_plain_runner, tmp_import_globals_19, tmp_import_globals_19, const_tuple_str_plain_TextTestRunner_str_plain_TextTestResult_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_19 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 65;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_24 = IMPORT_NAME( tmp_import_name_from_19, const_str_plain_TextTestResult );
    Py_DECREF( tmp_import_name_from_19 );
    if ( tmp_assign_source_24 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 65;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_TextTestResult, tmp_assign_source_24 );
    tmp_import_globals_20 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 66;
    tmp_import_name_from_20 = IMPORT_MODULE( const_str_plain_signals, tmp_import_globals_20, tmp_import_globals_20, const_tuple_fc8c7e19e3ce48ab8190e98be8ffe351_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_20 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 66;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_25 = IMPORT_NAME( tmp_import_name_from_20, const_str_plain_installHandler );
    Py_DECREF( tmp_import_name_from_20 );
    if ( tmp_assign_source_25 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 66;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_installHandler, tmp_assign_source_25 );
    tmp_import_globals_21 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 66;
    tmp_import_name_from_21 = IMPORT_MODULE( const_str_plain_signals, tmp_import_globals_21, tmp_import_globals_21, const_tuple_fc8c7e19e3ce48ab8190e98be8ffe351_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_21 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 66;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_26 = IMPORT_NAME( tmp_import_name_from_21, const_str_plain_registerResult );
    Py_DECREF( tmp_import_name_from_21 );
    if ( tmp_assign_source_26 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 66;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_registerResult, tmp_assign_source_26 );
    tmp_import_globals_22 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 66;
    tmp_import_name_from_22 = IMPORT_MODULE( const_str_plain_signals, tmp_import_globals_22, tmp_import_globals_22, const_tuple_fc8c7e19e3ce48ab8190e98be8ffe351_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_22 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 66;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_27 = IMPORT_NAME( tmp_import_name_from_22, const_str_plain_removeResult );
    Py_DECREF( tmp_import_name_from_22 );
    if ( tmp_assign_source_27 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 66;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_removeResult, tmp_assign_source_27 );
    tmp_import_globals_23 = ((PyModuleObject *)module_unittest)->md_dict;
    frame_module->f_lineno = 66;
    tmp_import_name_from_23 = IMPORT_MODULE( const_str_plain_signals, tmp_import_globals_23, tmp_import_globals_23, const_tuple_fc8c7e19e3ce48ab8190e98be8ffe351_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_23 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 66;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_28 = IMPORT_NAME( tmp_import_name_from_23, const_str_plain_removeHandler );
    Py_DECREF( tmp_import_name_from_23 );
    if ( tmp_assign_source_28 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 66;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_removeHandler, tmp_assign_source_28 );
    tmp_assign_source_29 = GET_STRING_DICT_VALUE( moduledict_unittest, (Nuitka_StringObject *)const_str_plain_TextTestResult );

    if (unlikely( tmp_assign_source_29 == NULL ))
    {
        tmp_assign_source_29 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_TextTestResult );
    }

    if ( tmp_assign_source_29 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "TextTestResult" );
        exception_tb = NULL;

        exception_lineno = 69;
        goto frame_exception_exit_1;
    }

    UPDATE_STRING_DICT0( moduledict_unittest, (Nuitka_StringObject *)const_str_plain__TextTestResult, tmp_assign_source_29 );

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

    return MOD_RETURN_VALUE( module_unittest );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
