classe = input("Qual será a sua classe de escolha?").lower()
pontos_forca = int(input("Determine seus pontos de força: "))
pontos_magia = int(input("Determine seus pontos de magia: "))

classe_guerreiro = classe == 'guerreiro' and pontos_forca >= 15 and pontos_magia <= 10
classe_mago = classe == 'mago' and pontos_forca <=10 and pontos_magia >=15
classe_arqueiro = classe == 'arqueiro' and (pontos_forca >= 5 >= pontos_magia) and (pontos_forca <= 15 >= pontos_magia)

valido = print()