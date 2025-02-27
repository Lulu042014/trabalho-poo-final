from moto_esportiva import STREETBOB
from moto_corrida import Kawasaki_Ninja_400

def test_drive(moto):
    print(f'\nTestando {moto.__class__.__name__}')
    moto.acelera()
    moto.exibe_velocidade()

if __name__ == '__main__':
    moto_esportiva = STREET_BOB(100)
    print('STREET BOB:')
    moto_esportiva.turbo()
    moto_esportiva.exibe_velocidade()
    moto_esportiva.freia()
    moto_esportiva.exibe_velocidade()
    test_drive(moto_esportiva)

    moto_corrida = Kawasaki_Ninja_400(50)
    test_drive(moto_corrida)
