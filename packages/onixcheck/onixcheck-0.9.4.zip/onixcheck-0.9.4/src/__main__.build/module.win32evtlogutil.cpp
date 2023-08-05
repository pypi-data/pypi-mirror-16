/* Generated code for Python source for module 'win32evtlogutil'
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

/* The _module_win32evtlogutil is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_win32evtlogutil;
PyDictObject *moduledict_win32evtlogutil;

/* The module constants used, if any. */
static PyObject *const_str_plain_RegSetValueEx;
static PyObject *const_str_digest_a90d46a4d0521f7077c95aeb9e33bbf7;
static PyObject *const_str_plain_hkey;
static PyObject *const_str_plain_logType;
extern PyObject *const_str_plain_data;
extern PyObject *const_str_plain_REG_DWORD;
static PyObject *const_str_plain_eventCategory;
extern PyObject *const_dict_empty;
static PyObject *const_str_plain_FormatMessage;
extern PyObject *const_str_plain_LANG_NEUTRAL;
extern PyObject *const_str_plain_win32con;
extern PyObject *const_str_plain_win32api;
static PyObject *const_str_plain_EventID;
static PyObject *const_str_digest_a7e1d98fe6ba5cf7013769ca16110b28;
extern PyObject *const_str_plain_exc;
static PyObject *const_str_digest_2578c28d01ce362f5d4d024ce24e3eb6;
static PyObject *const_tuple_f4ed6fcc27dcb5d0c0496d9a809bcc3e_tuple;
static PyObject *const_str_plain_eventType;
static PyObject *const_tuple_str_plain_eventLogRecord_str_plain_logType_str_plain_desc_tuple;
extern PyObject *const_str_plain_h;
extern PyObject *const_str_plain_HRESULT_CODE;
static PyObject *const_str_plain_feeder;
extern PyObject *const_tuple_empty;
static PyObject *const_tuple_39e627f944d7a5d85d06f4101de1e726_tuple;
extern PyObject *const_str_plain_RegQueryValueEx;
extern PyObject *const_str_plain_HKEY_LOCAL_MACHINE;
extern PyObject *const_str_plain_EVENTLOG_INFORMATION_TYPE;
static PyObject *const_unicode_digest_db35ab94a03c3cbeb13cbe2a1d728b77;
extern PyObject *const_str_plain_EVENTLOG_SEQUENTIAL_READ;
static PyObject *const_str_digest_89551213e33a0c2c1f8df3aacc402cb1;
static PyObject *const_str_plain_RemoveSourceFromRegistry;
static PyObject *const_str_digest_a970d4942e13293b290143946644e24a;
extern PyObject *const_int_neg_1;
static PyObject *const_str_digest_131a3a4da4bff7e80ca7f276f0aad597;
static PyObject *const_str_plain_FreeLibrary;
static PyObject *const_tuple_str_plain_Application_tuple;
static PyObject *const_str_plain_ExpandEnvironmentStrings;
static PyObject *const_tuple_none_str_plain_Application_none_tuple;
extern PyObject *const_str_plain_RegCloseKey;
extern PyObject *const_str_plain_map;
static PyObject *const_str_digest_ea2d4888e032144a549f6c845bc4daf5;
extern PyObject *const_str_plain_error;
static PyObject *const_str_plain_langid;
static PyObject *const_str_plain_TypesSupported;
extern PyObject *const_str_plain___file__;
static PyObject *const_str_plain_RegOpenKey;
extern PyObject *const_str_plain_Application;
extern PyObject *const_str_plain_EVENTLOG_WARNING_TYPE;
static PyObject *const_str_plain_RegCreateKey;
extern PyObject *const_str_plain_REG_EXPAND_SZ;
static PyObject *const_str_plain_ReadEventLog;
extern PyObject *const_str_plain_EVENTLOG_BACKWARDS_READ;
extern PyObject *const_str_plain_ERROR_FILE_NOT_FOUND;
static PyObject *const_str_plain_objects;
extern PyObject *const_str_plain_item;
static PyObject *const_str_plain_EventMessageFile;
extern PyObject *const_str_plain_LOAD_LIBRARY_AS_DATAFILE;
static PyObject *const_tuple_d07948d6b1957946e6b58f7e40f0cb85_tuple;
static PyObject *const_str_plain_msgDLL;
static PyObject *const_str_plain_logName;
static PyObject *const_str_plain_SourceName;
extern PyObject *const_str_plain_join;
extern PyObject *const_str_plain_EVENTLOG_ERROR_TYPE;
static PyObject *const_str_plain_StringInserts;
static PyObject *const_str_plain_SafeFormatMessage;
extern PyObject *const_unicode_empty;
static PyObject *const_str_plain_appName;
static PyObject *const_str_plain_OpenEventLog;
extern PyObject *const_str_plain_AddSourceToRegistry;
static PyObject *const_str_plain_FormatMessageW;
static PyObject *const_tuple_7bf371154b54da35ea158621f29deac9_tuple;
static PyObject *const_str_plain_DeregisterEventSource;
extern PyObject *const_str_chr_59;
static PyObject *const_str_digest_b3058d3f630aa2c74cf839db3e555357;
extern PyObject *const_str_plain_strings;
static PyObject *const_str_plain_eventID;
static PyObject *const_str_plain_CloseEventLog;
extern PyObject *const_str_plain_handle;
extern PyObject *const_str_plain_split;
static PyObject *const_str_plain_RegisterEventSource;
static PyObject *const_str_plain_eventLogType;
static PyObject *const_str_plain_dllName;
static PyObject *const_str_plain_MAKELANGID;
extern PyObject *const_str_plain_desc;
static PyObject *const_str_plain_LoadLibraryEx;
extern PyObject *const_str_plain_ReportEvent;
static PyObject *const_str_plain_dllHandle;
static PyObject *const_str_plain_FeedEventLogRecords;
extern PyObject *const_tuple_str_chr_59_tuple;
extern PyObject *const_str_plain_FORMAT_MESSAGE_FROM_HMODULE;
extern PyObject *const_str_plain_win32evtlog;
static PyObject *const_unicode_digest_863683e3a5be671913b94c371b27c7ba;
extern PyObject *const_str_plain___doc__;
static PyObject *const_str_plain_dllNames;
extern PyObject *const_int_0;
static PyObject *const_str_plain_keyName;
extern PyObject *const_str_plain_SUBLANG_NEUTRAL;
static PyObject *const_str_plain_eventLogFlags;
static PyObject *const_str_plain_machineName;
static PyObject *const_tuple_str_plain_item_str_plain_feeder_tuple;
extern PyObject *const_str_empty;
static PyObject *const_str_plain_eventLogRecord;
extern PyObject *const_str_plain_win32evtlogutil;
extern PyObject *const_str_plain_sid;
static PyObject *const_str_plain_RegDeleteKey;
static PyObject *const_str_plain_hAppLog;
extern PyObject *const_str_plain_winerror;
static PyObject *const_tuple_str_plain_appName_str_plain_eventLogType_str_plain_exc_tuple;
static PyObject *const_str_plain_readFlags;
extern PyObject *const_tuple_none_tuple;
extern PyObject *const_str_angle_lambda;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_plain_RegSetValueEx = UNSTREAM_STRING( &constant_bin[ 1096012 ], 13, 1 );
    const_str_digest_a90d46a4d0521f7077c95aeb9e33bbf7 = UNSTREAM_STRING( &constant_bin[ 1096025 ], 57, 0 );
    const_str_plain_hkey = UNSTREAM_STRING( &constant_bin[ 659051 ], 4, 1 );
    const_str_plain_logType = UNSTREAM_STRING( &constant_bin[ 1096082 ], 7, 1 );
    const_str_plain_eventCategory = UNSTREAM_STRING( &constant_bin[ 1096089 ], 13, 1 );
    const_str_plain_FormatMessage = UNSTREAM_STRING( &constant_bin[ 1096102 ], 13, 1 );
    const_str_plain_EventID = UNSTREAM_STRING( &constant_bin[ 1096115 ], 7, 1 );
    const_str_digest_a7e1d98fe6ba5cf7013769ca16110b28 = UNSTREAM_STRING( &constant_bin[ 1096122 ], 53, 0 );
    const_str_digest_2578c28d01ce362f5d4d024ce24e3eb6 = UNSTREAM_STRING( &constant_bin[ 1096175 ], 301, 0 );
    const_tuple_f4ed6fcc27dcb5d0c0496d9a809bcc3e_tuple = PyTuple_New( 8 );
    const_str_plain_eventLogRecord = UNSTREAM_STRING( &constant_bin[ 1096476 ], 14, 1 );
    PyTuple_SET_ITEM( const_tuple_f4ed6fcc27dcb5d0c0496d9a809bcc3e_tuple, 0, const_str_plain_eventLogRecord ); Py_INCREF( const_str_plain_eventLogRecord );
    PyTuple_SET_ITEM( const_tuple_f4ed6fcc27dcb5d0c0496d9a809bcc3e_tuple, 1, const_str_plain_logType ); Py_INCREF( const_str_plain_logType );
    const_str_plain_keyName = UNSTREAM_STRING( &constant_bin[ 1096490 ], 7, 1 );
    PyTuple_SET_ITEM( const_tuple_f4ed6fcc27dcb5d0c0496d9a809bcc3e_tuple, 2, const_str_plain_keyName ); Py_INCREF( const_str_plain_keyName );
    PyTuple_SET_ITEM( const_tuple_f4ed6fcc27dcb5d0c0496d9a809bcc3e_tuple, 3, const_str_plain_handle ); Py_INCREF( const_str_plain_handle );
    const_str_plain_dllNames = UNSTREAM_STRING( &constant_bin[ 1096497 ], 8, 1 );
    PyTuple_SET_ITEM( const_tuple_f4ed6fcc27dcb5d0c0496d9a809bcc3e_tuple, 4, const_str_plain_dllNames ); Py_INCREF( const_str_plain_dllNames );
    PyTuple_SET_ITEM( const_tuple_f4ed6fcc27dcb5d0c0496d9a809bcc3e_tuple, 5, const_str_plain_data ); Py_INCREF( const_str_plain_data );
    const_str_plain_dllName = UNSTREAM_STRING( &constant_bin[ 1096497 ], 7, 1 );
    PyTuple_SET_ITEM( const_tuple_f4ed6fcc27dcb5d0c0496d9a809bcc3e_tuple, 6, const_str_plain_dllName ); Py_INCREF( const_str_plain_dllName );
    const_str_plain_dllHandle = UNSTREAM_STRING( &constant_bin[ 1096505 ], 9, 1 );
    PyTuple_SET_ITEM( const_tuple_f4ed6fcc27dcb5d0c0496d9a809bcc3e_tuple, 7, const_str_plain_dllHandle ); Py_INCREF( const_str_plain_dllHandle );
    const_str_plain_eventType = UNSTREAM_STRING( &constant_bin[ 1096514 ], 9, 1 );
    const_tuple_str_plain_eventLogRecord_str_plain_logType_str_plain_desc_tuple = PyTuple_New( 3 );
    PyTuple_SET_ITEM( const_tuple_str_plain_eventLogRecord_str_plain_logType_str_plain_desc_tuple, 0, const_str_plain_eventLogRecord ); Py_INCREF( const_str_plain_eventLogRecord );
    PyTuple_SET_ITEM( const_tuple_str_plain_eventLogRecord_str_plain_logType_str_plain_desc_tuple, 1, const_str_plain_logType ); Py_INCREF( const_str_plain_logType );
    PyTuple_SET_ITEM( const_tuple_str_plain_eventLogRecord_str_plain_logType_str_plain_desc_tuple, 2, const_str_plain_desc ); Py_INCREF( const_str_plain_desc );
    const_str_plain_feeder = UNSTREAM_STRING( &constant_bin[ 670519 ], 6, 1 );
    const_tuple_39e627f944d7a5d85d06f4101de1e726_tuple = PyTuple_New( 8 );
    const_str_plain_appName = UNSTREAM_STRING( &constant_bin[ 1096523 ], 7, 1 );
    PyTuple_SET_ITEM( const_tuple_39e627f944d7a5d85d06f4101de1e726_tuple, 0, const_str_plain_appName ); Py_INCREF( const_str_plain_appName );
    const_str_plain_eventID = UNSTREAM_STRING( &constant_bin[ 1096530 ], 7, 1 );
    PyTuple_SET_ITEM( const_tuple_39e627f944d7a5d85d06f4101de1e726_tuple, 1, const_str_plain_eventID ); Py_INCREF( const_str_plain_eventID );
    PyTuple_SET_ITEM( const_tuple_39e627f944d7a5d85d06f4101de1e726_tuple, 2, const_str_plain_eventCategory ); Py_INCREF( const_str_plain_eventCategory );
    PyTuple_SET_ITEM( const_tuple_39e627f944d7a5d85d06f4101de1e726_tuple, 3, const_str_plain_eventType ); Py_INCREF( const_str_plain_eventType );
    PyTuple_SET_ITEM( const_tuple_39e627f944d7a5d85d06f4101de1e726_tuple, 4, const_str_plain_strings ); Py_INCREF( const_str_plain_strings );
    PyTuple_SET_ITEM( const_tuple_39e627f944d7a5d85d06f4101de1e726_tuple, 5, const_str_plain_data ); Py_INCREF( const_str_plain_data );
    PyTuple_SET_ITEM( const_tuple_39e627f944d7a5d85d06f4101de1e726_tuple, 6, const_str_plain_sid ); Py_INCREF( const_str_plain_sid );
    const_str_plain_hAppLog = UNSTREAM_STRING( &constant_bin[ 1096537 ], 7, 1 );
    PyTuple_SET_ITEM( const_tuple_39e627f944d7a5d85d06f4101de1e726_tuple, 7, const_str_plain_hAppLog ); Py_INCREF( const_str_plain_hAppLog );
    const_unicode_digest_db35ab94a03c3cbeb13cbe2a1d728b77 = UNSTREAM_UNICODE( &constant_bin[ 2433 ], 2 );
    const_str_digest_89551213e33a0c2c1f8df3aacc402cb1 = UNSTREAM_STRING( &constant_bin[ 1096544 ], 550, 0 );
    const_str_plain_RemoveSourceFromRegistry = UNSTREAM_STRING( &constant_bin[ 1097094 ], 24, 1 );
    const_str_digest_a970d4942e13293b290143946644e24a = UNSTREAM_STRING( &constant_bin[ 1097118 ], 99, 0 );
    const_str_digest_131a3a4da4bff7e80ca7f276f0aad597 = UNSTREAM_STRING( &constant_bin[ 1097217 ], 18, 0 );
    const_str_plain_FreeLibrary = UNSTREAM_STRING( &constant_bin[ 1097235 ], 11, 1 );
    const_tuple_str_plain_Application_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_Application_tuple, 0, const_str_plain_Application ); Py_INCREF( const_str_plain_Application );
    const_str_plain_ExpandEnvironmentStrings = UNSTREAM_STRING( &constant_bin[ 1097246 ], 24, 1 );
    const_tuple_none_str_plain_Application_none_tuple = PyTuple_New( 3 );
    PyTuple_SET_ITEM( const_tuple_none_str_plain_Application_none_tuple, 0, Py_None ); Py_INCREF( Py_None );
    PyTuple_SET_ITEM( const_tuple_none_str_plain_Application_none_tuple, 1, const_str_plain_Application ); Py_INCREF( const_str_plain_Application );
    PyTuple_SET_ITEM( const_tuple_none_str_plain_Application_none_tuple, 2, Py_None ); Py_INCREF( Py_None );
    const_str_digest_ea2d4888e032144a549f6c845bc4daf5 = UNSTREAM_STRING( &constant_bin[ 1097270 ], 48, 0 );
    const_str_plain_langid = UNSTREAM_STRING( &constant_bin[ 1097318 ], 6, 1 );
    const_str_plain_TypesSupported = UNSTREAM_STRING( &constant_bin[ 1097324 ], 14, 1 );
    const_str_plain_RegOpenKey = UNSTREAM_STRING( &constant_bin[ 746909 ], 10, 1 );
    const_str_plain_RegCreateKey = UNSTREAM_STRING( &constant_bin[ 1097338 ], 12, 1 );
    const_str_plain_ReadEventLog = UNSTREAM_STRING( &constant_bin[ 1096194 ], 12, 1 );
    const_str_plain_objects = UNSTREAM_STRING( &constant_bin[ 5265 ], 7, 1 );
    const_str_plain_EventMessageFile = UNSTREAM_STRING( &constant_bin[ 1097350 ], 16, 1 );
    const_tuple_d07948d6b1957946e6b58f7e40f0cb85_tuple = PyTuple_New( 5 );
    PyTuple_SET_ITEM( const_tuple_d07948d6b1957946e6b58f7e40f0cb85_tuple, 0, const_str_plain_appName ); Py_INCREF( const_str_plain_appName );
    const_str_plain_msgDLL = UNSTREAM_STRING( &constant_bin[ 1097366 ], 6, 1 );
    PyTuple_SET_ITEM( const_tuple_d07948d6b1957946e6b58f7e40f0cb85_tuple, 1, const_str_plain_msgDLL ); Py_INCREF( const_str_plain_msgDLL );
    const_str_plain_eventLogType = UNSTREAM_STRING( &constant_bin[ 1097372 ], 12, 1 );
    PyTuple_SET_ITEM( const_tuple_d07948d6b1957946e6b58f7e40f0cb85_tuple, 2, const_str_plain_eventLogType ); Py_INCREF( const_str_plain_eventLogType );
    const_str_plain_eventLogFlags = UNSTREAM_STRING( &constant_bin[ 1097384 ], 13, 1 );
    PyTuple_SET_ITEM( const_tuple_d07948d6b1957946e6b58f7e40f0cb85_tuple, 3, const_str_plain_eventLogFlags ); Py_INCREF( const_str_plain_eventLogFlags );
    PyTuple_SET_ITEM( const_tuple_d07948d6b1957946e6b58f7e40f0cb85_tuple, 4, const_str_plain_hkey ); Py_INCREF( const_str_plain_hkey );
    const_str_plain_logName = UNSTREAM_STRING( &constant_bin[ 1097397 ], 7, 1 );
    const_str_plain_SourceName = UNSTREAM_STRING( &constant_bin[ 1097404 ], 10, 1 );
    const_str_plain_StringInserts = UNSTREAM_STRING( &constant_bin[ 1097414 ], 13, 1 );
    const_str_plain_SafeFormatMessage = UNSTREAM_STRING( &constant_bin[ 1096390 ], 17, 1 );
    const_str_plain_OpenEventLog = UNSTREAM_STRING( &constant_bin[ 1097427 ], 12, 1 );
    const_str_plain_FormatMessageW = UNSTREAM_STRING( &constant_bin[ 1097439 ], 14, 1 );
    const_tuple_7bf371154b54da35ea158621f29deac9_tuple = PyTuple_New( 6 );
    PyTuple_SET_ITEM( const_tuple_7bf371154b54da35ea158621f29deac9_tuple, 0, const_str_plain_feeder ); Py_INCREF( const_str_plain_feeder );
    const_str_plain_machineName = UNSTREAM_STRING( &constant_bin[ 1097453 ], 11, 1 );
    PyTuple_SET_ITEM( const_tuple_7bf371154b54da35ea158621f29deac9_tuple, 1, const_str_plain_machineName ); Py_INCREF( const_str_plain_machineName );
    PyTuple_SET_ITEM( const_tuple_7bf371154b54da35ea158621f29deac9_tuple, 2, const_str_plain_logName ); Py_INCREF( const_str_plain_logName );
    const_str_plain_readFlags = UNSTREAM_STRING( &constant_bin[ 1097464 ], 9, 1 );
    PyTuple_SET_ITEM( const_tuple_7bf371154b54da35ea158621f29deac9_tuple, 3, const_str_plain_readFlags ); Py_INCREF( const_str_plain_readFlags );
    PyTuple_SET_ITEM( const_tuple_7bf371154b54da35ea158621f29deac9_tuple, 4, const_str_plain_h ); Py_INCREF( const_str_plain_h );
    PyTuple_SET_ITEM( const_tuple_7bf371154b54da35ea158621f29deac9_tuple, 5, const_str_plain_objects ); Py_INCREF( const_str_plain_objects );
    const_str_plain_DeregisterEventSource = UNSTREAM_STRING( &constant_bin[ 1097473 ], 21, 1 );
    const_str_digest_b3058d3f630aa2c74cf839db3e555357 = UNSTREAM_STRING( &constant_bin[ 1097494 ], 49, 0 );
    const_str_plain_CloseEventLog = UNSTREAM_STRING( &constant_bin[ 1097543 ], 13, 1 );
    const_str_plain_RegisterEventSource = UNSTREAM_STRING( &constant_bin[ 1097556 ], 19, 1 );
    const_str_plain_MAKELANGID = UNSTREAM_STRING( &constant_bin[ 1097575 ], 10, 1 );
    const_str_plain_LoadLibraryEx = UNSTREAM_STRING( &constant_bin[ 1097585 ], 13, 1 );
    const_str_plain_FeedEventLogRecords = UNSTREAM_STRING( &constant_bin[ 1097598 ], 19, 1 );
    const_unicode_digest_863683e3a5be671913b94c371b27c7ba = UNSTREAM_UNICODE( &constant_bin[ 1097617 ], 124 );
    const_tuple_str_plain_item_str_plain_feeder_tuple = PyTuple_New( 2 );
    PyTuple_SET_ITEM( const_tuple_str_plain_item_str_plain_feeder_tuple, 0, const_str_plain_item ); Py_INCREF( const_str_plain_item );
    PyTuple_SET_ITEM( const_tuple_str_plain_item_str_plain_feeder_tuple, 1, const_str_plain_feeder ); Py_INCREF( const_str_plain_feeder );
    const_str_plain_RegDeleteKey = UNSTREAM_STRING( &constant_bin[ 1097741 ], 12, 1 );
    const_tuple_str_plain_appName_str_plain_eventLogType_str_plain_exc_tuple = PyTuple_New( 3 );
    PyTuple_SET_ITEM( const_tuple_str_plain_appName_str_plain_eventLogType_str_plain_exc_tuple, 0, const_str_plain_appName ); Py_INCREF( const_str_plain_appName );
    PyTuple_SET_ITEM( const_tuple_str_plain_appName_str_plain_eventLogType_str_plain_exc_tuple, 1, const_str_plain_eventLogType ); Py_INCREF( const_str_plain_eventLogType );
    PyTuple_SET_ITEM( const_tuple_str_plain_appName_str_plain_eventLogType_str_plain_exc_tuple, 2, const_str_plain_exc ); Py_INCREF( const_str_plain_exc );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_win32evtlogutil( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_843f9cdc0334dfe4e8545a24d53ebbfd;
static PyCodeObject *codeobj_758d5442516f0ec97cbaf08014152191;
static PyCodeObject *codeobj_366d412a45eef79bfd41a727819b2246;
static PyCodeObject *codeobj_35a7c46c79a10f4e0265e1fea4b9e5e8;
static PyCodeObject *codeobj_a17e3f58c52d52f38410a275487e8e8d;
static PyCodeObject *codeobj_b1a4e3bc221a84707e5ac6ce4f201129;
static PyCodeObject *codeobj_7cee90ab7624d8980a8341b242e3cc90;
static PyCodeObject *codeobj_ef1a4625ec0c7ad40c4e18d1afed0eed;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_131a3a4da4bff7e80ca7f276f0aad597 );
    codeobj_843f9cdc0334dfe4e8545a24d53ebbfd = MAKE_CODEOBJ( module_filename_obj, const_str_angle_lambda, 150, const_tuple_str_plain_item_str_plain_feeder_tuple, 2, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_758d5442516f0ec97cbaf08014152191 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_AddSourceToRegistry, 10, const_tuple_d07948d6b1957946e6b58f7e40f0cb85_tuple, 4, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_366d412a45eef79bfd41a727819b2246 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_FeedEventLogRecords, 140, const_tuple_7bf371154b54da35ea158621f29deac9_tuple, 4, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_35a7c46c79a10f4e0265e1fea4b9e5e8 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_FormatMessage, 84, const_tuple_f4ed6fcc27dcb5d0c0496d9a809bcc3e_tuple, 2, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_a17e3f58c52d52f38410a275487e8e8d = MAKE_CODEOBJ( module_filename_obj, const_str_plain_RemoveSourceFromRegistry, 54, const_tuple_str_plain_appName_str_plain_eventLogType_str_plain_exc_tuple, 2, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_b1a4e3bc221a84707e5ac6ce4f201129 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_ReportEvent, 67, const_tuple_39e627f944d7a5d85d06f4101de1e726_tuple, 7, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_7cee90ab7624d8980a8341b242e3cc90 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_SafeFormatMessage, 126, const_tuple_str_plain_eventLogRecord_str_plain_logType_str_plain_desc_tuple, 2, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_ef1a4625ec0c7ad40c4e18d1afed0eed = MAKE_CODEOBJ( module_filename_obj, const_str_plain_win32evtlogutil, 1, const_tuple_empty, 0, CO_NOFREE );
}

// The module function declarations.
NUITKA_CROSS_MODULE PyObject *impl_function_2_complex_call_helper_star_list_of___internal__( PyObject **python_pars );


static PyObject *MAKE_FUNCTION_function_1_AddSourceToRegistry_of_win32evtlogutil( PyObject *defaults );


static PyObject *MAKE_FUNCTION_function_1_lambda_of_function_6_FeedEventLogRecords_of_win32evtlogutil( PyObject *defaults );


static PyObject *MAKE_FUNCTION_function_2_RemoveSourceFromRegistry_of_win32evtlogutil( PyObject *defaults );


static PyObject *MAKE_FUNCTION_function_3_ReportEvent_of_win32evtlogutil( PyObject *defaults );


static PyObject *MAKE_FUNCTION_function_4_FormatMessage_of_win32evtlogutil( PyObject *defaults );


static PyObject *MAKE_FUNCTION_function_5_SafeFormatMessage_of_win32evtlogutil( PyObject *defaults );


static PyObject *MAKE_FUNCTION_function_6_FeedEventLogRecords_of_win32evtlogutil( PyObject *defaults );


// The module function definitions.
static PyObject *impl_function_1_AddSourceToRegistry_of_win32evtlogutil( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_appName = python_pars[ 0 ];
    PyObject *par_msgDLL = python_pars[ 1 ];
    PyObject *par_eventLogType = python_pars[ 2 ];
    PyObject *par_eventLogFlags = python_pars[ 3 ];
    PyObject *var_hkey = NULL;
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_args_element_name_2;
    PyObject *tmp_args_element_name_3;
    PyObject *tmp_args_element_name_4;
    PyObject *tmp_args_element_name_5;
    PyObject *tmp_args_element_name_6;
    PyObject *tmp_args_element_name_7;
    PyObject *tmp_args_element_name_8;
    PyObject *tmp_args_element_name_9;
    PyObject *tmp_args_element_name_10;
    PyObject *tmp_args_element_name_11;
    PyObject *tmp_args_element_name_12;
    PyObject *tmp_args_element_name_13;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_called_name_3;
    PyObject *tmp_called_name_4;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_left_2;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_compare_right_2;
    PyObject *tmp_frame_locals;
    bool tmp_is_1;
    bool tmp_is_2;
    PyObject *tmp_left_name_1;
    PyObject *tmp_left_name_2;
    PyObject *tmp_left_name_3;
    PyObject *tmp_return_value;
    PyObject *tmp_right_name_1;
    PyObject *tmp_right_name_2;
    PyObject *tmp_right_name_3;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    PyObject *tmp_source_name_3;
    PyObject *tmp_source_name_4;
    PyObject *tmp_source_name_5;
    PyObject *tmp_source_name_6;
    PyObject *tmp_source_name_7;
    PyObject *tmp_source_name_8;
    PyObject *tmp_source_name_9;
    PyObject *tmp_source_name_10;
    PyObject *tmp_source_name_11;
    PyObject *tmp_tuple_element_1;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_758d5442516f0ec97cbaf08014152191, module_win32evtlogutil );
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
    tmp_compare_left_1 = par_msgDLL;

    tmp_compare_right_1 = Py_None;
    tmp_is_1 = ( tmp_compare_left_1 == tmp_compare_right_1 );
    if ( tmp_is_1 )
    {
        goto branch_yes_1;
    }
    else
    {
        goto branch_no_1;
    }
    branch_yes_1:;
    tmp_source_name_1 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog );

    if (unlikely( tmp_source_name_1 == NULL ))
    {
        tmp_source_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32evtlog );
    }

    if ( tmp_source_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32evtlog" );
        exception_tb = NULL;

        exception_lineno = 31;
        goto frame_exception_exit_1;
    }

    tmp_assign_source_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain___file__ );
    if ( tmp_assign_source_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 31;
        goto frame_exception_exit_1;
    }
    {
        PyObject *old = par_msgDLL;
        assert( old != NULL );
        par_msgDLL = tmp_assign_source_1;
        Py_DECREF( old );
    }

    branch_no_1:;
    tmp_source_name_2 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_2 == NULL ))
    {
        tmp_source_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 34;
        goto frame_exception_exit_1;
    }

    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_RegCreateKey );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    tmp_source_name_3 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32con );

    if (unlikely( tmp_source_name_3 == NULL ))
    {
        tmp_source_name_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32con );
    }

    if ( tmp_source_name_3 == NULL )
    {
        Py_DECREF( tmp_called_name_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32con" );
        exception_tb = NULL;

        exception_lineno = 34;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_3, const_str_plain_HKEY_LOCAL_MACHINE );
    if ( tmp_args_element_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_1 );

        exception_lineno = 34;
        goto frame_exception_exit_1;
    }
    tmp_left_name_1 = const_str_digest_ea2d4888e032144a549f6c845bc4daf5;
    tmp_right_name_1 = PyTuple_New( 2 );
    tmp_tuple_element_1 = par_eventLogType;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_right_name_1, 0, tmp_tuple_element_1 );
    tmp_tuple_element_1 = par_appName;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_right_name_1, 1, tmp_tuple_element_1 );
    tmp_args_element_name_2 = BINARY_OPERATION_REMAINDER( tmp_left_name_1, tmp_right_name_1 );
    Py_DECREF( tmp_right_name_1 );
    if ( tmp_args_element_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_1 );
        Py_DECREF( tmp_args_element_name_1 );

        exception_lineno = 35;
        goto frame_exception_exit_1;
    }
    frame_function->f_lineno = 35;
    {
        PyObject *call_args[] = { tmp_args_element_name_1, tmp_args_element_name_2 };
        tmp_assign_source_2 = CALL_FUNCTION_WITH_ARGS2( tmp_called_name_1, call_args );
    }

    Py_DECREF( tmp_called_name_1 );
    Py_DECREF( tmp_args_element_name_1 );
    Py_DECREF( tmp_args_element_name_2 );
    if ( tmp_assign_source_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 35;
        goto frame_exception_exit_1;
    }
    assert( var_hkey == NULL );
    var_hkey = tmp_assign_source_2;

    tmp_source_name_4 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_4 == NULL ))
    {
        tmp_source_name_4 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_4 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 38;
        goto frame_exception_exit_1;
    }

    tmp_called_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_4, const_str_plain_RegSetValueEx );
    if ( tmp_called_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 38;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_3 = var_hkey;

    tmp_args_element_name_4 = const_str_plain_EventMessageFile;
    tmp_args_element_name_5 = const_int_0;
    tmp_source_name_5 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32con );

    if (unlikely( tmp_source_name_5 == NULL ))
    {
        tmp_source_name_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32con );
    }

    if ( tmp_source_name_5 == NULL )
    {
        Py_DECREF( tmp_called_name_2 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32con" );
        exception_tb = NULL;

        exception_lineno = 41;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_6 = LOOKUP_ATTRIBUTE( tmp_source_name_5, const_str_plain_REG_EXPAND_SZ );
    if ( tmp_args_element_name_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_2 );

        exception_lineno = 41;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_7 = par_msgDLL;

    frame_function->f_lineno = 42;
    {
        PyObject *call_args[] = { tmp_args_element_name_3, tmp_args_element_name_4, tmp_args_element_name_5, tmp_args_element_name_6, tmp_args_element_name_7 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS5( tmp_called_name_2, call_args );
    }

    Py_DECREF( tmp_called_name_2 );
    Py_DECREF( tmp_args_element_name_6 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 42;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_compare_left_2 = par_eventLogFlags;

    tmp_compare_right_2 = Py_None;
    tmp_is_2 = ( tmp_compare_left_2 == tmp_compare_right_2 );
    if ( tmp_is_2 )
    {
        goto branch_yes_2;
    }
    else
    {
        goto branch_no_2;
    }
    branch_yes_2:;
    tmp_source_name_6 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog );

    if (unlikely( tmp_source_name_6 == NULL ))
    {
        tmp_source_name_6 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32evtlog );
    }

    if ( tmp_source_name_6 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32evtlog" );
        exception_tb = NULL;

        exception_lineno = 46;
        goto frame_exception_exit_1;
    }

    tmp_left_name_3 = LOOKUP_ATTRIBUTE( tmp_source_name_6, const_str_plain_EVENTLOG_ERROR_TYPE );
    if ( tmp_left_name_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 46;
        goto frame_exception_exit_1;
    }
    tmp_source_name_7 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog );

    if (unlikely( tmp_source_name_7 == NULL ))
    {
        tmp_source_name_7 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32evtlog );
    }

    if ( tmp_source_name_7 == NULL )
    {
        Py_DECREF( tmp_left_name_3 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32evtlog" );
        exception_tb = NULL;

        exception_lineno = 46;
        goto frame_exception_exit_1;
    }

    tmp_right_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_7, const_str_plain_EVENTLOG_WARNING_TYPE );
    if ( tmp_right_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_left_name_3 );

        exception_lineno = 46;
        goto frame_exception_exit_1;
    }
    tmp_left_name_2 = BINARY_OPERATION( PyNumber_Or, tmp_left_name_3, tmp_right_name_2 );
    Py_DECREF( tmp_left_name_3 );
    Py_DECREF( tmp_right_name_2 );
    if ( tmp_left_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 46;
        goto frame_exception_exit_1;
    }
    tmp_source_name_8 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog );

    if (unlikely( tmp_source_name_8 == NULL ))
    {
        tmp_source_name_8 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32evtlog );
    }

    if ( tmp_source_name_8 == NULL )
    {
        Py_DECREF( tmp_left_name_2 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32evtlog" );
        exception_tb = NULL;

        exception_lineno = 46;
        goto frame_exception_exit_1;
    }

    tmp_right_name_3 = LOOKUP_ATTRIBUTE( tmp_source_name_8, const_str_plain_EVENTLOG_INFORMATION_TYPE );
    if ( tmp_right_name_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_left_name_2 );

        exception_lineno = 46;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_3 = BINARY_OPERATION( PyNumber_Or, tmp_left_name_2, tmp_right_name_3 );
    Py_DECREF( tmp_left_name_2 );
    Py_DECREF( tmp_right_name_3 );
    if ( tmp_assign_source_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 46;
        goto frame_exception_exit_1;
    }
    {
        PyObject *old = par_eventLogFlags;
        assert( old != NULL );
        par_eventLogFlags = tmp_assign_source_3;
        Py_DECREF( old );
    }

    branch_no_2:;
    tmp_source_name_9 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_9 == NULL ))
    {
        tmp_source_name_9 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_9 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 47;
        goto frame_exception_exit_1;
    }

    tmp_called_name_3 = LOOKUP_ATTRIBUTE( tmp_source_name_9, const_str_plain_RegSetValueEx );
    if ( tmp_called_name_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 47;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_8 = var_hkey;

    tmp_args_element_name_9 = const_str_plain_TypesSupported;
    tmp_args_element_name_10 = const_int_0;
    tmp_source_name_10 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32con );

    if (unlikely( tmp_source_name_10 == NULL ))
    {
        tmp_source_name_10 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32con );
    }

    if ( tmp_source_name_10 == NULL )
    {
        Py_DECREF( tmp_called_name_3 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32con" );
        exception_tb = NULL;

        exception_lineno = 50;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_11 = LOOKUP_ATTRIBUTE( tmp_source_name_10, const_str_plain_REG_DWORD );
    if ( tmp_args_element_name_11 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_3 );

        exception_lineno = 50;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_12 = par_eventLogFlags;

    frame_function->f_lineno = 51;
    {
        PyObject *call_args[] = { tmp_args_element_name_8, tmp_args_element_name_9, tmp_args_element_name_10, tmp_args_element_name_11, tmp_args_element_name_12 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS5( tmp_called_name_3, call_args );
    }

    Py_DECREF( tmp_called_name_3 );
    Py_DECREF( tmp_args_element_name_11 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 51;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_source_name_11 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_11 == NULL ))
    {
        tmp_source_name_11 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_11 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 52;
        goto frame_exception_exit_1;
    }

    tmp_called_name_4 = LOOKUP_ATTRIBUTE( tmp_source_name_11, const_str_plain_RegCloseKey );
    if ( tmp_called_name_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 52;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_13 = var_hkey;

    frame_function->f_lineno = 52;
    {
        PyObject *call_args[] = { tmp_args_element_name_13 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_4, call_args );
    }

    Py_DECREF( tmp_called_name_4 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 52;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );

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
            if ( par_appName )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_appName,
                    par_appName
                );

                assert( res == 0 );
            }

            if ( par_msgDLL )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_msgDLL,
                    par_msgDLL
                );

                assert( res == 0 );
            }

            if ( par_eventLogType )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_eventLogType,
                    par_eventLogType
                );

                assert( res == 0 );
            }

            if ( par_eventLogFlags )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_eventLogFlags,
                    par_eventLogFlags
                );

                assert( res == 0 );
            }

            if ( var_hkey )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_hkey,
                    var_hkey
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

    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_1_AddSourceToRegistry_of_win32evtlogutil );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_appName );
    Py_DECREF( par_appName );
    par_appName = NULL;

    CHECK_OBJECT( (PyObject *)par_msgDLL );
    Py_DECREF( par_msgDLL );
    par_msgDLL = NULL;

    CHECK_OBJECT( (PyObject *)par_eventLogType );
    Py_DECREF( par_eventLogType );
    par_eventLogType = NULL;

    CHECK_OBJECT( (PyObject *)par_eventLogFlags );
    Py_DECREF( par_eventLogFlags );
    par_eventLogFlags = NULL;

    CHECK_OBJECT( (PyObject *)var_hkey );
    Py_DECREF( var_hkey );
    var_hkey = NULL;

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

    CHECK_OBJECT( (PyObject *)par_appName );
    Py_DECREF( par_appName );
    par_appName = NULL;

    Py_XDECREF( par_msgDLL );
    par_msgDLL = NULL;

    CHECK_OBJECT( (PyObject *)par_eventLogType );
    Py_DECREF( par_eventLogType );
    par_eventLogType = NULL;

    Py_XDECREF( par_eventLogFlags );
    par_eventLogFlags = NULL;

    Py_XDECREF( var_hkey );
    var_hkey = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_1_AddSourceToRegistry_of_win32evtlogutil );
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


