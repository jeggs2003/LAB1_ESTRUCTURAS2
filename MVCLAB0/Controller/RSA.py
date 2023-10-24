from Controller.GeneratorKey import GeneratorKey

class RSA:

    def __init__(self, generator_key):
        self.generator_key = generator_key

    def encrypt(self, message):
        public_key = self.generator_key.public_key
        n, e = public_key
        encrypted_message = [pow(ord(char), e, n) for char in message]
        return encrypted_message

    def decrypt(self, encrypted_message):
        private_key = self.generator_key.private_key
        n, d = private_key
        decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
        return ''.join(decrypted_message)
