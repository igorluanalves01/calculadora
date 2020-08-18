"""
1. Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
if __name__ == '__main__':
    print('Iniciado')

    execute = 1
    while execute == 1: # if <condição>: ### Exemplos de condição: 2 + 2 == 4; 4*2 == 16; 10 > 20
        nota = int(input('indique o valor informado'))
        if nota <0 or nota>10:
            print('valor invalido')
        else:
            execute = 0





    # 1ª forma
    """
    while <condicao>:
        <conteudo>
    for item : <lista>
        <conteudo>
    """
    i = 0
    print('While')
    while i < 10:
        print(i)
        i += 1
    print('For')
    lista = [1, 2, 3]
    for item in lista:
        print(item)

    print('While com break')
    i = 0
    while i < 10:
        print(i)
        i += 1
        if i >= 5:
            print('interrompendo o laço while')
            break
    print('i')

    print('While com continue')
    i = 0
    while i < 10:
        i += 1
        if i == 5:
            continue
        print(i)

    print('i')

