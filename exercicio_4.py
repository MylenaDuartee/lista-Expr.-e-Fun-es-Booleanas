from utilitarios import numero_real_max

     
    
def situacao_aluno(nota1,nota2,nota3):
     media = (nota1 + nota2 + nota3) / 3

     if media < 5:
        return f'''         Sua média é:{media: .1f} 
        Você está reprovado!'''
     elif media <= 6.9:
         return f'''         Sua média é:{media: .1f}
         Você está de recuperação!'''
     else:
         return f'''         Sua média é:{media: .1f}
         Parabéns, você está aprovado!'''
    
     

def main():
    nota1 = numero_real_max('digite sua primeira nota: ')
    nota2 = numero_real_max('digite sua segunda nota: ')
    nota3 = numero_real_max('digite sua terceira nota: ')

    if nota1 == 0 or nota2 == 0 or nota3 == 0:
        return 'Você reprovou pois uma das notas foi 0'
    else: 
        return situacao_aluno(nota1,nota2,nota3)


print(main())