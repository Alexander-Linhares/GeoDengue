from flask import Blueprint

upload_files_bp = Blueprint('upload_files', __name__, url_prefix='/upload_files')

from .upload import upload