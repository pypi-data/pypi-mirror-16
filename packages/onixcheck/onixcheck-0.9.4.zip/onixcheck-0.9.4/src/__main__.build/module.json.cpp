/* Generated code for Python source for module 'json'
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

/* The _module_json is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_json;
PyDictObject *moduledict_json;

/* The module constants used, if any. */
extern PyObject *const_str_plain_decoder;
extern PyObject *const_str_plain_loads;
extern PyObject *const_str_plain_write;
static PyObject *const_str_digest_04be16761a7196498ae170f991a729f0;
extern PyObject *const_str_plain_kw;
static PyObject *const_dict_ff68e34582c54715c2cc14151b7335ab;
extern PyObject *const_str_plain_load;
extern PyObject *const_str_digest_c075052d723d6707083e869a0e3659bb;
extern PyObject *const_str_plain_allow_nan;
static PyObject *const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple;
extern PyObject *const_str_plain_encode;
extern PyObject *const_str_plain_check_circular;
extern PyObject *const_str_plain_object_hook;
static PyObject *const_list_6cd5adbff82562af8bdb9be2ac48d46e_list;
extern PyObject *const_str_plain_decode;
static PyObject *const_str_digest_29128799e6868180fe0bd02edfedaa2d;
extern PyObject *const_dict_empty;
extern PyObject *const_str_plain_cls;
static PyObject *const_tuple_ebe32b9cef343bb6fea29014b50cc4d6_tuple;
static PyObject *const_tuple_b82128f02299582589bd5ccc8bee006e_tuple;
extern PyObject *const_str_plain_indent;
static PyObject *const_tuple_str_plain_JSONDecoder_tuple;
extern PyObject *const_str_plain_iterencode;
extern PyObject *const_str_plain_separators;
extern PyObject *const_str_plain_JSONEncoder;
static PyObject *const_str_digest_01cc92d89a14824bb4a6c88c061a6627;
static PyObject *const_tuple_str_plain_JSONEncoder_tuple;
static PyObject *const_dict_cf20e1096400ee55a5aafd036f22d909;
static PyObject *const_str_digest_a8285b38753418ae48ba4b92941cb5a1;
extern PyObject *const_str_plain___doc__;
static PyObject *const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple;
static PyObject *const_str_plain__default_decoder;
extern PyObject *const_str_plain___all__;
extern PyObject *const_tuple_empty;
extern PyObject *const_str_plain_json;
extern PyObject *const_str_plain_dump;
extern PyObject *const_str_plain_chunk;
extern PyObject *const_str_plain_ensure_ascii;
extern PyObject *const_str_plain_parse_float;
extern PyObject *const_str_plain___file__;
extern PyObject *const_str_plain___version__;
static PyObject *const_str_digest_599555fb243d72d0e4ff1c872e536554;
extern PyObject *const_tuple_none_none_none_none_none_none_none_tuple;
extern PyObject *const_str_plain_encoding;
extern PyObject *const_str_plain_read;
extern PyObject *const_str_plain_fp;
extern PyObject *const_int_pos_1;
extern PyObject *const_str_plain_dumps;
extern PyObject *const_str_plain_encoder;
static PyObject *const_str_plain__default_encoder;
extern PyObject *const_str_plain___path__;
extern PyObject *const_str_plain_obj;
extern PyObject *const_str_plain_iterable;
extern PyObject *const_str_plain_sort_keys;
extern PyObject *const_str_plain_JSONDecoder;
extern PyObject *const_str_plain_default;
static PyObject *const_tuple_d2703034e59b735961c96079f0ddd038_tuple;
extern PyObject *const_str_plain_object_pairs_hook;
extern PyObject *const_str_plain_dirname;
extern PyObject *const_str_plain_parse_int;
extern PyObject *const_str_plain___author__;
static PyObject *const_str_digest_cc54928f376395365d5feab06837d749;
static PyObject *const_str_digest_ed013416b9a126b331b47fab35fa159c;
static PyObject *const_str_digest_ca0af13e597c29ab9da2136cfc95efe2;
extern PyObject *const_str_plain_s;
extern PyObject *const_str_plain_skipkeys;
extern PyObject *const_str_plain_parse_constant;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_digest_04be16761a7196498ae170f991a729f0 = UNSTREAM_STRING( &constant_bin[ 536141 ], 1441, 0 );
    const_dict_ff68e34582c54715c2cc14151b7335ab = _PyDict_NewPresized( 3 );
    PyDict_SetItem( const_dict_ff68e34582c54715c2cc14151b7335ab, const_str_plain_object_pairs_hook, Py_None );
    PyDict_SetItem( const_dict_ff68e34582c54715c2cc14151b7335ab, const_str_plain_object_hook, Py_None );
    PyDict_SetItem( const_dict_ff68e34582c54715c2cc14151b7335ab, const_str_plain_encoding, Py_None );
    assert( PyDict_Size( const_dict_ff68e34582c54715c2cc14151b7335ab ) == 3 );
    const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple = PyTuple_New( 15 );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 0, const_str_plain_obj ); Py_INCREF( const_str_plain_obj );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 1, const_str_plain_fp ); Py_INCREF( const_str_plain_fp );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 2, const_str_plain_skipkeys ); Py_INCREF( const_str_plain_skipkeys );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 3, const_str_plain_ensure_ascii ); Py_INCREF( const_str_plain_ensure_ascii );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 4, const_str_plain_check_circular ); Py_INCREF( const_str_plain_check_circular );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 5, const_str_plain_allow_nan ); Py_INCREF( const_str_plain_allow_nan );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 6, const_str_plain_cls ); Py_INCREF( const_str_plain_cls );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 7, const_str_plain_indent ); Py_INCREF( const_str_plain_indent );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 8, const_str_plain_separators ); Py_INCREF( const_str_plain_separators );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 9, const_str_plain_encoding ); Py_INCREF( const_str_plain_encoding );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 10, const_str_plain_default ); Py_INCREF( const_str_plain_default );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 11, const_str_plain_sort_keys ); Py_INCREF( const_str_plain_sort_keys );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 12, const_str_plain_kw ); Py_INCREF( const_str_plain_kw );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 13, const_str_plain_iterable ); Py_INCREF( const_str_plain_iterable );
    PyTuple_SET_ITEM( const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 14, const_str_plain_chunk ); Py_INCREF( const_str_plain_chunk );
    const_list_6cd5adbff82562af8bdb9be2ac48d46e_list = PyList_New( 6 );
    PyList_SET_ITEM( const_list_6cd5adbff82562af8bdb9be2ac48d46e_list, 0, const_str_plain_dump ); Py_INCREF( const_str_plain_dump );
    PyList_SET_ITEM( const_list_6cd5adbff82562af8bdb9be2ac48d46e_list, 1, const_str_plain_dumps ); Py_INCREF( const_str_plain_dumps );
    PyList_SET_ITEM( const_list_6cd5adbff82562af8bdb9be2ac48d46e_list, 2, const_str_plain_load ); Py_INCREF( const_str_plain_load );
    PyList_SET_ITEM( const_list_6cd5adbff82562af8bdb9be2ac48d46e_list, 3, const_str_plain_loads ); Py_INCREF( const_str_plain_loads );
    PyList_SET_ITEM( const_list_6cd5adbff82562af8bdb9be2ac48d46e_list, 4, const_str_plain_JSONDecoder ); Py_INCREF( const_str_plain_JSONDecoder );
    PyList_SET_ITEM( const_list_6cd5adbff82562af8bdb9be2ac48d46e_list, 5, const_str_plain_JSONEncoder ); Py_INCREF( const_str_plain_JSONEncoder );
    const_str_digest_29128799e6868180fe0bd02edfedaa2d = UNSTREAM_STRING( &constant_bin[ 537582 ], 29, 0 );
    const_tuple_ebe32b9cef343bb6fea29014b50cc4d6_tuple = PyTuple_New( 9 );
    PyTuple_SET_ITEM( const_tuple_ebe32b9cef343bb6fea29014b50cc4d6_tuple, 0, const_str_plain_s ); Py_INCREF( const_str_plain_s );
    PyTuple_SET_ITEM( const_tuple_ebe32b9cef343bb6fea29014b50cc4d6_tuple, 1, const_str_plain_encoding ); Py_INCREF( const_str_plain_encoding );
    PyTuple_SET_ITEM( const_tuple_ebe32b9cef343bb6fea29014b50cc4d6_tuple, 2, const_str_plain_cls ); Py_INCREF( const_str_plain_cls );
    PyTuple_SET_ITEM( const_tuple_ebe32b9cef343bb6fea29014b50cc4d6_tuple, 3, const_str_plain_object_hook ); Py_INCREF( const_str_plain_object_hook );
    PyTuple_SET_ITEM( const_tuple_ebe32b9cef343bb6fea29014b50cc4d6_tuple, 4, const_str_plain_parse_float ); Py_INCREF( const_str_plain_parse_float );
    PyTuple_SET_ITEM( const_tuple_ebe32b9cef343bb6fea29014b50cc4d6_tuple, 5, const_str_plain_parse_int ); Py_INCREF( const_str_plain_parse_int );
    PyTuple_SET_ITEM( const_tuple_ebe32b9cef343bb6fea29014b50cc4d6_tuple, 6, const_str_plain_parse_constant ); Py_INCREF( const_str_plain_parse_constant );
    PyTuple_SET_ITEM( const_tuple_ebe32b9cef343bb6fea29014b50cc4d6_tuple, 7, const_str_plain_object_pairs_hook ); Py_INCREF( const_str_plain_object_pairs_hook );
    PyTuple_SET_ITEM( const_tuple_ebe32b9cef343bb6fea29014b50cc4d6_tuple, 8, const_str_plain_kw ); Py_INCREF( const_str_plain_kw );
    const_tuple_b82128f02299582589bd5ccc8bee006e_tuple = PyTuple_New( 10 );
    PyTuple_SET_ITEM( const_tuple_b82128f02299582589bd5ccc8bee006e_tuple, 0, Py_False ); Py_INCREF( Py_False );
    PyTuple_SET_ITEM( const_tuple_b82128f02299582589bd5ccc8bee006e_tuple, 1, Py_True ); Py_INCREF( Py_True );
    PyTuple_SET_ITEM( const_tuple_b82128f02299582589bd5ccc8bee006e_tuple, 2, Py_True ); Py_INCREF( Py_True );
    PyTuple_SET_ITEM( const_tuple_b82128f02299582589bd5ccc8bee006e_tuple, 3, Py_True ); Py_INCREF( Py_True );
    PyTuple_SET_ITEM( const_tuple_b82128f02299582589bd5ccc8bee006e_tuple, 4, Py_None ); Py_INCREF( Py_None );
    PyTuple_SET_ITEM( const_tuple_b82128f02299582589bd5ccc8bee006e_tuple, 5, Py_None ); Py_INCREF( Py_None );
    PyTuple_SET_ITEM( const_tuple_b82128f02299582589bd5ccc8bee006e_tuple, 6, Py_None ); Py_INCREF( Py_None );
    PyTuple_SET_ITEM( const_tuple_b82128f02299582589bd5ccc8bee006e_tuple, 7, const_str_digest_c075052d723d6707083e869a0e3659bb ); Py_INCREF( const_str_digest_c075052d723d6707083e869a0e3659bb );
    PyTuple_SET_ITEM( const_tuple_b82128f02299582589bd5ccc8bee006e_tuple, 8, Py_None ); Py_INCREF( Py_None );
    PyTuple_SET_ITEM( const_tuple_b82128f02299582589bd5ccc8bee006e_tuple, 9, Py_False ); Py_INCREF( Py_False );
    const_tuple_str_plain_JSONDecoder_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_JSONDecoder_tuple, 0, const_str_plain_JSONDecoder ); Py_INCREF( const_str_plain_JSONDecoder );
    const_str_digest_01cc92d89a14824bb4a6c88c061a6627 = UNSTREAM_STRING( &constant_bin[ 537611 ], 2070, 0 );
    const_tuple_str_plain_JSONEncoder_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_JSONEncoder_tuple, 0, const_str_plain_JSONEncoder ); Py_INCREF( const_str_plain_JSONEncoder );
    const_dict_cf20e1096400ee55a5aafd036f22d909 = _PyDict_NewPresized( 8 );
    PyDict_SetItem( const_dict_cf20e1096400ee55a5aafd036f22d909, const_str_plain_indent, Py_None );
    PyDict_SetItem( const_dict_cf20e1096400ee55a5aafd036f22d909, const_str_plain_encoding, const_str_digest_c075052d723d6707083e869a0e3659bb );
    PyDict_SetItem( const_dict_cf20e1096400ee55a5aafd036f22d909, const_str_plain_default, Py_None );
    PyDict_SetItem( const_dict_cf20e1096400ee55a5aafd036f22d909, const_str_plain_separators, Py_None );
    PyDict_SetItem( const_dict_cf20e1096400ee55a5aafd036f22d909, const_str_plain_skipkeys, Py_False );
    PyDict_SetItem( const_dict_cf20e1096400ee55a5aafd036f22d909, const_str_plain_allow_nan, Py_True );
    PyDict_SetItem( const_dict_cf20e1096400ee55a5aafd036f22d909, const_str_plain_ensure_ascii, Py_True );
    PyDict_SetItem( const_dict_cf20e1096400ee55a5aafd036f22d909, const_str_plain_check_circular, Py_True );
    assert( PyDict_Size( const_dict_cf20e1096400ee55a5aafd036f22d909 ) == 8 );
    const_str_digest_a8285b38753418ae48ba4b92941cb5a1 = UNSTREAM_STRING( &constant_bin[ 539681 ], 16, 0 );
    const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple = PyTuple_New( 12 );
    PyTuple_SET_ITEM( const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple, 0, const_str_plain_obj ); Py_INCREF( const_str_plain_obj );
    PyTuple_SET_ITEM( const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple, 1, const_str_plain_skipkeys ); Py_INCREF( const_str_plain_skipkeys );
    PyTuple_SET_ITEM( const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple, 2, const_str_plain_ensure_ascii ); Py_INCREF( const_str_plain_ensure_ascii );
    PyTuple_SET_ITEM( const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple, 3, const_str_plain_check_circular ); Py_INCREF( const_str_plain_check_circular );
    PyTuple_SET_ITEM( const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple, 4, const_str_plain_allow_nan ); Py_INCREF( const_str_plain_allow_nan );
    PyTuple_SET_ITEM( const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple, 5, const_str_plain_cls ); Py_INCREF( const_str_plain_cls );
    PyTuple_SET_ITEM( const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple, 6, const_str_plain_indent ); Py_INCREF( const_str_plain_indent );
    PyTuple_SET_ITEM( const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple, 7, const_str_plain_separators ); Py_INCREF( const_str_plain_separators );
    PyTuple_SET_ITEM( const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple, 8, const_str_plain_encoding ); Py_INCREF( const_str_plain_encoding );
    PyTuple_SET_ITEM( const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple, 9, const_str_plain_default ); Py_INCREF( const_str_plain_default );
    PyTuple_SET_ITEM( const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple, 10, const_str_plain_sort_keys ); Py_INCREF( const_str_plain_sort_keys );
    PyTuple_SET_ITEM( const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple, 11, const_str_plain_kw ); Py_INCREF( const_str_plain_kw );
    const_str_plain__default_decoder = UNSTREAM_STRING( &constant_bin[ 539697 ], 16, 1 );
    const_str_digest_599555fb243d72d0e4ff1c872e536554 = UNSTREAM_STRING( &constant_bin[ 539713 ], 2514, 0 );
    const_str_plain__default_encoder = UNSTREAM_STRING( &constant_bin[ 542227 ], 16, 1 );
    const_tuple_d2703034e59b735961c96079f0ddd038_tuple = PyTuple_New( 9 );
    PyTuple_SET_ITEM( const_tuple_d2703034e59b735961c96079f0ddd038_tuple, 0, const_str_plain_fp ); Py_INCREF( const_str_plain_fp );
    PyTuple_SET_ITEM( const_tuple_d2703034e59b735961c96079f0ddd038_tuple, 1, const_str_plain_encoding ); Py_INCREF( const_str_plain_encoding );
    PyTuple_SET_ITEM( const_tuple_d2703034e59b735961c96079f0ddd038_tuple, 2, const_str_plain_cls ); Py_INCREF( const_str_plain_cls );
    PyTuple_SET_ITEM( const_tuple_d2703034e59b735961c96079f0ddd038_tuple, 3, const_str_plain_object_hook ); Py_INCREF( const_str_plain_object_hook );
    PyTuple_SET_ITEM( const_tuple_d2703034e59b735961c96079f0ddd038_tuple, 4, const_str_plain_parse_float ); Py_INCREF( const_str_plain_parse_float );
    PyTuple_SET_ITEM( const_tuple_d2703034e59b735961c96079f0ddd038_tuple, 5, const_str_plain_parse_int ); Py_INCREF( const_str_plain_parse_int );
    PyTuple_SET_ITEM( const_tuple_d2703034e59b735961c96079f0ddd038_tuple, 6, const_str_plain_parse_constant ); Py_INCREF( const_str_plain_parse_constant );
    PyTuple_SET_ITEM( const_tuple_d2703034e59b735961c96079f0ddd038_tuple, 7, const_str_plain_object_pairs_hook ); Py_INCREF( const_str_plain_object_pairs_hook );
    PyTuple_SET_ITEM( const_tuple_d2703034e59b735961c96079f0ddd038_tuple, 8, const_str_plain_kw ); Py_INCREF( const_str_plain_kw );
    const_str_digest_cc54928f376395365d5feab06837d749 = UNSTREAM_STRING( &constant_bin[ 542243 ], 5, 0 );
    const_str_digest_ed013416b9a126b331b47fab35fa159c = UNSTREAM_STRING( &constant_bin[ 542248 ], 3016, 0 );
    const_str_digest_ca0af13e597c29ab9da2136cfc95efe2 = UNSTREAM_STRING( &constant_bin[ 545264 ], 2064, 0 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_json( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_f4b82912b430e4f95cdab9d7bfa5d5a0;
static PyCodeObject *codeobj_302192d0398477b76c1ba9f6dfe0ff65;
static PyCodeObject *codeobj_3c62dcc14467fb105363c695850fa8e4;
static PyCodeObject *codeobj_735324f70dba261090f9d2f5690acb6e;
static PyCodeObject *codeobj_2341cd23c9e319db0ab6441980201c94;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_a8285b38753418ae48ba4b92941cb5a1 );
    codeobj_f4b82912b430e4f95cdab9d7bfa5d5a0 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_dump, 122, const_tuple_139bbf516dd20c2cc321096e99604b9c_tuple, 12, CO_OPTIMIZED | CO_NEWLOCALS | CO_VARKEYWORDS | CO_NOFREE );
    codeobj_302192d0398477b76c1ba9f6dfe0ff65 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_dumps, 193, const_tuple_d7490feb9ff9892ed433fb1586d6b11a_tuple, 11, CO_OPTIMIZED | CO_NEWLOCALS | CO_VARKEYWORDS | CO_NOFREE );
    codeobj_3c62dcc14467fb105363c695850fa8e4 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_json, 1, const_tuple_empty, 0, CO_NOFREE );
    codeobj_735324f70dba261090f9d2f5690acb6e = MAKE_CODEOBJ( module_filename_obj, const_str_plain_load, 257, const_tuple_d2703034e59b735961c96079f0ddd038_tuple, 8, CO_OPTIMIZED | CO_NEWLOCALS | CO_VARKEYWORDS | CO_NOFREE );
    codeobj_2341cd23c9e319db0ab6441980201c94 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_loads, 293, const_tuple_ebe32b9cef343bb6fea29014b50cc4d6_tuple, 8, CO_OPTIMIZED | CO_NEWLOCALS | CO_VARKEYWORDS | CO_NOFREE );
}

