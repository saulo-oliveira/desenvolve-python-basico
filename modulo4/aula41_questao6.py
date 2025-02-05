experimentos = int(input("Quantos experimentos foram realizados?: "))

n = 0
sapo = 0
rato = 0
coelho = 0
controle = experimentos
while n < experimentos:
    
    quant ,cobaia = int(input("Quanto cobaias foram utilizadas: ")),input("Qual cobaia foi utilizada? 'S', 'R' ou 'C': ").lower() 

    if quant > controle:
        print("Entrada de cobaias maior que o restante de experimentos!")

    elif cobaia == 's':
        sapo += quant
        n += quant
        controle -= quant
    elif cobaia == 'r': 
        rato += quant
        n += quant
        controle -= quant
    elif cobaia == 'c':
        coelho += quant
        n += quant
        controle -= quant
    else:
        print("Entrada inválida!")
    

p_coelho = (coelho / experimentos) * 100
p_sapo = (sapo / experimentos) * 100
p_rato = (rato / experimentos) * 100

print(f"Total: {experimentos} \n Total de ratos: {rato} \n Total de sapos: {sapo} \n Total de coelhos: {coelho} \n Percentual de coelhos: {p_rato:.2f}% \n Percentual de sapos: {p_sapo:.2f}% \n Percentual de ratos: {p_coelho:.2f}% \n")