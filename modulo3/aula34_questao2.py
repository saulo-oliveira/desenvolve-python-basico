#Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. O programa deve imprimir uma mensagem correspondente à classificação do filme:Se a avaliação for 5, imprima "Excelente!"Se a avaliação for 4, imprima "Muito Bom!"Se a avaliação for 3, imprima "Bom!"Se a avaliação for 2, imprima "Regular."Se a avaliação for 1, imprima "Ruim."

nota = int(input("Digite qual a sua nota para o filme em uma escala de 1 a 5: "))

if 1 <= nota <=5:
    if nota == 1:
        print("A nota foi Ruim")
    if nota == 2:
        print("A nota foi Regular")
    if nota == 3:
        print("A nota foi Bom!")
    if nota == 4:
        print("A nota foi Muito Bom!")
    if nota == 5:
        print("A nota foi Excelente!")
else: 
    print("A nota digitada não é válida")