static PyObject *impl_function_2_RemoveSourceFromRegistry_of_win32evtlogutil( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_appName = python_pars[ 0 ];
    PyObject *par_eventLogType = python_pars[ 1 ];
    PyObject *var_exc = NULL;
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
    PyObject *tmp_assign_source_1;
    PyObject *tmp_called_name_1;
    int tmp_cmp_NotEq_1;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_left_2;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_compare_right_2;
    int tmp_exc_match_exception_match_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_left_name_1;
    PyObject *tmp_return_value;
    PyObject *tmp_right_name_1;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    PyObject *tmp_source_name_3;
    PyObject *tmp_source_name_4;
    PyObject *tmp_source_name_5;
    PyObject *tmp_tuple_element_1;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_a17e3f58c52d52f38410a275487e8e8d, module_win32evtlogutil );
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
    // Tried code:
    tmp_source_name_1 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_1 == NULL ))
    {
        tmp_source_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 60;
        goto try_except_handler_2;
    }

    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_RegDeleteKey );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 60;
        goto try_except_handler_2;
    }
    tmp_source_name_2 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32con );

    if (unlikely( tmp_source_name_2 == NULL ))
    {
        tmp_source_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32con );
    }

    if ( tmp_source_name_2 == NULL )
    {
        Py_DECREF( tmp_called_name_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32con" );
        exception_tb = NULL;

        exception_lineno = 60;
        goto try_except_handler_2;
    }

    tmp_args_element_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_HKEY_LOCAL_MACHINE );
    if ( tmp_args_element_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_1 );

        exception_lineno = 60;
        goto try_except_handler_2;
    }
    tmp_left_name_1 = const_str_digest_ea2d4888e032144a549f6c845bc4daf5;
    tmp_right_name_1 = PyTuple_New( 2 );
    tmp_tuple_element_1 = par_eventLogType;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_right_name_1, 0, tmp_tuple_element_1 );
    tmp_tuple_element_1 = par_appName;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_right_name_1, 1, tmp_tuple_element_1 );
    tmp_args_element_name_2 = BINARY_OPERATION_REMAINDER( tmp_left_name_1, tmp_right_name_1 );
    Py_DECREF( tmp_right_name_1 );
    if ( tmp_args_element_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_1 );
        Py_DECREF( tmp_args_element_name_1 );

        exception_lineno = 61;
        goto try_except_handler_2;
    }
    frame_function->f_lineno = 61;
    {
        PyObject *call_args[] = { tmp_args_element_name_1, tmp_args_element_name_2 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS2( tmp_called_name_1, call_args );
    }

    Py_DECREF( tmp_called_name_1 );
    Py_DECREF( tmp_args_element_name_1 );
    Py_DECREF( tmp_args_element_name_2 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 61;
        goto try_except_handler_2;
    }
    Py_DECREF( tmp_unused );
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

    // Preserve existing published exception.
    PRESERVE_FRAME_EXCEPTION( frame_function );
    if ( exception_keeper_tb_1 == NULL )
    {
        exception_keeper_tb_1 = MAKE_TRACEBACK( frame_function, exception_keeper_lineno_1 );
    }
    else if ( exception_keeper_lineno_1 != -1 )
    {
        exception_keeper_tb_1 = ADD_TRACEBACK( exception_keeper_tb_1, frame_function, exception_keeper_lineno_1 );
    }

    NORMALIZE_EXCEPTION( &exception_keeper_type_1, &exception_keeper_value_1, &exception_keeper_tb_1 );
    PUBLISH_EXCEPTION( &exception_keeper_type_1, &exception_keeper_value_1, &exception_keeper_tb_1 );
    tmp_compare_left_1 = PyThreadState_GET()->exc_type;
    tmp_source_name_3 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_3 == NULL ))
    {
        tmp_source_name_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_3 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 62;
        goto frame_exception_exit_1;
    }

    tmp_compare_right_1 = LOOKUP_ATTRIBUTE( tmp_source_name_3, const_str_plain_error );
    if ( tmp_compare_right_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 62;
        goto frame_exception_exit_1;
    }
    tmp_exc_match_exception_match_1 = EXCEPTION_MATCH_BOOL( tmp_compare_left_1, tmp_compare_right_1 );
    if ( tmp_exc_match_exception_match_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_compare_right_1 );

        exception_lineno = 62;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_compare_right_1 );
    if ( tmp_exc_match_exception_match_1 == 1 )
    {
        goto branch_yes_1;
    }
    else
    {
        goto branch_no_1;
    }
    branch_yes_1:;
    tmp_assign_source_1 = PyThreadState_GET()->exc_value;
    assert( var_exc == NULL );
    Py_INCREF( tmp_assign_source_1 );
    var_exc = tmp_assign_source_1;

    tmp_source_name_4 = var_exc;

    tmp_compare_left_2 = LOOKUP_ATTRIBUTE( tmp_source_name_4, const_str_plain_winerror );
    if ( tmp_compare_left_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 63;
        goto frame_exception_exit_1;
    }
    tmp_source_name_5 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_winerror );

    if (unlikely( tmp_source_name_5 == NULL ))
    {
        tmp_source_name_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_winerror );
    }

    if ( tmp_source_name_5 == NULL )
    {
        Py_DECREF( tmp_compare_left_2 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "winerror" );
        exception_tb = NULL;

        exception_lineno = 63;
        goto frame_exception_exit_1;
    }

    tmp_compare_right_2 = LOOKUP_ATTRIBUTE( tmp_source_name_5, const_str_plain_ERROR_FILE_NOT_FOUND );
    if ( tmp_compare_right_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_compare_left_2 );

        exception_lineno = 63;
        goto frame_exception_exit_1;
    }
    tmp_cmp_NotEq_1 = RICH_COMPARE_BOOL_NE( tmp_compare_left_2, tmp_compare_right_2 );
    if ( tmp_cmp_NotEq_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_compare_left_2 );
        Py_DECREF( tmp_compare_right_2 );

        exception_lineno = 63;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_compare_left_2 );
    Py_DECREF( tmp_compare_right_2 );
    if ( tmp_cmp_NotEq_1 == 1 )
    {
        goto branch_yes_2;
    }
    else
    {
        goto branch_no_2;
    }
    branch_yes_2:;
    RERAISE_EXCEPTION( &exception_type, &exception_value, &exception_tb );
    if (exception_tb && exception_tb->tb_frame == frame_function) frame_function->f_lineno = exception_tb->tb_lineno;
    goto frame_exception_exit_1;
    branch_no_2:;
    goto branch_end_1;
    branch_no_1:;
    RERAISE_EXCEPTION( &exception_type, &exception_value, &exception_tb );
    if (exception_tb && exception_tb->tb_frame == frame_function) frame_function->f_lineno = exception_tb->tb_lineno;
    goto frame_exception_exit_1;
    branch_end_1:;
    goto try_end_1;
    // exception handler codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_2_RemoveSourceFromRegistry_of_win32evtlogutil );
    return NULL;
    // End of try:
    try_end_1:;

