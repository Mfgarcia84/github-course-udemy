# Exercício 75

numeros = (
    int(input("Digite um número: ")),
    int(input("Digite outro número: ")),
    int(input("Digite mais um número: ")),
    int(input("Digite o último número: ")),
)

print(f"Você digitou os valores {numeros}.")
print(f"O valor 3 apareceu na {numeros.index(3)+1}ª posição.")
print(f"Os valores pares digitados foram:", end=" ")
for num in numeros:
    if num % 2 == 0:
        print(num, end=" ")
print()