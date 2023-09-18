
porcentagens = {
    "Basic": 0.30,
    "Silver": 0.20,
    "Gold": 0.10,
    "Platinum": 0.05
}

tipo_assinatura = input("Digite o tipo de assinatura (Basic, Silver, Gold ou Platinum): ")
faturamento_anual = float(input("Digite o faturamento anual do cliente: "))


if tipo_assinatura in porcentagens:
    
    porcentagem = porcentagens[tipo_assinatura]
    bonus = faturamento_anual * porcentagem
    print(f"Valor do bônus a ser pago é: R${bonus:.2f}")
else:
    print("Tipo de assinatura inválido.")
