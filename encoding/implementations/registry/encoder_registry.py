from encoding.interfaces.registery_encoder import RegisteryEncoder

class EncoderRegistry(RegisteryEncoder):
    def __init__(self, data, content_type = 'dict'):
        self.data = data
        self.content_type = content_type
    
    def init_encoder(self):
        if self.content_type == 'dict':
            pass
        # based on the type of the data Instatiate the right encoder
    
