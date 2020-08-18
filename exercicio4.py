from funcoes import soma, subtrair, multiplicacao, divisao
## --------------------------------------------------
def converter_numero(valor):
    try:
        return float(valor.replace(',', '.'))
    except Exception as e:
        p
if __name__ == '__main__':
    nota1 = int(input('Digite a primeira nota: '))
    nota2 = int(input('Digite a segunda nota: '))
    media = (nota1 + nota2)/2

    if media == 10:
        print('Aprovado com Distinção.')
    elif media >= 7 and media < 10:
        print('Aprovado.')
    else:
        print('Reprovado.')


