#5 - Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:A: Para mulheres, ter mais de 60 anos. Para homens, 65.B: Ou ter trabalhado pelo menos 30 anosC: Ou ter 60 anos  e trabalhado pelo menos 25.

genero = input("Qual o seu genero M/F?").lower()
idade = int(input("Qual a sua idade"))
tempo = int(input("Qual o seu tempo de serviço?"))

a = genero == 'f' and idade >=60
b = genero == 'm' and idade >=65
c = tempo >=30 
d = idade >60 and tempo >=25

aposentadoria = (a or b) or (c) or (d)

print(f"Sua aposentadoria é valida: {aposentadoria}")