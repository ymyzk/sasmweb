#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import traceback

from bottle import request, route, run, template
from sasm.assembler import Assembler


@route('/')
def index():
    return template('index')


@route('/assemble/', method='POST')
def assemble():
    code = request.forms.code
    assembler = Assembler()
    asm = None
    error = None
    try:
        assembler.load(code)
        asm = assembler.compile()
    except:
        error = traceback.format_exc()

    return template('assemble', asm=asm, code=code, error=error)


if __name__ == "__main__":
    try:
        host = sys.argv[1]
    except IndexError:
        host = "127.0.0.1"
    try:
        port = sys.argv[2]
    except IndexError:
        port = 8000
    run(host=host, port=port)
