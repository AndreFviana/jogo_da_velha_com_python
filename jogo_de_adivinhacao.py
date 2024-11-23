from random import randint


print("Bem Vindo(a) ao jogo de Adivinhação! Seu objetivo é acertar um número secreto que só o computador sabe. Terá também que estar atento as dicas para chutar o número certo, pois, existe um limite de 10 tentativas. Boa sorte!")

numeroSoteado = randint(0,10)
meuPalpite = False
palpites = 0
limiteDePalpites = 3

while not meuPalpite and palpites < limiteDePalpites:
    jogador =int(input("insira um numero:"))
    palpites += 1
    
    if jogador == numeroSoteado:
        meuPalpite = True
        print("acertou com {} tentativas!".format(palpites))
        
    elif jogador < numeroSoteado:
        print("Vixe...É um número MAIOR")
    elif jogador > numeroSoteado:
        print("chuta um número menor")
if not meuPalpite:
    print("Você perdeu porque atingiu o limite de chutes")