// The module function declarations.
NUITKA_CROSS_MODULE PyObject *impl_function_9_complex_call_helper_keywords_star_dict_of___internal__( PyObject **python_pars );


NUITKA_CROSS_MODULE PyObject *impl_function_11_complex_call_helper_pos_keywords_star_dict_of___internal__( PyObject **python_pars );


static PyObject *MAKE_FUNCTION_function_1_dump_of_json( PyObject *defaults );


static PyObject *MAKE_FUNCTION_function_2_dumps_of_json( PyObject *defaults );


static PyObject *MAKE_FUNCTION_function_3_load_of_json( PyObject *defaults );


static PyObject *MAKE_FUNCTION_function_4_loads_of_json( PyObject *defaults );


// The module function definitions.
static PyObject *impl_function_1_dump_of_json( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_obj = python_pars[ 0 ];
    PyObject *par_fp = python_pars[ 1 ];
    PyObject *par_skipkeys = python_pars[ 2 ];
    PyObject *par_ensure_ascii = python_pars[ 3 ];
    PyObject *par_check_circular = python_pars[ 4 ];
    PyObject *par_allow_nan = python_pars[ 5 ];
    PyObject *par_cls = python_pars[ 6 ];
    PyObject *par_indent = python_pars[ 7 ];
    PyObject *par_separators = python_pars[ 8 ];
    PyObject *par_encoding = python_pars[ 9 ];
    PyObject *par_default = python_pars[ 10 ];
    PyObject *par_sort_keys = python_pars[ 11 ];
    PyObject *par_kw = python_pars[ 12 ];
    PyObject *var_iterable = NULL;
    PyObject *var_chunk = NULL;
    PyObject *tmp_for_loop_1__for_iterator = NULL;
    PyObject *tmp_for_loop_1__iter_value = NULL;
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
    int tmp_and_left_truth_1;
    int tmp_and_left_truth_2;
    int tmp_and_left_truth_3;
    int tmp_and_left_truth_4;
    int tmp_and_left_truth_5;
    int tmp_and_left_truth_6;
    int tmp_and_left_truth_7;
    int tmp_and_left_truth_8;
    int tmp_and_left_truth_9;
    int tmp_and_left_truth_10;
    PyObject *tmp_and_left_value_1;
    PyObject *tmp_and_left_value_2;
    PyObject *tmp_and_left_value_3;
    PyObject *tmp_and_left_value_4;
    PyObject *tmp_and_left_value_5;
    PyObject *tmp_and_left_value_6;
    PyObject *tmp_and_left_value_7;
    PyObject *tmp_and_left_value_8;
    PyObject *tmp_and_left_value_9;
    PyObject *tmp_and_left_value_10;
    PyObject *tmp_and_right_value_1;
    PyObject *tmp_and_right_value_2;
    PyObject *tmp_and_right_value_3;
    PyObject *tmp_and_right_value_4;
    PyObject *tmp_and_right_value_5;
    PyObject *tmp_and_right_value_6;
    PyObject *tmp_and_right_value_7;
    PyObject *tmp_and_right_value_8;
    PyObject *tmp_and_right_value_9;
    PyObject *tmp_and_right_value_10;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_args_element_name_2;
    PyObject *tmp_args_element_name_3;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_assign_source_4;
    PyObject *tmp_assign_source_5;
    PyObject *tmp_assign_source_6;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_called_name_3;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_compexpr_left_1;
    PyObject *tmp_compexpr_left_2;
    PyObject *tmp_compexpr_left_3;
    PyObject *tmp_compexpr_left_4;
    PyObject *tmp_compexpr_left_5;
    PyObject *tmp_compexpr_right_1;
    PyObject *tmp_compexpr_right_2;
    PyObject *tmp_compexpr_right_3;
    PyObject *tmp_compexpr_right_4;
    PyObject *tmp_compexpr_right_5;
    int tmp_cond_truth_1;
    PyObject *tmp_cond_value_1;
    PyObject *tmp_dict_key_1;
    PyObject *tmp_dict_key_2;
    PyObject *tmp_dict_key_3;
    PyObject *tmp_dict_key_4;
    PyObject *tmp_dict_key_5;
    PyObject *tmp_dict_key_6;
    PyObject *tmp_dict_key_7;
    PyObject *tmp_dict_key_8;
    PyObject *tmp_dict_key_9;
    PyObject *tmp_dict_value_1;
    PyObject *tmp_dict_value_2;
    PyObject *tmp_dict_value_3;
    PyObject *tmp_dict_value_4;
    PyObject *tmp_dict_value_5;
    PyObject *tmp_dict_value_6;
    PyObject *tmp_dict_value_7;
    PyObject *tmp_dict_value_8;
    PyObject *tmp_dict_value_9;
    PyObject *tmp_dircall_arg1_1;
    PyObject *tmp_dircall_arg2_1;
    PyObject *tmp_dircall_arg3_1;
    PyObject *tmp_frame_locals;
    bool tmp_is_1;
    PyObject *tmp_iter_arg_1;
    PyObject *tmp_next_source_1;
    PyObject *tmp_operand_name_1;
    PyObject *tmp_operand_name_2;
    PyObject *tmp_operand_name_3;
    PyObject *tmp_return_value;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    PyObject *tmp_source_name_3;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_f4b82912b430e4f95cdab9d7bfa5d5a0, module_json );
    frame_function = cache_frame_function;

    // Push the new frame as the currently active one.
    pushFrameStack( frame_function );

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    Py_INCREF( frame_function );
    assert( Py_REFCNT( frame_function ) == 2 ); // Frame stack

#if PYTHON_VERSION >= 340
    frame_function->f_executing += 1;
