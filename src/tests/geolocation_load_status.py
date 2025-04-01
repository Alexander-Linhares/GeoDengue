if __name__ == "__main__":
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), "../")))

    from classes.futures.data_load_status import GeolocationLoadStatus

    gls = GeolocationLoadStatus()

    gls.coordinates.add_coordinate((23, 21))

    print(gls.coordinates)
