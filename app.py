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
        print(error)

    return template('assemble', asm=asm, code=code, error=error)


run(host='0.0.0.0', port=sys.argv[1])