#endif

    // Framed code:
    tmp_operand_name_1 = par_skipkeys;

    tmp_and_left_value_1 = UNARY_OPERATION( UNARY_NOT, tmp_operand_name_1 );
    if ( tmp_and_left_value_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 175;
        goto frame_exception_exit_1;
    }
    tmp_and_left_truth_1 = CHECK_IF_TRUE( tmp_and_left_value_1 );
    if ( tmp_and_left_truth_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 178;
        goto frame_exception_exit_1;
    }
    if ( tmp_and_left_truth_1 == 1 )
    {
        goto and_right_1;
    }
    else
    {
        goto and_left_1;
    }
    and_right_1:;
    tmp_and_left_value_2 = par_ensure_ascii;

    tmp_and_left_truth_2 = CHECK_IF_TRUE( tmp_and_left_value_2 );
    if ( tmp_and_left_truth_2 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 178;
        goto frame_exception_exit_1;
    }
    if ( tmp_and_left_truth_2 == 1 )
    {
        goto and_right_2;
    }
    else
    {
        goto and_left_2;
    }
    and_right_2:;
    tmp_and_left_value_3 = par_check_circular;

    tmp_and_left_truth_3 = CHECK_IF_TRUE( tmp_and_left_value_3 );
    if ( tmp_and_left_truth_3 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 178;
        goto frame_exception_exit_1;
    }
    if ( tmp_and_left_truth_3 == 1 )
    {
        goto and_right_3;
    }
    else
    {
        goto and_left_3;
    }
    and_right_3:;
    tmp_and_left_value_4 = par_allow_nan;

    tmp_and_left_truth_4 = CHECK_IF_TRUE( tmp_and_left_value_4 );
    if ( tmp_and_left_truth_4 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 178;
        goto frame_exception_exit_1;
    }
    if ( tmp_and_left_truth_4 == 1 )
    {
        goto and_right_4;
    }
    else
    {
        goto and_left_4;
    }
    and_right_4:;
    tmp_compexpr_left_1 = par_cls;

    tmp_compexpr_right_1 = Py_None;
    tmp_and_left_value_5 = BOOL_FROM( tmp_compexpr_left_1 == tmp_compexpr_right_1 );
    tmp_and_left_truth_5 = CHECK_IF_TRUE( tmp_and_left_value_5 );
    assert( !(tmp_and_left_truth_5 == -1) );
    if ( tmp_and_left_truth_5 == 1 )
    {
        goto and_right_5;
    }
    else
    {
        goto and_left_5;
    }
    and_right_5:;
    tmp_compexpr_left_2 = par_indent;

    tmp_compexpr_right_2 = Py_None;
    tmp_and_left_value_6 = BOOL_FROM( tmp_compexpr_left_2 == tmp_compexpr_right_2 );
    tmp_and_left_truth_6 = CHECK_IF_TRUE( tmp_and_left_value_6 );
    assert( !(tmp_and_left_truth_6 == -1) );
    if ( tmp_and_left_truth_6 == 1 )
    {
        goto and_right_6;
    }
    else
    {
        goto and_left_6;
    }
    and_right_6:;
    tmp_compexpr_left_3 = par_separators;

    tmp_compexpr_right_3 = Py_None;
    tmp_and_left_value_7 = BOOL_FROM( tmp_compexpr_left_3 == tmp_compexpr_right_3 );
    tmp_and_left_truth_7 = CHECK_IF_TRUE( tmp_and_left_value_7 );
    assert( !(tmp_and_left_truth_7 == -1) );
    if ( tmp_and_left_truth_7 == 1 )
    {
        goto and_right_7;
    }
    else
    {
        goto and_left_7;
    }
    and_right_7:;
    tmp_compexpr_left_4 = par_encoding;

    tmp_compexpr_right_4 = const_str_digest_c075052d723d6707083e869a0e3659bb;
    tmp_and_left_value_8 = RICH_COMPARE_EQ( tmp_compexpr_left_4, tmp_compexpr_right_4 );
    if ( tmp_and_left_value_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 178;
        goto frame_exception_exit_1;
    }
    tmp_and_left_truth_8 = CHECK_IF_TRUE( tmp_and_left_value_8 );
    if ( tmp_and_left_truth_8 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_and_left_value_8 );

        exception_lineno = 178;
        goto frame_exception_exit_1;
    }
    if ( tmp_and_left_truth_8 == 1 )
    {
        goto and_right_8;
    }
    else
    {
        goto and_left_8;
    }
    and_right_8:;
    Py_DECREF( tmp_and_left_value_8 );
    tmp_compexpr_left_5 = par_default;

    tmp_compexpr_right_5 = Py_None;
    tmp_and_left_value_9 = BOOL_FROM( tmp_compexpr_left_5 == tmp_compexpr_right_5 );
    tmp_and_left_truth_9 = CHECK_IF_TRUE( tmp_and_left_value_9 );
    assert( !(tmp_and_left_truth_9 == -1) );
    if ( tmp_and_left_truth_9 == 1 )
    {
        goto and_right_9;
    }
    else
    {
        goto and_left_9;
    }
    and_right_9:;
    tmp_operand_name_2 = par_sort_keys;

    tmp_and_left_value_10 = UNARY_OPERATION( UNARY_NOT, tmp_operand_name_2 );
    if ( tmp_and_left_value_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 178;
        goto frame_exception_exit_1;
    }
    tmp_and_left_truth_10 = CHECK_IF_TRUE( tmp_and_left_value_10 );
    if ( tmp_and_left_truth_10 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 178;
        goto frame_exception_exit_1;
    }
    if ( tmp_and_left_truth_10 == 1 )
    {
        goto and_right_10;
    }
    else
    {
        goto and_left_10;
    }
    and_right_10:;
    tmp_operand_name_3 = par_kw;

    tmp_and_right_value_10 = UNARY_OPERATION( UNARY_NOT, tmp_operand_name_3 );
    if ( tmp_and_right_value_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 178;
        goto frame_exception_exit_1;
    }
    tmp_and_right_value_9 = tmp_and_right_value_10;
    goto and_end_10;
    and_left_10:;
    tmp_and_right_value_9 = tmp_and_left_value_10;
    and_end_10:;
    tmp_and_right_value_8 = tmp_and_right_value_9;
    goto and_end_9;
    and_left_9:;
    tmp_and_right_value_8 = tmp_and_left_value_9;
    and_end_9:;
    Py_INCREF( tmp_and_right_value_8 );
    tmp_and_right_value_7 = tmp_and_right_value_8;
    goto and_end_8;
    and_left_8:;
    tmp_and_right_value_7 = tmp_and_left_value_8;
    and_end_8:;
    tmp_and_right_value_6 = tmp_and_right_value_7;
    goto and_end_7;
    and_left_7:;
    Py_INCREF( tmp_and_left_value_7 );
    tmp_and_right_value_6 = tmp_and_left_value_7;
    and_end_7:;
    tmp_and_right_value_5 = tmp_and_right_value_6;
    goto and_end_6;
    and_left_6:;
    Py_INCREF( tmp_and_left_value_6 );
    tmp_and_right_value_5 = tmp_and_left_value_6;
    and_end_6:;
    tmp_and_right_value_4 = tmp_and_right_value_5;
    goto and_end_5;
    and_left_5:;
    Py_INCREF( tmp_and_left_value_5 );
    tmp_and_right_value_4 = tmp_and_left_value_5;
    and_end_5:;
    tmp_and_right_value_3 = tmp_and_right_value_4;
    goto and_end_4;
    and_left_4:;
    Py_INCREF( tmp_and_left_value_4 );
    tmp_and_right_value_3 = tmp_and_left_value_4;
    and_end_4:;
    tmp_and_right_value_2 = tmp_and_right_value_3;
    goto and_end_3;
    and_left_3:;
    Py_INCREF( tmp_and_left_value_3 );
    tmp_and_right_value_2 = tmp_and_left_value_3;
    and_end_3:;
    tmp_and_right_value_1 = tmp_and_right_value_2;
    goto and_end_2;
    and_left_2:;
    Py_INCREF( tmp_and_left_value_2 );
    tmp_and_right_value_1 = tmp_and_left_value_2;
    and_end_2:;
    tmp_cond_value_1 = tmp_and_right_value_1;
    goto and_end_1;
    and_left_1:;
    Py_INCREF( tmp_and_left_value_1 );
    tmp_cond_value_1 = tmp_and_left_value_1;
    and_end_1:;
    tmp_cond_truth_1 = CHECK_IF_TRUE( tmp_cond_value_1 );
    if ( tmp_cond_truth_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_cond_value_1 );

        exception_lineno = 178;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_cond_value_1 );
    if ( tmp_cond_truth_1 == 1 )
    {
        goto branch_yes_1;
    }
    else
    {
        goto branch_no_1;
    }
    branch_yes_1:;
    tmp_source_name_1 = GET_STRING_DICT_VALUE( moduledict_json, (Nuitka_StringObject *)const_str_plain__default_encoder );

    if (unlikely( tmp_source_name_1 == NULL ))
    {
        tmp_source_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__default_encoder );
    }

    if ( tmp_source_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "_default_encoder" );
        exception_tb = NULL;

        exception_lineno = 179;
        goto frame_exception_exit_1;
    }

    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_iterencode );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 179;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_1 = par_obj;

    frame_function->f_lineno = 179;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_assign_source_1 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    Py_DECREF( tmp_called_name_1 );
    if ( tmp_assign_source_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 179;
        goto frame_exception_exit_1;
    }
    assert( var_iterable == NULL );
    var_iterable = tmp_assign_source_1;

    goto branch_end_1;
    branch_no_1:;
    tmp_compare_left_1 = par_cls;

    tmp_compare_right_1 = Py_None;
    tmp_is_1 = ( tmp_compare_left_1 == tmp_compare_right_1 );
    if ( tmp_is_1 )
    {
        goto branch_yes_2;
    }
    else
    {
        goto branch_no_2;
    }
    branch_yes_2:;
    tmp_assign_source_2 = GET_STRING_DICT_VALUE( moduledict_json, (Nuitka_StringObject *)const_str_plain_JSONEncoder );

    if (unlikely( tmp_assign_source_2 == NULL ))
    {
        tmp_assign_source_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_JSONEncoder );
    }

    if ( tmp_assign_source_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "JSONEncoder" );
        exception_tb = NULL;

        exception_lineno = 182;
        goto frame_exception_exit_1;
    }

    {
        PyObject *old = par_cls;
        assert( old != NULL );
        par_cls = tmp_assign_source_2;
        Py_INCREF( par_cls );
        Py_DECREF( old );
    }

    branch_no_2:;
    tmp_dircall_arg1_1 = par_cls;

    tmp_dircall_arg2_1 = _PyDict_NewPresized( 9 );
    tmp_dict_value_1 = par_skipkeys;

    tmp_dict_key_1 = const_str_plain_skipkeys;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_1, tmp_dict_value_1 );
    tmp_dict_value_2 = par_ensure_ascii;

    tmp_dict_key_2 = const_str_plain_ensure_ascii;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_2, tmp_dict_value_2 );
    tmp_dict_value_3 = par_check_circular;

    tmp_dict_key_3 = const_str_plain_check_circular;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_3, tmp_dict_value_3 );
    tmp_dict_value_4 = par_allow_nan;

    tmp_dict_key_4 = const_str_plain_allow_nan;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_4, tmp_dict_value_4 );
    tmp_dict_value_5 = par_indent;

    tmp_dict_key_5 = const_str_plain_indent;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_5, tmp_dict_value_5 );
    tmp_dict_value_6 = par_separators;

    tmp_dict_key_6 = const_str_plain_separators;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_6, tmp_dict_value_6 );
    tmp_dict_value_7 = par_encoding;

    tmp_dict_key_7 = const_str_plain_encoding;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_7, tmp_dict_value_7 );
    tmp_dict_value_8 = par_default;

    tmp_dict_key_8 = const_str_plain_default;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_8, tmp_dict_value_8 );
    tmp_dict_value_9 = par_sort_keys;

    tmp_dict_key_9 = const_str_plain_sort_keys;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_9, tmp_dict_value_9 );
    tmp_dircall_arg3_1 = par_kw;

    Py_INCREF( tmp_dircall_arg1_1 );
    Py_INCREF( tmp_dircall_arg3_1 );

    {
        PyObject *dir_call_args[] = {tmp_dircall_arg1_1, tmp_dircall_arg2_1, tmp_dircall_arg3_1};
        tmp_source_name_2 = impl_function_9_complex_call_helper_keywords_star_dict_of___internal__( dir_call_args );
    }
    if ( tmp_source_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 186;
        goto frame_exception_exit_1;
    }
    tmp_called_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_iterencode );
    Py_DECREF( tmp_source_name_2 );
    if ( tmp_called_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 183;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_2 = par_obj;

    frame_function->f_lineno = 186;
    {
        PyObject *call_args[] = { tmp_args_element_name_2 };
        tmp_assign_source_3 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_2, call_args );
    }

    Py_DECREF( tmp_called_name_2 );
    if ( tmp_assign_source_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 186;
        goto frame_exception_exit_1;
    }
    assert( var_iterable == NULL );
    var_iterable = tmp_assign_source_3;

    branch_end_1:;
    tmp_iter_arg_1 = var_iterable;

    tmp_assign_source_4 = MAKE_ITERATOR( tmp_iter_arg_1 );
    if ( tmp_assign_source_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 189;
        goto frame_exception_exit_1;
    }
    assert( tmp_for_loop_1__for_iterator == NULL );
    tmp_for_loop_1__for_iterator = tmp_assign_source_4;

    // Tried code:
    loop_start_1:;
    tmp_next_source_1 = tmp_for_loop_1__for_iterator;

    tmp_assign_source_5 = ITERATOR_NEXT( tmp_next_source_1 );
    if ( tmp_assign_source_5 == NULL )
    {
        if ( CHECK_AND_CLEAR_STOP_ITERATION_OCCURRED() )
        {

            goto loop_end_1;
        }
        else
        {

            FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
            frame_function->f_lineno = 189;
            goto try_except_handler_2;
        }
    }

    {
        PyObject *old = tmp_for_loop_1__iter_value;
        tmp_for_loop_1__iter_value = tmp_assign_source_5;
        Py_XDECREF( old );
    }

    tmp_assign_source_6 = tmp_for_loop_1__iter_value;

    {
        PyObject *old = var_chunk;
        var_chunk = tmp_assign_source_6;
        Py_INCREF( var_chunk );
        Py_XDECREF( old );
    }

    tmp_source_name_3 = par_fp;

    tmp_called_name_3 = LOOKUP_ATTRIBUTE( tmp_source_name_3, const_str_plain_write );
    if ( tmp_called_name_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 190;
        goto try_except_handler_2;
    }
    tmp_args_element_name_3 = var_chunk;

    frame_function->f_lineno = 190;
    {
        PyObject *call_args[] = { tmp_args_element_name_3 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_3, call_args );
    }

    Py_DECREF( tmp_called_name_3 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 190;
        goto try_except_handler_2;
    }
    Py_DECREF( tmp_unused );
    if ( CONSIDER_THREADING() == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 189;
        goto try_except_handler_2;
    }
    goto loop_start_1;
    loop_end_1:;
    goto try_end_1;
    // Exception handler code:
    try_except_handler_2:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    Py_XDECREF( tmp_for_loop_1__iter_value );
    tmp_for_loop_1__iter_value = NULL;

    CHECK_OBJECT( (PyObject *)tmp_for_loop_1__for_iterator );
    Py_DECREF( tmp_for_loop_1__for_iterator );
    tmp_for_loop_1__for_iterator = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto frame_exception_exit_1;
    // End of try:
    try_end_1:;

