#4-Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado.

valor = int(input("Qual o valor para troco?"))

notas_100 = valor // 100 
valor = valor % 100 

notas_50 = valor // 50 
valor = valor % 50 

notas_20 = valor // 20 
valor = valor % 20 

notas_10 = valor // 10 
valor = valor % 10 

notas_5 = valor // 5 
valor = valor % 5 

notas_2 = valor // 2 
valor = valor % 2 

notas_1 = valor // 1 
valor = valor % 1

print(f"{notas_100} de R$100,00")
print(f"{notas_50} de R$50,00")
print(f"{notas_20} de R$20,00")
print(f"{notas_10} de R$10,00")
print(f"{notas_5} de R$5,00")
print(f"{notas_2} de R$2,00")
print(f"{notas_1} de R$1,00")