#if 1
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
#if 1
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
            if ( par_appName )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_appName,
                    par_appName
                );

                assert( res == 0 );
            }

            if ( par_eventLogType )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_eventLogType,
                    par_eventLogType
                );

                assert( res == 0 );
            }

            if ( var_exc )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_exc,
                    var_exc
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

    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_2_RemoveSourceFromRegistry_of_win32evtlogutil );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_appName );
    Py_DECREF( par_appName );
    par_appName = NULL;

    CHECK_OBJECT( (PyObject *)par_eventLogType );
    Py_DECREF( par_eventLogType );
    par_eventLogType = NULL;

    Py_XDECREF( var_exc );
    var_exc = NULL;

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

    CHECK_OBJECT( (PyObject *)par_appName );
    Py_DECREF( par_appName );
    par_appName = NULL;

    CHECK_OBJECT( (PyObject *)par_eventLogType );
    Py_DECREF( par_eventLogType );
    par_eventLogType = NULL;

    Py_XDECREF( var_exc );
    var_exc = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_2;
    exception_value = exception_keeper_value_2;
    exception_tb = exception_keeper_tb_2;
    exception_lineno = exception_keeper_lineno_2;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_2_RemoveSourceFromRegistry_of_win32evtlogutil );
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


static PyObject *impl_function_3_ReportEvent_of_win32evtlogutil( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_appName = python_pars[ 0 ];
    PyObject *par_eventID = python_pars[ 1 ];
    PyObject *par_eventCategory = python_pars[ 2 ];
    PyObject *par_eventType = python_pars[ 3 ];
    PyObject *par_strings = python_pars[ 4 ];
    PyObject *par_data = python_pars[ 5 ];
    PyObject *par_sid = python_pars[ 6 ];
    PyObject *var_hAppLog = NULL;
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_args_element_name_2;
    PyObject *tmp_args_element_name_3;
    PyObject *tmp_args_element_name_4;
    PyObject *tmp_args_element_name_5;
    PyObject *tmp_args_element_name_6;
    PyObject *tmp_args_element_name_7;
    PyObject *tmp_args_element_name_8;
    PyObject *tmp_args_element_name_9;
    PyObject *tmp_args_element_name_10;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_called_name_3;
    PyObject *tmp_frame_locals;
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
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_b1a4e3bc221a84707e5ac6ce4f201129, module_win32evtlogutil );
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
    tmp_source_name_1 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog );

    if (unlikely( tmp_source_name_1 == NULL ))
    {
        tmp_source_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32evtlog );
    }

    if ( tmp_source_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32evtlog" );
        exception_tb = NULL;

        exception_lineno = 71;
        goto frame_exception_exit_1;
    }

    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_RegisterEventSource );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 71;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_1 = Py_None;
    tmp_args_element_name_2 = par_appName;

    frame_function->f_lineno = 71;
    {
        PyObject *call_args[] = { tmp_args_element_name_1, tmp_args_element_name_2 };
        tmp_assign_source_1 = CALL_FUNCTION_WITH_ARGS2( tmp_called_name_1, call_args );
    }

    Py_DECREF( tmp_called_name_1 );
    if ( tmp_assign_source_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 71;
        goto frame_exception_exit_1;
    }
    assert( var_hAppLog == NULL );
    var_hAppLog = tmp_assign_source_1;

    tmp_source_name_2 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog );

    if (unlikely( tmp_source_name_2 == NULL ))
    {
        tmp_source_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32evtlog );
    }

    if ( tmp_source_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32evtlog" );
        exception_tb = NULL;

        exception_lineno = 74;
        goto frame_exception_exit_1;
    }

    tmp_called_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_ReportEvent );
    if ( tmp_called_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 74;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_3 = var_hAppLog;

    tmp_args_element_name_4 = par_eventType;

    tmp_args_element_name_5 = par_eventCategory;

    tmp_args_element_name_6 = par_eventID;

    tmp_args_element_name_7 = par_sid;

    tmp_args_element_name_8 = par_strings;

    tmp_args_element_name_9 = par_data;

    frame_function->f_lineno = 80;
    {
        PyObject *call_args[] = { tmp_args_element_name_3, tmp_args_element_name_4, tmp_args_element_name_5, tmp_args_element_name_6, tmp_args_element_name_7, tmp_args_element_name_8, tmp_args_element_name_9 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS7( tmp_called_name_2, call_args );
    }

    Py_DECREF( tmp_called_name_2 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 80;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_source_name_3 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog );

    if (unlikely( tmp_source_name_3 == NULL ))
    {
        tmp_source_name_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32evtlog );
    }

    if ( tmp_source_name_3 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32evtlog" );
        exception_tb = NULL;

        exception_lineno = 82;
        goto frame_exception_exit_1;
    }

    tmp_called_name_3 = LOOKUP_ATTRIBUTE( tmp_source_name_3, const_str_plain_DeregisterEventSource );
    if ( tmp_called_name_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 82;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_10 = var_hAppLog;

    frame_function->f_lineno = 82;
    {
        PyObject *call_args[] = { tmp_args_element_name_10 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_3, call_args );
    }

    Py_DECREF( tmp_called_name_3 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 82;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );

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
            if ( par_appName )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_appName,
                    par_appName
                );

                assert( res == 0 );
            }

            if ( par_eventID )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_eventID,
                    par_eventID
                );

                assert( res == 0 );
            }

            if ( par_eventCategory )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_eventCategory,
                    par_eventCategory
                );

                assert( res == 0 );
            }

            if ( par_eventType )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_eventType,
                    par_eventType
                );

                assert( res == 0 );
            }

            if ( par_strings )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_strings,
                    par_strings
                );

                assert( res == 0 );
            }

            if ( par_data )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_data,
                    par_data
                );

                assert( res == 0 );
            }

            if ( par_sid )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_sid,
                    par_sid
                );

                assert( res == 0 );
            }

            if ( var_hAppLog )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_hAppLog,
                    var_hAppLog
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

    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_3_ReportEvent_of_win32evtlogutil );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_appName );
    Py_DECREF( par_appName );
    par_appName = NULL;

    CHECK_OBJECT( (PyObject *)par_eventID );
    Py_DECREF( par_eventID );
    par_eventID = NULL;

    CHECK_OBJECT( (PyObject *)par_eventCategory );
    Py_DECREF( par_eventCategory );
    par_eventCategory = NULL;

    CHECK_OBJECT( (PyObject *)par_eventType );
    Py_DECREF( par_eventType );
    par_eventType = NULL;

    CHECK_OBJECT( (PyObject *)par_strings );
    Py_DECREF( par_strings );
    par_strings = NULL;

    CHECK_OBJECT( (PyObject *)par_data );
    Py_DECREF( par_data );
    par_data = NULL;

    CHECK_OBJECT( (PyObject *)par_sid );
    Py_DECREF( par_sid );
    par_sid = NULL;

    CHECK_OBJECT( (PyObject *)var_hAppLog );
    Py_DECREF( var_hAppLog );
    var_hAppLog = NULL;

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

    CHECK_OBJECT( (PyObject *)par_appName );
    Py_DECREF( par_appName );
    par_appName = NULL;

    CHECK_OBJECT( (PyObject *)par_eventID );
    Py_DECREF( par_eventID );
    par_eventID = NULL;

    CHECK_OBJECT( (PyObject *)par_eventCategory );
    Py_DECREF( par_eventCategory );
    par_eventCategory = NULL;

    CHECK_OBJECT( (PyObject *)par_eventType );
    Py_DECREF( par_eventType );
    par_eventType = NULL;

    CHECK_OBJECT( (PyObject *)par_strings );
    Py_DECREF( par_strings );
    par_strings = NULL;

    CHECK_OBJECT( (PyObject *)par_data );
    Py_DECREF( par_data );
    par_data = NULL;

    CHECK_OBJECT( (PyObject *)par_sid );
    Py_DECREF( par_sid );
    par_sid = NULL;

    Py_XDECREF( var_hAppLog );
    var_hAppLog = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_3_ReportEvent_of_win32evtlogutil );
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


