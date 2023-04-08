# Recebe o valor dos minutos do usuário
minutos = int(input("Digite a quantidade de minutos atuais: "))

# Calcula o fatorial dos minutos
fatorial = 1
for i in range(1, minutos + 1):
    fatorial *= i

# Concatena a senha com o fatorial calculado
senha = "LIBERDADE" + str(fatorial)

# Exibe a senha na tela
print("Senha necessária para desbloqueio: " + senha)
