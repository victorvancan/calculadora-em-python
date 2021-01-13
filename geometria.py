import math


def area_triangulo():
    try:
        base = float(input('insira o valor da base: '))
        altura = float(input('insira valor da altura: '))

        resultado = (base * altura) / 2
    except:
        print('valor invalido, insira um valor válido')
        area_triangulo()

    print(resultado)


def area_trapezio():
    try:
        base_maior = float(input('informe a base maior: '))
        base_menor = float(input('informe a base menor: '))
        altura = float(input('informe a altura: '))

        resultado = ((base_maior + base_menor) * altura)/2
    except:
        print('valor invalido, insira um valor válido ')
        area_trapezio()
    print(f'{resultado}\n')


def area_cubo():
    try:
        lado = float(input('inria o valor do lado '))

        resultado = lado ** 3
    except:
        print('valor invalido, insira um valor válido ')
        area_cubo()
    print(resultado)


def area_quadrado():
    try:
        lado = float(input('insira o valor do lado: '))

        resultado = lado * lado
    except:
        print('valor invalido, insira um valor válido ')
        area_quadrado()

    print(resultado)


def area_retangulo():
    try:
        b = float(input('informe o valor da base: '))
        h = float(input('informe o valor da altura: '))

        resultado = 2*(b+h)
    except:
        print('valor invalido, insira um valor válido ')
        area_retangulo()
    print(resultado)


def area_circulo():
    try:
        r = float(input('informe o valor do raio: '))

        resultado = math.pi*r**2
    except:
        print('valor invalido, insira um valor válido ')
        area_circulo()

    print(f'{resultado} π')


def diametro_circ():
    try:
        r = float(input('insira o raio: '))

        resultado = 2 * r
    except:
        print('valor invalido, insira um valor válido ')
        diametro_circ()
    print(resultado)


def peri_circulo():
    try:
        r = float(input('insira o raio: '))

        resultado = 2*math.pi*r
    except:
        print('valor invalido, insira um valor válido ')
        peri_circulo()

    print(f'{resultado} π')


def area_losango():
    try:
        d_maior = float(input('insira a diagonal maior: '))
        d_menor = float(input('insira a diagonal menor'))

        resultado = (d_maior * d_menor)/2

    except:
        print('valor invalido, insira um valor válido ')
        area_losango()
    print(resultado)


def cosseno():
    try:
        valor = float(input('insira o valor: '))

        resultado = math.cos(valor)
    except:
        print('valor invalido, insira um valor válido')
        cosseno()
    print(resultado)


def seno():
    try:
        valor = float(input('insira o valor: '))

        resultado = math.sin(valor)
    except:
        print('valor invalido, insira um valor válido')
        seno()

    print(resultado)


def tang():
    try:
        valor = float(input('insira o valor: '))

        resultado = math.tan(valor)
    except:
        print('valor invalido, insira um valor válido')
        tang()

    print(resultado)


def hipotenusa():
    try:
        numero1 = float(input('insira o primeiro numero: '))
        numero2 = float(input('insira o segundo numero: '))

        resultado = math.hypot(numero1,numero2)
    except:
        print('valor invalido, insira um valor válido')
        hipotenusa()

    print(resultado)


def calculo():
    usuario = input("""informe a operação desejada: 
                    1 - area de um triangulo     |  10 - cosseno
                    2 - area de um trapezio      |  11 - seno
                    3 - area de um cubo          |  12 - tangente
                    4 - area do quadrado         |  13- hipotenusa
                    5 - area de um retangulo     |
                    6 - area de um circulo       |
                    7 - diametro do circulo      |
                    8 - perimetro de um circulo  |
                    9 - area de um losango       | 
                                                              
                                          """)
    try:
        if usuario == '1':
            area_triangulo()
        elif usuario == '2':
            area_trapezio()
        elif usuario == '3':
            area_cubo()
        elif usuario == '4':
            area_quadrado()
        elif usuario == '5':
            area_retangulo()
        elif usuario == '6':
            area_circulo()
        elif usuario == '7':
            diametro_circ()
        elif usuario == '8':
            peri_circulo()
        elif usuario == '9':
            area_losango()
        elif usuario == '10':
            cosseno()
        elif usuario == '11':
            seno()
        elif usuario == '12':
            tang()
        elif usuario == '13':
            hipotenusa()
    except:
        print('essa não é uma opção valida! ')
        calculo()

    de_novo()


def de_novo():
    calc_again = input(''' voce gostaria de realizar outra opearação?
                           1 - sim
                           2 - não 
                           3 - trocar a seção
    ''')

    if calc_again == '1':
        calculo()

    elif calc_again == '2':
        print('Até a proxima \U0001F917')

    elif calc_again == '3':
        import algebra
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
        calculo()

    elif calc_again == '2':
        print('Até a proxima \U0001F917')

calculo()