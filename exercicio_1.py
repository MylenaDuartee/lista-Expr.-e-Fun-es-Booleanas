
def receber_ano():
    ano = input('diga o ano: ')
    
    try:
       numero = int(ano)
       return numero
    except ValueError:
        print(f'O valor "{ano}" não é um inteiro válido!')
        return receber_ano()
     

def ano_min():
    numero = receber_ano()
    minimo = 1000

    if numero >= minimo:
        return numero

    else: 
        print(f'O número deve ser no mínimo {minimo}')
        return ano_min()
    
def bisexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

def main():
    ano = ano_min()

    if bisexto(ano):
        print('É um ano bisexto!')
    else:
        print('Não é um ano bisexto!')


main()
