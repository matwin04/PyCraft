from bottle import route, run, static_file, template, redirect
import socket


@route('/')
def index():
    return "index"

run(host='127.0.0.1',port=8888,debug=True,reloader=True)