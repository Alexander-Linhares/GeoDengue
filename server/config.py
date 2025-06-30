import secrets
import os
from urllib.parse import quote

SECRET_KEY = secrets.token_hex(16)
SQLALCHEMY_DATABASE_URI = '{SGBD}://{user}:{password}@{host}:{port}/{database}'.format(
        SGBD='postgresql',
        user='postgres',
        password=quote('Alex0205Admin!'),
        host='127.0.0.1',
        port='5432',
        database='notifications'
    )

SQLALCHEMY_TRACK_MODIFICATIONS = False
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_PATH_FOLDER = os.path.normpath(os.path.join(BASE_DIR, '../static/uploads'))


if __name__ == "__main__":
    print(f"SECRET_KEY: {SECRET_KEY}")
    print(f"SQLALCHEMY_DATABASE_URI: {SQLALCHEMY_DATABASE_URI}")
    print(f"UPLOAD_PATH_FOLDER: {UPLOAD_PATH_FOLDER}")
    print(f"SQLALCHEMY_TRACK_MODIFICATIONS: {SQLALCHEMY_TRACK_MODIFICATIONS}")