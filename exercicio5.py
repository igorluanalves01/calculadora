from funcoes import soma, subtrair, multiplicacao, divisao
## --------------------------------------------------
def converter_numero(valor):
    try:
        return float(valor.replace(',', '.'))
    except Exception as e:
        p
if __name__ == '__main__':
    n1 = int(input(' numero um:'))
    n2 = int(input(' numero dois:'))
    n3 = int(input(' numero tres:'))

    if n1 > n2 and n1 > n3:
        print ('numero um é o maior')
    elif n2 > n1 and n2 > n3:
        print("O número dois é o maior: {0}".format(n2))
    elif n3 > n1 and n2:
        print('O número três é o maior: {}'.format(n3))
    else:
        print('os numeros colocados não tem nenhum maior que o outro')

