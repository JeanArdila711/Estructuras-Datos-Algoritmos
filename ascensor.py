class Ascensor:
    def __init__(self, piso_actual, piso_destino, ocupado = False, emergencia = False):
        self.piso_actual = piso_actual
        self.piso_destino = piso_destino
        self.ocupado = ocupado
        self.emergencia = emergencia 
        