static PyObject *impl_function_4_FormatMessage_of_win32evtlogutil( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_eventLogRecord = python_pars[ 0 ];
    PyObject *par_logType = python_pars[ 1 ];
    PyObject *var_keyName = NULL;
    PyObject *var_handle = NULL;
    PyObject *var_dllNames = NULL;
    PyObject *var_data = NULL;
    PyObject *var_dllName = NULL;
    PyObject *var_dllHandle = NULL;
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
    PyObject *exception_keeper_type_3;
    PyObject *exception_keeper_value_3;
    PyTracebackObject *exception_keeper_tb_3;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_3;
    PyObject *exception_keeper_type_4;
    PyObject *exception_keeper_value_4;
    PyTracebackObject *exception_keeper_tb_4;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_4;
    PyObject *exception_keeper_type_5;
    PyObject *exception_keeper_value_5;
    PyTracebackObject *exception_keeper_tb_5;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_5;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_args_element_name_2;
    PyObject *tmp_args_element_name_3;
    PyObject *tmp_args_element_name_4;
    PyObject *tmp_args_element_name_5;
    PyObject *tmp_args_element_name_6;
    PyObject *tmp_args_element_name_7;
    PyObject *tmp_args_element_name_8;
    PyObject *tmp_args_element_name_9;
    PyObject *tmp_args_element_name_10;
    PyObject *tmp_args_element_name_11;
    PyObject *tmp_args_element_name_12;
    PyObject *tmp_args_element_name_13;
    PyObject *tmp_args_element_name_14;
    PyObject *tmp_args_element_name_15;
    PyObject *tmp_args_element_name_16;
    PyObject *tmp_args_element_name_17;
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
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_called_name_3;
    PyObject *tmp_called_name_4;
    PyObject *tmp_called_name_5;
    PyObject *tmp_called_name_6;
    PyObject *tmp_called_name_7;
    PyObject *tmp_called_name_8;
    PyObject *tmp_called_name_9;
    PyObject *tmp_called_name_10;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_left_2;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_compare_right_2;
    int tmp_exc_match_exception_match_1;
    PyObject *tmp_frame_locals;
    bool tmp_isnot_1;
    PyObject *tmp_iter_arg_1;
    PyObject *tmp_left_name_1;
    PyObject *tmp_next_source_1;
    int tmp_or_left_truth_1;
    PyObject *tmp_or_left_value_1;
    PyObject *tmp_or_right_value_1;
    PyObject *tmp_return_value;
    PyObject *tmp_right_name_1;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    PyObject *tmp_source_name_3;
    PyObject *tmp_source_name_4;
    PyObject *tmp_source_name_5;
    PyObject *tmp_source_name_6;
    PyObject *tmp_source_name_7;
    PyObject *tmp_source_name_8;
    PyObject *tmp_source_name_9;
    PyObject *tmp_source_name_10;
    PyObject *tmp_source_name_11;
    PyObject *tmp_source_name_12;
    PyObject *tmp_source_name_13;
    PyObject *tmp_source_name_14;
    PyObject *tmp_source_name_15;
    PyObject *tmp_source_name_16;
    PyObject *tmp_source_name_17;
    PyObject *tmp_subscribed_name_1;
    PyObject *tmp_subscript_name_1;
    PyObject *tmp_tuple_element_1;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_35a7c46c79a10f4e0265e1fea4b9e5e8, module_win32evtlogutil );
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
    tmp_left_name_1 = const_str_digest_ea2d4888e032144a549f6c845bc4daf5;
    tmp_right_name_1 = PyTuple_New( 2 );
    tmp_tuple_element_1 = par_logType;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_right_name_1, 0, tmp_tuple_element_1 );
    tmp_source_name_1 = par_eventLogRecord;

    tmp_tuple_element_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_SourceName );
    if ( tmp_tuple_element_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_right_name_1 );

        exception_lineno = 97;
        goto frame_exception_exit_1;
    }
    PyTuple_SET_ITEM( tmp_right_name_1, 1, tmp_tuple_element_1 );
    tmp_assign_source_1 = BINARY_OPERATION_REMAINDER( tmp_left_name_1, tmp_right_name_1 );
    Py_DECREF( tmp_right_name_1 );
    if ( tmp_assign_source_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 97;
        goto frame_exception_exit_1;
    }
    assert( var_keyName == NULL );
    var_keyName = tmp_assign_source_1;

    tmp_source_name_2 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_2 == NULL ))
    {
        tmp_source_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 101;
        goto frame_exception_exit_1;
    }

    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_RegOpenKey );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 101;
        goto frame_exception_exit_1;
    }
    tmp_source_name_3 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32con );

    if (unlikely( tmp_source_name_3 == NULL ))
    {
        tmp_source_name_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32con );
    }

    if ( tmp_source_name_3 == NULL )
    {
        Py_DECREF( tmp_called_name_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32con" );
        exception_tb = NULL;

        exception_lineno = 101;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_3, const_str_plain_HKEY_LOCAL_MACHINE );
    if ( tmp_args_element_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_1 );

        exception_lineno = 101;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_2 = var_keyName;

    frame_function->f_lineno = 101;
    {
        PyObject *call_args[] = { tmp_args_element_name_1, tmp_args_element_name_2 };
        tmp_assign_source_2 = CALL_FUNCTION_WITH_ARGS2( tmp_called_name_1, call_args );
    }

    Py_DECREF( tmp_called_name_1 );
    Py_DECREF( tmp_args_element_name_1 );
    if ( tmp_assign_source_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 101;
        goto frame_exception_exit_1;
    }
    assert( var_handle == NULL );
    var_handle = tmp_assign_source_2;

    // Tried code:
    tmp_source_name_5 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_5 == NULL ))
    {
        tmp_source_name_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_5 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 103;
        goto try_except_handler_2;
    }

    tmp_called_name_3 = LOOKUP_ATTRIBUTE( tmp_source_name_5, const_str_plain_RegQueryValueEx );
    if ( tmp_called_name_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 103;
        goto try_except_handler_2;
    }
    tmp_args_element_name_3 = var_handle;

    tmp_args_element_name_4 = const_str_plain_EventMessageFile;
    frame_function->f_lineno = 103;
    {
        PyObject *call_args[] = { tmp_args_element_name_3, tmp_args_element_name_4 };
        tmp_subscribed_name_1 = CALL_FUNCTION_WITH_ARGS2( tmp_called_name_3, call_args );
    }

    Py_DECREF( tmp_called_name_3 );
    if ( tmp_subscribed_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 103;
        goto try_except_handler_2;
    }
    tmp_subscript_name_1 = const_int_0;
    tmp_source_name_4 = LOOKUP_SUBSCRIPT( tmp_subscribed_name_1, tmp_subscript_name_1 );
    Py_DECREF( tmp_subscribed_name_1 );
    if ( tmp_source_name_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 103;
        goto try_except_handler_2;
    }
    tmp_called_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_4, const_str_plain_split );
    Py_DECREF( tmp_source_name_4 );
    if ( tmp_called_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 103;
        goto try_except_handler_2;
    }
    frame_function->f_lineno = 103;
    tmp_assign_source_3 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_2, &PyTuple_GET_ITEM( const_tuple_str_chr_59_tuple, 0 ) );

    Py_DECREF( tmp_called_name_2 );
    if ( tmp_assign_source_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 103;
        goto try_except_handler_2;
    }
    assert( var_dllNames == NULL );
    var_dllNames = tmp_assign_source_3;

    tmp_assign_source_4 = Py_None;
    assert( var_data == NULL );
    Py_INCREF( tmp_assign_source_4 );
    var_data = tmp_assign_source_4;

    tmp_iter_arg_1 = var_dllNames;

    tmp_assign_source_5 = MAKE_ITERATOR( tmp_iter_arg_1 );
    if ( tmp_assign_source_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 106;
        goto try_except_handler_2;
    }
    assert( tmp_for_loop_1__for_iterator == NULL );
    tmp_for_loop_1__for_iterator = tmp_assign_source_5;

    // Tried code:
    loop_start_1:;
    tmp_next_source_1 = tmp_for_loop_1__for_iterator;

    tmp_assign_source_6 = ITERATOR_NEXT( tmp_next_source_1 );
    if ( tmp_assign_source_6 == NULL )
    {
        if ( CHECK_AND_CLEAR_STOP_ITERATION_OCCURRED() )
        {

            goto loop_end_1;
        }
        else
        {

            FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
            frame_function->f_lineno = 106;
            goto try_except_handler_3;
        }
    }

    {
        PyObject *old = tmp_for_loop_1__iter_value;
        tmp_for_loop_1__iter_value = tmp_assign_source_6;
        Py_XDECREF( old );
    }

    tmp_assign_source_7 = tmp_for_loop_1__iter_value;

    {
        PyObject *old = var_dllName;
        var_dllName = tmp_assign_source_7;
        Py_INCREF( var_dllName );
        Py_XDECREF( old );
    }

    // Tried code:
    tmp_source_name_6 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_6 == NULL ))
    {
        tmp_source_name_6 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_6 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 110;
        goto try_except_handler_4;
    }

    tmp_called_name_4 = LOOKUP_ATTRIBUTE( tmp_source_name_6, const_str_plain_ExpandEnvironmentStrings );
    if ( tmp_called_name_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 110;
        goto try_except_handler_4;
    }
    tmp_args_element_name_5 = var_dllName;

    frame_function->f_lineno = 110;
    {
        PyObject *call_args[] = { tmp_args_element_name_5 };
        tmp_assign_source_8 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_4, call_args );
    }

    Py_DECREF( tmp_called_name_4 );
    if ( tmp_assign_source_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 110;
        goto try_except_handler_4;
    }
    {
        PyObject *old = var_dllName;
        assert( old != NULL );
        var_dllName = tmp_assign_source_8;
        Py_DECREF( old );
    }

    tmp_source_name_7 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_7 == NULL ))
    {
        tmp_source_name_7 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_7 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 112;
        goto try_except_handler_4;
    }

    tmp_called_name_5 = LOOKUP_ATTRIBUTE( tmp_source_name_7, const_str_plain_LoadLibraryEx );
    if ( tmp_called_name_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 112;
        goto try_except_handler_4;
    }
    tmp_args_element_name_6 = var_dllName;

    tmp_args_element_name_7 = const_int_0;
    tmp_source_name_8 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32con );

    if (unlikely( tmp_source_name_8 == NULL ))
    {
        tmp_source_name_8 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32con );
    }

    if ( tmp_source_name_8 == NULL )
    {
        Py_DECREF( tmp_called_name_5 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32con" );
        exception_tb = NULL;

        exception_lineno = 112;
        goto try_except_handler_4;
    }

    tmp_args_element_name_8 = LOOKUP_ATTRIBUTE( tmp_source_name_8, const_str_plain_LOAD_LIBRARY_AS_DATAFILE );
    if ( tmp_args_element_name_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_5 );

        exception_lineno = 112;
        goto try_except_handler_4;
    }
    frame_function->f_lineno = 112;
    {
        PyObject *call_args[] = { tmp_args_element_name_6, tmp_args_element_name_7, tmp_args_element_name_8 };
        tmp_assign_source_9 = CALL_FUNCTION_WITH_ARGS3( tmp_called_name_5, call_args );
    }

    Py_DECREF( tmp_called_name_5 );
    Py_DECREF( tmp_args_element_name_8 );
    if ( tmp_assign_source_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 112;
        goto try_except_handler_4;
    }
    {
        PyObject *old = var_dllHandle;
        var_dllHandle = tmp_assign_source_9;
        Py_XDECREF( old );
    }

    // Tried code:
    tmp_source_name_9 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_9 == NULL ))
    {
        tmp_source_name_9 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_9 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 114;
        goto try_except_handler_5;
    }

    tmp_called_name_6 = LOOKUP_ATTRIBUTE( tmp_source_name_9, const_str_plain_FormatMessageW );
    if ( tmp_called_name_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 114;
        goto try_except_handler_5;
    }
    tmp_source_name_10 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32con );

    if (unlikely( tmp_source_name_10 == NULL ))
    {
        tmp_source_name_10 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32con );
    }

    if ( tmp_source_name_10 == NULL )
    {
        Py_DECREF( tmp_called_name_6 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32con" );
        exception_tb = NULL;

        exception_lineno = 114;
        goto try_except_handler_5;
    }

    tmp_args_element_name_9 = LOOKUP_ATTRIBUTE( tmp_source_name_10, const_str_plain_FORMAT_MESSAGE_FROM_HMODULE );
    if ( tmp_args_element_name_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_6 );

        exception_lineno = 114;
        goto try_except_handler_5;
    }
    tmp_args_element_name_10 = var_dllHandle;

    tmp_source_name_11 = par_eventLogRecord;

    tmp_args_element_name_11 = LOOKUP_ATTRIBUTE( tmp_source_name_11, const_str_plain_EventID );
    if ( tmp_args_element_name_11 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_6 );
        Py_DECREF( tmp_args_element_name_9 );

        exception_lineno = 115;
        goto try_except_handler_5;
    }
    tmp_args_element_name_12 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_langid );

    if (unlikely( tmp_args_element_name_12 == NULL ))
    {
        tmp_args_element_name_12 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_langid );
    }

    if ( tmp_args_element_name_12 == NULL )
    {
        Py_DECREF( tmp_called_name_6 );
        Py_DECREF( tmp_args_element_name_9 );
        Py_DECREF( tmp_args_element_name_11 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "langid" );
        exception_tb = NULL;

        exception_lineno = 115;
        goto try_except_handler_5;
    }

    tmp_source_name_12 = par_eventLogRecord;

    tmp_args_element_name_13 = LOOKUP_ATTRIBUTE( tmp_source_name_12, const_str_plain_StringInserts );
    if ( tmp_args_element_name_13 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_6 );
        Py_DECREF( tmp_args_element_name_9 );
        Py_DECREF( tmp_args_element_name_11 );

        exception_lineno = 115;
        goto try_except_handler_5;
    }
    frame_function->f_lineno = 115;
    {
        PyObject *call_args[] = { tmp_args_element_name_9, tmp_args_element_name_10, tmp_args_element_name_11, tmp_args_element_name_12, tmp_args_element_name_13 };
        tmp_assign_source_10 = CALL_FUNCTION_WITH_ARGS5( tmp_called_name_6, call_args );
    }

    Py_DECREF( tmp_called_name_6 );
    Py_DECREF( tmp_args_element_name_9 );
    Py_DECREF( tmp_args_element_name_11 );
    Py_DECREF( tmp_args_element_name_13 );
    if ( tmp_assign_source_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 115;
        goto try_except_handler_5;
    }
    {
        PyObject *old = var_data;
        var_data = tmp_assign_source_10;
        Py_XDECREF( old );
    }

    goto try_end_1;
    // Exception handler code:
    try_except_handler_5:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    tmp_source_name_13 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_13 == NULL ))
    {
        tmp_source_name_13 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_13 == NULL )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 117;
        goto try_except_handler_4;
    }

    tmp_called_name_7 = LOOKUP_ATTRIBUTE( tmp_source_name_13, const_str_plain_FreeLibrary );
    if ( tmp_called_name_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );

        exception_lineno = 117;
        goto try_except_handler_4;
    }
    tmp_args_element_name_14 = var_dllHandle;

    frame_function->f_lineno = 117;
    {
        PyObject *call_args[] = { tmp_args_element_name_14 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_7, call_args );
    }

    Py_DECREF( tmp_called_name_7 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );

        exception_lineno = 117;
        goto try_except_handler_4;
    }
    Py_DECREF( tmp_unused );
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto try_except_handler_4;
    // End of try:
    try_end_1:;
    tmp_source_name_14 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_14 == NULL ))
    {
        tmp_source_name_14 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_14 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 117;
        goto try_except_handler_4;
    }

    tmp_called_name_8 = LOOKUP_ATTRIBUTE( tmp_source_name_14, const_str_plain_FreeLibrary );
    if ( tmp_called_name_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 117;
        goto try_except_handler_4;
    }
    tmp_args_element_name_15 = var_dllHandle;

    frame_function->f_lineno = 117;
    {
        PyObject *call_args[] = { tmp_args_element_name_15 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_8, call_args );
    }

    Py_DECREF( tmp_called_name_8 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 117;
        goto try_except_handler_4;
    }
    Py_DECREF( tmp_unused );
    goto try_end_2;
    // Exception handler code:
    try_except_handler_4:;
    exception_keeper_type_2 = exception_type;
    exception_keeper_value_2 = exception_value;
    exception_keeper_tb_2 = exception_tb;
    exception_keeper_lineno_2 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    // Preserve existing published exception.
    PRESERVE_FRAME_EXCEPTION( frame_function );
    if ( exception_keeper_tb_2 == NULL )
    {
        exception_keeper_tb_2 = MAKE_TRACEBACK( frame_function, exception_keeper_lineno_2 );
    }
    else if ( exception_keeper_lineno_2 != -1 )
    {
        exception_keeper_tb_2 = ADD_TRACEBACK( exception_keeper_tb_2, frame_function, exception_keeper_lineno_2 );
    }

    NORMALIZE_EXCEPTION( &exception_keeper_type_2, &exception_keeper_value_2, &exception_keeper_tb_2 );
    PUBLISH_EXCEPTION( &exception_keeper_type_2, &exception_keeper_value_2, &exception_keeper_tb_2 );
    tmp_compare_left_1 = PyThreadState_GET()->exc_type;
    tmp_source_name_15 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_15 == NULL ))
    {
        tmp_source_name_15 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_15 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 118;
        goto try_except_handler_3;
    }

    tmp_compare_right_1 = LOOKUP_ATTRIBUTE( tmp_source_name_15, const_str_plain_error );
    if ( tmp_compare_right_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 118;
        goto try_except_handler_3;
    }
    tmp_exc_match_exception_match_1 = EXCEPTION_MATCH_BOOL( tmp_compare_left_1, tmp_compare_right_1 );
    if ( tmp_exc_match_exception_match_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_compare_right_1 );

        exception_lineno = 118;
        goto try_except_handler_3;
    }
    Py_DECREF( tmp_compare_right_1 );
    if ( tmp_exc_match_exception_match_1 == 1 )
    {
        goto branch_no_1;
    }
    else
    {
        goto branch_yes_1;
    }
    branch_yes_1:;
    RERAISE_EXCEPTION( &exception_type, &exception_value, &exception_tb );
    if (exception_tb && exception_tb->tb_frame == frame_function) frame_function->f_lineno = exception_tb->tb_lineno;
    goto try_except_handler_3;
    branch_no_1:;
    goto try_end_2;
    // exception handler codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_4_FormatMessage_of_win32evtlogutil );
    return NULL;
    // End of try:
    try_end_2:;
    tmp_compare_left_2 = var_data;

    if ( tmp_compare_left_2 == NULL )
    {

        exception_type = PyExc_UnboundLocalError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "local variable '%s' referenced before assignment", "data" );
        exception_tb = NULL;

        exception_lineno = 120;
        goto try_except_handler_3;
    }

    tmp_compare_right_2 = Py_None;
    tmp_isnot_1 = ( tmp_compare_left_2 != tmp_compare_right_2 );
    if ( tmp_isnot_1 )
    {
        goto branch_yes_2;
    }
    else
    {
        goto branch_no_2;
    }
    branch_yes_2:;
    goto loop_end_1;
    branch_no_2:;
    if ( CONSIDER_THREADING() == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 106;
        goto try_except_handler_3;
    }
    goto loop_start_1;
    loop_end_1:;
    goto try_end_3;
    // Exception handler code:
    try_except_handler_3:;
    exception_keeper_type_3 = exception_type;
    exception_keeper_value_3 = exception_value;
    exception_keeper_tb_3 = exception_tb;
    exception_keeper_lineno_3 = exception_lineno;
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
    exception_type = exception_keeper_type_3;
    exception_value = exception_keeper_value_3;
    exception_tb = exception_keeper_tb_3;
    exception_lineno = exception_keeper_lineno_3;

    goto try_except_handler_2;
    // End of try:
    try_end_3:;
    goto try_end_4;
    // Exception handler code:
    try_except_handler_2:;
    exception_keeper_type_4 = exception_type;
    exception_keeper_value_4 = exception_value;
    exception_keeper_tb_4 = exception_tb;
    exception_keeper_lineno_4 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    tmp_source_name_16 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_16 == NULL ))
    {
        tmp_source_name_16 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_16 == NULL )
    {

        Py_DECREF( exception_keeper_type_4 );
        Py_XDECREF( exception_keeper_value_4 );
        Py_XDECREF( exception_keeper_tb_4 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 123;
        goto frame_exception_exit_1;
    }

    tmp_called_name_9 = LOOKUP_ATTRIBUTE( tmp_source_name_16, const_str_plain_RegCloseKey );
    if ( tmp_called_name_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );

        Py_DECREF( exception_keeper_type_4 );
        Py_XDECREF( exception_keeper_value_4 );
        Py_XDECREF( exception_keeper_tb_4 );

        exception_lineno = 123;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_16 = var_handle;

    frame_function->f_lineno = 123;
    {
        PyObject *call_args[] = { tmp_args_element_name_16 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_9, call_args );
    }

    Py_DECREF( tmp_called_name_9 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );

        Py_DECREF( exception_keeper_type_4 );
        Py_XDECREF( exception_keeper_value_4 );
        Py_XDECREF( exception_keeper_tb_4 );

        exception_lineno = 123;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    // Re-raise.
    exception_type = exception_keeper_type_4;
    exception_value = exception_keeper_value_4;
    exception_tb = exception_keeper_tb_4;
    exception_lineno = exception_keeper_lineno_4;

    goto frame_exception_exit_1;
    // End of try:
    try_end_4:;
    Py_XDECREF( tmp_for_loop_1__iter_value );
    tmp_for_loop_1__iter_value = NULL;

    CHECK_OBJECT( (PyObject *)tmp_for_loop_1__for_iterator );
    Py_DECREF( tmp_for_loop_1__for_iterator );
    tmp_for_loop_1__for_iterator = NULL;

    tmp_source_name_17 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_17 == NULL ))
    {
        tmp_source_name_17 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_17 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 123;
        goto frame_exception_exit_1;
    }

    tmp_called_name_10 = LOOKUP_ATTRIBUTE( tmp_source_name_17, const_str_plain_RegCloseKey );
    if ( tmp_called_name_10 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 123;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_17 = var_handle;

    frame_function->f_lineno = 123;
    {
        PyObject *call_args[] = { tmp_args_element_name_17 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_10, call_args );
    }

    Py_DECREF( tmp_called_name_10 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 123;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_or_left_value_1 = var_data;

    if ( tmp_or_left_value_1 == NULL )
    {

        exception_type = PyExc_UnboundLocalError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "local variable '%s' referenced before assignment", "data" );
        exception_tb = NULL;

        exception_lineno = 124;
        goto frame_exception_exit_1;
    }

    tmp_or_left_truth_1 = CHECK_IF_TRUE( tmp_or_left_value_1 );
    if ( tmp_or_left_truth_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 124;
        goto frame_exception_exit_1;
    }
    if ( tmp_or_left_truth_1 == 1 )
    {
        goto or_left_1;
    }
    else
    {
        goto or_right_1;
    }
    or_right_1:;
    tmp_or_right_value_1 = const_unicode_empty;
    tmp_return_value = tmp_or_right_value_1;
    goto or_end_1;
    or_left_1:;
    tmp_return_value = tmp_or_left_value_1;
    or_end_1:;
    Py_INCREF( tmp_return_value );
    goto frame_return_exit_1;

#if 1
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
#if 1
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto try_return_handler_1;

    frame_exception_exit_1:;
#if 1
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
            if ( par_eventLogRecord )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_eventLogRecord,
                    par_eventLogRecord
                );

                assert( res == 0 );
            }

            if ( par_logType )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_logType,
                    par_logType
                );

                assert( res == 0 );
            }

            if ( var_keyName )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_keyName,
                    var_keyName
                );

                assert( res == 0 );
            }

            if ( var_handle )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_handle,
                    var_handle
                );

                assert( res == 0 );
            }

            if ( var_dllNames )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_dllNames,
                    var_dllNames
                );

                assert( res == 0 );
            }

            if ( var_data )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_data,
                    var_data
                );

                assert( res == 0 );
            }

            if ( var_dllName )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_dllName,
                    var_dllName
                );

                assert( res == 0 );
            }

            if ( var_dllHandle )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_dllHandle,
                    var_dllHandle
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
    NUITKA_CANNOT_GET_HERE( function_4_FormatMessage_of_win32evtlogutil );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_eventLogRecord );
    Py_DECREF( par_eventLogRecord );
    par_eventLogRecord = NULL;

    CHECK_OBJECT( (PyObject *)par_logType );
    Py_DECREF( par_logType );
    par_logType = NULL;

    CHECK_OBJECT( (PyObject *)var_keyName );
    Py_DECREF( var_keyName );
    var_keyName = NULL;

    CHECK_OBJECT( (PyObject *)var_handle );
    Py_DECREF( var_handle );
    var_handle = NULL;

    CHECK_OBJECT( (PyObject *)var_dllNames );
    Py_DECREF( var_dllNames );
    var_dllNames = NULL;

    Py_XDECREF( var_data );
    var_data = NULL;

    Py_XDECREF( var_dllName );
    var_dllName = NULL;

    Py_XDECREF( var_dllHandle );
    var_dllHandle = NULL;

    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_5 = exception_type;
    exception_keeper_value_5 = exception_value;
    exception_keeper_tb_5 = exception_tb;
    exception_keeper_lineno_5 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = -1;

    CHECK_OBJECT( (PyObject *)par_eventLogRecord );
    Py_DECREF( par_eventLogRecord );
    par_eventLogRecord = NULL;

    CHECK_OBJECT( (PyObject *)par_logType );
    Py_DECREF( par_logType );
    par_logType = NULL;

    Py_XDECREF( var_keyName );
    var_keyName = NULL;

    Py_XDECREF( var_handle );
    var_handle = NULL;

    Py_XDECREF( var_dllNames );
    var_dllNames = NULL;

    Py_XDECREF( var_data );
    var_data = NULL;

    Py_XDECREF( var_dllName );
    var_dllName = NULL;

    Py_XDECREF( var_dllHandle );
    var_dllHandle = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_5;
    exception_value = exception_keeper_value_5;
    exception_tb = exception_keeper_tb_5;
    exception_lineno = exception_keeper_lineno_5;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_4_FormatMessage_of_win32evtlogutil );
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


