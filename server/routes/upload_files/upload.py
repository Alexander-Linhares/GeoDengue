import pandas as pd

from flask import redirect, request, url_for

from server.routes.upload_files import upload_files_bp
from server.config import UPLOAD_PATH_FOLDER
from werkzeug.datastructures import FileStorage

@upload_files_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    """
    Redirects to the upload page.
    """
    print('Lidando com upload')
   
    file: FileStorage = request.files.get('file_input')
    if file:
        df = None
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.filename.endswith('.xlsx'):
            df = pd.read_excel(file)

            
        print(f'Arquivo CSV carregado com sucesso: {file.filename}')
        print(df.info())
        # Aqui você pode processar o DataFrame df conforme necessário
        df.to_csv(f'{UPLOAD_PATH_FOLDER}/{file.filename}', index=False)
        return """
        <h1>Arquivo CSV carregado com sucesso!</h1>
        <p>Nome do arquivo: {}</p>
        <p>Conteúdo do DataFrame:</p>
        <pre>{}</pre>
        """.format(file.filename, df.to_html())
        
    
    return redirect(url_for('map.maps'))