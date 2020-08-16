from funcoes import soma, subtrair, multiplicacao, divisao
## --------------------------------------------------
if __name__ == '__main__':
    # A entrada (input) do peso e da idade de uma pessoa
    continuar_executando = True
    while continuar_executando:
        nome = input('qual o seu nome?')
        peso = input('digite o seu peso: ')
        peso = float(peso)
        altura = input('digite a sua altura: ')
        altura = float(altura) # converterndo a alturam em STRING para uma altura em INTEIRO

        imc = peso /(altura*altura)
        print(round(imc, 2))

        peso_normal = False

        if imc < 18.5:
            print('abaixo do peso')
        elif imc > 18.5 and imc < 24.9:
            print('peso normal')
            peso_normal = True
        elif imc > 24.9 and imc < 29.9:
            print('sobrepeso')
        elif imc > 30.0 and imc < 34.9:
            print('obesidade grau1')
        elif imc > 35.0 and imc < 39.9:
            print('obesidade grau2')
        else:
            print('obesidade grau3')


        if peso_normal:
            print('Parabens {}, vc é saudavel'.format(nome))

        encerrar = input('aperte q para encerrar')
        if encerrar == 'q':
            continuar_executando = False










"""
+ soma
- subtrai
* multiplica
/ divide
a e b

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

"""