static PyObject *impl_function_5_SafeFormatMessage_of_win32evtlogutil( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_eventLogRecord = python_pars[ 0 ];
    PyObject *par_logType = python_pars[ 1 ];
    PyObject *var_desc = NULL;
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
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_called_name_3;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_left_2;
    PyObject *tmp_compare_left_3;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_compare_right_2;
    PyObject *tmp_compare_right_3;
    int tmp_exc_match_exception_match_1;
    PyObject *tmp_frame_locals;
    bool tmp_is_1;
    bool tmp_is_2;
    PyObject *tmp_left_name_1;
    PyObject *tmp_return_value;
    PyObject *tmp_right_name_1;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    PyObject *tmp_source_name_3;
    PyObject *tmp_source_name_4;
    PyObject *tmp_source_name_5;
    PyObject *tmp_source_name_6;
    PyObject *tmp_source_name_7;
    PyObject *tmp_tuple_element_1;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    tmp_compare_left_1 = par_logType;

    tmp_compare_right_1 = Py_None;
    tmp_is_1 = ( tmp_compare_left_1 == tmp_compare_right_1 );
    if ( tmp_is_1 )
    {
        goto branch_yes_1;
    }
    else
    {
        goto branch_no_1;
    }
    branch_yes_1:;
    tmp_assign_source_1 = const_str_plain_Application;
    {
        PyObject *old = par_logType;
        assert( old != NULL );
        par_logType = tmp_assign_source_1;
        Py_INCREF( par_logType );
        Py_DECREF( old );
    }

    branch_no_1:;
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_7cee90ab7624d8980a8341b242e3cc90, module_win32evtlogutil );
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
    // Tried code:
    tmp_called_name_1 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_FormatMessage );

    if (unlikely( tmp_called_name_1 == NULL ))
    {
        tmp_called_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_FormatMessage );
    }

    if ( tmp_called_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "FormatMessage" );
        exception_tb = NULL;

        exception_lineno = 132;
        goto try_except_handler_2;
    }

    tmp_args_element_name_1 = par_eventLogRecord;

    tmp_args_element_name_2 = par_logType;

    frame_function->f_lineno = 132;
    {
        PyObject *call_args[] = { tmp_args_element_name_1, tmp_args_element_name_2 };
        tmp_return_value = CALL_FUNCTION_WITH_ARGS2( tmp_called_name_1, call_args );
    }

    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 132;
        goto try_except_handler_2;
    }
    goto frame_return_exit_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_5_SafeFormatMessage_of_win32evtlogutil );
    return NULL;
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

    // Preserve existing published exception.
    PRESERVE_FRAME_EXCEPTION( frame_function );
    if ( exception_keeper_tb_1 == NULL )
    {
        exception_keeper_tb_1 = MAKE_TRACEBACK( frame_function, exception_keeper_lineno_1 );
    }
    else if ( exception_keeper_lineno_1 != -1 )
    {
        exception_keeper_tb_1 = ADD_TRACEBACK( exception_keeper_tb_1, frame_function, exception_keeper_lineno_1 );
    }

    NORMALIZE_EXCEPTION( &exception_keeper_type_1, &exception_keeper_value_1, &exception_keeper_tb_1 );
    PUBLISH_EXCEPTION( &exception_keeper_type_1, &exception_keeper_value_1, &exception_keeper_tb_1 );
    tmp_compare_left_2 = PyThreadState_GET()->exc_type;
    tmp_source_name_1 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_1 == NULL ))
    {
        tmp_source_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 133;
        goto frame_exception_exit_1;
    }

    tmp_compare_right_2 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_error );
    if ( tmp_compare_right_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 133;
        goto frame_exception_exit_1;
    }
    tmp_exc_match_exception_match_1 = EXCEPTION_MATCH_BOOL( tmp_compare_left_2, tmp_compare_right_2 );
    if ( tmp_exc_match_exception_match_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_compare_right_2 );

        exception_lineno = 133;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_compare_right_2 );
    if ( tmp_exc_match_exception_match_1 == 1 )
    {
        goto branch_yes_2;
    }
    else
    {
        goto branch_no_2;
    }
    branch_yes_2:;
    tmp_source_name_2 = par_eventLogRecord;

    tmp_compare_left_3 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_StringInserts );
    if ( tmp_compare_left_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 134;
        goto frame_exception_exit_1;
    }
    tmp_compare_right_3 = Py_None;
    tmp_is_2 = ( tmp_compare_left_3 == tmp_compare_right_3 );
    Py_DECREF( tmp_compare_left_3 );
    if ( tmp_is_2 )
    {
        goto branch_yes_3;
    }
    else
    {
        goto branch_no_3;
    }
    branch_yes_3:;
    tmp_assign_source_2 = const_str_empty;
    assert( var_desc == NULL );
    Py_INCREF( tmp_assign_source_2 );
    var_desc = tmp_assign_source_2;

    goto branch_end_3;
    branch_no_3:;
    tmp_source_name_3 = const_unicode_digest_db35ab94a03c3cbeb13cbe2a1d728b77;
    tmp_called_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_3, const_str_plain_join );
    assert( tmp_called_name_2 != NULL );
    tmp_source_name_4 = par_eventLogRecord;

    tmp_args_element_name_3 = LOOKUP_ATTRIBUTE( tmp_source_name_4, const_str_plain_StringInserts );
    if ( tmp_args_element_name_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_2 );

        exception_lineno = 137;
        goto frame_exception_exit_1;
    }
    frame_function->f_lineno = 137;
    {
        PyObject *call_args[] = { tmp_args_element_name_3 };
        tmp_assign_source_3 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_2, call_args );
    }

    Py_DECREF( tmp_called_name_2 );
    Py_DECREF( tmp_args_element_name_3 );
    if ( tmp_assign_source_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 137;
        goto frame_exception_exit_1;
    }
    assert( var_desc == NULL );
    var_desc = tmp_assign_source_3;

    branch_end_3:;
    tmp_left_name_1 = const_unicode_digest_863683e3a5be671913b94c371b27c7ba;
    tmp_right_name_1 = PyTuple_New( 3 );
    tmp_source_name_5 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_winerror );

    if (unlikely( tmp_source_name_5 == NULL ))
    {
        tmp_source_name_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_winerror );
    }

    if ( tmp_source_name_5 == NULL )
    {
        Py_DECREF( tmp_right_name_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "winerror" );
        exception_tb = NULL;

        exception_lineno = 138;
        goto frame_exception_exit_1;
    }

    tmp_called_name_3 = LOOKUP_ATTRIBUTE( tmp_source_name_5, const_str_plain_HRESULT_CODE );
    if ( tmp_called_name_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_right_name_1 );

        exception_lineno = 138;
        goto frame_exception_exit_1;
    }
    tmp_source_name_6 = par_eventLogRecord;

    tmp_args_element_name_4 = LOOKUP_ATTRIBUTE( tmp_source_name_6, const_str_plain_EventID );
    if ( tmp_args_element_name_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_right_name_1 );
        Py_DECREF( tmp_called_name_3 );

        exception_lineno = 138;
        goto frame_exception_exit_1;
    }
    frame_function->f_lineno = 138;
    {
        PyObject *call_args[] = { tmp_args_element_name_4 };
        tmp_tuple_element_1 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_3, call_args );
    }

    Py_DECREF( tmp_called_name_3 );
    Py_DECREF( tmp_args_element_name_4 );
    if ( tmp_tuple_element_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_right_name_1 );

        exception_lineno = 138;
        goto frame_exception_exit_1;
    }
    PyTuple_SET_ITEM( tmp_right_name_1, 0, tmp_tuple_element_1 );
    tmp_source_name_7 = par_eventLogRecord;

    tmp_tuple_element_1 = LOOKUP_ATTRIBUTE( tmp_source_name_7, const_str_plain_SourceName );
    if ( tmp_tuple_element_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_right_name_1 );

        exception_lineno = 138;
        goto frame_exception_exit_1;
    }
    PyTuple_SET_ITEM( tmp_right_name_1, 1, tmp_tuple_element_1 );
    tmp_tuple_element_1 = var_desc;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_right_name_1, 2, tmp_tuple_element_1 );
    tmp_return_value = BINARY_OPERATION_REMAINDER( tmp_left_name_1, tmp_right_name_1 );
    Py_DECREF( tmp_right_name_1 );
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 138;
        goto frame_exception_exit_1;
    }
    goto frame_return_exit_1;
    goto branch_end_2;
    branch_no_2:;
    RERAISE_EXCEPTION( &exception_type, &exception_value, &exception_tb );
    if (exception_tb && exception_tb->tb_frame == frame_function) frame_function->f_lineno = exception_tb->tb_lineno;
    goto frame_exception_exit_1;
    branch_end_2:;
    // End of try:

