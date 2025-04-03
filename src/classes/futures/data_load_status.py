from asyncio import Future
from pandas import DataFrame
from ..patterns.observer import Observable

#retorna se o número n está contido no intervalo simétrico fechado de x
def inv_interval(n: float, x: int):
    """
    Retorna se o número `n` está contido no intervalo simétrico fechado de `-x` a `x`.
    
    Parâmetros:
    - n (float): Número real a ser verificado.
    - x (int): Limite do intervalo simétrico.

    Retorno:
    - bool: True se `n` está no intervalo, False caso contrário.
    """

    return -x <= n <= x

class CoordinateList:

    MAX_LON = 180
    MAX_LAT = 90
    HEADER = ("Longitude", "Latitude")

    def __init__(self):
        self.__coordinates = []

    @property
    def coordinates(self):
        return self.to_dataframe()

    def add_coordinate(self, pair: tuple[float, float] | dict):
        if isinstance(pair, dict):
            pair = tuple(pair.values())

        if isinstance(pair, tuple) and len(pair) == 2:
            if (c1 := (inv_interval(pair[0], self.MAX_LON))
                ) and (c2 := inv_interval(pair[1], self.MAX_LAT)):
                self.__coordinates.append(pair)
            else:
                h_error = self.HEADER[c1]
                raise ValueError(f"O valor {pair[c1]} não pertence ao intervalo da {h_error}")
        else:
            raise ValueError("O parâmetro pair precisa corresponder a uma tupla: (longitude, latitude)")
    
    def to_dataframe(self):
        return DataFrame(
            self.__coordinates, 
            columns=["Longitude", "Latitude"]
        )
    
    
    

class GeolocationLoadStatus(Future, Observable):

    def __init__(self):
        Future.__init__(self)
        Observable.__init__(self)
        self.__coordinates = CoordinateList()
        self.__loaded: dict = {"number": 0}
        self.__not_found: dict = {"address": []}
        self.__api_error: dict = {"error_log": []}

    @property
    def coordinates(self):
        return self.__coordinates

    @property
    def loaded(self):
        return self.__loaded.copy()
    
    @property
    def not_found(self):
        return self.__not_found.copy()
    
    @property
    def api_error(self):
        return self.__api_error.copy()
    
    @staticmethod
    def _update_data(func):
        """
        Atualiza todos os subjects com todos os dados recettivamente carregados"""
        def inner(self, *args, **kwargs):
            func(self, *args, **kwargs)
            self.notify_all(
                {
                    "loaded": self.loaded,
                    "not_found": self.not_found,
                    "api_error": self.api_error,
                    "coordinates": self.coordinates.coordinates
                }
            )
        return inner
    
    @_update_data
    def add_loaded(self, number: int):
        self.__loaded["number"] += number

    @_update_data
    def add_not_found(self, address: str):
        self.__not_found["address"].append(address)

    @_update_data
    def add_api_error(self, error: str):
        self.__api_error["error_log"].append(error)