#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    // Put the previous frame back on top.
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto frame_no_exception_1;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif

    {
        bool needs_detach = false;

        if ( exception_tb == NULL )
        {
            exception_tb = MAKE_TRACEBACK( frame_function, exception_lineno );
            needs_detach = true;
        }
        else if ( exception_lineno != -1 )
        {
            PyTracebackObject *traceback_new = MAKE_TRACEBACK( frame_function, exception_lineno );
            traceback_new->tb_next = exception_tb;
            exception_tb = traceback_new;

            needs_detach = true;
        }

        if (needs_detach)
        {

            tmp_frame_locals = PyDict_New();
            if ( par_obj )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_obj,
                    par_obj
                );

                assert( res == 0 );
            }

            if ( par_fp )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_fp,
                    par_fp
                );

                assert( res == 0 );
            }

            if ( par_skipkeys )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_skipkeys,
                    par_skipkeys
                );

                assert( res == 0 );
            }

            if ( par_ensure_ascii )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_ensure_ascii,
                    par_ensure_ascii
                );

                assert( res == 0 );
            }

            if ( par_check_circular )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_check_circular,
                    par_check_circular
                );

                assert( res == 0 );
            }

            if ( par_allow_nan )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_allow_nan,
                    par_allow_nan
                );

                assert( res == 0 );
            }

            if ( par_cls )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_cls,
                    par_cls
                );

                assert( res == 0 );
            }

            if ( par_indent )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_indent,
                    par_indent
                );

                assert( res == 0 );
            }

            if ( par_separators )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_separators,
                    par_separators
                );

                assert( res == 0 );
            }

            if ( par_encoding )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_encoding,
                    par_encoding
                );

                assert( res == 0 );
            }

            if ( par_default )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_default,
                    par_default
                );

                assert( res == 0 );
            }

            if ( par_sort_keys )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_sort_keys,
                    par_sort_keys
                );

                assert( res == 0 );
            }

            if ( par_kw )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_kw,
                    par_kw
                );

                assert( res == 0 );
            }

            if ( var_iterable )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_iterable,
                    var_iterable
                );

                assert( res == 0 );
            }

            if ( var_chunk )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_chunk,
                    var_chunk
                );

                assert( res == 0 );
            }



            detachFrame( exception_tb, tmp_frame_locals );
        }
    }

    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;

    Py_XDECREF( tmp_for_loop_1__iter_value );
    tmp_for_loop_1__iter_value = NULL;

    CHECK_OBJECT( (PyObject *)tmp_for_loop_1__for_iterator );
    Py_DECREF( tmp_for_loop_1__for_iterator );
    tmp_for_loop_1__for_iterator = NULL;

    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_1_dump_of_json );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_obj );
    Py_DECREF( par_obj );
    par_obj = NULL;

    CHECK_OBJECT( (PyObject *)par_fp );
    Py_DECREF( par_fp );
    par_fp = NULL;

    CHECK_OBJECT( (PyObject *)par_skipkeys );
    Py_DECREF( par_skipkeys );
    par_skipkeys = NULL;

    CHECK_OBJECT( (PyObject *)par_ensure_ascii );
    Py_DECREF( par_ensure_ascii );
    par_ensure_ascii = NULL;

    CHECK_OBJECT( (PyObject *)par_check_circular );
    Py_DECREF( par_check_circular );
    par_check_circular = NULL;

    CHECK_OBJECT( (PyObject *)par_allow_nan );
    Py_DECREF( par_allow_nan );
    par_allow_nan = NULL;

    Py_XDECREF( par_cls );
    par_cls = NULL;

    CHECK_OBJECT( (PyObject *)par_indent );
    Py_DECREF( par_indent );
    par_indent = NULL;

    CHECK_OBJECT( (PyObject *)par_separators );
    Py_DECREF( par_separators );
    par_separators = NULL;

    CHECK_OBJECT( (PyObject *)par_encoding );
    Py_DECREF( par_encoding );
    par_encoding = NULL;

    CHECK_OBJECT( (PyObject *)par_default );
    Py_DECREF( par_default );
    par_default = NULL;

    CHECK_OBJECT( (PyObject *)par_sort_keys );
    Py_DECREF( par_sort_keys );
    par_sort_keys = NULL;

    CHECK_OBJECT( (PyObject *)par_kw );
    Py_DECREF( par_kw );
    par_kw = NULL;

    CHECK_OBJECT( (PyObject *)var_iterable );
    Py_DECREF( var_iterable );
    var_iterable = NULL;

    Py_XDECREF( var_chunk );
    var_chunk = NULL;

    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_2 = exception_type;
    exception_keeper_value_2 = exception_value;
    exception_keeper_tb_2 = exception_tb;
    exception_keeper_lineno_2 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    CHECK_OBJECT( (PyObject *)par_obj );
    Py_DECREF( par_obj );
    par_obj = NULL;

    CHECK_OBJECT( (PyObject *)par_fp );
    Py_DECREF( par_fp );
    par_fp = NULL;

    CHECK_OBJECT( (PyObject *)par_skipkeys );
    Py_DECREF( par_skipkeys );
    par_skipkeys = NULL;

    CHECK_OBJECT( (PyObject *)par_ensure_ascii );
    Py_DECREF( par_ensure_ascii );
    par_ensure_ascii = NULL;

    CHECK_OBJECT( (PyObject *)par_check_circular );
    Py_DECREF( par_check_circular );
    par_check_circular = NULL;

    CHECK_OBJECT( (PyObject *)par_allow_nan );
    Py_DECREF( par_allow_nan );
    par_allow_nan = NULL;

    Py_XDECREF( par_cls );
    par_cls = NULL;

    CHECK_OBJECT( (PyObject *)par_indent );
    Py_DECREF( par_indent );
    par_indent = NULL;

    CHECK_OBJECT( (PyObject *)par_separators );
    Py_DECREF( par_separators );
    par_separators = NULL;

    CHECK_OBJECT( (PyObject *)par_encoding );
    Py_DECREF( par_encoding );
    par_encoding = NULL;

    CHECK_OBJECT( (PyObject *)par_default );
    Py_DECREF( par_default );
    par_default = NULL;

    CHECK_OBJECT( (PyObject *)par_sort_keys );
    Py_DECREF( par_sort_keys );
    par_sort_keys = NULL;

    CHECK_OBJECT( (PyObject *)par_kw );
    Py_DECREF( par_kw );
    par_kw = NULL;

    Py_XDECREF( var_iterable );
    var_iterable = NULL;

    Py_XDECREF( var_chunk );
    var_chunk = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_2;
    exception_value = exception_keeper_value_2;
    exception_tb = exception_keeper_tb_2;
    exception_lineno = exception_keeper_lineno_2;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_1_dump_of_json );
    return NULL;

function_exception_exit:
    assert( exception_type );
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );

    return NULL;
    function_return_exit:

    CHECK_OBJECT( tmp_return_value );
    assert( had_error || !ERROR_OCCURRED() );
    return tmp_return_value;

}


