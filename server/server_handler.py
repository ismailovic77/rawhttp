import socketserver
from encoding.implementations.dict_encoder import DictEncoder

class Handler(socketserver.BaseRequestHandler):

    HEADER_SEP = "\n".encode()

    def setup(self):
        print(f"New connection from {self.client_address}")

    def handle(self):
        raw = b""
        i = 1
        while b"\n\n" not in raw:
            raw += self.request.recv(100)
            print(f"stream {i} of bytes received from client ...")
            i += 1 

        
        header_encoded, body_start_encoded = raw.split(self.HEADER_SEP * 2, 1)
        print(f"this is the header encoded : {header_encoded}")
        print('-----------------------')
        print(f"this is the body_start encoded : {body_start_encoded}")
        #raw_decoded = raw.decode()
        print("")

        # here instead of using the decode method directly , we would call the factory , to get a dict encoded , that will decode the header for us 
        header_decoder = DictEncoder()
        header = header_decoder.decode(header_encoded)
        print(f"receiived header from client : {header}")
        print('-----------------------')
        
        # since for this example the body is just a text then you can call it 
        """"""
        body_start = body_start_encoded.decode()
        print(f"body_start received from {self.client_address} => {body_start}")
        print('-----------------------')

        # receive the rest of the body message (here this expects the message to be longer then the 100 so the if the message is less it stops in this recv waiting for somehting else)
        # this could be solved obviously using the content length param
        body_rest = self.request.recv(1024)  # here instead of the 1024 it should be the number read from content-lengh in header
        body_rest_decoded = body_rest.decode()
        print(len(body_rest_decoded))
        print('-----------------------')

        # get the whole body back to orginal
        body = body_start + body_rest_decoded
        print(f"body received from {self.client_address} => {body}")
        print("")
        self.request.sendall(b"Message received")

    def finish(self):
        print(f"Connection closed: {self.client_address}")