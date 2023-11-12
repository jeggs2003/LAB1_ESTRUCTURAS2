import random

class GeneradorLlaves:

    def __init__(self):
        # Genera números primos p y q. En la práctica.
        self.p = self.generate_prime()
        self.q = self.generate_prime()
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.generate_e(self.phi)
        self.d = self.mod_inverse(self.e, self.phi)

    def generate_prime(self):

        return random.choice([3, 5, 7, 11, 13, 17])

    def generate_e(self, phi):
        e = 3
        while e < phi:
            if self.coprime(e, phi):
                return e
            e += 2
        raise Exception("No se pudo encontrar un 'e' válido.")

    def coprime(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a == 1

    def mod_inverse(self, a, m):

        m0 = m
        y = 0
        x = 1

        if m == 1:
            return 0

        while a > 1:
            q = a // m
            t = m
            m = a % m
            a = t
            t = y
            y = x - q * y
            x = t

        if x < 0:
            x += m0

        return x

    def get_keys(self):
        return {'public_key': (self.n, self.e), 'private_key': (self.n, self.d)}
