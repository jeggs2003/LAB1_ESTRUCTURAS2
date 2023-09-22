class Persona:

    def __init__(self):
        self.nombre = ""  # Inicialización de propiedades
        self.dpi = 0
        self.direccion = ""
        self.fecha_nac = ""
        self.Encriptado = []
        self.Desencriptado = []
        self.Companies = []

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_dpi(self):
        return self.dpi

    def set_dpi(self, dpi):
        self.dpi = dpi

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_fecha(self):
        return self.fecha_nac

    def set_fecha(self, fecha_nac):
        self.fecha_nac = fecha_nac

    def get_enc(self):
        return self.Encriptado

    def set_enc(self, Encriptado):
        self.Encriptado = Encriptado

    def get_des(self):
        return self.Desencriptado

    def set_des(self, Desencriptado):
        self.Desencriptado = Desencriptado

    def get_compa(self):
        return self.Companies

    def set_compa(self, Companies):
        self.Companies = Companies


