#Primeiro exemplo

def say_hello(name='World', greeting=None):
    if greeting == None:

        print(f'Hellooooooooo {name}')
    else:
        print(f'{greeting} {name}')

say_hello('Iris')
say_hello()
say_hello(greeting='inhaiiiii')
say_hello('iris', 'inhaiiiii')

#segundo exemplo

def soma(x,y):
    return x + y

print(soma(4,6))
result = soma(5,7)
print(result)

#terceiro exemplo

def criar_baralho():
    naipes = ["copas", "espadas", "paus", "ouros"]
    cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Rainha", "Rei", "Ás"]
    baralho = []

    for naipe in naipes:
        for carta in cartas:
            baralho.append(f'{carta} de {naipe}')

    return baralho

meu_baralho = criar_baralho()
print(len(meu_baralho))
print(meu_baralho)