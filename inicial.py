

def login():
    usuario = input('insira seu usuario: ')
    senha = input('insira sua senha: ')
    if usuario == senha:
        print('usuario e senha não podem ser iguais, tente novamente')
        login()
    elif usuario != senha:
        print(f'bem vindo(a) {usuario}')
        escolha = input("""
       1 - algebra
       2 - geometria
       """)

    if escolha == '1':
        import algebra
    if escolha == '2':
        import geometria


login()
