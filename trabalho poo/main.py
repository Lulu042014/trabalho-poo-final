from moto_esportiva import Harley_Davidson_Street_750
from moto_corrida import Kawasaki_Ninja_400

def test_drive(moto):
    print(f'\nTestando {moto.__class__.__name__}')
    moto.acelera()
    moto.exibe_velocidade()

if __name__ == '__main__':
    moto_esportiva = Harley_Davidson_Street_750(100)
    print('Harley_Davidson_Street_750:')
    moto_esportiva.turbo()
    moto_esportiva.exibe_velocidade()
    moto_esportiva.freia()
    moto_esportiva.exibe_velocidade()
    test_drive(moto_esportiva)

    moto_corrida = Kawasaki_Ninja_400(50)
    test_drive(moto_corrida)
