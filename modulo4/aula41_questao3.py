n1, n2, n3 = float(input("Insira a nota 1: ")), float(input("Insira a nota 2: ")), float(input("Insira a nota 3: "))

m = (n1 + n2 + n3) / 3 
print(f"{m:.2f}")
while m >=40: 
    if m>= 60:
        print("Aprovado!")
    else:
        print("Recuperação!")
    
    n1, n2, n3 = float(input("Insira a nota 1: ")), float(input("Insira a nota 2: ")), float(input("Insira a nota 3: "))

    m = (n1 + n2 + n3) / 3 
    print(f"{m:.2f}")

print("Reprovado!")
print("FIM")