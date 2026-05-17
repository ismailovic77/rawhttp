

NEWLINE = "\n".encode()

class Request : 
    """
    The request object represent the request components (body and header) .
    The requet variable will contain the request value after encoding
    """
    

    def __init__(self, header, body):
        self.header = header
        self.body = body
        self.request = b""
    
    def get_body(self):
        return self.body
    
    def get_header(self):
        return self.header
    
    def get_encoded_request(self):
        return self.request
    
    def set_encoded_request(self,header_encoded, body_encoded):
        self.request = header_encoded + (NEWLINE * 2) + body_encoded
