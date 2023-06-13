salario= float(input ('digite valor do salario:'))
if salario < 280:
    reaj = salario * 0.2
    salario_novo = reaj + salario
    print( 'salario antigo:' , salario)
    print('salrio novo:' , salario_novo)
    print('porcentual aplicado: 20%')
    print(' valor do aumento:', reaj)
    
if salario >= 280 and 700:
    reaj = salario * 0.15
    salario_novo = reaj +salario
    print('salario antigo:',salario )
    print('salrio novo:' , salario_novo)
    print('porcentual aplicado: 15%')
    print(' valor do aumento:', reaj)
    
if salario >= 700 and 1500:
    reaj = salario * 0.1
    salario_novo= reaj +salario
    print('salario antigo:',salario )
    print('salrio novo:' , salario_novo)
    print('porcentual aplicado: 10%')
    print(' valor do aumento:', reaj)
    
if salario >= 700 and 1500:
    reaj = salario * 0.5
    salario_novo= reaj +salario
    print('salario antigo:',salario )
    print('salrio novo:' , salario_novo)
    print('porcentual aplicado: 5%')
    print(' valor do aumento:', reaj)

