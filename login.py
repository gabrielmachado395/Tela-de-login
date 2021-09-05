usuario = 1234
senha = 9999
erros = 0

usuario_acesso = int(input('Digite o código de usuário: '))

if usuario_acesso != usuario:
    print('Usuário invalido.')
    print('Sistema encerrado')

elif usuario_acesso == usuario:
    senha_acesso = int(input('Digite sua senha: '))

    while senha_acesso != senha:
        opcoes = int(input('''[1] Tentar novamente\n[0] Encerrar sistema\nDigite uma das opções: '''))

        if opcoes == 1:
            senha_acesso = int(input('Digite sua senha novamente: '))

        elif opcoes != 1 and opcoes != 0:
            print('Opção invalida. Tente novamente.')

        else:
            print('Sistema encerrado.')
            break

    if senha_acesso == senha:
        print('Acesso permitido.')
        print('Bem-Vindo(a) Usuário.')
