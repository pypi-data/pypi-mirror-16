// This provides the frozen (compiled bytecode) files that are included if
// any.
#include <Python.h>

// Blob from which modules are unstreamed.
#if defined(_WIN32) && defined(_NUITKA_EXE)
extern const unsigned char* constant_bin;
#else
extern "C" const unsigned char constant_bin[];
#endif

#define stream_data constant_bin

// These modules should be loaded as bytecode. They may e.g. have to be loadable
// during "Py_Initialize" already, or for irrelevance, they are only included
// in this un-optimized form. These are not compiled by Nuitka, and therefore
// are not accelerated at all, merely bundled with the binary or module, so
// that CPython library can start out finding them.

void copyFrozenModulesTo( void* destination )
{
    _frozen frozen_modules[] = {
        { (char *)"encodings.ascii", (unsigned char *)&constant_bin[ 1450966 ], 2223 },
        { (char *)"encodings.cp1251", (unsigned char *)&constant_bin[ 1453189 ], 2830 },
        { (char *)"encodings.cp1252", (unsigned char *)&constant_bin[ 1456019 ], 2833 },
        { (char *)"encodings.cp850", (unsigned char *)&constant_bin[ 1458852 ], 7778 },
        { (char *)"encodings.hex_codec", (unsigned char *)&constant_bin[ 1466630 ], 3707 },
        { (char *)"encodings.idna", (unsigned char *)&constant_bin[ 1470337 ], 6326 },
        { (char *)"encodings.iso8859_5", (unsigned char *)&constant_bin[ 1476663 ], 2836 },
        { (char *)"encodings.latin_1", (unsigned char *)&constant_bin[ 1479499 ], 2253 },
        { (char *)"encodings.mbcs", (unsigned char *)&constant_bin[ 1481752 ], 1995 },
        { (char *)"encodings.punycode", (unsigned char *)&constant_bin[ 1483747 ], 7911 },
        { (char *)"encodings.raw_unicode_escape", (unsigned char *)&constant_bin[ 1491658 ], 2175 },
        { (char *)"encodings.unicode_escape", (unsigned char *)&constant_bin[ 1493833 ], 2123 },
        { (char *)"encodings.utf_16", (unsigned char *)&constant_bin[ 1495956 ], 5100 },
        { (char *)"encodings.utf_16_le", (unsigned char *)&constant_bin[ 1501056 ], 1966 },
        { (char *)"encodings.utf_32_be", (unsigned char *)&constant_bin[ 1503022 ], 1859 },
        { (char *)"encodings.utf_8", (unsigned char *)&constant_bin[ 1504881 ], 1918 },
        { (char *)"stringprep", (unsigned char *)&constant_bin[ 1506799 ], 14381 },
        { NULL, NULL, 0 }
    };

    memcpy(
        destination,
        frozen_modules,
        ( _NUITKA_FROZEN + 1 ) * sizeof( struct _frozen )
    );
}
