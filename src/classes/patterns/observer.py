from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def update(self, data):
        pass

class Observable(object):
    def __init__(self):
        super().__init__()
        self.observers: list[Subject] = []

    def subscribe(self, subject: Subject):
        print("inscrevendo novo objeto")
        self.observers.append(subject)

    def unsubscribe(self, subject: Subject):
        print("desescrevendo objeto")
        ind = self.observers.index(subject)
        self.observers.pop(ind)

    def notify_all(self, data):
        if not data:
            raise ValueError("O parâmetro data não pode ser vazio")
        
        if len(self.observers) >= 1:
            for observer in self.observers:
                observer.update(data)
        else:
            raise ValueError("É necessário ter pelo menos um objeto inscrito para notificar")