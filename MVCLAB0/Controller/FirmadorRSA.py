import hashlib
from Controller.PublicKey import PublicKey
from Controller.PrivateKey import PrivateKey
from Controller.GeneratorKey import GeneratorKey

class FirmadorRSA:


    def __init__(self):
        generator_key = GeneratorKey()
        keys = generator_key.get_keys()
        self.public_key = keys.get_public_key()
        self.private_key = keys.get_private_key()

    def firmar(self, message):
        message_bytes = message.encode('utf-8')
        message_hash = hashlib.sha256(message_bytes).digest()
        j = self.private_key.get_j()
        n = self.private_key.get_n()
        message_hash_int = int.from_bytes(message_hash, byteorder='big')
        digital_signature = pow(message_hash_int, j, n)
        return digital_signature.to_bytes((digital_signature.bit_length() + 7) // 8, byteorder='big')

    def validar(self, message, digital_signature):
        message_bytes = message.encode('utf-8')
        message_hash = hashlib.sha256(message_bytes).digest()
        message_hash_int = int.from_bytes(message_hash, byteorder='big')
        digital_signature_bytes = bytes.fromhex(digital_signature)
        signature_int = int.from_bytes(digital_signature_bytes, byteorder='big')
        k = self.public_key.get_k()
        n = self.public_key.get_n()
        decrypted_signature = pow(signature_int, k, n)
        return message_hash_int == decrypted_signature
