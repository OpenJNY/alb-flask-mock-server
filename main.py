#!/usr/bin/env python3
#coding: utf-8
#
# FileName:     main
# CreatedDate:  2020-11-04 08:20:39

import sys
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return "Hello World!"

@app.route('/health', methods=['GET'])
def res_health():
    # https://werkzeug.palletsprojects.com/en/1.0.x/wrappers/#base-wrappers
    print(request.headers, file=sys.stderr)
    print(request.body, file=sys.stderr)
    return "OK, I'm good."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
