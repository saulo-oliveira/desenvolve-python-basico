import random

lista = []

for i in range(20):
    numero = random.randint(-100,100)
    lista.append(numero)

print("Lista Ordenada: \n" ,sorted(lista))
print("Lista Não ordenada: \n",lista)
print("Maior valor: \n",max(lista))
print("Menor valor: \n",min(lista))