docstrings = {
    "add_coordinate": """
        Adiciona uma coordenada ao conjunto de coordenadas existentes.

        Este método aceita uma tupla ou um dicionário que represente uma coordenada 
        com valores de longitude e latitude. A função verifica se os valores fornecidos 
        estão dentro do intervalo permitido para longitude e latitude. Caso contrário, 
        uma exceção será levantada.

        Parâmetros:
        ----------
        pair : tuple[float, float] | dict
            A coordenada a ser adicionada. Deve ser uma tupla no formato (longitude, latitude),
            ou um dicionário com as chaves correspondentes a longitude e latitude.

        Comportamento:
        --------------
        - Se `pair` for um dicionário, os valores serão convertidos para uma tupla.
        - Se a tupla ou os valores do dicionário não corresponderem ao formato esperado
        ou estiverem fora dos intervalos permitidos, uma `ValueError` será levantada.
        - A coordenada válida será adicionada à lista privada de coordenadas (`self.__coordinates`).

        Exceções:
        ---------
        - ValueError: Levantada quando os valores fornecidos estão fora do intervalo
        permitido para longitude e latitude ou o parâmetro `pair` não está no formato adequado.

        Exemplo:
        --------
        pair = (-34.56, 23.45)
        self.add_coordinate(pair)  # Adiciona a coordenada (-34.56, 23.45)
    """,
}