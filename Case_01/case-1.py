valor_bonus = faturamento_anual * porcentagem_bonus

def calcular_bonus(tipo_assinatura, faturamento_anual):
    if tipo_assinatura == 'basica':
        porcentagem_bonus = 0.05
    elif tipo_assinatura == 'premium':
        porcentagem_bonus = 0.1
    elif tipo_assinatura == 'vip':
        porcentagem_bonus = 0.15
    else:
        return 'Tipo de assinatura inválido'

    print (valor_bonus)