static PyObject *impl_function_2_dumps_of_json( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_obj = python_pars[ 0 ];
    PyObject *par_skipkeys = python_pars[ 1 ];
    PyObject *par_ensure_ascii = python_pars[ 2 ];
    PyObject *par_check_circular = python_pars[ 3 ];
    PyObject *par_allow_nan = python_pars[ 4 ];
    PyObject *par_cls = python_pars[ 5 ];
    PyObject *par_indent = python_pars[ 6 ];
    PyObject *par_separators = python_pars[ 7 ];
    PyObject *par_encoding = python_pars[ 8 ];
    PyObject *par_default = python_pars[ 9 ];
    PyObject *par_sort_keys = python_pars[ 10 ];
    PyObject *par_kw = python_pars[ 11 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    int tmp_and_left_truth_1;
    int tmp_and_left_truth_2;
    int tmp_and_left_truth_3;
    int tmp_and_left_truth_4;
    int tmp_and_left_truth_5;
    int tmp_and_left_truth_6;
    int tmp_and_left_truth_7;
    int tmp_and_left_truth_8;
    int tmp_and_left_truth_9;
    int tmp_and_left_truth_10;
    PyObject *tmp_and_left_value_1;
    PyObject *tmp_and_left_value_2;
    PyObject *tmp_and_left_value_3;
    PyObject *tmp_and_left_value_4;
    PyObject *tmp_and_left_value_5;
    PyObject *tmp_and_left_value_6;
    PyObject *tmp_and_left_value_7;
    PyObject *tmp_and_left_value_8;
    PyObject *tmp_and_left_value_9;
    PyObject *tmp_and_left_value_10;
    PyObject *tmp_and_right_value_1;
    PyObject *tmp_and_right_value_2;
    PyObject *tmp_and_right_value_3;
    PyObject *tmp_and_right_value_4;
    PyObject *tmp_and_right_value_5;
    PyObject *tmp_and_right_value_6;
    PyObject *tmp_and_right_value_7;
    PyObject *tmp_and_right_value_8;
    PyObject *tmp_and_right_value_9;
    PyObject *tmp_and_right_value_10;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_args_element_name_2;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_compexpr_left_1;
    PyObject *tmp_compexpr_left_2;
    PyObject *tmp_compexpr_left_3;
    PyObject *tmp_compexpr_left_4;
    PyObject *tmp_compexpr_left_5;
    PyObject *tmp_compexpr_right_1;
    PyObject *tmp_compexpr_right_2;
    PyObject *tmp_compexpr_right_3;
    PyObject *tmp_compexpr_right_4;
    PyObject *tmp_compexpr_right_5;
    int tmp_cond_truth_1;
    PyObject *tmp_cond_value_1;
    PyObject *tmp_dict_key_1;
    PyObject *tmp_dict_key_2;
    PyObject *tmp_dict_key_3;
    PyObject *tmp_dict_key_4;
    PyObject *tmp_dict_key_5;
    PyObject *tmp_dict_key_6;
    PyObject *tmp_dict_key_7;
    PyObject *tmp_dict_key_8;
    PyObject *tmp_dict_key_9;
    PyObject *tmp_dict_value_1;
    PyObject *tmp_dict_value_2;
    PyObject *tmp_dict_value_3;
    PyObject *tmp_dict_value_4;
    PyObject *tmp_dict_value_5;
    PyObject *tmp_dict_value_6;
    PyObject *tmp_dict_value_7;
    PyObject *tmp_dict_value_8;
    PyObject *tmp_dict_value_9;
    PyObject *tmp_dircall_arg1_1;
    PyObject *tmp_dircall_arg2_1;
    PyObject *tmp_dircall_arg3_1;
    PyObject *tmp_frame_locals;
    bool tmp_is_1;
    PyObject *tmp_operand_name_1;
    PyObject *tmp_operand_name_2;
    PyObject *tmp_operand_name_3;
    PyObject *tmp_return_value;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_302192d0398477b76c1ba9f6dfe0ff65, module_json );
    frame_function = cache_frame_function;

    // Push the new frame as the currently active one.
    pushFrameStack( frame_function );

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    Py_INCREF( frame_function );
    assert( Py_REFCNT( frame_function ) == 2 ); // Frame stack

#if PYTHON_VERSION >= 340
    frame_function->f_executing += 1;
#endif

    // Framed code:
    tmp_operand_name_1 = par_skipkeys;

    tmp_and_left_value_1 = UNARY_OPERATION( UNARY_NOT, tmp_operand_name_1 );
    if ( tmp_and_left_value_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 239;
        goto frame_exception_exit_1;
    }
    tmp_and_left_truth_1 = CHECK_IF_TRUE( tmp_and_left_value_1 );
    if ( tmp_and_left_truth_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 242;
        goto frame_exception_exit_1;
    }
    if ( tmp_and_left_truth_1 == 1 )
    {
        goto and_right_1;
    }
    else
    {
        goto and_left_1;
    }
    and_right_1:;
    tmp_and_left_value_2 = par_ensure_ascii;

    tmp_and_left_truth_2 = CHECK_IF_TRUE( tmp_and_left_value_2 );
    if ( tmp_and_left_truth_2 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 242;
        goto frame_exception_exit_1;
    }
    if ( tmp_and_left_truth_2 == 1 )
    {
        goto and_right_2;
    }
    else
    {
        goto and_left_2;
    }
    and_right_2:;
    tmp_and_left_value_3 = par_check_circular;

    tmp_and_left_truth_3 = CHECK_IF_TRUE( tmp_and_left_value_3 );
    if ( tmp_and_left_truth_3 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 242;
        goto frame_exception_exit_1;
    }
    if ( tmp_and_left_truth_3 == 1 )
    {
        goto and_right_3;
    }
    else
    {
        goto and_left_3;
    }
    and_right_3:;
    tmp_and_left_value_4 = par_allow_nan;

    tmp_and_left_truth_4 = CHECK_IF_TRUE( tmp_and_left_value_4 );
    if ( tmp_and_left_truth_4 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 242;
        goto frame_exception_exit_1;
    }
    if ( tmp_and_left_truth_4 == 1 )
    {
        goto and_right_4;
    }
    else
    {
        goto and_left_4;
    }
    and_right_4:;
    tmp_compexpr_left_1 = par_cls;

    tmp_compexpr_right_1 = Py_None;
    tmp_and_left_value_5 = BOOL_FROM( tmp_compexpr_left_1 == tmp_compexpr_right_1 );
    tmp_and_left_truth_5 = CHECK_IF_TRUE( tmp_and_left_value_5 );
    assert( !(tmp_and_left_truth_5 == -1) );
    if ( tmp_and_left_truth_5 == 1 )
    {
        goto and_right_5;
    }
    else
    {
        goto and_left_5;
    }
    and_right_5:;
    tmp_compexpr_left_2 = par_indent;

    tmp_compexpr_right_2 = Py_None;
    tmp_and_left_value_6 = BOOL_FROM( tmp_compexpr_left_2 == tmp_compexpr_right_2 );
    tmp_and_left_truth_6 = CHECK_IF_TRUE( tmp_and_left_value_6 );
    assert( !(tmp_and_left_truth_6 == -1) );
    if ( tmp_and_left_truth_6 == 1 )
    {
        goto and_right_6;
    }
    else
    {
        goto and_left_6;
    }
    and_right_6:;
    tmp_compexpr_left_3 = par_separators;

    tmp_compexpr_right_3 = Py_None;
    tmp_and_left_value_7 = BOOL_FROM( tmp_compexpr_left_3 == tmp_compexpr_right_3 );
    tmp_and_left_truth_7 = CHECK_IF_TRUE( tmp_and_left_value_7 );
    assert( !(tmp_and_left_truth_7 == -1) );
    if ( tmp_and_left_truth_7 == 1 )
    {
        goto and_right_7;
    }
    else
    {
        goto and_left_7;
    }
    and_right_7:;
    tmp_compexpr_left_4 = par_encoding;

    tmp_compexpr_right_4 = const_str_digest_c075052d723d6707083e869a0e3659bb;
    tmp_and_left_value_8 = RICH_COMPARE_EQ( tmp_compexpr_left_4, tmp_compexpr_right_4 );
    if ( tmp_and_left_value_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 242;
        goto frame_exception_exit_1;
    }
    tmp_and_left_truth_8 = CHECK_IF_TRUE( tmp_and_left_value_8 );
    if ( tmp_and_left_truth_8 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_and_left_value_8 );

        exception_lineno = 242;
        goto frame_exception_exit_1;
    }
    if ( tmp_and_left_truth_8 == 1 )
    {
        goto and_right_8;
    }
    else
    {
        goto and_left_8;
    }
    and_right_8:;
    Py_DECREF( tmp_and_left_value_8 );
    tmp_compexpr_left_5 = par_default;

    tmp_compexpr_right_5 = Py_None;
    tmp_and_left_value_9 = BOOL_FROM( tmp_compexpr_left_5 == tmp_compexpr_right_5 );
    tmp_and_left_truth_9 = CHECK_IF_TRUE( tmp_and_left_value_9 );
    assert( !(tmp_and_left_truth_9 == -1) );
    if ( tmp_and_left_truth_9 == 1 )
    {
        goto and_right_9;
    }
    else
    {
        goto and_left_9;
    }
    and_right_9:;
    tmp_operand_name_2 = par_sort_keys;

    tmp_and_left_value_10 = UNARY_OPERATION( UNARY_NOT, tmp_operand_name_2 );
    if ( tmp_and_left_value_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 242;
        goto frame_exception_exit_1;
    }
    tmp_and_left_truth_10 = CHECK_IF_TRUE( tmp_and_left_value_10 );
    if ( tmp_and_left_truth_10 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 242;
        goto frame_exception_exit_1;
    }
    if ( tmp_and_left_truth_10 == 1 )
    {
        goto and_right_10;
    }
    else
    {
        goto and_left_10;
    }
    and_right_10:;
    tmp_operand_name_3 = par_kw;

    tmp_and_right_value_10 = UNARY_OPERATION( UNARY_NOT, tmp_operand_name_3 );
    if ( tmp_and_right_value_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 242;
        goto frame_exception_exit_1;
    }
    tmp_and_right_value_9 = tmp_and_right_value_10;
    goto and_end_10;
    and_left_10:;
    tmp_and_right_value_9 = tmp_and_left_value_10;
    and_end_10:;
    tmp_and_right_value_8 = tmp_and_right_value_9;
    goto and_end_9;
    and_left_9:;
    tmp_and_right_value_8 = tmp_and_left_value_9;
    and_end_9:;
    Py_INCREF( tmp_and_right_value_8 );
    tmp_and_right_value_7 = tmp_and_right_value_8;
    goto and_end_8;
    and_left_8:;
    tmp_and_right_value_7 = tmp_and_left_value_8;
    and_end_8:;
    tmp_and_right_value_6 = tmp_and_right_value_7;
    goto and_end_7;
    and_left_7:;
    Py_INCREF( tmp_and_left_value_7 );
    tmp_and_right_value_6 = tmp_and_left_value_7;
    and_end_7:;
    tmp_and_right_value_5 = tmp_and_right_value_6;
    goto and_end_6;
    and_left_6:;
    Py_INCREF( tmp_and_left_value_6 );
    tmp_and_right_value_5 = tmp_and_left_value_6;
    and_end_6:;
    tmp_and_right_value_4 = tmp_and_right_value_5;
    goto and_end_5;
    and_left_5:;
    Py_INCREF( tmp_and_left_value_5 );
    tmp_and_right_value_4 = tmp_and_left_value_5;
    and_end_5:;
    tmp_and_right_value_3 = tmp_and_right_value_4;
    goto and_end_4;
    and_left_4:;
    Py_INCREF( tmp_and_left_value_4 );
    tmp_and_right_value_3 = tmp_and_left_value_4;
    and_end_4:;
    tmp_and_right_value_2 = tmp_and_right_value_3;
    goto and_end_3;
    and_left_3:;
    Py_INCREF( tmp_and_left_value_3 );
    tmp_and_right_value_2 = tmp_and_left_value_3;
    and_end_3:;
    tmp_and_right_value_1 = tmp_and_right_value_2;
    goto and_end_2;
    and_left_2:;
    Py_INCREF( tmp_and_left_value_2 );
    tmp_and_right_value_1 = tmp_and_left_value_2;
    and_end_2:;
    tmp_cond_value_1 = tmp_and_right_value_1;
    goto and_end_1;
    and_left_1:;
    Py_INCREF( tmp_and_left_value_1 );
    tmp_cond_value_1 = tmp_and_left_value_1;
    and_end_1:;
    tmp_cond_truth_1 = CHECK_IF_TRUE( tmp_cond_value_1 );
    if ( tmp_cond_truth_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_cond_value_1 );

        exception_lineno = 242;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_cond_value_1 );
    if ( tmp_cond_truth_1 == 1 )
    {
        goto branch_yes_1;
    }
    else
    {
        goto branch_no_1;
    }
    branch_yes_1:;
    tmp_source_name_1 = GET_STRING_DICT_VALUE( moduledict_json, (Nuitka_StringObject *)const_str_plain__default_encoder );

    if (unlikely( tmp_source_name_1 == NULL ))
    {
        tmp_source_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__default_encoder );
    }

    if ( tmp_source_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "_default_encoder" );
        exception_tb = NULL;

        exception_lineno = 243;
        goto frame_exception_exit_1;
    }

    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_encode );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 243;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_1 = par_obj;

    frame_function->f_lineno = 243;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_return_value = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    Py_DECREF( tmp_called_name_1 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 243;
        goto frame_exception_exit_1;
    }
    goto frame_return_exit_1;
    branch_no_1:;
    tmp_compare_left_1 = par_cls;

    tmp_compare_right_1 = Py_None;
    tmp_is_1 = ( tmp_compare_left_1 == tmp_compare_right_1 );
    if ( tmp_is_1 )
    {
        goto branch_yes_2;
    }
    else
    {
        goto branch_no_2;
    }
    branch_yes_2:;
    tmp_assign_source_1 = GET_STRING_DICT_VALUE( moduledict_json, (Nuitka_StringObject *)const_str_plain_JSONEncoder );

    if (unlikely( tmp_assign_source_1 == NULL ))
    {
        tmp_assign_source_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_JSONEncoder );
    }

    if ( tmp_assign_source_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "JSONEncoder" );
        exception_tb = NULL;

        exception_lineno = 245;
        goto frame_exception_exit_1;
    }

    {
        PyObject *old = par_cls;
        assert( old != NULL );
        par_cls = tmp_assign_source_1;
        Py_INCREF( par_cls );
        Py_DECREF( old );
    }

    branch_no_2:;
    tmp_dircall_arg1_1 = par_cls;

    tmp_dircall_arg2_1 = _PyDict_NewPresized( 9 );
    tmp_dict_value_1 = par_skipkeys;

    tmp_dict_key_1 = const_str_plain_skipkeys;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_1, tmp_dict_value_1 );
    tmp_dict_value_2 = par_ensure_ascii;

    tmp_dict_key_2 = const_str_plain_ensure_ascii;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_2, tmp_dict_value_2 );
    tmp_dict_value_3 = par_check_circular;

    tmp_dict_key_3 = const_str_plain_check_circular;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_3, tmp_dict_value_3 );
    tmp_dict_value_4 = par_allow_nan;

    tmp_dict_key_4 = const_str_plain_allow_nan;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_4, tmp_dict_value_4 );
    tmp_dict_value_5 = par_indent;

    tmp_dict_key_5 = const_str_plain_indent;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_5, tmp_dict_value_5 );
    tmp_dict_value_6 = par_separators;

    tmp_dict_key_6 = const_str_plain_separators;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_6, tmp_dict_value_6 );
    tmp_dict_value_7 = par_encoding;

    tmp_dict_key_7 = const_str_plain_encoding;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_7, tmp_dict_value_7 );
    tmp_dict_value_8 = par_default;

    tmp_dict_key_8 = const_str_plain_default;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_8, tmp_dict_value_8 );
    tmp_dict_value_9 = par_sort_keys;

    tmp_dict_key_9 = const_str_plain_sort_keys;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_9, tmp_dict_value_9 );
    tmp_dircall_arg3_1 = par_kw;

    Py_INCREF( tmp_dircall_arg1_1 );
    Py_INCREF( tmp_dircall_arg3_1 );

    {
        PyObject *dir_call_args[] = {tmp_dircall_arg1_1, tmp_dircall_arg2_1, tmp_dircall_arg3_1};
        tmp_source_name_2 = impl_function_9_complex_call_helper_keywords_star_dict_of___internal__( dir_call_args );
    }
    if ( tmp_source_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 250;
        goto frame_exception_exit_1;
    }
    tmp_called_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_encode );
    Py_DECREF( tmp_source_name_2 );
    if ( tmp_called_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 246;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_2 = par_obj;

    frame_function->f_lineno = 250;
    {
        PyObject *call_args[] = { tmp_args_element_name_2 };
        tmp_return_value = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_2, call_args );
    }

    Py_DECREF( tmp_called_name_2 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 250;
        goto frame_exception_exit_1;
    }
    goto frame_return_exit_1;

#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    // Put the previous frame back on top.
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto frame_no_exception_1;

    frame_return_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto try_return_handler_1;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif

    {
        bool needs_detach = false;

        if ( exception_tb == NULL )
        {
            exception_tb = MAKE_TRACEBACK( frame_function, exception_lineno );
            needs_detach = true;
        }
        else if ( exception_lineno != -1 )
        {
            PyTracebackObject *traceback_new = MAKE_TRACEBACK( frame_function, exception_lineno );
            traceback_new->tb_next = exception_tb;
            exception_tb = traceback_new;

            needs_detach = true;
        }

        if (needs_detach)
        {

            tmp_frame_locals = PyDict_New();
            if ( par_obj )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_obj,
                    par_obj
                );

                assert( res == 0 );
            }

            if ( par_skipkeys )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_skipkeys,
                    par_skipkeys
                );

                assert( res == 0 );
            }

            if ( par_ensure_ascii )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_ensure_ascii,
                    par_ensure_ascii
                );

                assert( res == 0 );
            }

            if ( par_check_circular )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_check_circular,
                    par_check_circular
                );

                assert( res == 0 );
            }

            if ( par_allow_nan )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_allow_nan,
                    par_allow_nan
                );

                assert( res == 0 );
            }

            if ( par_cls )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_cls,
                    par_cls
                );

                assert( res == 0 );
            }

            if ( par_indent )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_indent,
                    par_indent
                );

                assert( res == 0 );
            }

            if ( par_separators )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_separators,
                    par_separators
                );

                assert( res == 0 );
            }

            if ( par_encoding )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_encoding,
                    par_encoding
                );

                assert( res == 0 );
            }

            if ( par_default )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_default,
                    par_default
                );

                assert( res == 0 );
            }

            if ( par_sort_keys )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_sort_keys,
                    par_sort_keys
                );

                assert( res == 0 );
            }

            if ( par_kw )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_kw,
                    par_kw
                );

                assert( res == 0 );
            }



            detachFrame( exception_tb, tmp_frame_locals );
        }
    }

    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;

    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_2_dumps_of_json );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_obj );
    Py_DECREF( par_obj );
    par_obj = NULL;

    CHECK_OBJECT( (PyObject *)par_skipkeys );
    Py_DECREF( par_skipkeys );
    par_skipkeys = NULL;

    CHECK_OBJECT( (PyObject *)par_ensure_ascii );
    Py_DECREF( par_ensure_ascii );
    par_ensure_ascii = NULL;

    CHECK_OBJECT( (PyObject *)par_check_circular );
    Py_DECREF( par_check_circular );
    par_check_circular = NULL;

    CHECK_OBJECT( (PyObject *)par_allow_nan );
    Py_DECREF( par_allow_nan );
    par_allow_nan = NULL;

    Py_XDECREF( par_cls );
    par_cls = NULL;

    CHECK_OBJECT( (PyObject *)par_indent );
    Py_DECREF( par_indent );
    par_indent = NULL;

    CHECK_OBJECT( (PyObject *)par_separators );
    Py_DECREF( par_separators );
    par_separators = NULL;

    CHECK_OBJECT( (PyObject *)par_encoding );
    Py_DECREF( par_encoding );
    par_encoding = NULL;

    CHECK_OBJECT( (PyObject *)par_default );
    Py_DECREF( par_default );
    par_default = NULL;

    CHECK_OBJECT( (PyObject *)par_sort_keys );
    Py_DECREF( par_sort_keys );
    par_sort_keys = NULL;

    CHECK_OBJECT( (PyObject *)par_kw );
    Py_DECREF( par_kw );
    par_kw = NULL;

    goto function_return_exit;
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

    CHECK_OBJECT( (PyObject *)par_obj );
    Py_DECREF( par_obj );
    par_obj = NULL;

    CHECK_OBJECT( (PyObject *)par_skipkeys );
    Py_DECREF( par_skipkeys );
    par_skipkeys = NULL;

    CHECK_OBJECT( (PyObject *)par_ensure_ascii );
    Py_DECREF( par_ensure_ascii );
    par_ensure_ascii = NULL;

    CHECK_OBJECT( (PyObject *)par_check_circular );
    Py_DECREF( par_check_circular );
    par_check_circular = NULL;

    CHECK_OBJECT( (PyObject *)par_allow_nan );
    Py_DECREF( par_allow_nan );
    par_allow_nan = NULL;

    Py_XDECREF( par_cls );
    par_cls = NULL;

    CHECK_OBJECT( (PyObject *)par_indent );
    Py_DECREF( par_indent );
    par_indent = NULL;

    CHECK_OBJECT( (PyObject *)par_separators );
    Py_DECREF( par_separators );
    par_separators = NULL;

    CHECK_OBJECT( (PyObject *)par_encoding );
    Py_DECREF( par_encoding );
    par_encoding = NULL;

    CHECK_OBJECT( (PyObject *)par_default );
    Py_DECREF( par_default );
    par_default = NULL;

    CHECK_OBJECT( (PyObject *)par_sort_keys );
    Py_DECREF( par_sort_keys );
    par_sort_keys = NULL;

    CHECK_OBJECT( (PyObject *)par_kw );
    Py_DECREF( par_kw );
    par_kw = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_2_dumps_of_json );
    return NULL;

