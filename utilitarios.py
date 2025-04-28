


def numero_real(label: str):
    entrada = input(label)
    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print(f"'{entrada}' não é um numero valido, digite novamente!")
        return numero_real(label)


def numero_real_max(label: str):
    max = numero_real(label)
    if 0 <= max <= 10:
        return max
    else: 
        print('A nota digitada é invalida, digite novamente!')
        return numero_real_max(label)

