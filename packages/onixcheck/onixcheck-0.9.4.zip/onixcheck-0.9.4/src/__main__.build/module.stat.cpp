/* Generated code for Python source for module 'stat'
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

/* The _module_stat is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_stat;
PyDictObject *moduledict_stat;

/* The module constants used, if any. */
static PyObject *const_str_plain_ST_ATIME;
extern PyObject *const_str_plain_S_ISLNK;
static PyObject *const_str_digest_79e34f0bc27f300d84435cb68c532bb3;
extern PyObject *const_int_pos_512;
extern PyObject *const_str_plain_S_IFREG;
static PyObject *const_str_plain_S_IRWXG;
extern PyObject *const_dict_empty;
static PyObject *const_str_plain_S_IRWXU;
extern PyObject *const_int_pos_49152;
extern PyObject *const_tuple_empty;
static PyObject *const_str_plain_S_IEXEC;
extern PyObject *const_int_pos_448;
static PyObject *const_str_plain_UF_APPEND;
extern PyObject *const_str_plain_S_IRGRP;
extern PyObject *const_int_pos_24576;
extern PyObject *const_str_plain_S_ISFIFO;
static PyObject *const_str_plain_UF_HIDDEN;
extern PyObject *const_int_pos_8192;
static PyObject *const_str_plain_S_ENFMT;
static PyObject *const_str_plain_SF_SNAPSHOT;
static PyObject *const_str_plain_UF_OPAQUE;
static PyObject *const_str_plain_ST_MODE;
static PyObject *const_str_plain_SF_ARCHIVED;
extern PyObject *const_int_pos_64;
extern PyObject *const_int_pos_128;
static PyObject *const_str_plain_SF_APPEND;
extern PyObject *const_str_plain_ST_INO;
static PyObject *const_str_plain_S_ISUID;
static PyObject *const_str_plain_ST_UID;
static PyObject *const_str_plain_SF_NOUNLINK;
static PyObject *const_str_plain_SF_IMMUTABLE;
extern PyObject *const_int_pos_16;
extern PyObject *const_str_plain_S_IMODE;
static PyObject *const_str_plain_S_IRWXO;
extern PyObject *const_int_pos_4096;
extern PyObject *const_str_plain_S_ISBLK;
extern PyObject *const_int_pos_4095;
extern PyObject *const_str_plain___file__;
static PyObject *const_str_plain_S_IFSOCK;
extern PyObject *const_int_pos_1048576;
extern PyObject *const_int_pos_6;
extern PyObject *const_int_pos_7;
extern PyObject *const_int_pos_4;
extern PyObject *const_int_pos_5;
extern PyObject *const_int_pos_2;
extern PyObject *const_int_pos_40960;
extern PyObject *const_int_pos_2097152;
extern PyObject *const_int_pos_1;
extern PyObject *const_int_pos_8;
extern PyObject *const_int_pos_9;
extern PyObject *const_int_pos_3;
extern PyObject *const_int_pos_1024;
extern PyObject *const_int_pos_2048;
extern PyObject *const_str_plain_S_IRUSR;
static PyObject *const_str_plain_S_ISSOCK;
extern PyObject *const_str_plain_mode;
static PyObject *const_str_plain_ST_NLINK;
extern PyObject *const_str_plain_S_IWUSR;
static PyObject *const_str_plain_UF_COMPRESSED;
extern PyObject *const_int_pos_256;
extern PyObject *const_int_pos_61440;
extern PyObject *const_str_plain_S_IWOTH;
extern PyObject *const_int_pos_32768;
extern PyObject *const_str_plain_S_IROTH;
extern PyObject *const_int_pos_262144;
extern PyObject *const_str_plain_S_IWGRP;
extern PyObject *const_int_pos_32;
static PyObject *const_str_plain_ST_CTIME;
extern PyObject *const_str_plain_stat;
static PyObject *const_str_plain_ST_SIZE;
static PyObject *const_str_plain_S_IFMT;
extern PyObject *const_str_plain_S_IFIFO;
static PyObject *const_str_digest_01b02879d1918d1e66ac4015cec6e093;
static PyObject *const_str_plain_S_IREAD;
extern PyObject *const_str_plain_ST_DEV;
extern PyObject *const_int_pos_16384;
extern PyObject *const_str_plain_S_ISREG;
extern PyObject *const_str_plain_ST_MTIME;
extern PyObject *const_str_plain_S_IFLNK;
static PyObject *const_tuple_str_plain_mode_tuple;
extern PyObject *const_str_plain_S_ISDIR;
static PyObject *const_str_plain_ST_GID;
static PyObject *const_str_plain_UF_NOUNLINK;
static PyObject *const_str_plain_S_IXUSR;
static PyObject *const_str_plain_S_IXGRP;
extern PyObject *const_str_plain_S_IFCHR;
extern PyObject *const_str_plain_S_IFBLK;
extern PyObject *const_int_pos_56;
extern PyObject *const_str_plain_S_IFDIR;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_int_0;
static PyObject *const_str_plain_UF_NODUMP;
extern PyObject *const_str_plain_S_ISCHR;
extern PyObject *const_int_pos_131072;
extern PyObject *const_int_pos_65536;
static PyObject *const_str_plain_S_IXOTH;
static PyObject *const_str_plain_S_IWRITE;
static PyObject *const_str_plain_S_ISGID;
static PyObject *const_str_plain_UF_IMMUTABLE;
static PyObject *const_str_plain_S_ISVTX;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_plain_ST_ATIME = UNSTREAM_STRING( &constant_bin[ 872838 ], 8, 1 );
    const_str_digest_79e34f0bc27f300d84435cb68c532bb3 = UNSTREAM_STRING( &constant_bin[ 872846 ], 7, 0 );
    const_str_plain_S_IRWXG = UNSTREAM_STRING( &constant_bin[ 872853 ], 7, 1 );
    const_str_plain_S_IRWXU = UNSTREAM_STRING( &constant_bin[ 872860 ], 7, 1 );
    const_str_plain_S_IEXEC = UNSTREAM_STRING( &constant_bin[ 872867 ], 7, 1 );
    const_str_plain_UF_APPEND = UNSTREAM_STRING( &constant_bin[ 872874 ], 9, 1 );
    const_str_plain_UF_HIDDEN = UNSTREAM_STRING( &constant_bin[ 872883 ], 9, 1 );
    const_str_plain_S_ENFMT = UNSTREAM_STRING( &constant_bin[ 872892 ], 7, 1 );
    const_str_plain_SF_SNAPSHOT = UNSTREAM_STRING( &constant_bin[ 872899 ], 11, 1 );
    const_str_plain_UF_OPAQUE = UNSTREAM_STRING( &constant_bin[ 872910 ], 9, 1 );
    const_str_plain_ST_MODE = UNSTREAM_STRING( &constant_bin[ 872919 ], 7, 1 );
    const_str_plain_SF_ARCHIVED = UNSTREAM_STRING( &constant_bin[ 872926 ], 11, 1 );
    const_str_plain_SF_APPEND = UNSTREAM_STRING( &constant_bin[ 872937 ], 9, 1 );
    const_str_plain_S_ISUID = UNSTREAM_STRING( &constant_bin[ 872946 ], 7, 1 );
    const_str_plain_ST_UID = UNSTREAM_STRING( &constant_bin[ 872953 ], 6, 1 );
    const_str_plain_SF_NOUNLINK = UNSTREAM_STRING( &constant_bin[ 872959 ], 11, 1 );
    const_str_plain_SF_IMMUTABLE = UNSTREAM_STRING( &constant_bin[ 872970 ], 12, 1 );
    const_str_plain_S_IRWXO = UNSTREAM_STRING( &constant_bin[ 872982 ], 7, 1 );
    const_str_plain_S_IFSOCK = UNSTREAM_STRING( &constant_bin[ 872989 ], 8, 1 );
    const_str_plain_S_ISSOCK = UNSTREAM_STRING( &constant_bin[ 872997 ], 8, 1 );
    const_str_plain_ST_NLINK = UNSTREAM_STRING( &constant_bin[ 873005 ], 8, 1 );
    const_str_plain_UF_COMPRESSED = UNSTREAM_STRING( &constant_bin[ 873013 ], 13, 1 );
    const_str_plain_ST_CTIME = UNSTREAM_STRING( &constant_bin[ 873026 ], 8, 1 );
    const_str_plain_ST_SIZE = UNSTREAM_STRING( &constant_bin[ 873034 ], 7, 1 );
    const_str_plain_S_IFMT = UNSTREAM_STRING( &constant_bin[ 873041 ], 6, 1 );
    const_str_digest_01b02879d1918d1e66ac4015cec6e093 = UNSTREAM_STRING( &constant_bin[ 873047 ], 111, 0 );
    const_str_plain_S_IREAD = UNSTREAM_STRING( &constant_bin[ 873158 ], 7, 1 );
    const_tuple_str_plain_mode_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_mode_tuple, 0, const_str_plain_mode ); Py_INCREF( const_str_plain_mode );
    const_str_plain_ST_GID = UNSTREAM_STRING( &constant_bin[ 873165 ], 6, 1 );
    const_str_plain_UF_NOUNLINK = UNSTREAM_STRING( &constant_bin[ 873171 ], 11, 1 );
    const_str_plain_S_IXUSR = UNSTREAM_STRING( &constant_bin[ 873182 ], 7, 1 );
    const_str_plain_S_IXGRP = UNSTREAM_STRING( &constant_bin[ 873189 ], 7, 1 );
    const_str_plain_UF_NODUMP = UNSTREAM_STRING( &constant_bin[ 873196 ], 9, 1 );
    const_str_plain_S_IXOTH = UNSTREAM_STRING( &constant_bin[ 873205 ], 7, 1 );
    const_str_plain_S_IWRITE = UNSTREAM_STRING( &constant_bin[ 873212 ], 8, 1 );
    const_str_plain_S_ISGID = UNSTREAM_STRING( &constant_bin[ 873220 ], 7, 1 );
    const_str_plain_UF_IMMUTABLE = UNSTREAM_STRING( &constant_bin[ 873227 ], 12, 1 );
    const_str_plain_S_ISVTX = UNSTREAM_STRING( &constant_bin[ 873239 ], 7, 1 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_stat( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_1815ae826879289e55197f5495a8d153;
static PyCodeObject *codeobj_34d7ac050bd3b999a8fce5c7796f75b8;
static PyCodeObject *codeobj_05f6148b5417bb5d0e19d0fef68547bc;
static PyCodeObject *codeobj_0b69cae80c279655b212a9542f5563b1;
static PyCodeObject *codeobj_389f2b6d584b6bb6ac777ad78a9a9cee;
static PyCodeObject *codeobj_efe1520176f8d36a0ba99113888eec80;
static PyCodeObject *codeobj_3c3a848307babcc6c3475e8ada0be824;
static PyCodeObject *codeobj_5a819278f79e36891b3732a8e469654c;
static PyCodeObject *codeobj_7f450f7263ee13c0d45a9b2c7123bf80;
static PyCodeObject *codeobj_76c12aea4748798ff5a1f3cc59623edc;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_79e34f0bc27f300d84435cb68c532bb3 );
    codeobj_1815ae826879289e55197f5495a8d153 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_S_IFMT, 24, const_tuple_str_plain_mode_tuple, 1, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_34d7ac050bd3b999a8fce5c7796f75b8 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_S_IMODE, 21, const_tuple_str_plain_mode_tuple, 1, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_05f6148b5417bb5d0e19d0fef68547bc = MAKE_CODEOBJ( module_filename_obj, const_str_plain_S_ISBLK, 46, const_tuple_str_plain_mode_tuple, 1, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_0b69cae80c279655b212a9542f5563b1 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_S_ISCHR, 43, const_tuple_str_plain_mode_tuple, 1, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_389f2b6d584b6bb6ac777ad78a9a9cee = MAKE_CODEOBJ( module_filename_obj, const_str_plain_S_ISDIR, 40, const_tuple_str_plain_mode_tuple, 1, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_efe1520176f8d36a0ba99113888eec80 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_S_ISFIFO, 52, const_tuple_str_plain_mode_tuple, 1, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_3c3a848307babcc6c3475e8ada0be824 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_S_ISLNK, 55, const_tuple_str_plain_mode_tuple, 1, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_5a819278f79e36891b3732a8e469654c = MAKE_CODEOBJ( module_filename_obj, const_str_plain_S_ISREG, 49, const_tuple_str_plain_mode_tuple, 1, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_7f450f7263ee13c0d45a9b2c7123bf80 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_S_ISSOCK, 58, const_tuple_str_plain_mode_tuple, 1, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_76c12aea4748798ff5a1f3cc59623edc = MAKE_CODEOBJ( module_filename_obj, const_str_plain_stat, 1, const_tuple_empty, 0, CO_NOFREE );
}

// The module function declarations.
static PyObject *MAKE_FUNCTION_function_1_S_IMODE_of_stat(  );


static PyObject *MAKE_FUNCTION_function_2_S_IFMT_of_stat(  );


static PyObject *MAKE_FUNCTION_function_3_S_ISDIR_of_stat(  );


static PyObject *MAKE_FUNCTION_function_4_S_ISCHR_of_stat(  );


static PyObject *MAKE_FUNCTION_function_5_S_ISBLK_of_stat(  );


static PyObject *MAKE_FUNCTION_function_6_S_ISREG_of_stat(  );


static PyObject *MAKE_FUNCTION_function_7_S_ISFIFO_of_stat(  );


static PyObject *MAKE_FUNCTION_function_8_S_ISLNK_of_stat(  );


static PyObject *MAKE_FUNCTION_function_9_S_ISSOCK_of_stat(  );


// The module function definitions.
static PyObject *impl_function_1_S_IMODE_of_stat( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_mode = python_pars[ 0 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_left_name_1;
    PyObject *tmp_return_value;
    PyObject *tmp_right_name_1;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_34d7ac050bd3b999a8fce5c7796f75b8, module_stat );
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
    tmp_left_name_1 = par_mode;

    tmp_right_name_1 = const_int_pos_4095;
    tmp_return_value = BINARY_OPERATION( PyNumber_And, tmp_left_name_1, tmp_right_name_1 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 22;
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
            if ( par_mode )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_mode,
                    par_mode
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
    NUITKA_CANNOT_GET_HERE( function_1_S_IMODE_of_stat );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

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

    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_1_S_IMODE_of_stat );
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


static PyObject *impl_function_2_S_IFMT_of_stat( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_mode = python_pars[ 0 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_left_name_1;
    PyObject *tmp_return_value;
    PyObject *tmp_right_name_1;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_1815ae826879289e55197f5495a8d153, module_stat );
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
    tmp_left_name_1 = par_mode;

    tmp_right_name_1 = const_int_pos_61440;
    tmp_return_value = BINARY_OPERATION( PyNumber_And, tmp_left_name_1, tmp_right_name_1 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 25;
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
            if ( par_mode )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_mode,
                    par_mode
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
    NUITKA_CANNOT_GET_HERE( function_2_S_IFMT_of_stat );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

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

    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_2_S_IFMT_of_stat );
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


static PyObject *impl_function_3_S_ISDIR_of_stat( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_mode = python_pars[ 0 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_compexpr_left_1;
    PyObject *tmp_compexpr_right_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_389f2b6d584b6bb6ac777ad78a9a9cee, module_stat );
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
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFMT );

    if (unlikely( tmp_called_name_1 == NULL ))
    {
        tmp_called_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_IFMT );
    }

    if ( tmp_called_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "S_IFMT" );
        exception_tb = NULL;

        exception_lineno = 41;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = par_mode;

    frame_function->f_lineno = 41;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_compexpr_left_1 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    if ( tmp_compexpr_left_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 41;
        goto frame_exception_exit_1;
    }
    tmp_compexpr_right_1 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFDIR );

    if (unlikely( tmp_compexpr_right_1 == NULL ))
    {
        tmp_compexpr_right_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_IFDIR );
    }

    if ( tmp_compexpr_right_1 == NULL )
    {
        Py_DECREF( tmp_compexpr_left_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "S_IFDIR" );
        exception_tb = NULL;

        exception_lineno = 41;
        goto frame_exception_exit_1;
    }

    tmp_return_value = RICH_COMPARE_EQ( tmp_compexpr_left_1, tmp_compexpr_right_1 );
    Py_DECREF( tmp_compexpr_left_1 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 41;
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
            if ( par_mode )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_mode,
                    par_mode
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
    NUITKA_CANNOT_GET_HERE( function_3_S_ISDIR_of_stat );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

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

    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_3_S_ISDIR_of_stat );
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


static PyObject *impl_function_4_S_ISCHR_of_stat( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_mode = python_pars[ 0 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_compexpr_left_1;
    PyObject *tmp_compexpr_right_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_0b69cae80c279655b212a9542f5563b1, module_stat );
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
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFMT );

    if (unlikely( tmp_called_name_1 == NULL ))
    {
        tmp_called_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_IFMT );
    }

    if ( tmp_called_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "S_IFMT" );
        exception_tb = NULL;

        exception_lineno = 44;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = par_mode;

    frame_function->f_lineno = 44;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_compexpr_left_1 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    if ( tmp_compexpr_left_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 44;
        goto frame_exception_exit_1;
    }
    tmp_compexpr_right_1 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFCHR );

    if (unlikely( tmp_compexpr_right_1 == NULL ))
    {
        tmp_compexpr_right_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_IFCHR );
    }

    if ( tmp_compexpr_right_1 == NULL )
    {
        Py_DECREF( tmp_compexpr_left_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "S_IFCHR" );
        exception_tb = NULL;

        exception_lineno = 44;
        goto frame_exception_exit_1;
    }

    tmp_return_value = RICH_COMPARE_EQ( tmp_compexpr_left_1, tmp_compexpr_right_1 );
    Py_DECREF( tmp_compexpr_left_1 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 44;
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
            if ( par_mode )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_mode,
                    par_mode
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
    NUITKA_CANNOT_GET_HERE( function_4_S_ISCHR_of_stat );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

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

    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_4_S_ISCHR_of_stat );
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


