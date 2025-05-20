from urllib.parse import quote

SECRET_KEY = 'keep_secret'
SQLALCHEMY_DATABASE_URI = '{SGBD}://{user}:{password}@{host}:{port}/{database}'.format(
        SGBD='postgresql',
        user='postgres',
        password=quote('Alex0205Admin!'),
        host='127.0.0.1',
        port='5432',
        database='notifications'
    )

SQLALCHEMY_TRACK_MODIFICATIONS = False
