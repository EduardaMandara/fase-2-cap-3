# Recebe a quantidade de votos para cada dia da semana
segunda = int(input("Digite a quantidade de votos para segunda-feira: "))
terca = int(input("Digite a quantidade de votos para terça-feira: "))
quarta = int(input("Digite a quantidade de votos para quarta-feira: "))
quinta = int(input("Digite a quantidade de votos para quinta-feira: "))
sexta = int(input("Digite a quantidade de votos para sexta-feira: "))

# Verifica o dia mais votado
max_votos = segunda
dia_mais_votado = "segunda-feira"

if terca > max_votos:
    max_votos = terca
    dia_mais_votado = "terça-feira"
if quarta > max_votos:
    max_votos = quarta
    dia_mais_votado = "quarta-feira"
if quinta > max_votos:
    max_votos = quinta
    dia_mais_votado = "quinta-feira"
if sexta > max_votos:
    max_votos = sexta
    dia_mais_votado = "sexta-feira"

# Exibe o resultado
print("O dia mais votado foi", dia_mais_votado, "com", max_votos, "votos.")