function_exception_exit:
    assert( exception_type );
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );

    return NULL;
    function_return_exit:

    CHECK_OBJECT( tmp_return_value );
    assert( had_error || !ERROR_OCCURRED() );
    return tmp_return_value;

}


static PyObject *impl_function_3_load_of_json( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_fp = python_pars[ 0 ];
    PyObject *par_encoding = python_pars[ 1 ];
    PyObject *par_cls = python_pars[ 2 ];
    PyObject *par_object_hook = python_pars[ 3 ];
    PyObject *par_parse_float = python_pars[ 4 ];
    PyObject *par_parse_int = python_pars[ 5 ];
    PyObject *par_parse_constant = python_pars[ 6 ];
    PyObject *par_object_pairs_hook = python_pars[ 7 ];
    PyObject *par_kw = python_pars[ 8 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_dict_key_1;
    PyObject *tmp_dict_key_2;
    PyObject *tmp_dict_key_3;
    PyObject *tmp_dict_key_4;
    PyObject *tmp_dict_key_5;
    PyObject *tmp_dict_key_6;
    PyObject *tmp_dict_key_7;
    PyObject *tmp_dict_value_1;
    PyObject *tmp_dict_value_2;
    PyObject *tmp_dict_value_3;
    PyObject *tmp_dict_value_4;
    PyObject *tmp_dict_value_5;
    PyObject *tmp_dict_value_6;
    PyObject *tmp_dict_value_7;
    PyObject *tmp_dircall_arg1_1;
    PyObject *tmp_dircall_arg2_1;
    PyObject *tmp_dircall_arg3_1;
    PyObject *tmp_dircall_arg4_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    PyObject *tmp_source_name_1;
    PyObject *tmp_tuple_element_1;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_735324f70dba261090f9d2f5690acb6e, module_json );
    frame_function = cache_frame_function;

    // Push the new frame as the currently active one.
    pushFrameStack( frame_function );

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    Py_INCREF( frame_function );
    assert( Py_REFCNT( frame_function ) == 2 ); // Frame stack

#if PYTHON_VERSION >= 340
    frame_function->f_executing += 1;
#endif

    // Framed code:
    tmp_dircall_arg1_1 = GET_STRING_DICT_VALUE( moduledict_json, (Nuitka_StringObject *)const_str_plain_loads );

    if (unlikely( tmp_dircall_arg1_1 == NULL ))
    {
        tmp_dircall_arg1_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_loads );
    }

    if ( tmp_dircall_arg1_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "loads" );
        exception_tb = NULL;

        exception_lineno = 286;
        goto frame_exception_exit_1;
    }

    tmp_dircall_arg2_1 = PyTuple_New( 1 );
    tmp_source_name_1 = par_fp;

    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_read );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_dircall_arg2_1 );

        exception_lineno = 286;
        goto frame_exception_exit_1;
    }
    frame_function->f_lineno = 286;
    tmp_tuple_element_1 = CALL_FUNCTION_NO_ARGS( tmp_called_name_1 );
    Py_DECREF( tmp_called_name_1 );
    if ( tmp_tuple_element_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_dircall_arg2_1 );

        exception_lineno = 286;
        goto frame_exception_exit_1;
    }
    PyTuple_SET_ITEM( tmp_dircall_arg2_1, 0, tmp_tuple_element_1 );
    tmp_dircall_arg3_1 = _PyDict_NewPresized( 7 );
    tmp_dict_value_1 = par_encoding;

    tmp_dict_key_1 = const_str_plain_encoding;
    PyDict_SetItem( tmp_dircall_arg3_1, tmp_dict_key_1, tmp_dict_value_1 );
    tmp_dict_value_2 = par_cls;

    tmp_dict_key_2 = const_str_plain_cls;
    PyDict_SetItem( tmp_dircall_arg3_1, tmp_dict_key_2, tmp_dict_value_2 );
    tmp_dict_value_3 = par_object_hook;

    tmp_dict_key_3 = const_str_plain_object_hook;
    PyDict_SetItem( tmp_dircall_arg3_1, tmp_dict_key_3, tmp_dict_value_3 );
    tmp_dict_value_4 = par_parse_float;

    tmp_dict_key_4 = const_str_plain_parse_float;
    PyDict_SetItem( tmp_dircall_arg3_1, tmp_dict_key_4, tmp_dict_value_4 );
    tmp_dict_value_5 = par_parse_int;

    tmp_dict_key_5 = const_str_plain_parse_int;
    PyDict_SetItem( tmp_dircall_arg3_1, tmp_dict_key_5, tmp_dict_value_5 );
    tmp_dict_value_6 = par_parse_constant;

    tmp_dict_key_6 = const_str_plain_parse_constant;
    PyDict_SetItem( tmp_dircall_arg3_1, tmp_dict_key_6, tmp_dict_value_6 );
    tmp_dict_value_7 = par_object_pairs_hook;

    tmp_dict_key_7 = const_str_plain_object_pairs_hook;
    PyDict_SetItem( tmp_dircall_arg3_1, tmp_dict_key_7, tmp_dict_value_7 );
    tmp_dircall_arg4_1 = par_kw;

    Py_INCREF( tmp_dircall_arg1_1 );
    Py_INCREF( tmp_dircall_arg4_1 );

    {
        PyObject *dir_call_args[] = {tmp_dircall_arg1_1, tmp_dircall_arg2_1, tmp_dircall_arg3_1, tmp_dircall_arg4_1};
        tmp_return_value = impl_function_11_complex_call_helper_pos_keywords_star_dict_of___internal__( dir_call_args );
    }
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 290;
        goto frame_exception_exit_1;
    }
    goto frame_return_exit_1;

#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    // Put the previous frame back on top.
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto frame_no_exception_1;

    frame_return_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto try_return_handler_1;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif

    {
        bool needs_detach = false;

        if ( exception_tb == NULL )
        {
            exception_tb = MAKE_TRACEBACK( frame_function, exception_lineno );
            needs_detach = true;
        }
        else if ( exception_lineno != -1 )
        {
            PyTracebackObject *traceback_new = MAKE_TRACEBACK( frame_function, exception_lineno );
            traceback_new->tb_next = exception_tb;
            exception_tb = traceback_new;

            needs_detach = true;
        }

        if (needs_detach)
        {

            tmp_frame_locals = PyDict_New();
            if ( par_fp )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_fp,
                    par_fp
                );

                assert( res == 0 );
            }

            if ( par_encoding )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_encoding,
                    par_encoding
                );

                assert( res == 0 );
            }

            if ( par_cls )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_cls,
                    par_cls
                );

                assert( res == 0 );
            }

            if ( par_object_hook )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_object_hook,
                    par_object_hook
                );

                assert( res == 0 );
            }

            if ( par_parse_float )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_parse_float,
                    par_parse_float
                );

                assert( res == 0 );
            }

            if ( par_parse_int )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_parse_int,
                    par_parse_int
                );

                assert( res == 0 );
            }

            if ( par_parse_constant )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_parse_constant,
                    par_parse_constant
                );

                assert( res == 0 );
            }

            if ( par_object_pairs_hook )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_object_pairs_hook,
                    par_object_pairs_hook
                );

                assert( res == 0 );
            }

            if ( par_kw )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_kw,
                    par_kw
                );

                assert( res == 0 );
            }



            detachFrame( exception_tb, tmp_frame_locals );
        }
    }

    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;

    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_3_load_of_json );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_fp );
    Py_DECREF( par_fp );
    par_fp = NULL;

    CHECK_OBJECT( (PyObject *)par_encoding );
    Py_DECREF( par_encoding );
    par_encoding = NULL;

    CHECK_OBJECT( (PyObject *)par_cls );
    Py_DECREF( par_cls );
    par_cls = NULL;

    CHECK_OBJECT( (PyObject *)par_object_hook );
    Py_DECREF( par_object_hook );
    par_object_hook = NULL;

    CHECK_OBJECT( (PyObject *)par_parse_float );
    Py_DECREF( par_parse_float );
    par_parse_float = NULL;

    CHECK_OBJECT( (PyObject *)par_parse_int );
    Py_DECREF( par_parse_int );
    par_parse_int = NULL;

    CHECK_OBJECT( (PyObject *)par_parse_constant );
    Py_DECREF( par_parse_constant );
    par_parse_constant = NULL;

    CHECK_OBJECT( (PyObject *)par_object_pairs_hook );
    Py_DECREF( par_object_pairs_hook );
    par_object_pairs_hook = NULL;

    CHECK_OBJECT( (PyObject *)par_kw );
    Py_DECREF( par_kw );
    par_kw = NULL;

    goto function_return_exit;
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

    CHECK_OBJECT( (PyObject *)par_fp );
    Py_DECREF( par_fp );
    par_fp = NULL;

    CHECK_OBJECT( (PyObject *)par_encoding );
    Py_DECREF( par_encoding );
    par_encoding = NULL;

    CHECK_OBJECT( (PyObject *)par_cls );
    Py_DECREF( par_cls );
    par_cls = NULL;

    CHECK_OBJECT( (PyObject *)par_object_hook );
    Py_DECREF( par_object_hook );
    par_object_hook = NULL;

    CHECK_OBJECT( (PyObject *)par_parse_float );
    Py_DECREF( par_parse_float );
    par_parse_float = NULL;

    CHECK_OBJECT( (PyObject *)par_parse_int );
    Py_DECREF( par_parse_int );
    par_parse_int = NULL;

    CHECK_OBJECT( (PyObject *)par_parse_constant );
    Py_DECREF( par_parse_constant );
    par_parse_constant = NULL;

    CHECK_OBJECT( (PyObject *)par_object_pairs_hook );
    Py_DECREF( par_object_pairs_hook );
    par_object_pairs_hook = NULL;

    CHECK_OBJECT( (PyObject *)par_kw );
    Py_DECREF( par_kw );
    par_kw = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_3_load_of_json );
    return NULL;

function_exception_exit:
    assert( exception_type );
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );

    return NULL;
    function_return_exit:

    CHECK_OBJECT( tmp_return_value );
    assert( had_error || !ERROR_OCCURRED() );
    return tmp_return_value;

}


