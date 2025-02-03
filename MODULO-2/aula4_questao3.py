#3 - Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que: Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito)A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).

nome_produto1, preco_produto1, quantidade_produto1 = input("Qual é o primeiro produto?"), float(input("Qual o preco do primeiro produto?")), int(input("Qual a quantidade do primeiro produto?"))

nome_produto2, preco_produto2, quantidade_produto2 = input("Qual é o segundo produto?"), float(input("Qual o preco do segundo produto?")), int(input("Qual a quantidade do segundo produto?"))

nome_produto3, preco_produto3, quantidade_produto3 = input("Qual é o  produto?"), float(input("Qual o preco do terceiro produto?")), int(input("Qual a quantidade do terceiro produto?"))

total=float((preco_produto1*quantidade_produto1)+(preco_produto2*quantidade_produto2)+(preco_produto3*quantidade_produto3))

print(f"Total: {total:,.2f}")