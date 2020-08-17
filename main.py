from funcoes import soma, subtrair, multiplicacao, divisao
## --------------------------------------------------
def converter_numero(valor):
    try:
        return float(valor.replace(',', '.'))
    except Exception as e:
        print('o valor digitado é invalido, indo para próxima pessoa: {}'.format(e))
        return None
if __name__ == '__main__':
    # A entrada (input) do peso e da idade de uma pessoa
    continuar_executando = True
    lista = []
    while continuar_executando:
        nome = input('qual o seu nome? ')
        lista.append(nome)
        peso = input('digite o seu peso: ')
        peso = converter_numero(peso)
        if peso is None:
            continue
        altura = input('digite a sua altura: ')
        altura = converter_numero(altura) # converterndo a alturam em STRING para uma altura em INTEIRO
        if altura is None:
            continue

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

    print('todas as pessoas que testaram: '+str(lista))

    for item in lista:
        print(item)

        if item == 'igor':
            print('hum seu nome é igor')











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