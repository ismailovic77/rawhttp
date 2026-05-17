from abc import ABC, abstractmethod

class Encode(ABC):

    @abstractmethod
    def encode():
        pass

    @abstractmethod
    def decode():
        pass