static PyObject *impl_function_4_loads_of_json( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_s = python_pars[ 0 ];
    PyObject *par_encoding = python_pars[ 1 ];
    PyObject *par_cls = python_pars[ 2 ];
    PyObject *par_object_hook = python_pars[ 3 ];
    PyObject *par_parse_float = python_pars[ 4 ];
    PyObject *par_parse_int = python_pars[ 5 ];
    PyObject *par_parse_constant = python_pars[ 6 ];
    PyObject *par_object_pairs_hook = python_pars[ 7 ];
    PyObject *par_kw = python_pars[ 8 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    int tmp_and_left_truth_1;
    int tmp_and_left_truth_2;
    int tmp_and_left_truth_3;
    int tmp_and_left_truth_4;
    int tmp_and_left_truth_5;
    int tmp_and_left_truth_6;
    int tmp_and_left_truth_7;
    PyObject *tmp_and_left_value_1;
    PyObject *tmp_and_left_value_2;
    PyObject *tmp_and_left_value_3;
    PyObject *tmp_and_left_value_4;
    PyObject *tmp_and_left_value_5;
    PyObject *tmp_and_left_value_6;
    PyObject *tmp_and_left_value_7;
    PyObject *tmp_and_right_value_1;
    PyObject *tmp_and_right_value_2;
    PyObject *tmp_and_right_value_3;
    PyObject *tmp_and_right_value_4;
    PyObject *tmp_and_right_value_5;
    PyObject *tmp_and_right_value_6;
    PyObject *tmp_and_right_value_7;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_args_element_name_2;
    PyObject *tmp_ass_subscribed_1;
    PyObject *tmp_ass_subscribed_2;
    PyObject *tmp_ass_subscribed_3;
    PyObject *tmp_ass_subscribed_4;
    PyObject *tmp_ass_subscribed_5;
    PyObject *tmp_ass_subscript_1;
    PyObject *tmp_ass_subscript_2;
    PyObject *tmp_ass_subscript_3;
    PyObject *tmp_ass_subscript_4;
    PyObject *tmp_ass_subscript_5;
    PyObject *tmp_ass_subvalue_1;
    PyObject *tmp_ass_subvalue_2;
    PyObject *tmp_ass_subvalue_3;
    PyObject *tmp_ass_subvalue_4;
    PyObject *tmp_ass_subvalue_5;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_left_2;
    PyObject *tmp_compare_left_3;
    PyObject *tmp_compare_left_4;
    PyObject *tmp_compare_left_5;
    PyObject *tmp_compare_left_6;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_compare_right_2;
    PyObject *tmp_compare_right_3;
    PyObject *tmp_compare_right_4;
    PyObject *tmp_compare_right_5;
    PyObject *tmp_compare_right_6;
    PyObject *tmp_compexpr_left_1;
    PyObject *tmp_compexpr_left_2;
    PyObject *tmp_compexpr_left_3;
    PyObject *tmp_compexpr_left_4;
    PyObject *tmp_compexpr_left_5;
    PyObject *tmp_compexpr_left_6;
    PyObject *tmp_compexpr_left_7;
    PyObject *tmp_compexpr_right_1;
    PyObject *tmp_compexpr_right_2;
    PyObject *tmp_compexpr_right_3;
    PyObject *tmp_compexpr_right_4;
    PyObject *tmp_compexpr_right_5;
    PyObject *tmp_compexpr_right_6;
    PyObject *tmp_compexpr_right_7;
    int tmp_cond_truth_1;
    PyObject *tmp_cond_value_1;
    PyObject *tmp_dict_key_1;
    PyObject *tmp_dict_value_1;
    PyObject *tmp_dircall_arg1_1;
    PyObject *tmp_dircall_arg2_1;
    PyObject *tmp_dircall_arg3_1;
    PyObject *tmp_frame_locals;
    bool tmp_is_1;
    bool tmp_isnot_1;
    bool tmp_isnot_2;
    bool tmp_isnot_3;
    bool tmp_isnot_4;
    bool tmp_isnot_5;
    PyObject *tmp_operand_name_1;
    bool tmp_result;
    PyObject *tmp_return_value;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_2341cd23c9e319db0ab6441980201c94, module_json );
    frame_function = cache_frame_function;

    // Push the new frame as the currently active one.
    pushFrameStack( frame_function );

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    Py_INCREF( frame_function );
    assert( Py_REFCNT( frame_function ) == 2 ); // Frame stack

#if PYTHON_VERSION >= 340
    frame_function->f_executing += 1;
#endif

    // Framed code:
    tmp_compexpr_left_1 = par_cls;

    tmp_compexpr_right_1 = Py_None;
    tmp_and_left_value_1 = BOOL_FROM( tmp_compexpr_left_1 == tmp_compexpr_right_1 );
    tmp_and_left_truth_1 = CHECK_IF_TRUE( tmp_and_left_value_1 );
    assert( !(tmp_and_left_truth_1 == -1) );
    if ( tmp_and_left_truth_1 == 1 )
    {
        goto and_right_1;
    }
    else
    {
        goto and_left_1;
    }
    and_right_1:;
    tmp_compexpr_left_2 = par_encoding;

    tmp_compexpr_right_2 = Py_None;
    tmp_and_left_value_2 = BOOL_FROM( tmp_compexpr_left_2 == tmp_compexpr_right_2 );
    tmp_and_left_truth_2 = CHECK_IF_TRUE( tmp_and_left_value_2 );
    assert( !(tmp_and_left_truth_2 == -1) );
    if ( tmp_and_left_truth_2 == 1 )
    {
        goto and_right_2;
    }
    else
    {
        goto and_left_2;
    }
    and_right_2:;
    tmp_compexpr_left_3 = par_object_hook;

    tmp_compexpr_right_3 = Py_None;
    tmp_and_left_value_3 = BOOL_FROM( tmp_compexpr_left_3 == tmp_compexpr_right_3 );
    tmp_and_left_truth_3 = CHECK_IF_TRUE( tmp_and_left_value_3 );
    assert( !(tmp_and_left_truth_3 == -1) );
    if ( tmp_and_left_truth_3 == 1 )
    {
        goto and_right_3;
    }
    else
    {
        goto and_left_3;
    }
    and_right_3:;
    tmp_compexpr_left_4 = par_parse_int;

    tmp_compexpr_right_4 = Py_None;
    tmp_and_left_value_4 = BOOL_FROM( tmp_compexpr_left_4 == tmp_compexpr_right_4 );
    tmp_and_left_truth_4 = CHECK_IF_TRUE( tmp_and_left_value_4 );
    assert( !(tmp_and_left_truth_4 == -1) );
    if ( tmp_and_left_truth_4 == 1 )
    {
        goto and_right_4;
    }
    else
    {
        goto and_left_4;
    }
    and_right_4:;
    tmp_compexpr_left_5 = par_parse_float;

    tmp_compexpr_right_5 = Py_None;
    tmp_and_left_value_5 = BOOL_FROM( tmp_compexpr_left_5 == tmp_compexpr_right_5 );
    tmp_and_left_truth_5 = CHECK_IF_TRUE( tmp_and_left_value_5 );
    assert( !(tmp_and_left_truth_5 == -1) );
    if ( tmp_and_left_truth_5 == 1 )
    {
        goto and_right_5;
    }
    else
    {
        goto and_left_5;
    }
    and_right_5:;
    tmp_compexpr_left_6 = par_parse_constant;

    tmp_compexpr_right_6 = Py_None;
    tmp_and_left_value_6 = BOOL_FROM( tmp_compexpr_left_6 == tmp_compexpr_right_6 );
    tmp_and_left_truth_6 = CHECK_IF_TRUE( tmp_and_left_value_6 );
    assert( !(tmp_and_left_truth_6 == -1) );
    if ( tmp_and_left_truth_6 == 1 )
    {
        goto and_right_6;
    }
    else
    {
        goto and_left_6;
    }
    and_right_6:;
    tmp_compexpr_left_7 = par_object_pairs_hook;

    tmp_compexpr_right_7 = Py_None;
    tmp_and_left_value_7 = BOOL_FROM( tmp_compexpr_left_7 == tmp_compexpr_right_7 );
    tmp_and_left_truth_7 = CHECK_IF_TRUE( tmp_and_left_value_7 );
    assert( !(tmp_and_left_truth_7 == -1) );
    if ( tmp_and_left_truth_7 == 1 )
    {
        goto and_right_7;
    }
    else
    {
        goto and_left_7;
    }
    and_right_7:;
    tmp_operand_name_1 = par_kw;

    tmp_and_right_value_7 = UNARY_OPERATION( UNARY_NOT, tmp_operand_name_1 );
    if ( tmp_and_right_value_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 337;
        goto frame_exception_exit_1;
    }
    tmp_and_right_value_6 = tmp_and_right_value_7;
    goto and_end_7;
    and_left_7:;
    tmp_and_right_value_6 = tmp_and_left_value_7;
    and_end_7:;
    tmp_and_right_value_5 = tmp_and_right_value_6;
    goto and_end_6;
    and_left_6:;
    tmp_and_right_value_5 = tmp_and_left_value_6;
    and_end_6:;
    tmp_and_right_value_4 = tmp_and_right_value_5;
    goto and_end_5;
    and_left_5:;
    tmp_and_right_value_4 = tmp_and_left_value_5;
    and_end_5:;
    tmp_and_right_value_3 = tmp_and_right_value_4;
    goto and_end_4;
    and_left_4:;
    tmp_and_right_value_3 = tmp_and_left_value_4;
    and_end_4:;
    tmp_and_right_value_2 = tmp_and_right_value_3;
    goto and_end_3;
    and_left_3:;
    tmp_and_right_value_2 = tmp_and_left_value_3;
    and_end_3:;
    tmp_and_right_value_1 = tmp_and_right_value_2;
    goto and_end_2;
    and_left_2:;
    tmp_and_right_value_1 = tmp_and_left_value_2;
    and_end_2:;
    tmp_cond_value_1 = tmp_and_right_value_1;
    goto and_end_1;
    and_left_1:;
    tmp_cond_value_1 = tmp_and_left_value_1;
    and_end_1:;
    tmp_cond_truth_1 = CHECK_IF_TRUE( tmp_cond_value_1 );
    if ( tmp_cond_truth_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 337;
        goto frame_exception_exit_1;
    }
    if ( tmp_cond_truth_1 == 1 )
    {
        goto branch_yes_1;
    }
    else
    {
        goto branch_no_1;
    }
    branch_yes_1:;
    tmp_source_name_1 = GET_STRING_DICT_VALUE( moduledict_json, (Nuitka_StringObject *)const_str_plain__default_decoder );

    if (unlikely( tmp_source_name_1 == NULL ))
    {
        tmp_source_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain__default_decoder );
    }

    if ( tmp_source_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "_default_decoder" );
        exception_tb = NULL;

        exception_lineno = 338;
        goto frame_exception_exit_1;
    }

    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_decode );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 338;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_1 = par_s;

    frame_function->f_lineno = 338;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_return_value = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    Py_DECREF( tmp_called_name_1 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 338;
        goto frame_exception_exit_1;
    }
    goto frame_return_exit_1;
    branch_no_1:;
    tmp_compare_left_1 = par_cls;

    tmp_compare_right_1 = Py_None;
    tmp_is_1 = ( tmp_compare_left_1 == tmp_compare_right_1 );
    if ( tmp_is_1 )
    {
        goto branch_yes_2;
    }
    else
    {
        goto branch_no_2;
    }
    branch_yes_2:;
    tmp_assign_source_1 = GET_STRING_DICT_VALUE( moduledict_json, (Nuitka_StringObject *)const_str_plain_JSONDecoder );

    if (unlikely( tmp_assign_source_1 == NULL ))
    {
        tmp_assign_source_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_JSONDecoder );
    }

    if ( tmp_assign_source_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "JSONDecoder" );
        exception_tb = NULL;

        exception_lineno = 340;
        goto frame_exception_exit_1;
    }

    {
        PyObject *old = par_cls;
        assert( old != NULL );
        par_cls = tmp_assign_source_1;
        Py_INCREF( par_cls );
        Py_DECREF( old );
    }

    branch_no_2:;
    tmp_compare_left_2 = par_object_hook;

    tmp_compare_right_2 = Py_None;
    tmp_isnot_1 = ( tmp_compare_left_2 != tmp_compare_right_2 );
    if ( tmp_isnot_1 )
    {
        goto branch_yes_3;
    }
    else
    {
        goto branch_no_3;
    }
    branch_yes_3:;
    tmp_ass_subvalue_1 = par_object_hook;

    tmp_ass_subscribed_1 = par_kw;

    tmp_ass_subscript_1 = const_str_plain_object_hook;
    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_1, tmp_ass_subscript_1, tmp_ass_subvalue_1 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 342;
        goto frame_exception_exit_1;
    }
    branch_no_3:;
    tmp_compare_left_3 = par_object_pairs_hook;

    tmp_compare_right_3 = Py_None;
    tmp_isnot_2 = ( tmp_compare_left_3 != tmp_compare_right_3 );
    if ( tmp_isnot_2 )
    {
        goto branch_yes_4;
    }
    else
    {
        goto branch_no_4;
    }
    branch_yes_4:;
    tmp_ass_subvalue_2 = par_object_pairs_hook;

    tmp_ass_subscribed_2 = par_kw;

    tmp_ass_subscript_2 = const_str_plain_object_pairs_hook;
    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_2, tmp_ass_subscript_2, tmp_ass_subvalue_2 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 344;
        goto frame_exception_exit_1;
    }
    branch_no_4:;
    tmp_compare_left_4 = par_parse_float;

    tmp_compare_right_4 = Py_None;
    tmp_isnot_3 = ( tmp_compare_left_4 != tmp_compare_right_4 );
    if ( tmp_isnot_3 )
    {
        goto branch_yes_5;
    }
    else
    {
        goto branch_no_5;
    }
    branch_yes_5:;
    tmp_ass_subvalue_3 = par_parse_float;

    tmp_ass_subscribed_3 = par_kw;

    tmp_ass_subscript_3 = const_str_plain_parse_float;
    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_3, tmp_ass_subscript_3, tmp_ass_subvalue_3 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 346;
        goto frame_exception_exit_1;
    }
    branch_no_5:;
    tmp_compare_left_5 = par_parse_int;

    tmp_compare_right_5 = Py_None;
    tmp_isnot_4 = ( tmp_compare_left_5 != tmp_compare_right_5 );
    if ( tmp_isnot_4 )
    {
        goto branch_yes_6;
    }
    else
    {
        goto branch_no_6;
    }
    branch_yes_6:;
    tmp_ass_subvalue_4 = par_parse_int;

    tmp_ass_subscribed_4 = par_kw;

    tmp_ass_subscript_4 = const_str_plain_parse_int;
    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_4, tmp_ass_subscript_4, tmp_ass_subvalue_4 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 348;
        goto frame_exception_exit_1;
    }
    branch_no_6:;
    tmp_compare_left_6 = par_parse_constant;

    tmp_compare_right_6 = Py_None;
    tmp_isnot_5 = ( tmp_compare_left_6 != tmp_compare_right_6 );
    if ( tmp_isnot_5 )
    {
        goto branch_yes_7;
    }
    else
    {
        goto branch_no_7;
    }
    branch_yes_7:;
    tmp_ass_subvalue_5 = par_parse_constant;

    tmp_ass_subscribed_5 = par_kw;

    tmp_ass_subscript_5 = const_str_plain_parse_constant;
    tmp_result = SET_SUBSCRIPT( tmp_ass_subscribed_5, tmp_ass_subscript_5, tmp_ass_subvalue_5 );
    if ( tmp_result == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 350;
        goto frame_exception_exit_1;
    }
    branch_no_7:;
    tmp_dircall_arg1_1 = par_cls;

    tmp_dircall_arg2_1 = _PyDict_NewPresized( 1 );
    tmp_dict_value_1 = par_encoding;

    tmp_dict_key_1 = const_str_plain_encoding;
    PyDict_SetItem( tmp_dircall_arg2_1, tmp_dict_key_1, tmp_dict_value_1 );
    tmp_dircall_arg3_1 = par_kw;

    Py_INCREF( tmp_dircall_arg1_1 );
    Py_INCREF( tmp_dircall_arg3_1 );

    {
        PyObject *dir_call_args[] = {tmp_dircall_arg1_1, tmp_dircall_arg2_1, tmp_dircall_arg3_1};
        tmp_source_name_2 = impl_function_9_complex_call_helper_keywords_star_dict_of___internal__( dir_call_args );
    }
    if ( tmp_source_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 351;
        goto frame_exception_exit_1;
    }
    tmp_called_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_decode );
    Py_DECREF( tmp_source_name_2 );
    if ( tmp_called_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 351;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_2 = par_s;

    frame_function->f_lineno = 351;
    {
        PyObject *call_args[] = { tmp_args_element_name_2 };
        tmp_return_value = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_2, call_args );
    }

    Py_DECREF( tmp_called_name_2 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 351;
        goto frame_exception_exit_1;
    }
    goto frame_return_exit_1;

