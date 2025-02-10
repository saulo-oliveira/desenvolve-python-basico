import random
import math


quantidade = int(input("Quantos valores deseja?: "))
soma = 0

for i in range(quantidade):
    aleatorio = random.randint(0,100)
    print(f"O numero aleatório é: {aleatorio}")
    soma += aleatorio
    print(f"Sua soma atual é: {soma}")

print(f"A soma total foi: {soma}")
print(f"A raiz quadrada da soma é: {math.sqrt(soma)}")
    