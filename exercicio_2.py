from utilitarios import numero_real

def main():
    peso = numero_real("diga seu peso: ")
    altura = numero_real("diga sua altura: ")

    imc = calculo_imc(peso,altura)
    classificar = classificar_imc(imc)
    saida = f'''    ---------------------------------   
    seu imc é: {imc:.1f}
    sua classificação é: {classificar}
    ---------------------------------'''
    print(saida)

def calculo_imc(peso,altura):
    return peso / (altura ** 2)
 
def classificar_imc(imc):
    
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc <= 24.9:
        return 'Peso normal'
    elif imc <= 29.9:
        return 'sobrepeso'
    elif imc <= 34.9:
        return 'obesidade I'
    elif imc <= 39.9:
        return 'obesidade II'
    else: 
        return 'obesidade III'
    
main()
