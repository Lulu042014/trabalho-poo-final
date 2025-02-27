from moto_esportiva import MotoEsportiva
from moto_corrida import MotoCorrida

def test_drive(moto):
    print(f'\nTestando {moto.__class__.__name__}')
    moto.acelera()
    moto.exibe_velocidade()

if __name__ == '__main__':
    moto_esportiva = MotoEsportiva(100)
    print('Moto Esportiva:')
    moto_esportiva.turbo()
    moto_esportiva.exibe_velocidade()
    moto_esportiva.freia()
    moto_esportiva.exibe_velocidade()
    test_drive(moto_esportiva)

    moto_corrida = MotoCorrida(50)
    test_drive(moto_corrida)
