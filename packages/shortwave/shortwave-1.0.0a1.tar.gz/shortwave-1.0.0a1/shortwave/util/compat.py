#!/usr/bin/env python
# coding: utf-8

# Copyright 2011-2016, Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from sys import version_info
try:
    from urllib.parse import quote, unquote_plus as unquote
except ImportError:
    from urllib import quote, unquote_plus as unquote


if version_info >= (3,):
    integer = int
    jsonable = (type(None), bool, int, float, str, list, dict)
    unicode = str

    SPACE = ord(' ')

    def bstr(s, encoding="utf-8"):
        if isinstance(s, bytes):
            return s
        elif isinstance(s, bytearray):
            return bytes(s)
        elif isinstance(s, str):
            return bytes(s, encoding)
        else:
            return bytes(str(s), encoding)

    def ustr(s, encoding="utf-8"):
        """ Convert argument to unicode string.
        """
        if isinstance(s, str):
            return s
        try:
            return s.decode(encoding)
        except AttributeError:
            return str(s)

    def xstr(s, encoding="utf-8"):
        """ Convert argument to string type returned by __str__.
        """
        if isinstance(s, str):
            return s
        elif isinstance(s, bytes):
            return s.decode(encoding)
        else:
            return str(s)

else:
    integer = (int, long)
    jsonable = (type(None), bool, int, long, float, unicode, list, dict)

    SPACE = b' '

    def bstr(s, encoding="utf-8"):
        if isinstance(s, bytes):
            return s
        elif isinstance(s, bytearray):
            return bytes(s)
        elif isinstance(s, unicode):
            return s.encode(encoding)
        else:
            return str(s)

    def ustr(s, encoding="utf-8"):
        """ Convert argument to unicode string.
        """
        if isinstance(s, str):
            return s.decode(encoding)
        else:
            return unicode(s)

    def xstr(s, encoding="utf-8"):
        """ Convert argument to string type returned by __str__.
        """
        if isinstance(s, str):
            return s
        else:
            return unicode(s).encode(encoding)

    def hexb(n):
        return hex(n)[2:]
