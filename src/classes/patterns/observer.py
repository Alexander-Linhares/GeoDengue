from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def update(self, data):
        pass

class Observable:
    def __init__(self):
        self.observers: list[Subject] = []

    def subscribe(self, subject: Subject):
        self.observers.append(subject)

    def unsubscribe(self, subject: Subject):
        ind = self.observers.index(subject)
        self.observers.pop(ind)

    def notify(self, data):
        for observer in self.observers:
            observer.update(data)