static PyObject *impl_function_5_S_ISBLK_of_stat( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_mode = python_pars[ 0 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_compexpr_left_1;
    PyObject *tmp_compexpr_right_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_05f6148b5417bb5d0e19d0fef68547bc, module_stat );
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
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFMT );

    if (unlikely( tmp_called_name_1 == NULL ))
    {
        tmp_called_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_IFMT );
    }

    if ( tmp_called_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "S_IFMT" );
        exception_tb = NULL;

        exception_lineno = 47;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = par_mode;

    frame_function->f_lineno = 47;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_compexpr_left_1 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    if ( tmp_compexpr_left_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 47;
        goto frame_exception_exit_1;
    }
    tmp_compexpr_right_1 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFBLK );

    if (unlikely( tmp_compexpr_right_1 == NULL ))
    {
        tmp_compexpr_right_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_IFBLK );
    }

    if ( tmp_compexpr_right_1 == NULL )
    {
        Py_DECREF( tmp_compexpr_left_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "S_IFBLK" );
        exception_tb = NULL;

        exception_lineno = 47;
        goto frame_exception_exit_1;
    }

    tmp_return_value = RICH_COMPARE_EQ( tmp_compexpr_left_1, tmp_compexpr_right_1 );
    Py_DECREF( tmp_compexpr_left_1 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 47;
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
            if ( par_mode )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_mode,
                    par_mode
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
    NUITKA_CANNOT_GET_HERE( function_5_S_ISBLK_of_stat );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

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

    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_5_S_ISBLK_of_stat );
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


