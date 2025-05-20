from server.app import create_app, socketio

if __name__ == "__main__":

    app = create_app(__name__)
    print(f"Eventos registrados no Flask-SocketIO: {socketio.handlers}")

    socketio.run(app, host='127.0.0.1', port=5000, debug=True)