#if 1
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
#if 1
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto try_return_handler_1;

    frame_exception_exit_1:;
#if 1
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
            if ( par_eventLogRecord )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_eventLogRecord,
                    par_eventLogRecord
                );

                assert( res == 0 );
            }

            if ( par_logType )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_logType,
                    par_logType
                );

                assert( res == 0 );
            }

            if ( var_desc )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_desc,
                    var_desc
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
    NUITKA_CANNOT_GET_HERE( function_5_SafeFormatMessage_of_win32evtlogutil );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_eventLogRecord );
    Py_DECREF( par_eventLogRecord );
    par_eventLogRecord = NULL;

    CHECK_OBJECT( (PyObject *)par_logType );
    Py_DECREF( par_logType );
    par_logType = NULL;

    Py_XDECREF( var_desc );
    var_desc = NULL;

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

    CHECK_OBJECT( (PyObject *)par_eventLogRecord );
    Py_DECREF( par_eventLogRecord );
    par_eventLogRecord = NULL;

    CHECK_OBJECT( (PyObject *)par_logType );
    Py_DECREF( par_logType );
    par_logType = NULL;

    Py_XDECREF( var_desc );
    var_desc = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_2;
    exception_value = exception_keeper_value_2;
    exception_tb = exception_keeper_tb_2;
    exception_lineno = exception_keeper_lineno_2;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_5_SafeFormatMessage_of_win32evtlogutil );
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