static PyObject *impl_function_6_S_ISREG_of_stat( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_mode = python_pars[ 0 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_compexpr_left_1;
    PyObject *tmp_compexpr_right_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_5a819278f79e36891b3732a8e469654c, module_stat );
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
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFMT );

    if (unlikely( tmp_called_name_1 == NULL ))
    {
        tmp_called_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_IFMT );
    }

    if ( tmp_called_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "S_IFMT" );
        exception_tb = NULL;

        exception_lineno = 50;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = par_mode;

    frame_function->f_lineno = 50;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_compexpr_left_1 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    if ( tmp_compexpr_left_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 50;
        goto frame_exception_exit_1;
    }
    tmp_compexpr_right_1 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFREG );

    if (unlikely( tmp_compexpr_right_1 == NULL ))
    {
        tmp_compexpr_right_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_IFREG );
    }

    if ( tmp_compexpr_right_1 == NULL )
    {
        Py_DECREF( tmp_compexpr_left_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "S_IFREG" );
        exception_tb = NULL;

        exception_lineno = 50;
        goto frame_exception_exit_1;
    }

    tmp_return_value = RICH_COMPARE_EQ( tmp_compexpr_left_1, tmp_compexpr_right_1 );
    Py_DECREF( tmp_compexpr_left_1 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 50;
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
            if ( par_mode )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_mode,
                    par_mode
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
    NUITKA_CANNOT_GET_HERE( function_6_S_ISREG_of_stat );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

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

    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_6_S_ISREG_of_stat );
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


