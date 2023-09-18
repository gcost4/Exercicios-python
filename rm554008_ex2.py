
votos = {
    "segunda-feira": 0,
    "terça-feira": 0,
    "quarta-feira": 0,
    "quinta-feira": 0,
    "sexta-feira": 0
}


for dia in votos:
    votos[dia] = int(input(f"Quantos votos para {dia}: "))


dia_mais_votado = max(votos, key=votos.get)
votos_maximos = votos[dia_mais_votado]


empate = [dia for dia, votos in votos.items() if votos == votos_maximos]


if len(empate) == 1:
    print(f"O dia mais votado é {dia_mais_votado} com {votos_maximos} votos.")
else:
    print("Houve um empate entre os seguintes dias:")
    for dia in empate:
        print(f"{dia} com {votos_maximos} votos.")
