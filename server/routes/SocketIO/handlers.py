from flask import request
from server.app import socketio
from colorama import Fore, Style

@socketio.on('connect')
def handle_connect():
    print(Fore.GREEN + f"Cliente {request.sid} conectado!" + Style.RESET_ALL)
    socketio.emit('server_message', {'msg': 'Bem-vindo ao servidor!'})