static PyObject *impl_function_7_S_ISFIFO_of_stat( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_mode = python_pars[ 0 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_compexpr_left_1;
    PyObject *tmp_compexpr_right_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_efe1520176f8d36a0ba99113888eec80, module_stat );
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
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFMT );

    if (unlikely( tmp_called_name_1 == NULL ))
    {
        tmp_called_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_IFMT );
    }

    if ( tmp_called_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "S_IFMT" );
        exception_tb = NULL;

        exception_lineno = 53;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = par_mode;

    frame_function->f_lineno = 53;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_compexpr_left_1 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    if ( tmp_compexpr_left_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 53;
        goto frame_exception_exit_1;
    }
    tmp_compexpr_right_1 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFIFO );

    if (unlikely( tmp_compexpr_right_1 == NULL ))
    {
        tmp_compexpr_right_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_IFIFO );
    }

    if ( tmp_compexpr_right_1 == NULL )
    {
        Py_DECREF( tmp_compexpr_left_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "S_IFIFO" );
        exception_tb = NULL;

        exception_lineno = 53;
        goto frame_exception_exit_1;
    }

    tmp_return_value = RICH_COMPARE_EQ( tmp_compexpr_left_1, tmp_compexpr_right_1 );
    Py_DECREF( tmp_compexpr_left_1 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 53;
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
            if ( par_mode )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_mode,
                    par_mode
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
    NUITKA_CANNOT_GET_HERE( function_7_S_ISFIFO_of_stat );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

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

    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_7_S_ISFIFO_of_stat );
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


