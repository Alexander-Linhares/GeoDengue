from asyncio import Future
from pandas import DataFrame
from ..patterns.observer import Observable

class CoordinateList:

    LON_SCALE = range(-180, 180)
    LAT_SCALE = range(-90, 90)
    HEADER = ("Longitude", "Latitude")

    def __init__(self):
        self._coordinates = []

    @property
    def coordinates(self):
        return self.to_dataframe()

    def add_coordinate(self, pair: tuple[float, float] | dict):
        if isinstance(pair, dict):
            pair = tuple(pair.values())

        if isinstance(pair, tuple) and len(pair) == 2:
            if (c1 := (pair[0] in self.LON_SCALE)) and (c2 := (pair[1] in self.LAT_SCALE)):
                self._coordinates.append(pair)
            else:
                h_error = self.HEADER[c1]
                raise ValueError(f"O valor {pair[c1]} não pertence ao intervalo da {h_error}")
        else:
            raise ValueError("O parâmetro pair precisa corresponder a uma tupla: (longitude, latitude)")
    
    def to_dataframe(self):
        return DataFrame(
            self._coordinates, 
            columns=["Longitude", "Latitude"]
        )
    

class GeolocationLoadStatus(Future, Observable):

    def __init__(self):
        super().__init__()
        self._coordinates = CoordinateList()
        self._loaded: dict = {"number": 0}
        self._not_found: dict = {"address": []}
        self._api_error: dict = {"error_log": []}

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def loaded(self):
        return self._loaded
    
    @property
    def not_found(self):
        return self._not_found
    
    @property
    def api_error(self):
        return self._api_error
