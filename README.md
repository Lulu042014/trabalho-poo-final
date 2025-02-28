README - Simulador de Motos com POO ----> verson python 3.12

Visão Geral

Este projeto implementa um sistema de simulação de diferentes tipos de motos utilizando os princípios da Programação Orientada a Objetos (POO) em Python. Ele demonstra conceitos como herança, polimorfismo, encapsulamento e abstração através das classes Moto, Kawasaki_Ninja_400 e Harley_Davidson_Street_750.

Estrutura do Código

O código é composto pelas seguintes classes:

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

Como Executar o Programa

Basta rodar o script Python e ele realizará os seguintes testes:

Criar uma Harley_Davidson_Street_750 com velocidade inicial de 100 km/h.

Aplicar o turbo(), aumentando a velocidade para 150 km/h.

Aplicar freia(), reduzindo para 140 km/h.

Testar a aceleração normal (+50 km/h).

Criar uma Kawasaki_Ninja_400 com velocidade inicial de 50 km/h.

Testar a aceleração especial de corrida (+150 km/h).

Saída Esperada

O programa imprimirá algo semelhante a:

Harley_Davidson_Street_750:
Turbo ativado! A velocidade aumentou em 50 km/h
Velocidade atual: 150 km/h
Velocidade atual: 140 km/h

Testando Harley_Davidson_Street_750
Velocidade atual: 190 km/h

Testando Kawasaki_Ninja_400
Aceleração de corrida! A velocidade aumentou em 150 km/h
Velocidade atual: 200 km/h

Conceitos de POO Aplicados

Encapsulamento: Atributo velocidade protegido por métodos.

Herança: Kawasaki_Ninja_400 e Harley_Davidson_Street_750 herdam de Moto.

Polimorfismo: O método acelera() tem diferentes comportamentos nas subclasses.

Abstração: A classe Moto define uma moto genérica e outras classes refinam comportamentos.

Contribuição

Sinta-se à vontade para modificar o código e adicionar novas funcionalidades, como novas categorias de motos ou novos métodos de aceleração!

