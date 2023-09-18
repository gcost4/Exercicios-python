
notas_pares = []
notas_impares = []


for i in range(1, 51):
    if i % 2 == 0:
        print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
    else:
        print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
    
    nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
    
    if i % 2 == 0:
        notas_pares.append(nota)
    else:
        notas_impares.append(nota)


media_pares = sum(notas_pares) / len(notas_pares)
media_impares = sum(notas_impares) / len(notas_impares)


if media_pares > media_impares:
    print("Alunos pares teve a maior nota.")
elif media_impares > media_pares:
    print("Alunos ímpares teve a maior nota.")
else:
    print("As duas metades tiveram a mesma média de notas.")
