# Exercício 076

precos_material_escolar = (
    'Lápis', 1.75,
    'Borracha', 2.0,
    'Caderno', 15.90,
    'Estojo', 25.0,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.3,
    'Livro', 34.90,
)
print("-"*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-"*40)
for posicao in range(len(precos_material_escolar)):
    if posicao % 2 == 0:
        print(f"{precos_material_escolar[posicao]:.<30}", end="")
    else:
        print(f"R${precos_material_escolar[posicao]:>8.2f}")
print("-"*40)
