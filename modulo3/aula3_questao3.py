#3-Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo. O programa deve imprimir True se o participante tiver entre 16 e 18 anos, já tiver jogado pelo menos 3 jogos e já ter vencido pelo menos 1 jogo, permitindo seu ingresso no clube. Sua expressão deve imprimir False caso contrário.

idade, qt_jogos, vitorias = int(input("Qual a sua idade? ")),input("Já jogou mais que 3 jogos?").lower()=='true', int(input("Quantas vitórias já teve?"))

resultado = (16<= idade <= 18) and qt_jogos and (vitorias >=1)

print(f"Apto para ingressar no grupo de jogos: {resultado}")