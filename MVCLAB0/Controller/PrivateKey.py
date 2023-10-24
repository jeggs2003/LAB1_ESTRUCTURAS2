
class PrivateKey:
    def __init__(self, n: int, j: int, z: int):
        self.n = n
        self.j = j
        self.z = z

    def get_n(self) -> int:
        return self.n

    def get_j(self) -> int:
        return self.j
