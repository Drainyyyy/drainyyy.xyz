# -*- coding: utf-8 -*-

#  Covered by The MIT License (MIT)
#
#  Copyright 2021 Jörg Reinhardt (Drainyyy)
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
#  (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,
#  publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
#  subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
#  WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
#  CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

__all__ = ["FLASK_SSH_ENABLED", "FLASK_RUN_CONFIG"]

# FLASK

FLASK_SSH_ENABLED = False

FLASK_RUN_CONFIG = {
    "host": "localhost",
    "port": 25163,
    "debug": True
}

if FLASK_SSH_ENABLED is True:
    FLASK_RUN_CONFIG["ssl_context"] = "adhoc"
