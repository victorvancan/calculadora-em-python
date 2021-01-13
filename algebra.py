import math

# definindo as funções dos calculos


def soma():
    try:
        numero1 = float(input('insira o primeiro numero: '))
        numero2 = float(input('insira o segundo numero: '))

        resultado = numero1 + numero2
    except:
        print('valor invalido, insira um valor válido')
        soma()

    print('{} + {}  ='.format(numero1, numero2))
    print(resultado)


def subtracao():
    try:
        numero1 = float(input('insira o primeiro numero: '))
        numero2 = float(input('insira o segundo numero: '))

        resultado = numero1 - numero2
    except:
        print('valor invalido, insira um valor válido')
        subtracao()

    print('{} - {} ='.format(numero1, numero2))
    print(resultado)


def multplicação():
    try:
        numero1 = float(input('insira o primeiro numero: '))
        numero2 = float(input('insira o segundo numero: '))

        resultado = numero1 * numero2
    except:
        print('valor invalido, insira um valor válido')
        multplicação()

    print('{} * {} ='.format(numero1,numero2))
    print(resultado)


def divisao():
    try:
        numero1 = float(input('insira o primeiro numero: '))
        numero2 = float(input('insira o segundo numero: '))

        resultado = numero1 / numero2
    except:
        print('valor invalido, insira um valor válido')
        divisao()

    print('{} / {} ='.format(numero1, numero2))
    print(resultado)


def potencia_2():
    try:
        valor = float(input('insira o numero: '))

        resultado = valor ** 2
    except:
        print('valor invalido, insira um valor válido')
        potencia_2()

    print('{}² = '.format(valor))
    print(resultado)


def potencia_3():
    try:
        valor = float(input('insira o numero: '))

        resultado = valor ** 3
    except:
        print('valor invalido, insira um valor válido')
        potencia_3()

    print('{}³ ='.format(valor))
    print(resultado)


def raiz():
    try:
        valor = float(input('insira o numero: '))

        resultado = math.sqrt(valor)
    except:
        print('valor invalido, insira um valor válido')
        raiz()

    print('√{} ='.format(valor))
    print(resultado)

def raiz_3():
    try:
        valor = float(input('insira o numero: '))

        resultado = valor ** (1 / 3)
    except:
        print('valor invalido, insira um valor válido')
        raiz_3()

    print('³√{} ='.format(valor))
    print(resultado)

def log():
    try:
        valor = float(input('insira o numero: '))
        base = float(input('insira o valor da base: '))

        resultado =(math.log(valor, base))
    except:
        print('valor invalido, insira um valor válido')
        log()

    print('log de {} na base {} ='.format(valor, base))
    print(resultado)



def percentual():
    try:
        valor = float(input('insira o numero : '))
        base = float(input('insira o valor da porcentagem desejada: '))

        resultado = valor*(base/100)
    except:
        print('valor invalido, insira um valor válido')
        percentual()

    print('{}% de {} = '.format(base, valor))
    print(resultado)







def calculadora():
    operação = input('''infome a operação desejada: 
                    1 - soma
                    2 - subtração
                    3 - multiplicação
                    4 - divisão
                    5 - elevado a 2
                    6 - elevado a 3
                    7 - raiz quadrada
                    8 - raiz cubica
                    9 - logaritimo
                    10 - percentual
                      ''')
    try:
        if operação == '1':
            soma()
        elif operação == '2':
            subtracao()
        elif operação == '3':
            multplicação()
        elif operação == '4':
            divisao()
        elif operação == '5':
            potencia_2()
        elif operação == '6':
            potencia_3()
        elif operação == '7':
            raiz()
        elif operação == '8':
            raiz_3()
        elif operação =='9':
            log()
        elif operação =='10':
            percentual()
    except:
        print('insira um valor valido')
    de_novo()



def de_novo():
    calc_again = input(''' voce gostaria de realizar outra opearação?
                           1 - sim
                           2 - não 
                           3 - trocar a seção
    ''')

    if calc_again == '1':
        calculadora()

    elif calc_again == '2':
        print('Até a proxima \U0001F917')

    elif calc_again == '3':
        import geometria
        while True:
            final()
            break
    elif calc_again != '1, 2, 3':
        print('opção invalida')
        de_novo()



def final():
    calc_again = input(''' não é possivel alterar seção, voce gostaria de realizar outra opearação nesta seção?
                               1 - sim
                               2 - não 
                               ''')
    if calc_again == '1':
        calculadora()
    elif calc_again == '2':
        print('Até a proxima \U0001F917')

calculadora()