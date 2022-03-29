
#Exercício 77

palavras = (
    'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
    'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
    'MERCADO', 'PROGRAMADOR', 'FUTURO', 'ZHS',
)

vogais = ('A', 'E', 'I', 'O', 'U')

for palavra in palavras:
    print(f"\nNa palavra {palavra} temos ", end="")
    for letra in palavra:
        if letra in vogais:
            print(letra.lower(), end=" ")
