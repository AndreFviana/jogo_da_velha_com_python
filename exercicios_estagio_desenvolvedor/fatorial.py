import math
"""
#calculando fatorial
def fatorial(n):
    resultado= 1
    for i in range(n,0,-1):
        resultado *= i
    return resultado
num = int(input("digite um numero: "))
print(f"o fatorial de {num} é {fatorial(num)}")
"""
"""
#versão sem o return
def fatorial(n):
    resultado= 1
    for i in range(n,0,-1):
        resultado *= i
    print(f"o fatorial de {n} é {resultado}")

print("ola")    
fatorial(3)
"""
"""
#fatorial com while
def fatorial(n):
    resultado= 1
    while n>1:
        resultado *= n
        n -= 1
    return resultado
n=3
resultado =fatorial(n)
print(f"fatorial de:{n} é {fatorial(n)} ")"
"""
"""
#fatorial com listas
def lista_fatorial(lista):
    fatorias = []
    for n in lista:
        fatorias.append(math.factorial(nms))
    return fatorias    
numeros = [3,4,5]
cpf_input = input("digite seu cpf")
#convertendo str para int
nms = list(map(int,cpf_input.split()))
print(nms)
resultado = lista_fatorial(nms)
print(f"o fatorial de {', '.join(map(str, nms))} é {', '.join(map(str,resultado))}")
"""

def fat(n):
    resultado = 1
    for i in range(n,0,-1):
        resultado *= i
        return 
    print(f"o fatorial de {n} é {resultado}")
resultado = fat(n)
numeros = list(map(int,input("digite um numero: ").split()))
print(f"fatorial de {numeros[0]} é {resultado}")
a
b
c
d

