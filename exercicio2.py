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
    metro = converter_numero(input('informe o valor em metro: '))
    print('o valor digitado em é: {} cm'.format( int(metro*100 )))













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