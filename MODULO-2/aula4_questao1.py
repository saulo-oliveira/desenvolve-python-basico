#1 - Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado como mostra o exemplo a seguir: O terreno possui 250m2 e custa R$512,490.50

#input de das medidas do terreno
comprimento, largura = int(input("Qual o comprimento do lote?")),int(input("Qual é a largura do lote?"))
#input do valor de do m² da área 
preco = float(input("Qual o preço do m² em sua região²"))
#calculo das contas
valor = (comprimento*largura)*preco
#função para mostrar na tela
print(f"O terreno possui {comprimento*largura}m² e custa R${valor:,.2f}")