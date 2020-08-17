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
    # 1. Faça um Programa que peça dois números e imprima o maior deles.
    num1 = int(input('Primeiro numero: '))

    num2 = int(input('Segundo numero: '))

    if num1 > num2:
        print(num1)
    else:
        print(num2)


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