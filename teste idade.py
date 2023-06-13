def ano_nascimento():
    ano= int(input('digite ano de nascimento: '))
    idade= 2023 - ano

    if idade >= 18:
        print('maior de idade:', ano)
    else:
        print('menor')
        
ano_nascimento()
    