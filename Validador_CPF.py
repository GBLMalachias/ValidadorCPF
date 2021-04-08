"""
Validador de CPF!

"""
def valida_digitos(cpf_novo):
    soma = 0
    regressivo = 11
    qtd = len(cpf_novo)

    if qtd == 9:
        for n in range(qtd):
            regressivo -= 1
            mult = int(cpf_novo[n]) * regressivo
            soma = soma + mult

    elif qtd > 9:
        for n in range(qtd):
            mult = int(cpf_novo[n]) * regressivo
            soma = soma + mult
            regressivo -= 1

    return soma

def continuar():

    deseja_continuar = str.upper(input('\nDeseja consultar outro CPF? ( S/N ): '))

    if deseja_continuar == 'S':
        return True

    elif deseja_continuar == 'N':

        print('Programa Finalizado !')
        return False

    else:
        print('Valor digitado é invalido !')
        return continuar()

condicao = True

while condicao:
    print('\nOBS: Digitar somente os numeros do CPF')
    cpf = input('Digite seu CPF: ')
    qtd_letras = len(cpf)

    if qtd_letras == 11: #valida a quantida de letras do cpf

        if cpf.isnumeric(): #Valida a se o usuário só digitou numerico !
            novo_cpf = ''

            for n in range(9): #adiciona a uma nova string até o 8 digito do cpf
                novo_cpf = novo_cpf + cpf[n]

            valida_cpf = 11 - (valida_digitos(novo_cpf) % 11) #Faz o calculo para descobrir o proximo digito

            if valida_cpf > 9:
                novo_cpf = novo_cpf + '0'
                valida_cpf = 11 - (valida_digitos(novo_cpf) % 11)
                novo_cpf = novo_cpf + str(valida_cpf)

                if novo_cpf == cpf:
                    print(f'O CPF: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]} - É VALIDO!')
                    condicao = continuar()

                else:
                    print(f'O CPF: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]} - É INVALIDO!')
                    condicao = continuar()

            else:
                novo_cpf = novo_cpf + str(valida_cpf)
                valida_cpf = 11 - (valida_digitos(novo_cpf) % 11)
                novo_cpf = novo_cpf + str(valida_cpf)

                if novo_cpf == cpf:
                    print(f'O CPF: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]} - É VALIDO!')
                    condicao = continuar()

                else:
                    print(f'O CPF: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]} - É INVALIDO!')
                    condicao = continuar()
        else:
            print('Digite um CPF Valido!')

    else:
        print('Digite um CPF valido !')