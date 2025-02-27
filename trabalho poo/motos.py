class Moto:
    def __init__(self, velocidade_inicial):
        self.velocidade = velocidade_inicial

    def acelera(self):
        self.velocidade += 50

    def freia(self):
        self.velocidade = max(0, self.velocidade - 10)  # Garante que a velocidade não fique negativa

    def exibe_velocidade(self):
        print(f'Velocidade atual: {self.velocidade} km/h')