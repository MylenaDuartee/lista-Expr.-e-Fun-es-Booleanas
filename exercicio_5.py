from utilitarios import numero_real

def main():

    valor_compra = numero_real('diga o valor da compra:')
    vip = input('é um cliente vip(sim/não)? ')
    aniversariante = input('é aniversariante(sim/não)? ')
    valor_pagar, valor_desconto, desconto_total = calculo_descontos(valor_compra, vip, aniversariante)
    saida = f'''
        Você teve um desconto de{desconto_total * 100: .1f}%
        O que equivale a R${valor_desconto:.2f}
        Você pagará R${valor_pagar:.2f}'''
    print(saida)
 

    
def acumulativo(vip,aniversariante):
    if vip == 'sim' and aniversariante == 'sim':
        return 0.08
    elif vip == 'não' and aniversariante == 'sim':
        return 0.03
    elif vip == 'sim' and aniversariante == 'não':
        return 0.05
    else:
        return 0


def desconto_base(valor_compra):
    if valor_compra >= 100 and valor_compra <= 199.99:
        return 0.05
    elif valor_compra <= 500:
        return 0.10
    else:
        return 0.15
    
def calculo_descontos(valor_compra,vip,aniversariante):
    desconto_total = desconto_base(valor_compra) + acumulativo(vip,aniversariante)
    valor_desconto = valor_compra * desconto_total
    valor_pagar = valor_compra - valor_desconto
    return valor_pagar, valor_desconto, desconto_total




main()