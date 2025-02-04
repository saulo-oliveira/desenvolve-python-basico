peso = float(input("Digite qual o peso do pacote: "))
distancia = int(input("Digite a distância da entrega: "))

if distancia > 0 and peso>0:
    if distancia <= 100:
        preco = distancia*1
    if 101<=distancia <=300:
        preco = distancia*1.5
    if distancia>=301: 
        preco = distancia*2
    if peso > 10:
        preco +=10
    print(f"O preco da sua entrega será de {preco}")
else:
    print("Distância ou peso inválidos")