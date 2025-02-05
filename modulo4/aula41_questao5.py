participantes = int(input("Digite quantos participantes haverão na pesquisa: "))
n = 1 
soma = 0


while n <= participantes:
    idade = int(input("Digite a idade do participante: ")) 
    soma += idade
    n += 1

media = soma/participantes
print(f"A media de idade entre os participantes da pesquisa é: {media:.0f}") 