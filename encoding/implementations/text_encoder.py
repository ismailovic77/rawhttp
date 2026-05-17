from encoding.interfaces.encode import Encode

class TextEncoder(Encode):

    def encode(self, data: str) -> bytes:
        print("Encoding Text ....... ")
        return data.encode("utf-8")

    def decode(self, data: bytes) -> str:
        print("Decoding Text ....... ")
        return data.decode("utf-8")