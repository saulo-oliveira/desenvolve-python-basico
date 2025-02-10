import random

correto = random.randint(1, 10)

while True:
    palpite = int(input("Digite o seu palpite: "))
    if palpite > correto:
        print("O numero correto é menor")
        continue
    elif palpite < correto:
        print("O numero correto é maior")
        continue
    else:break

print(f"Você acertou! O número correto é {correto}")
