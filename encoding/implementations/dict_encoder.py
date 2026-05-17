from encoding.interfaces.encode import Encode
import pickle

class DictEncoder(Encode):
    def __init__(self):
        pass

    def encode(self,data):
        print(" Enconding dict .....")
        return pickle.dumps(data)

    def decode(self,data):
        print(" Decoding dict .....")
        return pickle.loads(data)
        