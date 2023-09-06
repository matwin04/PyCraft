from bottle import route, run, static_file, template, redirect
import socket
import subprocess
from mcipc.rcon.be import Client

import minestat
ip=socket.gethostbyname(socket.gethostname())

host = "localhost"
port = 19132

ms = minestat.MineStat(f'{ip}',19132)



#Server Status
server_status = "OFFLINE"
#Online Status
if ms.online:
    server_status = "ONLINE"
else:
    server_status = "OFFLINE"

gamemode = ms.gamemode

#Inde
@route('/pages/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./pages/')

@route('/')
def login():
    return template('./pages/login.html')
@route('/home')
def index():
    global server_status
    status_class = "online" if server_status == "ONLINE" else "offline"
    return template('./pages/index.html',
                    server_status = server_status,
                    status_class=status_class
                    )
@route('/bedrock')
def index():
    return template('./pages/bedrock_index.html',
                    gamemode=ms.gamemode,
                    address=ms.address,
                    server_status = server_status
                    )
@route('/pm')
def index():
    return template('./pages/pocketmine_index.html',
                    gamemode=ms.gamemode,
                    address=ms.address,
                    server_status = server_status
                    )

#command files
@route('/start')
def start():
    subprocess.Popen(['BedrockServer/bedrock_server.exe'])
    redirect('/')
    
    
@route('/pm/start')
def start():
    subprocess.Popen(['/pocketmine_server/start.ps1'])
    redirect('/pm')
run(host=ip,port=5555,debug=True,reloader=True,)
