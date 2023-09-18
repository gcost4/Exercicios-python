
minutos = int(input("Digite o número de minutos atuais: "))

#calcular o fatorial
def calcular_fatorial(numero):
    if numero == 0:
        return 1
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

fatorial_minutos = calcular_fatorial(minutos)


senha = "LIBERDADE" + str(fatorial_minutos)


print("A senha para desbloqueio é:", senha)
