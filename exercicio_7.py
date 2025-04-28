def main():
    uni_orig = uni_valida('digite a unidade de origem: ')
    uni_dest = uni_valida('digite a unidade de destino: ')
    temp = receber_temp(uni_orig)

    if uni_orig == 'celsius' and uni_dest == 'kelvin':
        ck = temp + 273
        print(f'{temp:.2f}°C são {ck:.2f}°K')
    elif uni_orig == 'celsius' and uni_dest == 'fahrenheit':
        cf = temp * 1.8 + 32
        print(f'{temp:.2f}°C são {cf:.2f}°F')
    elif uni_orig == 'fahrenheit' and uni_dest == 'celsius':
        fc = (temp - 32) / 1.8
        print(f'{temp:.2f}°F são {fc:.2f}°C')
    elif uni_orig == 'fahrenheit' and uni_dest == 'kelvin':
        fk = (temp - 32) * 5 / 9 + 273
        print(f'{temp:.2f}°F são {fk:.2f}°K')
    elif uni_orig == 'kelvin' and uni_dest == 'celsius':
        kc = temp - 273
        print(f'{temp:.2f}°K são {kc:.2f}°C')
    else:
        kf = (temp - 273) * 1.8 + 32
        print(f'{temp:.2f}°K são {kf:.2f}°F')


def unidades(label:str):
    entrada = input(label)
    try:
        letra = str(entrada)
        return letra
    except:
        print('A unidade é inválida, digite novamente')
        return unidades(label)
    

def uni_valida(label):
    entrada = unidades(label)
    if entrada != 'celsius' and entrada != 'fahrenheit' and entrada != 'kelvin':
        print('A unidade é inválida, digite novamente')
        return uni_valida(label)
    else:
        return entrada
    

def receber_temp(uni_orig):
    if uni_orig =='celsius':
        celsius = vali_celsius()
        return celsius
    elif uni_orig == 'kelvin':
        kelvin = vali_kelvin()
        return kelvin
    else:
        fahrenheit = receber_numero_real('digite a temperatura em fahrenheit')
        return fahrenheit
    

def receber_numero_real(label:str):
    entrada = input(label)
    try:
        numero = float(entrada)
        return numero
    except:
        print('A temperatura é inválida, digite novamente')
        return receber_numero_real(label)
    

def vali_celsius():
    entrada = receber_numero_real('digite a temperatura em celsius: ')
    if entrada < -273.15:
        print('A temperatura em celsius não pode ser menor que -273.15, digite novamente')
        return vali_celsius()
    else:
        return entrada
    

def vali_kelvin():
    entrada = receber_numero_real('digite a temperatura em kelvin: ')
    if entrada < 0:
        print('A temperatura em kelvin não pode ser menor que 0, digite novamente')
        return vali_kelvin()
    else:
        return entrada
    
main()