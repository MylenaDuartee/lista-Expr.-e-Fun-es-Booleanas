import math

def main():
    a = receber_lado_valido("Digite o lado a: ")
    b = receber_lado_valido("Digite o lado b: ")
    c = receber_lado_valido("Digite o lado c: ")

    if not validar_triangulo(a, b, c):
        print("Esses lados não formam um triângulo.")
        return
    
    perimetro = calcular_perimetro(a, b, c)
    area = calcular_area(a, b, c)
    tipo_lado = classificar_lados(a, b, c)
    tipo_angulo = classificar_angulos(a, b, c)

    print(f"--> Resultado <---")
    print(f"Perímetro: {perimetro}")
    print(f"Área: {area:.2f}")
    print(f"Classificação por lados: {tipo_lado}")
    print(f"Classificação por ângulos: {tipo_angulo}")

def receber_lado_valido(label):
    try:
        lado = float(input(label))
        if lado <= 0:
            print("O lado deve ser positivo.")
            return receber_lado_valido(label)
        return lado
    except ValueError:
        print("Digite um número válido.")
        return receber_lado_valido(label)

def validar_triangulo(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def calcular_perimetro(a, b, c):
    return a + b + c

def calcular_area(a, b, c):
    s = calcular_perimetro(a, b, c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def classificar_lados(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def classificar_angulos(a, b, c):
    
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c

    # Encontrar os outros dois lados
    if maior == a:
        lado1, lado2 = b, c
    elif maior == b:
        lado1, lado2 = a, c
    else:
        lado1, lado2 = a, b

    if math.isclose(maior**2, lado1**2 + lado2**2):
        return "Triângulo Retângulo"
    elif maior**2 > lado1**2 + lado2**2:
        return "Triângulo Obtusângulo"
    else:
        return "Triângulo Acutângulo"

main()
