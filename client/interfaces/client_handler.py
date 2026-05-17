from abc import ABC, abstractmethod

class ClientHandler(ABC):

    @abstractmethod
    def receive():
        pass
    
    @abstractmethod
    def handle():
        pass

    @abstractmethod
    def send():
        pass