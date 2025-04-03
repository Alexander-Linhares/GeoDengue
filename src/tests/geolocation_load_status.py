if __name__ == "__main__":
    import os
    import sys
    import asyncio
    from random import uniform, randint
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), "../")))
    
    from classes.futures.data_load_status import GeolocationLoadStatus
    from classes.patterns.observer import Subject

    #Um exemplo de funcionalidade da classe GeolocationLoadStatus
    class DataHandler(Subject):
        def __init__(self):
            super().__init__()
            self.data = None
        
        def update(self, data):
            self.data = data

        async def show_data(self, load_status: GeolocationLoadStatus):
            res = None
            while res != "finish":
                await asyncio.sleep(5)
                print("Atualizando data")
                print(self.data, end="\n\n")
                if not load_status.done():
                    continue
                res = load_status.result()
            print("A tarefa foi concluída com sucesso, atualizando layout")

    async def load_data(load_status: GeolocationLoadStatus, timeout: int=3):
        print(f"Carregando 10 localizações com um timeout = {timeout}")
        for i in range(10):
            try:
                print(f"Carregando o endereço {i}/10\n\n", end="\r")
                await asyncio.sleep(timeout)

                error_simulation = randint(0, 10)
                if error_simulation > 7:
                    raise ValueError("Simulação de erro")

                lon = uniform(-180, 180)
                lat = uniform(-90, 90)

                load_status.coordinates.add_coordinate((lon, lat))
                load_status.add_loaded(1)
                
            except Exception as e:
                print(f"houve um erro ao carregar essa localização\n{e}")
                load_status.add_api_error(str(e))
        
        load_status.set_result("finish")

    async def update_layout(load_status: GeolocationLoadStatus):
        print("Esperando a conclusão do carregamento das coordenadas..")
        res = await load_status
        if res == "finish":
            print("A tarefa foi concluída com sucesso, atualizando layout")

    async def main():
        gls = GeolocationLoadStatus()
        dh = DataHandler()

        gls.subscribe(dh)
        tasks = [
            asyncio.create_task(load_data(gls)),
            asyncio.create_task(dh.show_data(gls)),
            asyncio.create_task(update_layout(gls))
        ]

        #gls.unsubscribe(dh)

        await asyncio.gather(*tasks)

    asyncio.run(main())


    def add_coordinate_test():
        gls = GeolocationLoadStatus()
        
        gls.coordinates.add_coordinate((34, -34.2342153235))

        print(gls.coordinates.coordinates)

    def add_loaded_test():
        gls = GeolocationLoadStatus()
        dh = DataHandler()
        gls.subscribe(dh)
        
        gls.add_loaded(10)

        print(dh.data)

    #add_loaded_test()