static PyObject *impl_function_8_S_ISLNK_of_stat( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_mode = python_pars[ 0 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_compexpr_left_1;
    PyObject *tmp_compexpr_right_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_3c3a848307babcc6c3475e8ada0be824, module_stat );
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
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFMT );

    if (unlikely( tmp_called_name_1 == NULL ))
    {
        tmp_called_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_IFMT );
    }

    if ( tmp_called_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "S_IFMT" );
        exception_tb = NULL;

        exception_lineno = 56;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = par_mode;

    frame_function->f_lineno = 56;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_compexpr_left_1 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    if ( tmp_compexpr_left_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 56;
        goto frame_exception_exit_1;
    }
    tmp_compexpr_right_1 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFLNK );

    if (unlikely( tmp_compexpr_right_1 == NULL ))
    {
        tmp_compexpr_right_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_IFLNK );
    }

    if ( tmp_compexpr_right_1 == NULL )
    {
        Py_DECREF( tmp_compexpr_left_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "S_IFLNK" );
        exception_tb = NULL;

        exception_lineno = 56;
        goto frame_exception_exit_1;
    }

    tmp_return_value = RICH_COMPARE_EQ( tmp_compexpr_left_1, tmp_compexpr_right_1 );
    Py_DECREF( tmp_compexpr_left_1 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 56;
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
            if ( par_mode )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_mode,
                    par_mode
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
    NUITKA_CANNOT_GET_HERE( function_8_S_ISLNK_of_stat );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

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

    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_8_S_ISLNK_of_stat );
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


