import random
import math
from Controller.PrivateKey import PrivateKey
from Controller.PublicKey import PublicKey
from Controller.Keys import Keys

class GeneratorKey:
    KEY_SIZE = 256

    def __init__(self):
        pass

    def generate_private_key(self, k, z, n):
        j = self.ext_euclid(k, z)[1]
        privatek = PrivateKey(n, j, z);
        return privatek

    def ext_euclid(self, a, b):
        if b == 0:
            return [a, 1, 0]
        else:
            vals = self.ext_euclid(b, a % b)
            d = vals[0]
            p = vals[2]
            q = vals[1] - (a // b) * vals[2]
            return [d, p, q]

    def generate_public_key(self):
        p = self.generar_primo()
        q = self.generar_primo()
        n = p * q
        z = (p - 1) * (q - 1)
        k = self.obtener_coprimo(z)
        publick = PublicKey(n, k, z)
        return publick

    def get_keys(self):
        public_key = self.generate_public_key()
        private_key = self.generate_private_key(public_key.k, public_key.z, public_key.n)
        return Keys(private_key, public_key)

    def generar_primo(self):
        random_integer = random.SystemRandom()
        return random_integer.getrandbits(GeneratorKey.KEY_SIZE)

    def calcular_mcd(self, a, b):
        return a if b == 0 else self.calcular_mcd(b, a % b)

    def obtener_coprimo(self, z):
        while True:
            e = random.getrandbits(GeneratorKey.KEY_SIZE)
            if e < z and self.calcular_mcd(e, z) == 1:
                return e
