def main():
    numero = obter_numero_valido("Digite um número: ")
    
    if verificar_primo(numero):
        print(f'{numero} é um número primo.')
    else:
        print(f'{numero} não é um número primo.')

def verificar_primo(num, divisor=2):
    if num <= 1:
        return False
    if divisor * divisor > num:
        return True
    if num % divisor == 0:
        return False
    return verificar_primo(num, divisor + 1)

def obter_numero_valido(label):
    try:
        numero = int(input(label))
        if numero <= 0:
            print("O número digitado não é válido, digite novamente")
            return obter_numero_valido(label)
        return numero
    except ValueError:
        print("insira um número inteiro válido")
        return obter_numero_valido(label)

main()