static PyObject *impl_function_9_S_ISSOCK_of_stat( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_mode = python_pars[ 0 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_compexpr_left_1;
    PyObject *tmp_compexpr_right_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_7f450f7263ee13c0d45a9b2c7123bf80, module_stat );
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
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFMT );

    if (unlikely( tmp_called_name_1 == NULL ))
    {
        tmp_called_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_IFMT );
    }

    if ( tmp_called_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "S_IFMT" );
        exception_tb = NULL;

        exception_lineno = 59;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = par_mode;

    frame_function->f_lineno = 59;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_compexpr_left_1 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    if ( tmp_compexpr_left_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
        goto frame_exception_exit_1;
    }
    tmp_compexpr_right_1 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFSOCK );

    if (unlikely( tmp_compexpr_right_1 == NULL ))
    {
        tmp_compexpr_right_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_IFSOCK );
    }

    if ( tmp_compexpr_right_1 == NULL )
    {
        Py_DECREF( tmp_compexpr_left_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "S_IFSOCK" );
        exception_tb = NULL;

        exception_lineno = 59;
        goto frame_exception_exit_1;
    }

    tmp_return_value = RICH_COMPARE_EQ( tmp_compexpr_left_1, tmp_compexpr_right_1 );
    Py_DECREF( tmp_compexpr_left_1 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 59;
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
            if ( par_mode )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_mode,
                    par_mode
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
    NUITKA_CANNOT_GET_HERE( function_9_S_ISSOCK_of_stat );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

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

    CHECK_OBJECT( (PyObject *)par_mode );
    Py_DECREF( par_mode );
    par_mode = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_9_S_ISSOCK_of_stat );
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



