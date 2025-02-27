from motos import Moto
class Kawasaki Ninja 400(Moto):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)

    def acelera(self):
        self.velocidade += 150
        print('Aceleração de corrida! A velocidade aumentou em 150 km/h')
