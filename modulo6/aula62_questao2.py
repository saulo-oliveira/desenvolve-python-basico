import random

elementos = []

num_elementos = random.randint(5,20)

for i in range(num_elementos):
    numero = random.randint(1,10)
    elementos.append(numero)

print("Os elementos da lista são: \n",elementos)

print("A soma dos elementos é: \n",sum(elementos))

print("A média dos elementos é: \n", sum(elementos)/len(elementos) )