static PyObject *MAKE_FUNCTION_function_1_S_IMODE_of_stat(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_1_S_IMODE_of_stat,
        const_str_plain_S_IMODE,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_34d7ac050bd3b999a8fce5c7796f75b8,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_stat,
        Py_None
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_2_S_IFMT_of_stat(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_2_S_IFMT_of_stat,
        const_str_plain_S_IFMT,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_1815ae826879289e55197f5495a8d153,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_stat,
        Py_None
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_3_S_ISDIR_of_stat(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_3_S_ISDIR_of_stat,
        const_str_plain_S_ISDIR,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_389f2b6d584b6bb6ac777ad78a9a9cee,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_stat,
        Py_None
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_4_S_ISCHR_of_stat(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_4_S_ISCHR_of_stat,
        const_str_plain_S_ISCHR,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_0b69cae80c279655b212a9542f5563b1,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_stat,
        Py_None
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_5_S_ISBLK_of_stat(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_5_S_ISBLK_of_stat,
        const_str_plain_S_ISBLK,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_05f6148b5417bb5d0e19d0fef68547bc,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_stat,
        Py_None
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_6_S_ISREG_of_stat(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_6_S_ISREG_of_stat,
        const_str_plain_S_ISREG,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_5a819278f79e36891b3732a8e469654c,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_stat,
        Py_None
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_7_S_ISFIFO_of_stat(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_7_S_ISFIFO_of_stat,
        const_str_plain_S_ISFIFO,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_efe1520176f8d36a0ba99113888eec80,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_stat,
        Py_None
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_8_S_ISLNK_of_stat(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_8_S_ISLNK_of_stat,
        const_str_plain_S_ISLNK,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_3c3a848307babcc6c3475e8ada0be824,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_stat,
        Py_None
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_9_S_ISSOCK_of_stat(  )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_9_S_ISSOCK_of_stat,
        const_str_plain_S_ISSOCK,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_7f450f7263ee13c0d45a9b2c7123bf80,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_stat,
        Py_None
    );

    return result;
}



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_stat =
{
    PyModuleDef_HEAD_INIT,
    "stat",   /* m_name */
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

MOD_INIT_DECL( stat )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_stat );
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

    // puts( "in initstat" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_stat = Py_InitModule4(
        "stat",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_stat = PyModule_Create( &mdef_stat );
#endif

    moduledict_stat = (PyDictObject *)((PyModuleObject *)module_stat)->md_dict;

    CHECK_OBJECT( module_stat );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_plain_stat, module_stat );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_stat );

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
    PyObject *tmp_assign_source_51;
    PyObject *tmp_assign_source_52;
    PyObject *tmp_assign_source_53;
    PyObject *tmp_assign_source_54;
    PyObject *tmp_assign_source_55;
    PyObject *tmp_assign_source_56;
    PyObject *tmp_assign_source_57;
    PyObject *tmp_assign_source_58;
    PyObject *tmp_assign_source_59;
    PyFrameObject *frame_module;


    // Module code.
    tmp_assign_source_1 = const_str_digest_01b02879d1918d1e66ac4015cec6e093;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    tmp_assign_source_3 = const_int_0;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_ST_MODE, tmp_assign_source_3 );
    tmp_assign_source_4 = const_int_pos_1;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_ST_INO, tmp_assign_source_4 );
    tmp_assign_source_5 = const_int_pos_2;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_ST_DEV, tmp_assign_source_5 );
    tmp_assign_source_6 = const_int_pos_3;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_ST_NLINK, tmp_assign_source_6 );
    tmp_assign_source_7 = const_int_pos_4;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_ST_UID, tmp_assign_source_7 );
    tmp_assign_source_8 = const_int_pos_5;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_ST_GID, tmp_assign_source_8 );
    tmp_assign_source_9 = const_int_pos_6;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_ST_SIZE, tmp_assign_source_9 );
    tmp_assign_source_10 = const_int_pos_7;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_ST_ATIME, tmp_assign_source_10 );
    tmp_assign_source_11 = const_int_pos_8;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_ST_MTIME, tmp_assign_source_11 );
    tmp_assign_source_12 = const_int_pos_9;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_ST_CTIME, tmp_assign_source_12 );
    tmp_assign_source_13 = MAKE_FUNCTION_function_1_S_IMODE_of_stat(  );
    UPDATE_STRING_DICT1( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IMODE, tmp_assign_source_13 );
    tmp_assign_source_14 = MAKE_FUNCTION_function_2_S_IFMT_of_stat(  );
    UPDATE_STRING_DICT1( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFMT, tmp_assign_source_14 );
    tmp_assign_source_15 = const_int_pos_16384;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFDIR, tmp_assign_source_15 );
    tmp_assign_source_16 = const_int_pos_8192;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFCHR, tmp_assign_source_16 );
    tmp_assign_source_17 = const_int_pos_24576;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFBLK, tmp_assign_source_17 );
    tmp_assign_source_18 = const_int_pos_32768;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFREG, tmp_assign_source_18 );
    tmp_assign_source_19 = const_int_pos_4096;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFIFO, tmp_assign_source_19 );
    tmp_assign_source_20 = const_int_pos_40960;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFLNK, tmp_assign_source_20 );
    tmp_assign_source_21 = const_int_pos_49152;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IFSOCK, tmp_assign_source_21 );
    tmp_assign_source_22 = MAKE_FUNCTION_function_3_S_ISDIR_of_stat(  );
    UPDATE_STRING_DICT1( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_ISDIR, tmp_assign_source_22 );
    tmp_assign_source_23 = MAKE_FUNCTION_function_4_S_ISCHR_of_stat(  );
    UPDATE_STRING_DICT1( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_ISCHR, tmp_assign_source_23 );
    tmp_assign_source_24 = MAKE_FUNCTION_function_5_S_ISBLK_of_stat(  );
    UPDATE_STRING_DICT1( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_ISBLK, tmp_assign_source_24 );
    tmp_assign_source_25 = MAKE_FUNCTION_function_6_S_ISREG_of_stat(  );
    UPDATE_STRING_DICT1( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_ISREG, tmp_assign_source_25 );
    tmp_assign_source_26 = MAKE_FUNCTION_function_7_S_ISFIFO_of_stat(  );
    UPDATE_STRING_DICT1( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_ISFIFO, tmp_assign_source_26 );
    tmp_assign_source_27 = MAKE_FUNCTION_function_8_S_ISLNK_of_stat(  );
    UPDATE_STRING_DICT1( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_ISLNK, tmp_assign_source_27 );
    tmp_assign_source_28 = MAKE_FUNCTION_function_9_S_ISSOCK_of_stat(  );
    UPDATE_STRING_DICT1( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_ISSOCK, tmp_assign_source_28 );
    tmp_assign_source_29 = const_int_pos_2048;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_ISUID, tmp_assign_source_29 );
    tmp_assign_source_30 = const_int_pos_1024;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_ISGID, tmp_assign_source_30 );
    // Frame without reuse.
    frame_module = MAKE_MODULE_FRAME( codeobj_76c12aea4748798ff5a1f3cc59623edc, module_stat );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_module );
    assert( Py_REFCNT( frame_module ) == 1 );

