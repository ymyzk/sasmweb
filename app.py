#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
