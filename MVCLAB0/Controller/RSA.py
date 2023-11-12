from Controller.GeneradorLLaves import GeneradorLlaves

class RSA:
    def __init__(self):
        generator_key = GeneradorLlaves()
        keys = generator_key.get_keys()
        self.public_key = keys['public_key']
        self.private_key = keys['private_key']

    def encrypt(self, message):
        n, e = self.public_key
        encrypted_message = [pow(ord(char), e, n) for char in message]
        return encrypted_message

    def decrypt(self, encrypted_message):
        n, d = self.private_key

        decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
        return ''.join(decrypted_message)

