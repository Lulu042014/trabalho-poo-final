from motos import Moto
class Harley_Davidson_Street_750(Moto):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)

    def turbo(self):
        self.velocidade += 50
        print('Turbo ativado! A velocidade aumentou em 50 km/h')