#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    // Put the previous frame back on top.
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto frame_no_exception_1;

    frame_return_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto try_return_handler_1;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif

    {
        bool needs_detach = false;

        if ( exception_tb == NULL )
        {
            exception_tb = MAKE_TRACEBACK( frame_function, exception_lineno );
            needs_detach = true;
        }
        else if ( exception_lineno != -1 )
        {
            PyTracebackObject *traceback_new = MAKE_TRACEBACK( frame_function, exception_lineno );
            traceback_new->tb_next = exception_tb;
            exception_tb = traceback_new;

            needs_detach = true;
        }

        if (needs_detach)
        {

            tmp_frame_locals = PyDict_New();
            if ( par_s )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_s,
                    par_s
                );

                assert( res == 0 );
            }

            if ( par_encoding )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_encoding,
                    par_encoding
                );

                assert( res == 0 );
            }

            if ( par_cls )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_cls,
                    par_cls
                );

                assert( res == 0 );
            }

            if ( par_object_hook )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_object_hook,
                    par_object_hook
                );

                assert( res == 0 );
            }

            if ( par_parse_float )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_parse_float,
                    par_parse_float
                );

                assert( res == 0 );
            }

            if ( par_parse_int )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_parse_int,
                    par_parse_int
                );

                assert( res == 0 );
            }

            if ( par_parse_constant )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_parse_constant,
                    par_parse_constant
                );

                assert( res == 0 );
            }

            if ( par_object_pairs_hook )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_object_pairs_hook,
                    par_object_pairs_hook
                );

                assert( res == 0 );
            }

            if ( par_kw )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_kw,
                    par_kw
                );

                assert( res == 0 );
            }



            detachFrame( exception_tb, tmp_frame_locals );
        }
    }

    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;

    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_4_loads_of_json );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_s );
    Py_DECREF( par_s );
    par_s = NULL;

    CHECK_OBJECT( (PyObject *)par_encoding );
    Py_DECREF( par_encoding );
    par_encoding = NULL;

    Py_XDECREF( par_cls );
    par_cls = NULL;

    CHECK_OBJECT( (PyObject *)par_object_hook );
    Py_DECREF( par_object_hook );
    par_object_hook = NULL;

    CHECK_OBJECT( (PyObject *)par_parse_float );
    Py_DECREF( par_parse_float );
    par_parse_float = NULL;

    CHECK_OBJECT( (PyObject *)par_parse_int );
    Py_DECREF( par_parse_int );
    par_parse_int = NULL;

    CHECK_OBJECT( (PyObject *)par_parse_constant );
    Py_DECREF( par_parse_constant );
    par_parse_constant = NULL;

    CHECK_OBJECT( (PyObject *)par_object_pairs_hook );
    Py_DECREF( par_object_pairs_hook );
    par_object_pairs_hook = NULL;

    CHECK_OBJECT( (PyObject *)par_kw );
    Py_DECREF( par_kw );
    par_kw = NULL;

    goto function_return_exit;
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

    CHECK_OBJECT( (PyObject *)par_s );
    Py_DECREF( par_s );
    par_s = NULL;

    CHECK_OBJECT( (PyObject *)par_encoding );
    Py_DECREF( par_encoding );
    par_encoding = NULL;

    Py_XDECREF( par_cls );
    par_cls = NULL;

    CHECK_OBJECT( (PyObject *)par_object_hook );
    Py_DECREF( par_object_hook );
    par_object_hook = NULL;

    CHECK_OBJECT( (PyObject *)par_parse_float );
    Py_DECREF( par_parse_float );
    par_parse_float = NULL;

    CHECK_OBJECT( (PyObject *)par_parse_int );
    Py_DECREF( par_parse_int );
    par_parse_int = NULL;

    CHECK_OBJECT( (PyObject *)par_parse_constant );
    Py_DECREF( par_parse_constant );
    par_parse_constant = NULL;

    CHECK_OBJECT( (PyObject *)par_object_pairs_hook );
    Py_DECREF( par_object_pairs_hook );
    par_object_pairs_hook = NULL;

    CHECK_OBJECT( (PyObject *)par_kw );
    Py_DECREF( par_kw );
    par_kw = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_4_loads_of_json );
    return NULL;

function_exception_exit:
    assert( exception_type );
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );

    return NULL;
    function_return_exit:

    CHECK_OBJECT( tmp_return_value );
    assert( had_error || !ERROR_OCCURRED() );
    return tmp_return_value;

}



static PyObject *MAKE_FUNCTION_function_1_dump_of_json( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_1_dump_of_json,
        const_str_plain_dump,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_f4b82912b430e4f95cdab9d7bfa5d5a0,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_json,
        const_str_digest_599555fb243d72d0e4ff1c872e536554
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_2_dumps_of_json( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_2_dumps_of_json,
        const_str_plain_dumps,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_302192d0398477b76c1ba9f6dfe0ff65,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_json,
        const_str_digest_01cc92d89a14824bb4a6c88c061a6627
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_3_load_of_json( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_3_load_of_json,
        const_str_plain_load,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_735324f70dba261090f9d2f5690acb6e,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_json,
        const_str_digest_04be16761a7196498ae170f991a729f0
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_4_loads_of_json( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_4_loads_of_json,
        const_str_plain_loads,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_2341cd23c9e319db0ab6441980201c94,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_json,
        const_str_digest_ca0af13e597c29ab9da2136cfc95efe2
    );

    return result;
}



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_json =
{
    PyModuleDef_HEAD_INIT,
    "json",   /* m_name */
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

MOD_INIT_DECL( json )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_json );
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

    // puts( "in initjson" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_json = Py_InitModule4(
        "json",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_json = PyModule_Create( &mdef_json );
#endif

    moduledict_json = (PyDictObject *)((PyModuleObject *)module_json)->md_dict;

    CHECK_OBJECT( module_json );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_plain_json, module_json );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_json );

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
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_called_name_3;
    PyObject *tmp_defaults_1;
    PyObject *tmp_defaults_2;
    PyObject *tmp_defaults_3;
    PyObject *tmp_defaults_4;
    PyObject *tmp_import_globals_1;
    PyObject *tmp_import_globals_2;
    PyObject *tmp_import_name_from_1;
    PyObject *tmp_import_name_from_2;
    PyObject *tmp_kw_name_1;
    PyObject *tmp_kw_name_2;
    PyObject *tmp_list_element_1;
    PyObject *tmp_source_name_1;
    PyFrameObject *frame_module;


    // Module code.
    tmp_assign_source_1 = const_str_digest_ed013416b9a126b331b47fab35fa159c;
    UPDATE_STRING_DICT0( moduledict_json, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_json, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    // Frame without reuse.
    frame_module = MAKE_MODULE_FRAME( codeobj_3c62dcc14467fb105363c695850fa8e4, module_json );

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
    UPDATE_STRING_DICT1( moduledict_json, (Nuitka_StringObject *)const_str_plain___path__, tmp_assign_source_3 );
    tmp_assign_source_4 = const_str_digest_cc54928f376395365d5feab06837d749;
    UPDATE_STRING_DICT0( moduledict_json, (Nuitka_StringObject *)const_str_plain___version__, tmp_assign_source_4 );
    tmp_assign_source_5 = LIST_COPY( const_list_6cd5adbff82562af8bdb9be2ac48d46e_list );
    UPDATE_STRING_DICT1( moduledict_json, (Nuitka_StringObject *)const_str_plain___all__, tmp_assign_source_5 );
    tmp_assign_source_6 = const_str_digest_29128799e6868180fe0bd02edfedaa2d;
    UPDATE_STRING_DICT0( moduledict_json, (Nuitka_StringObject *)const_str_plain___author__, tmp_assign_source_6 );
    tmp_import_globals_1 = ((PyModuleObject *)module_json)->md_dict;
    frame_module->f_lineno = 108;
    tmp_import_name_from_1 = IMPORT_MODULE( const_str_plain_decoder, tmp_import_globals_1, tmp_import_globals_1, const_tuple_str_plain_JSONDecoder_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 108;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_7 = IMPORT_NAME( tmp_import_name_from_1, const_str_plain_JSONDecoder );
    Py_DECREF( tmp_import_name_from_1 );
    if ( tmp_assign_source_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 108;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_json, (Nuitka_StringObject *)const_str_plain_JSONDecoder, tmp_assign_source_7 );
    tmp_import_globals_2 = ((PyModuleObject *)module_json)->md_dict;
    frame_module->f_lineno = 109;
    tmp_import_name_from_2 = IMPORT_MODULE( const_str_plain_encoder, tmp_import_globals_2, tmp_import_globals_2, const_tuple_str_plain_JSONEncoder_tuple, const_int_pos_1 );
    if ( tmp_import_name_from_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 109;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_8 = IMPORT_NAME( tmp_import_name_from_2, const_str_plain_JSONEncoder );
    Py_DECREF( tmp_import_name_from_2 );
    if ( tmp_assign_source_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 109;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_json, (Nuitka_StringObject *)const_str_plain_JSONEncoder, tmp_assign_source_8 );
    tmp_called_name_2 = GET_STRING_DICT_VALUE( moduledict_json, (Nuitka_StringObject *)const_str_plain_JSONEncoder );

    if (unlikely( tmp_called_name_2 == NULL ))
    {
        tmp_called_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_JSONEncoder );
    }

    if ( tmp_called_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "JSONEncoder" );
        exception_tb = NULL;

        exception_lineno = 111;
        goto frame_exception_exit_1;
    }

    tmp_kw_name_1 = PyDict_Copy( const_dict_cf20e1096400ee55a5aafd036f22d909 );
    frame_module->f_lineno = 119;
    tmp_assign_source_9 = CALL_FUNCTION_WITH_KEYARGS( tmp_called_name_2, tmp_kw_name_1 );
    Py_DECREF( tmp_kw_name_1 );
    if ( tmp_assign_source_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 119;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_json, (Nuitka_StringObject *)const_str_plain__default_encoder, tmp_assign_source_9 );
    tmp_defaults_1 = const_tuple_b82128f02299582589bd5ccc8bee006e_tuple;
    tmp_assign_source_10 = MAKE_FUNCTION_function_1_dump_of_json( INCREASE_REFCOUNT( tmp_defaults_1 ) );
    UPDATE_STRING_DICT1( moduledict_json, (Nuitka_StringObject *)const_str_plain_dump, tmp_assign_source_10 );
    tmp_defaults_2 = const_tuple_b82128f02299582589bd5ccc8bee006e_tuple;
    tmp_assign_source_11 = MAKE_FUNCTION_function_2_dumps_of_json( INCREASE_REFCOUNT( tmp_defaults_2 ) );
    UPDATE_STRING_DICT1( moduledict_json, (Nuitka_StringObject *)const_str_plain_dumps, tmp_assign_source_11 );
    tmp_called_name_3 = GET_STRING_DICT_VALUE( moduledict_json, (Nuitka_StringObject *)const_str_plain_JSONDecoder );

    if (unlikely( tmp_called_name_3 == NULL ))
    {
        tmp_called_name_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_JSONDecoder );
    }

    if ( tmp_called_name_3 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "JSONDecoder" );
        exception_tb = NULL;

        exception_lineno = 253;
        goto frame_exception_exit_1;
    }

    tmp_kw_name_2 = PyDict_Copy( const_dict_ff68e34582c54715c2cc14151b7335ab );
    frame_module->f_lineno = 254;
    tmp_assign_source_12 = CALL_FUNCTION_WITH_KEYARGS( tmp_called_name_3, tmp_kw_name_2 );
    Py_DECREF( tmp_kw_name_2 );
    if ( tmp_assign_source_12 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 254;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_json, (Nuitka_StringObject *)const_str_plain__default_decoder, tmp_assign_source_12 );

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
    tmp_defaults_3 = const_tuple_none_none_none_none_none_none_none_tuple;
    tmp_assign_source_13 = MAKE_FUNCTION_function_3_load_of_json( INCREASE_REFCOUNT( tmp_defaults_3 ) );
    UPDATE_STRING_DICT1( moduledict_json, (Nuitka_StringObject *)const_str_plain_load, tmp_assign_source_13 );
    tmp_defaults_4 = const_tuple_none_none_none_none_none_none_none_tuple;
    tmp_assign_source_14 = MAKE_FUNCTION_function_4_loads_of_json( INCREASE_REFCOUNT( tmp_defaults_4 ) );
    UPDATE_STRING_DICT1( moduledict_json, (Nuitka_StringObject *)const_str_plain_loads, tmp_assign_source_14 );

    return MOD_RETURN_VALUE( module_json );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
