#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from bottle import route, run

@route('/')
def index(name):
    return '<b>Hello</b>!'

run(server='gevent', port=int(os.environ.get("PORT", 5000)))
