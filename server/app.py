from flask import Flask, url_for, request
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

socketio = SocketIO(
    cors_allowed_origins=['http://127.0.0.1:8080'], 
    logger=True, 
    engineio_logger=True)

def create_app(path):
    app = Flask(path)

    app.config.from_pyfile('server/config.py', silent=False)
    
    ##for i, config in enumerate(app.config):
    ##    s = f'{i} -- {config}:{app.config[config]}'
    ##   print(len(s[:s.index(':')]))

    socketio.init_app(app)
    db.init_app(app)

    with app.app_context():
        from server.routes.map import map_bp
        from server.routes.upload_files import upload_files_bp


        app.register_blueprint(map_bp)
        app.register_blueprint(upload_files_bp)

    #app.register_blueprint()

    return app
