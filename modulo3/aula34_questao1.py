#Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão. 

numero1=int(input("Digite o primeiro numero: "))
numero2=int(input("Digite o segundo numero: "))

teste = (numero1 + numero2) % 2

if teste == 0:
    print(f"A soma de {numero1} mais {numero2} é par")
else:
    print(f"A soma de {numero1} mais {numero2} é impar")

