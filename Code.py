from abc import ABC, abstractmethod

class App:
    def __init__(self):


class Screen(ABC):
    @abstractmethod
    def draw(self):
        pass

class Inputs(ABC):
    @abstractmethod
    def get(self):
        pass

class Outputs(ABC):
    @abstractmethod
    def set(self):
        pass
