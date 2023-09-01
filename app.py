from bottle import route, run, static_file, template, redirect
import socket
import subprocess

ip=socket.gethostbyname(socket.gethostname())
@route('/')
def index():
    return template('./pages/index.html')


#command files
@route('/start')
def start():
    subprocess.Popen(['bedrock_server.exe'])
    redirect('/')
run(host=ip,port=5555,debug=True,reloader=True)