static PyObject *impl_function_6_FeedEventLogRecords_of_win32evtlogutil( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_feeder = python_pars[ 0 ];
    PyObject *par_machineName = python_pars[ 1 ];
    PyObject *par_logName = python_pars[ 2 ];
    PyObject *par_readFlags = python_pars[ 3 ];
    PyObject *var_h = NULL;
    PyObject *var_objects = NULL;
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
    PyObject *tmp_args_element_name_6;
    PyObject *tmp_args_element_name_7;
    PyObject *tmp_args_element_name_8;
    PyObject *tmp_args_element_name_9;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_called_name_3;
    PyObject *tmp_called_name_4;
    PyObject *tmp_called_name_5;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_right_1;
    int tmp_cond_truth_1;
    PyObject *tmp_cond_value_1;
    PyObject *tmp_defaults_1;
    PyObject *tmp_frame_locals;
    bool tmp_is_1;
    PyObject *tmp_left_name_1;
    PyObject *tmp_return_value;
    PyObject *tmp_right_name_1;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    PyObject *tmp_source_name_3;
    PyObject *tmp_source_name_4;
    PyObject *tmp_source_name_5;
    PyObject *tmp_source_name_6;
    PyObject *tmp_tuple_element_1;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_366d412a45eef79bfd41a727819b2246, module_win32evtlogutil );
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
    tmp_compare_left_1 = par_readFlags;

    tmp_compare_right_1 = Py_None;
    tmp_is_1 = ( tmp_compare_left_1 == tmp_compare_right_1 );
    if ( tmp_is_1 )
    {
        goto branch_yes_1;
    }
    else
    {
        goto branch_no_1;
    }
    branch_yes_1:;
    tmp_source_name_1 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog );

    if (unlikely( tmp_source_name_1 == NULL ))
    {
        tmp_source_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32evtlog );
    }

    if ( tmp_source_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32evtlog" );
        exception_tb = NULL;

        exception_lineno = 142;
        goto frame_exception_exit_1;
    }

    tmp_left_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_EVENTLOG_BACKWARDS_READ );
    if ( tmp_left_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 142;
        goto frame_exception_exit_1;
    }
    tmp_source_name_2 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog );

    if (unlikely( tmp_source_name_2 == NULL ))
    {
        tmp_source_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32evtlog );
    }

    if ( tmp_source_name_2 == NULL )
    {
        Py_DECREF( tmp_left_name_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32evtlog" );
        exception_tb = NULL;

        exception_lineno = 142;
        goto frame_exception_exit_1;
    }

    tmp_right_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_EVENTLOG_SEQUENTIAL_READ );
    if ( tmp_right_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_left_name_1 );

        exception_lineno = 142;
        goto frame_exception_exit_1;
    }
    tmp_assign_source_1 = BINARY_OPERATION( PyNumber_Or, tmp_left_name_1, tmp_right_name_1 );
    Py_DECREF( tmp_left_name_1 );
    Py_DECREF( tmp_right_name_1 );
    if ( tmp_assign_source_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 142;
        goto frame_exception_exit_1;
    }
    {
        PyObject *old = par_readFlags;
        assert( old != NULL );
        par_readFlags = tmp_assign_source_1;
        Py_DECREF( old );
    }

    branch_no_1:;
    tmp_source_name_3 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog );

    if (unlikely( tmp_source_name_3 == NULL ))
    {
        tmp_source_name_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32evtlog );
    }

    if ( tmp_source_name_3 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32evtlog" );
        exception_tb = NULL;

        exception_lineno = 144;
        goto frame_exception_exit_1;
    }

    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_3, const_str_plain_OpenEventLog );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 144;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_1 = par_machineName;

    tmp_args_element_name_2 = par_logName;

    frame_function->f_lineno = 144;
    {
        PyObject *call_args[] = { tmp_args_element_name_1, tmp_args_element_name_2 };
        tmp_assign_source_2 = CALL_FUNCTION_WITH_ARGS2( tmp_called_name_1, call_args );
    }

    Py_DECREF( tmp_called_name_1 );
    if ( tmp_assign_source_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 144;
        goto frame_exception_exit_1;
    }
    assert( var_h == NULL );
    var_h = tmp_assign_source_2;

    // Tried code:
    loop_start_1:;
    tmp_source_name_4 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog );

    if (unlikely( tmp_source_name_4 == NULL ))
    {
        tmp_source_name_4 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32evtlog );
    }

    if ( tmp_source_name_4 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32evtlog" );
        exception_tb = NULL;

        exception_lineno = 147;
        goto try_except_handler_2;
    }

    tmp_called_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_4, const_str_plain_ReadEventLog );
    if ( tmp_called_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 147;
        goto try_except_handler_2;
    }
    tmp_args_element_name_3 = var_h;

    tmp_args_element_name_4 = par_readFlags;

    tmp_args_element_name_5 = const_int_0;
    frame_function->f_lineno = 147;
    {
        PyObject *call_args[] = { tmp_args_element_name_3, tmp_args_element_name_4, tmp_args_element_name_5 };
        tmp_assign_source_3 = CALL_FUNCTION_WITH_ARGS3( tmp_called_name_2, call_args );
    }

    Py_DECREF( tmp_called_name_2 );
    if ( tmp_assign_source_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 147;
        goto try_except_handler_2;
    }
    {
        PyObject *old = var_objects;
        var_objects = tmp_assign_source_3;
        Py_XDECREF( old );
    }

    tmp_cond_value_1 = var_objects;

    tmp_cond_truth_1 = CHECK_IF_TRUE( tmp_cond_value_1 );
    if ( tmp_cond_truth_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 148;
        goto try_except_handler_2;
    }
    if ( tmp_cond_truth_1 == 1 )
    {
        goto branch_no_2;
    }
    else
    {
        goto branch_yes_2;
    }
    branch_yes_2:;
    goto loop_end_1;
    branch_no_2:;
    tmp_called_name_3 = LOOKUP_BUILTIN( const_str_plain_map );
    assert( tmp_called_name_3 != NULL );
    tmp_defaults_1 = PyTuple_New( 1 );
    tmp_tuple_element_1 = par_feeder;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_defaults_1, 0, tmp_tuple_element_1 );
    tmp_args_element_name_6 = MAKE_FUNCTION_function_1_lambda_of_function_6_FeedEventLogRecords_of_win32evtlogutil( tmp_defaults_1 );
    tmp_args_element_name_7 = var_objects;

    frame_function->f_lineno = 150;
    {
        PyObject *call_args[] = { tmp_args_element_name_6, tmp_args_element_name_7 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS2( tmp_called_name_3, call_args );
    }

    Py_DECREF( tmp_args_element_name_6 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 150;
        goto try_except_handler_2;
    }
    Py_DECREF( tmp_unused );
    if ( CONSIDER_THREADING() == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 146;
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

    tmp_source_name_5 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog );

    if (unlikely( tmp_source_name_5 == NULL ))
    {
        tmp_source_name_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32evtlog );
    }

    if ( tmp_source_name_5 == NULL )
    {

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32evtlog" );
        exception_tb = NULL;

        exception_lineno = 152;
        goto frame_exception_exit_1;
    }

    tmp_called_name_4 = LOOKUP_ATTRIBUTE( tmp_source_name_5, const_str_plain_CloseEventLog );
    if ( tmp_called_name_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );

        exception_lineno = 152;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_8 = var_h;

    frame_function->f_lineno = 152;
    {
        PyObject *call_args[] = { tmp_args_element_name_8 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_4, call_args );
    }

    Py_DECREF( tmp_called_name_4 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );

        Py_DECREF( exception_keeper_type_1 );
        Py_XDECREF( exception_keeper_value_1 );
        Py_XDECREF( exception_keeper_tb_1 );

        exception_lineno = 152;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto frame_exception_exit_1;
    // End of try:
    try_end_1:;
    tmp_source_name_6 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog );

    if (unlikely( tmp_source_name_6 == NULL ))
    {
        tmp_source_name_6 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32evtlog );
    }

    if ( tmp_source_name_6 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "global name '%s' is not defined", "win32evtlog" );
        exception_tb = NULL;

        exception_lineno = 152;
        goto frame_exception_exit_1;
    }

    tmp_called_name_5 = LOOKUP_ATTRIBUTE( tmp_source_name_6, const_str_plain_CloseEventLog );
    if ( tmp_called_name_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 152;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_9 = var_h;

    frame_function->f_lineno = 152;
    {
        PyObject *call_args[] = { tmp_args_element_name_9 };
        tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_5, call_args );
    }

    Py_DECREF( tmp_called_name_5 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 152;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );

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
            if ( par_feeder )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_feeder,
                    par_feeder
                );

                assert( res == 0 );
            }

            if ( par_machineName )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_machineName,
                    par_machineName
                );

                assert( res == 0 );
            }

            if ( par_logName )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_logName,
                    par_logName
                );

                assert( res == 0 );
            }

            if ( par_readFlags )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_readFlags,
                    par_readFlags
                );

                assert( res == 0 );
            }

            if ( var_h )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_h,
                    var_h
                );

                assert( res == 0 );
            }

            if ( var_objects )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_objects,
                    var_objects
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

    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( function_6_FeedEventLogRecords_of_win32evtlogutil );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_feeder );
    Py_DECREF( par_feeder );
    par_feeder = NULL;

    CHECK_OBJECT( (PyObject *)par_machineName );
    Py_DECREF( par_machineName );
    par_machineName = NULL;

    CHECK_OBJECT( (PyObject *)par_logName );
    Py_DECREF( par_logName );
    par_logName = NULL;

    CHECK_OBJECT( (PyObject *)par_readFlags );
    Py_DECREF( par_readFlags );
    par_readFlags = NULL;

    CHECK_OBJECT( (PyObject *)var_h );
    Py_DECREF( var_h );
    var_h = NULL;

    CHECK_OBJECT( (PyObject *)var_objects );
    Py_DECREF( var_objects );
    var_objects = NULL;

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

    CHECK_OBJECT( (PyObject *)par_feeder );
    Py_DECREF( par_feeder );
    par_feeder = NULL;

    CHECK_OBJECT( (PyObject *)par_machineName );
    Py_DECREF( par_machineName );
    par_machineName = NULL;

    CHECK_OBJECT( (PyObject *)par_logName );
    Py_DECREF( par_logName );
    par_logName = NULL;

    Py_XDECREF( par_readFlags );
    par_readFlags = NULL;

    Py_XDECREF( var_h );
    var_h = NULL;

    Py_XDECREF( var_objects );
    var_objects = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_2;
    exception_value = exception_keeper_value_2;
    exception_tb = exception_keeper_tb_2;
    exception_lineno = exception_keeper_lineno_2;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_6_FeedEventLogRecords_of_win32evtlogutil );
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


