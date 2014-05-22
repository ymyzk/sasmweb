#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

try:
    import gevent.monkey
    gevent.monkey.patch_all()
except:
    pass
from bottle import route, run

@route('/')
def index(name):
    return '<b>Hello</b>!'

run(server='gevent', host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