#if PYTHON_VERSION >= 340
    frame_module->f_executing += 1;
#endif

    // Framed code:
    tmp_assign_source_31 = GET_STRING_DICT_VALUE( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_ISGID );

    if (unlikely( tmp_assign_source_31 == NULL ))
    {
        tmp_assign_source_31 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_S_ISGID );
    }

    if ( tmp_assign_source_31 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "S_ISGID" );
        exception_tb = NULL;

        exception_lineno = 65;
        goto frame_exception_exit_1;
    }

    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_ENFMT, tmp_assign_source_31 );

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
    tmp_assign_source_32 = const_int_pos_512;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_ISVTX, tmp_assign_source_32 );
    tmp_assign_source_33 = const_int_pos_256;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IREAD, tmp_assign_source_33 );
    tmp_assign_source_34 = const_int_pos_128;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IWRITE, tmp_assign_source_34 );
    tmp_assign_source_35 = const_int_pos_64;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IEXEC, tmp_assign_source_35 );
    tmp_assign_source_36 = const_int_pos_448;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IRWXU, tmp_assign_source_36 );
    tmp_assign_source_37 = const_int_pos_256;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IRUSR, tmp_assign_source_37 );
    tmp_assign_source_38 = const_int_pos_128;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IWUSR, tmp_assign_source_38 );
    tmp_assign_source_39 = const_int_pos_64;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IXUSR, tmp_assign_source_39 );
    tmp_assign_source_40 = const_int_pos_56;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IRWXG, tmp_assign_source_40 );
    tmp_assign_source_41 = const_int_pos_32;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IRGRP, tmp_assign_source_41 );
    tmp_assign_source_42 = const_int_pos_16;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IWGRP, tmp_assign_source_42 );
    tmp_assign_source_43 = const_int_pos_8;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IXGRP, tmp_assign_source_43 );
    tmp_assign_source_44 = const_int_pos_7;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IRWXO, tmp_assign_source_44 );
    tmp_assign_source_45 = const_int_pos_4;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IROTH, tmp_assign_source_45 );
    tmp_assign_source_46 = const_int_pos_2;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IWOTH, tmp_assign_source_46 );
    tmp_assign_source_47 = const_int_pos_1;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_S_IXOTH, tmp_assign_source_47 );
    tmp_assign_source_48 = const_int_pos_1;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_UF_NODUMP, tmp_assign_source_48 );
    tmp_assign_source_49 = const_int_pos_2;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_UF_IMMUTABLE, tmp_assign_source_49 );
    tmp_assign_source_50 = const_int_pos_4;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_UF_APPEND, tmp_assign_source_50 );
    tmp_assign_source_51 = const_int_pos_8;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_UF_OPAQUE, tmp_assign_source_51 );
    tmp_assign_source_52 = const_int_pos_16;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_UF_NOUNLINK, tmp_assign_source_52 );
    tmp_assign_source_53 = const_int_pos_32;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_UF_COMPRESSED, tmp_assign_source_53 );
    tmp_assign_source_54 = const_int_pos_32768;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_UF_HIDDEN, tmp_assign_source_54 );
    tmp_assign_source_55 = const_int_pos_65536;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_SF_ARCHIVED, tmp_assign_source_55 );
    tmp_assign_source_56 = const_int_pos_131072;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_SF_IMMUTABLE, tmp_assign_source_56 );
    tmp_assign_source_57 = const_int_pos_262144;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_SF_APPEND, tmp_assign_source_57 );
    tmp_assign_source_58 = const_int_pos_1048576;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_SF_NOUNLINK, tmp_assign_source_58 );
    tmp_assign_source_59 = const_int_pos_2097152;
    UPDATE_STRING_DICT0( moduledict_stat, (Nuitka_StringObject *)const_str_plain_SF_SNAPSHOT, tmp_assign_source_59 );

    return MOD_RETURN_VALUE( module_stat );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
