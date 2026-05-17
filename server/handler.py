import socketserver

class Handler(socketserver.BaseRequestHandler):

    HEADER_SEP = "\n"

    def setup(self):
        print(f"New connection from {self.client_address}")

    def handle(self):
        raw = b""
        i = 1
        while b"\n" not in raw:
            raw += self.request.recv(100)
            print(f"stream {i} of bytes received from client ...")
            i += 1 

        raw_decoded = raw.decode()
        header, body_start = raw_decoded.split(self.HEADER_SEP, 1)
        print("")
        print(f"Header received from {self.client_address} => {header}")
        print('-----------------------')
        
        #print(f"body_start received from {self.client_address} => {body_start}")
        #print('-----------------------')

        # receive the rest of the body message
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