static PyObject *impl_function_1_lambda_of_function_6_FeedEventLogRecords_of_win32evtlogutil( Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_item = python_pars[ 0 ];
    PyObject *par_feeder = python_pars[ 1 ];
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = -1;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *tmp_dircall_arg1_1;
    PyObject *tmp_dircall_arg2_1;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    PyObject *tmp_tuple_element_1;
    static PyFrameObject *cache_frame_function = NULL;

    PyFrameObject *frame_function;

    tmp_return_value = NULL;

    // Actual function code.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_843f9cdc0334dfe4e8545a24d53ebbfd, module_win32evtlogutil );
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
    tmp_dircall_arg1_1 = par_feeder;

    tmp_dircall_arg2_1 = PyTuple_New( 1 );
    tmp_tuple_element_1 = par_item;

    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_dircall_arg2_1, 0, tmp_tuple_element_1 );
    Py_INCREF( tmp_dircall_arg1_1 );

    {
        PyObject *dir_call_args[] = {tmp_dircall_arg1_1, tmp_dircall_arg2_1};
        tmp_return_value = impl_function_2_complex_call_helper_star_list_of___internal__( dir_call_args );
    }
    if ( tmp_return_value == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 150;
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
            if ( par_item )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_item,
                    par_item
                );

                assert( res == 0 );
            }

            if ( par_feeder )
            {
                int res = PyDict_SetItem(
                    tmp_frame_locals,
                    const_str_plain_feeder,
                    par_feeder
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
    NUITKA_CANNOT_GET_HERE( function_1_lambda_of_function_6_FeedEventLogRecords_of_win32evtlogutil );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_item );
    Py_DECREF( par_item );
    par_item = NULL;

    CHECK_OBJECT( (PyObject *)par_feeder );
    Py_DECREF( par_feeder );
    par_feeder = NULL;

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

    CHECK_OBJECT( (PyObject *)par_item );
    Py_DECREF( par_item );
    par_item = NULL;

    CHECK_OBJECT( (PyObject *)par_feeder );
    Py_DECREF( par_feeder );
    par_feeder = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( function_1_lambda_of_function_6_FeedEventLogRecords_of_win32evtlogutil );
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



static PyObject *MAKE_FUNCTION_function_1_AddSourceToRegistry_of_win32evtlogutil( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_1_AddSourceToRegistry_of_win32evtlogutil,
        const_str_plain_AddSourceToRegistry,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_758d5442516f0ec97cbaf08014152191,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_win32evtlogutil,
        const_str_digest_89551213e33a0c2c1f8df3aacc402cb1
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_1_lambda_of_function_6_FeedEventLogRecords_of_win32evtlogutil( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_1_lambda_of_function_6_FeedEventLogRecords_of_win32evtlogutil,
        const_str_angle_lambda,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_843f9cdc0334dfe4e8545a24d53ebbfd,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_win32evtlogutil,
        Py_None
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_2_RemoveSourceFromRegistry_of_win32evtlogutil( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_2_RemoveSourceFromRegistry_of_win32evtlogutil,
        const_str_plain_RemoveSourceFromRegistry,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_a17e3f58c52d52f38410a275487e8e8d,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_win32evtlogutil,
        const_str_digest_a7e1d98fe6ba5cf7013769ca16110b28
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_3_ReportEvent_of_win32evtlogutil( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_3_ReportEvent_of_win32evtlogutil,
        const_str_plain_ReportEvent,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_b1a4e3bc221a84707e5ac6ce4f201129,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_win32evtlogutil,
        const_str_digest_a90d46a4d0521f7077c95aeb9e33bbf7
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_4_FormatMessage_of_win32evtlogutil( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_4_FormatMessage_of_win32evtlogutil,
        const_str_plain_FormatMessage,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_35a7c46c79a10f4e0265e1fea4b9e5e8,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_win32evtlogutil,
        const_str_digest_2578c28d01ce362f5d4d024ce24e3eb6
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_5_SafeFormatMessage_of_win32evtlogutil( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_5_SafeFormatMessage_of_win32evtlogutil,
        const_str_plain_SafeFormatMessage,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_7cee90ab7624d8980a8341b242e3cc90,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_win32evtlogutil,
        const_str_digest_a970d4942e13293b290143946644e24a
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_6_FeedEventLogRecords_of_win32evtlogutil( PyObject *defaults )
{
    PyObject *result = Nuitka_Function_New(
        impl_function_6_FeedEventLogRecords_of_win32evtlogutil,
        const_str_plain_FeedEventLogRecords,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_366d412a45eef79bfd41a727819b2246,
        defaults,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module_win32evtlogutil,
        Py_None
    );

    return result;
}



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_win32evtlogutil =
{
    PyModuleDef_HEAD_INIT,
    "win32evtlogutil",   /* m_name */
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

MOD_INIT_DECL( win32evtlogutil )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_win32evtlogutil );
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

    // puts( "in initwin32evtlogutil" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_win32evtlogutil = Py_InitModule4(
        "win32evtlogutil",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_win32evtlogutil = PyModule_Create( &mdef_win32evtlogutil );
#endif

    moduledict_win32evtlogutil = (PyDictObject *)((PyModuleObject *)module_win32evtlogutil)->md_dict;

    CHECK_OBJECT( module_win32evtlogutil );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_plain_win32evtlogutil, module_win32evtlogutil );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_win32evtlogutil );

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
    PyObject *tmp_args_element_name_2;
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
    PyObject *tmp_defaults_1;
    PyObject *tmp_defaults_2;
    PyObject *tmp_defaults_3;
    PyObject *tmp_defaults_4;
    PyObject *tmp_defaults_5;
    PyObject *tmp_defaults_6;
    PyObject *tmp_import_globals_1;
    PyObject *tmp_import_globals_2;
    PyObject *tmp_import_globals_3;
    PyObject *tmp_import_globals_4;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    PyObject *tmp_source_name_3;
    PyObject *tmp_source_name_4;
    PyObject *tmp_source_name_5;
    PyObject *tmp_tuple_element_1;
    PyFrameObject *frame_module;


    // Module code.
    tmp_assign_source_1 = const_str_digest_b3058d3f630aa2c74cf839db3e555357;
    UPDATE_STRING_DICT0( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = module_filename_obj;
    UPDATE_STRING_DICT0( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    // Frame without reuse.
    frame_module = MAKE_MODULE_FRAME( codeobj_ef1a4625ec0c7ad40c4e18d1afed0eed, module_win32evtlogutil );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_module );
    assert( Py_REFCNT( frame_module ) == 1 );

#if PYTHON_VERSION >= 340
    frame_module->f_executing += 1;
#endif

    // Framed code:
    tmp_import_globals_1 = ((PyModuleObject *)module_win32evtlogutil)->md_dict;
    frame_module->f_lineno = 4;
    tmp_assign_source_3 = IMPORT_MODULE( const_str_plain_win32api, tmp_import_globals_1, tmp_import_globals_1, Py_None, const_int_neg_1 );
    if ( tmp_assign_source_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api, tmp_assign_source_3 );
    tmp_import_globals_2 = ((PyModuleObject *)module_win32evtlogutil)->md_dict;
    frame_module->f_lineno = 4;
    tmp_assign_source_4 = IMPORT_MODULE( const_str_plain_win32con, tmp_import_globals_2, tmp_import_globals_2, Py_None, const_int_neg_1 );
    if ( tmp_assign_source_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32con, tmp_assign_source_4 );
    tmp_import_globals_3 = ((PyModuleObject *)module_win32evtlogutil)->md_dict;
    frame_module->f_lineno = 4;
    tmp_assign_source_5 = IMPORT_MODULE( const_str_plain_winerror, tmp_import_globals_3, tmp_import_globals_3, Py_None, const_int_neg_1 );
    if ( tmp_assign_source_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_winerror, tmp_assign_source_5 );
    tmp_import_globals_4 = ((PyModuleObject *)module_win32evtlogutil)->md_dict;
    frame_module->f_lineno = 4;
    tmp_assign_source_6 = IMPORT_MODULE( const_str_plain_win32evtlog, tmp_import_globals_4, tmp_import_globals_4, Py_None, const_int_neg_1 );
    if ( tmp_assign_source_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 4;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog, tmp_assign_source_6 );
    tmp_source_name_1 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_1 == NULL ))
    {
        tmp_source_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 6;
        goto frame_exception_exit_1;
    }

    tmp_assign_source_7 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_error );
    if ( tmp_assign_source_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 6;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_error, tmp_assign_source_7 );
    tmp_source_name_2 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32api );

    if (unlikely( tmp_source_name_2 == NULL ))
    {
        tmp_source_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32api );
    }

    if ( tmp_source_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "win32api" );
        exception_tb = NULL;

        exception_lineno = 8;
        goto frame_exception_exit_1;
    }

    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_MAKELANGID );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 8;
        goto frame_exception_exit_1;
    }
    tmp_source_name_3 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32con );

    if (unlikely( tmp_source_name_3 == NULL ))
    {
        tmp_source_name_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32con );
    }

    if ( tmp_source_name_3 == NULL )
    {
        Py_DECREF( tmp_called_name_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "win32con" );
        exception_tb = NULL;

        exception_lineno = 8;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_3, const_str_plain_LANG_NEUTRAL );
    if ( tmp_args_element_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_1 );

        exception_lineno = 8;
        goto frame_exception_exit_1;
    }
    tmp_source_name_4 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32con );

    if (unlikely( tmp_source_name_4 == NULL ))
    {
        tmp_source_name_4 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32con );
    }

    if ( tmp_source_name_4 == NULL )
    {
        Py_DECREF( tmp_called_name_1 );
        Py_DECREF( tmp_args_element_name_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "win32con" );
        exception_tb = NULL;

        exception_lineno = 8;
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_4, const_str_plain_SUBLANG_NEUTRAL );
    if ( tmp_args_element_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_1 );
        Py_DECREF( tmp_args_element_name_1 );

        exception_lineno = 8;
        goto frame_exception_exit_1;
    }
    frame_module->f_lineno = 8;
    {
        PyObject *call_args[] = { tmp_args_element_name_1, tmp_args_element_name_2 };
        tmp_assign_source_8 = CALL_FUNCTION_WITH_ARGS2( tmp_called_name_1, call_args );
    }

    Py_DECREF( tmp_called_name_1 );
    Py_DECREF( tmp_args_element_name_1 );
    Py_DECREF( tmp_args_element_name_2 );
    if ( tmp_assign_source_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 8;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_langid, tmp_assign_source_8 );
    tmp_defaults_1 = const_tuple_none_str_plain_Application_none_tuple;
    tmp_assign_source_9 = MAKE_FUNCTION_function_1_AddSourceToRegistry_of_win32evtlogutil( INCREASE_REFCOUNT( tmp_defaults_1 ) );
    UPDATE_STRING_DICT1( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_AddSourceToRegistry, tmp_assign_source_9 );
    tmp_defaults_2 = const_tuple_str_plain_Application_tuple;
    tmp_assign_source_10 = MAKE_FUNCTION_function_2_RemoveSourceFromRegistry_of_win32evtlogutil( INCREASE_REFCOUNT( tmp_defaults_2 ) );
    UPDATE_STRING_DICT1( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_RemoveSourceFromRegistry, tmp_assign_source_10 );
    tmp_defaults_3 = PyTuple_New( 5 );
    tmp_tuple_element_1 = const_int_0;
    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_defaults_3, 0, tmp_tuple_element_1 );
    tmp_source_name_5 = GET_STRING_DICT_VALUE( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_win32evtlog );

    if (unlikely( tmp_source_name_5 == NULL ))
    {
        tmp_source_name_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_win32evtlog );
    }

    if ( tmp_source_name_5 == NULL )
    {
        Py_DECREF( tmp_defaults_3 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyString_FromFormat( "name '%s' is not defined", "win32evtlog" );
        exception_tb = NULL;

        exception_lineno = 67;
        goto frame_exception_exit_1;
    }

    tmp_tuple_element_1 = LOOKUP_ATTRIBUTE( tmp_source_name_5, const_str_plain_EVENTLOG_ERROR_TYPE );
    if ( tmp_tuple_element_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_defaults_3 );

        exception_lineno = 67;
        goto frame_exception_exit_1;
    }
    PyTuple_SET_ITEM( tmp_defaults_3, 1, tmp_tuple_element_1 );
    tmp_tuple_element_1 = Py_None;
    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_defaults_3, 2, tmp_tuple_element_1 );
    tmp_tuple_element_1 = Py_None;
    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_defaults_3, 3, tmp_tuple_element_1 );
    tmp_tuple_element_1 = Py_None;
    Py_INCREF( tmp_tuple_element_1 );
    PyTuple_SET_ITEM( tmp_defaults_3, 4, tmp_tuple_element_1 );
    tmp_assign_source_11 = MAKE_FUNCTION_function_3_ReportEvent_of_win32evtlogutil( tmp_defaults_3 );
    UPDATE_STRING_DICT1( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_ReportEvent, tmp_assign_source_11 );

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
    tmp_defaults_4 = const_tuple_str_plain_Application_tuple;
    tmp_assign_source_12 = MAKE_FUNCTION_function_4_FormatMessage_of_win32evtlogutil( INCREASE_REFCOUNT( tmp_defaults_4 ) );
    UPDATE_STRING_DICT1( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_FormatMessage, tmp_assign_source_12 );
    tmp_defaults_5 = const_tuple_none_tuple;
    tmp_assign_source_13 = MAKE_FUNCTION_function_5_SafeFormatMessage_of_win32evtlogutil( INCREASE_REFCOUNT( tmp_defaults_5 ) );
    UPDATE_STRING_DICT1( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_SafeFormatMessage, tmp_assign_source_13 );
    tmp_defaults_6 = const_tuple_none_str_plain_Application_none_tuple;
    tmp_assign_source_14 = MAKE_FUNCTION_function_6_FeedEventLogRecords_of_win32evtlogutil( INCREASE_REFCOUNT( tmp_defaults_6 ) );
    UPDATE_STRING_DICT1( moduledict_win32evtlogutil, (Nuitka_StringObject *)const_str_plain_FeedEventLogRecords, tmp_assign_source_14 );

    return MOD_RETURN_VALUE( module_win32evtlogutil );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
