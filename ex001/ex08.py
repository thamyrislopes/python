faltas = int(input("Quantidade de faltas: "))
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1+n2)/2

print(f"Média: {media}")

if faltas <= 5 and media >= 7:
    print("ALUNO APROVADO!")
else:
    print("ALUNO REPROVADO!")