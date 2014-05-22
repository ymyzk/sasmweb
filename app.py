#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from bottle import route, run

@route('/')
def index(name):
    return 'Hello!'

run(host='0.0.0.0', port=sys.argv[1])
