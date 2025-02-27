from moto_usual import Harley_Davidson_Street_750
from moto_esportiva import Kawasaki_Ninja_400

def test_drive(moto):
    print(f'\nTestando {moto.__class__.__name__}')
    moto.acelera()
    moto.exibe_velocidade()

if __name__ == '__main__':
    moto_usual = Harley_Davidson_Street_750(100)
    print('Harley_Davidson_Street_750:')
    moto_usual.turbo()
    moto_usual.exibe_velocidade()
    moto_usual.freia()
    moto_usual.exibe_velocidade()
    test_drive(moto_usual)

    moto_esportiva = Kawasaki_Ninja_400(50)
    test_drive(moto_esportiva)
