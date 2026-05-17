class Header : 
    def __init__(self):
        self.header = {}
    
    def get_header(self):
        return self.header
    
    def set_header(self, header):
        self.header = header
        self.set_mandatory_header()
    
    def set_mandatory_header(self):
        self.host = self.header['host']
        self.port = self.header['port']
        self.content_type = self.header['content_type']
        self.content_length = self.header['content_length']

    def get_header_values(self, key):
        return self.header[key]
