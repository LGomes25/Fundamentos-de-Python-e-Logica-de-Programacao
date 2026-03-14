print()
texto = input('Informe um texto:')
VOGAIS = "AEIOU"

# Exemplo com iteravel
for letras in texto:
    if letras.upper() in VOGAIS:
        print(letras, end=" ")
else:
    print()

# Exemplo com range("start", "end", "step") onde: ["start" incluso]; ["end" excluso]; ["step" opcional]
for numero in range(0, 51, 5):
    print(numero, end=" ")