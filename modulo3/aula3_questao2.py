#2-Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.

#1 - Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, indicando que podem entrar no bar, e False caso contrário. 


idade_ju, idade_cr=int(input("Digite a idade de Juliana: ")), int(input("Digite a idade de Cris: "))

permissao = idade_ju > 17 or idade_cr > 17

print(permissao)