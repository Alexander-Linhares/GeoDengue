from flask import Flask, url_for, request
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

socketio = SocketIO(logger=True, engineio_logger=True)

def create_app(path):
    app = Flask(path)

    app.config.from_pyfile('server/config.py', silent=False)
    
    socketio.init_app(app)
    db.init_app(app)

    with app.app_context():
        from server.routes.map import map_bp
        

        app.register_blueprint(map_bp)

    #app.register_blueprint()

    return app
