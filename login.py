from time import sleep

usuario = 1234
senha = 9999
erros = 0
erros_bloqueio = 0

print('-=' * 11)
print('{:^22}' .format('OLÁ USUÁRIO'))
print('-=' * 11)

usuario_acesso = int(input('Digite o seu código de acesso: '))

if usuario_acesso != usuario:
    print('Usuário invalido.')
    print('Sistema encerrado')

elif usuario_acesso == usuario:
    senha_acesso = int(input('Digite sua senha: '))

    while senha_acesso != senha:
        print('-=' * 11)
        opcoes = int(input('''[1] Tentar novamente\n[0] Encerrar sistema\nDigite uma das opções: '''))
        print('-=' * 11)

        if opcoes == 1:
            senha_acesso = int(input('Digite sua senha novamente: '))
            erros += 1

        elif opcoes != 1 and opcoes != 0:
            print('Opção invalida. Tente novamente.')

        else:
            print('Sistema encerrado.')
            break

        if erros == 5:
            print('-=' * 11)
            print('Você errou sua senha várias vezes, espere 5 segundos antes de tentar novamente.')
            erros = 0
            erros_bloqueio += 1

            for espera in range(1, 6):
                print(espera)
                sleep(1)

        elif erros_bloqueio == 3:
            print('Você excedeu o limite de tentativas.\nO sistema foi bloqueado.')
            break

    if senha_acesso == senha:
        print('-=' * 11)
        print('Acesso permitido.')
        print('Bem-Vindo(a) Usuário.')
        print('-=' * 11)
