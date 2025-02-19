lista1 = []
lista2 = []
lista_intercalada = []

qt_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {qt_lista1} elementos da lista 1: ")

for i in range(qt_lista1):
    elemento = int(input())
    lista1.append(elemento)

print(lista1)

qt_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {qt_lista2} elementos da lista 2: ")

for i in range(qt_lista2):
    elemento = int(input())
    lista2.append(elemento)

tamanho = lambda lista1,lista2: len(lista1) if len(lista1) >=len(lista2) else len(lista2)
maior = tamanho(lista1,lista2)

for i in range(maior):
    if i < len(lista1):
        lista_intercalada.append(lista1[i])
    if i < len(lista2):
        lista_intercalada.append(lista2[i])

print(lista_intercalada)