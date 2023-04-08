# Define as listas para armazenar as notas dos alunos
notas_pares = []
notas_impares = []

# Recebe as notas dos alunos de cada metade da turma
for i in range(1, 51):
    if i % 2 == 0:
        print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
        msg = "POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO " + str(i) + ": "
        nota = float(input(msg))
        notas_pares.append(nota)
    else:
        print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
        msg = "POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO " + str(i) + ": "
        nota = float(input(msg))
        notas_impares.append(nota)

# Calcula as médias das notas de cada metade da turma
media_pares = sum(notas_pares) / len(notas_pares)
media_impares = sum(notas_impares) / len(notas_impares)

# Identifica a maior média
if media_pares > media_impares:
    print("A metade dos alunos pares teve a maior média, com", media_pares, "pontos.")
elif media_impares > media_pares:
    print("A metade dos alunos ímpares teve a maior média, com", media_impares, "pontos.")
else:
    print("As duas metades tiveram a mesma média, com", media_pares, "pontos.")    
