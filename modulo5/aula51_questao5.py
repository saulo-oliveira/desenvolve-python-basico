import emoji

print("Emoji Disponíveis: ")
print(emoji.emojize(":red_heart: "),"- :red_heart:")
print(emoji.emojize(":goblin:"),"- :goblin:")
print(emoji.emojize(":supervillain:"),"- :supervillain:")
print(emoji.emojize(":coffin: "),"- :coffin:")

simbolo = input(str("Digite uma frase e ela será emojizada: "))
print("Frase emojizada: ")
print(emoji.emojize(simbolo))