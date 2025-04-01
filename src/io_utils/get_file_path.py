import os

#Essa função encontra o diretório raiz busca o diretório informado e procura os arquivos com sufixo informados
#dirname: retorna o nome do diretório do caminho especificado
#abspath: retorna o caminho absoluto de determinado subpath 
#join: concatena de forma inteligente dois caminhos
#__file__: possui o caminho do arquivo em execução

def get_file_path(folder_name: str, file_sufix: str) -> list[str]:
    root = os.path.dirname(os.path.abspath(__file__))

    folder_path = os.path.join(root, folder_name)
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"O diretório {folder_name} não existe")

    archives = os.listdir(folder_path)
    if not archives:
        print("Este diretório está vazio")

    excel_files = [
        full_path 
        for file in archives if (
            full_path := os.path.join(folder_path, file)) 
                and file.endswith(file_sufix)
    ]

    return excel_files