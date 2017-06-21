# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request
from pyo import *

import time
import signal
import sys

app = Flask(__name__)

s = Server(duplex=0,audio="jack").boot()
s.setJackAuto(False, False)
s.start()

silenceTable = LinTable([(0,0),(8191,0)])
presquareTable = SquareTable(15).normalize()
presawTable = SawTable(15).normalize()
sawTable = DataTable(size=8191)
squareTable = DataTable(size=8191)
scale1 = TableScale(presawTable, sawTable, mul=0.08)
scale2 = TableScale(presquareTable, squareTable, mul=0.08)
sinTable = HarmTable([0.08])

step=None;

@app.route('/_stop')
def stop():
    global step
    #code = request.args.get('code', 0, type=str)
    code="""
try:
  step.destroy()
  del step
except:
  pass
"""
    exec(code)
    return jsonify(result=code)

@app.route('/_play')
def add_numbers():
    global step
    code = request.args.get('code', 0, type=str)
    exec(code)
    step=Steps()
    return jsonify(result=code)


@app.route('/')
def index():
    return render_template('BlockFlut0.html')

if __name__ == '__main__':
    app.run()
