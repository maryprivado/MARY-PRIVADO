#FUNCAO
#criando uma funcao
#def area_retangulo(base , area):
#    area = base * altura
#    return base
#chamando uma funcao:
#resultado = area_retangulo(5, 10)
#print(resultado)

#funcao de soma dois numeros
#def m (n1 ,n2):
#    soma = n1 + n2 
#    return soma
#resultado = m (5 , 8)
#r2 = m (6 , 8)
#print(resultado)
#print(r2)


#def somar (nun1 , nun2):
#    resultado = nun1 + nun2

#    return resultado
#print(somar(8,6))


#def conta (numero1 , numero2):
#    soma =numero1 + numero2
#    return soma
#resultado = conta(15, 82)
#print( resultado)

#1 funcao de notas
#def medianotas ():
#    n1= float(input('digite a primeira nota: '))
#    n2=float(input('digite segunta nota: '))
#    n3= float(input('digite o terceira nota: '))
#    media = (n1 + n2 + n3)/3
#    return media
#print(medianotas())


#funcao de notas
#def medianotas(n1, n2, n3):
#    media = (n1 + n2 + n3)/3
#    return media
#print(medianotas(8,8,9))

#area do triangulo 
#def area_triagulo (altura, base):
#    area = altura * base /2
#    print(area)
#    return area
#print(area_triagulo(9, 5))



# funcao 2 forma
#def area_triagulo (altura, base):
#    area = altura * base /2
#    print(area)
#    return area
#area_triagulo(5, 8)

#funcao
#def area_triagulo (altura, base):
#    area = (altura * base) /2
#    print(area)
#    return area
#criando variavel dentro da funcao
#aa= area_triagulo(6, 8)
#print(' a area do triangulo é: ' , aa)


#def calcular_pagamento(qtd_horas, valor_hora):
#  horas = float(input(qtd_horas))
#  taxa = float(input(valor_hora))
#  if horas <= 40:
#    salario=horas*taxa
#  else:
#    h_excd = horas - 40
#    salario = 40*taxa+(h_excd*(1.5*taxa))
#  return salario


#str_horas= input('Digite as horas: ')
#str_taxa=input('Digite a taxa: ')
#total_salario = calcular_pagamento(str_horas,str_taxa)
#print('O valor de seus rendimentos é R$',total_salario)

#b**2 -4ac

#resolever esse codigo 

#def equacao(a , b ,c):
#    raiz= (b**2) - (4 * a )*c
#    print(raiz)
#    return raiz
#equacao(8 , 4, 2)


#import math
#a= 2
#b= 4
#c= 2
#delta = (b**2) - ( 4*a*c)
#raiz= delta / 2 *a
#x= - b+- raiz / 2*a
#print(x)
#def equacao (a, b, c):
#    delta = (b**2)-(4*a)*c
#    return delta
#resultado= equacao(2, 4, 2)
#print(resultado)
#print(delta)



#funcao sem parametros
#def idade (i):
    
#    if i <= 18:
#        print('maior de idade')
#    else:
#        print('maior idade')
#idade(19)


# funcao usando parametro
#def idade ():
#      i= int(input('digite idade:'))
#      if i <= 18:
#        print('maior de idade')
#      else:
          
#        print('menor idade')
#idade()



#fucao verificar numero
#def pares(n):
#    if n % 2 == 0:
#        n= float(input('digite valor: '))

#        print(' numero par')
#    else:
#        print(' impar')
#pares(12)

    

#def pares(n):
#    if n % 2 == 0:
#        return True
#    else:
#        return False

#pares(9)

#if delta > 0:
#    x1
#    x2
#    return x1, x2
#elif delta == 0:
#    x= -b / (2*a)
#    return x
#else:
#    print()
    
#def notas(n, n1, n2):
#        media = (n + n1 + n2) /3
#if media < 7:
#       print(reprovado)
#else:
#        print(aprovado)
#notas(8, 8, 9)


#deu certo
#def salario_mes ():
#        ghora=float(input('digite valor ghora: '))
#        horastra=int(input( 'digite horastra: '))
#
#        salariofinal= ghora * horastra
#        print('salario é: ', salariofinal)
        
#print(salario_mes())
        


#def temperatura ():
#    f= float(input('digite a temperatura: '))
#    c= 5*((f-32) / 9)
#    print('a temperatura em celcius é:', c)
#chama a funcao
#temperatura()





#USANDO O COMANDO IF
#def pessoaalt ():
#        h= float(input('digite a altura: '))
#        sex= input('digite m para masculino e f para fminimino:')
#        if sex == 'm':
#                homem(72.7 * h)-58
#                print(' o pseo ideal é:', homem)
#        elif sex == 'f':
#                mulher(62.1 * h) -44.7
#                print('o peso ideal é: ', mulher)
#pessoaalt()
        
        
        
        
def triangulo():
        a= float(input('digite valor para A: '))
        b= float(input('digite valor para B: '))
        c= float(input(' digite valor para C: '))
        
        if a==b==c:
                print('triangulo equilatero')
        elif a==b or b==c or a==c:
                print('triangulo isosceles')
        elif a!=b!=c:
                print('triangulo escoceno')
triangulo()