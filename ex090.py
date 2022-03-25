#90 Dicionário em Python
aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['media'] < 5:
    situacao = "Reprovado"
elif aluno['media'] < 7:
    situacao = "Recuperação"
else:
    situacao = "Aprovado"
aluno['situação'] = situacao

print("-="*40)
for k, v in aluno.items():
    print(f"{k} é igual a {v}")

