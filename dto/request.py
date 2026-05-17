

class Request : 
    """
    The request object represent the request components (body and header) .
    The requet variable will contain the request value after encoding
    """


    def __init__(self, header, body):
        self.header = header
        self.body = body
        self.request = ""
    
    def get_body(self):
        return self.body
    
    def get_header(self):
        return self.header
    
    def get_request(self):
        return self.request
    
    def set_request(self):
        self.request = self.header + (NEWLINE * 2) + self.body
