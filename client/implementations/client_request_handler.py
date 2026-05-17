from client.interfaces.client_handler import ClientHandler
from dto.request import Request

class ClientRequestHandler(ClientHandler):

    def __init__(self, header, body):
        self.header = header
        self.body = body
        self.request = Request(header, body)

    def receive():
        pass

    def handle():
        pass

    def send():
        pass
    

