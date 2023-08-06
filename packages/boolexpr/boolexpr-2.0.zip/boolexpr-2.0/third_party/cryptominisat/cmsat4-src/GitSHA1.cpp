/*
 * CryptoMiniSat
 *
 * Copyright (c) 2009-2014, Mate Soos. All rights reserved.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation
 * version 2.0 of the License.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301  USA
*/

#include "src/GitSHA1.h"
const char* get_version_sha1()
{
    static const char myversion_sha1[] = "";
    return myversion_sha1;
}

const char* get_version_tag()
{
    static const char myversion_tag[] = "4.5.3";
    return myversion_tag;
}

const char* get_compilation_env()
{
    static const char compilation_env[] =
    "CMAKE_CXX_COMPILER = /usr/bin/c++ | "
    "CMAKE_CXX_FLAGS =  -std=c++11 -pthread -g -Wall -Wextra -Wunused -pedantic -Wsign-compare -Wtype-limits -Wuninitialized -Wno-deprecated -Wstrict-aliasing -Wpointer-arith -fvisibility=hidden -Wpointer-arith -Wformat-nonliteral -Winit-self -Wunreachable-code -fPIC | "
    "COMPILE_DEFINES =  -DBOOST_TEST_DYN_LINK -DUSE_ZLIB -DUSE_VALGRIND -DUSE_M4RI | "
    "STATICCOMPILE = OFF | "
    "ONLY_SIMPLE = ON | "
    "Boost_FOUND = 0 | "
    "TBB_FOUND =  | "
    "STATS = OFF | "
    "MYSQL_FOUND =  | "
    "SQLITE3_FOUND =  | "
    "ZLIB_FOUND = TRUE | "
    "VALGRIND_FOUND = TRUE | "
    "ENABLE_TESTING = OFF | "
    "M4RI_FOUND = TRUE | "
    "SLOW_DEBUG = OFF | "
    "PYTHON_EXECUTABLE =  | "
    "PYTHON_LIBRARY =  | "
    "PYTHON_INCLUDE_DIRS =  | "
    "MY_TARGETS = "
    ""
    ;
    return compilation_env;
}
