# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.


def verificar_paridade(uff):
    par = (a % 2)
    if par == 0:
        print (f"O número {a} é par.    ")
    else:
        print(f"O número {a} é Ímpar.   ")
    return par

a = int(input("Digite um número inteiro para verificar a paridade:  "))

par = verificar_paridade(a)