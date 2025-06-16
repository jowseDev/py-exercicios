def valorPagamento(val, atr):
    if atr > 0:
        multa = 0.03
        multa_dia = 0.001 * atr
        total = float(val + (val * multa_dia) + (val * multa))
    else:
        total = val
    return total
