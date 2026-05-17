from encoding.interfaces.registery_encoder import RegisteryEncoder
from encoding.implementations.binary_encoder import BinaryEncoder
from encoding.implementations.json_encoder import JsonEncoder
from encoding.implementations.primitive_encoder import PrimitiveEncoder
from encoding.implementations.text_encoder import TextEncoder
from encoding.implementations.dict_encoder import DictEncoder


class EncoderRegistry(RegisteryEncoder):
    def __init__(self):
        pass
    
    def init_encoder(self, content_type = 'dict'):
        if content_type == 'dict':
            return DictEncoder()
        
        if content_type == 'text':
            return TextEncoder()
        
        if content_type == 'binary':
            return BinaryEncoder()
        
        if content_type == 'json':
            return JsonEncoder()
        
        return PrimitiveEncoder()

    
