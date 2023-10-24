
class PublicKey:

    def __init__(self, n: int, k: int, z: int):
        self.n = n
        self.k = k
        self.z = z

    def get_n(self) -> int:
        return self.n

    def get_k(self) -> int:
        return self.k

    def get_z(self) -> int:
        return self.z
