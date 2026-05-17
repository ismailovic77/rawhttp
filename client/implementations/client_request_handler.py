from client.interfaces.client_handler import ClientHandler
from dto.request import Request
from encoding.implementations.registry.encoder_registry import EncoderRegistry

class ClientRequestHandler(ClientHandler):

    def __init__(self, header, body):
        self.header = header
        self.body = body
        self.request = Request(header, body)

    def receive(self):
        pass

    def handle(self):
        # step 1 for a request is encoding (no need for preparation here because the header is already a dictionary)
        # call the registery encoder  
        encoder_registry = EncoderRegistry()

        # -- start with header
        header_encoder = encoder_registry.init_encoder(content_type="dict")
        print(f"header encoder : {header_encoder}")
        print(f"here is the header sent to the server : {self.header.get_header()}")
        header_encoded = header_encoder.encode(self.header.get_header())
        print(f"header encoded : {header_encoded}")

        # -- body
        body_encoder = encoder_registry.init_encoder(content_type="text")
        print(f"body encoder : {body_encoder}")
        body_encoded = body_encoder.encode(self.body.get_body())
        print(f"body encoded : {body_encoded}")

        # -- set the request encoded
        self.request.set_encoded_request(header_encoded, body_encoded)
        print('********************')
        print(f"[ CLIENT ] request encoded : {self.request.get_encoded_request()}")
        print('********************')

        return self.request.get_encoded_request()

    def send(self):
        pass
    

