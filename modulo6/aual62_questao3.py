import random

lista1 = []
lista2 = []
interseccao = []

for i in range(20):
    numero1=random.randint(0,50)
    lista1.append(numero1)
    numero2=random.randint(0,50)
    lista2.append(numero2)


print("A lista 1 é: \n",lista1)
print("A lista 2 é: \n",lista2)

for i in lista1:
    if i in lista2 and i not in interseccao:
        interseccao.append(i)

interseccao.sort()
print("A interseccao é: \n",interseccao)

for i in interseccao:
    contagem1 = lista1.count(i)
    contagem2 = lista2.count(i)
    print(f"{i}: (lista1:{contagem1}, (lista2: {contagem2})")
    