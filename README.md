1. Classe Moto

A classe base que representa uma moto genérica. Possui os seguintes atributos e métodos:

Atributo: velocidade (representa a velocidade da moto)

Métodos:

acelera(): Aumenta a velocidade em 50 km/h.

freia(): Reduz a velocidade em 10 km/h, garantindo que não fique negativa.

exibe_velocidade(): Exibe a velocidade atual.

2. Classe Kawasaki_Ninja_400

Uma subclasse de Moto, que representa uma moto esportiva de alta velocidade. Modifica o método acelera() para aumentar a velocidade em 150 km/h ao invés de 50 km/h.

3. Classe Harley_Davidson_Street_750

Uma subclasse de Moto, que adiciona um novo método turbo(), permitindo aumentar a velocidade em 50 km/h de uma vez.

4. Função test_drive(moto)

Uma função que recebe um objeto do tipo Moto ou de suas subclasses e executa um teste de aceleração, demonstrando o conceito de polimorfismo.

PASSOS DO CODIGO 

Criar uma Harley_Davidson_Street_750 com velocidade inicial de 100 km/h.

Aplicar o turbo(), aumentando a velocidade para 150 km/h.

Aplicar freia(), reduzindo para 140 km/h.

Testar a aceleração normal (+50 km/h).

Criar uma Kawasaki_Ninja_400 com velocidade inicial de 50 km/h.

Testar a aceleração especial de corrida (+150 km/h).

CONCEITOS DE POO APLICADOS 

Encapsulamento: Atributo velocidade protegido por métodos.

Herança: Kawasaki_Ninja_400 e Harley_Davidson_Street_750 herdam de Moto.

Polimorfismo: O método acelera() tem diferentes comportamentos nas subclasses.

Abstração: A classe Moto define uma moto genérica e outras classes refinam comportamentos.
