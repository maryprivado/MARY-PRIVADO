# usando contador em uma funcao pratica 09: foi criada uma lista, utilizado um contador(resp.appende) que adiciona os valores dentro da lista
# cria uma variavel para receber o valores da matriz e no final foi utilizado o comando if   
def desvcrime():

    resp = []
    print(' deigite s ou n')
    a=input('telefonou para a vitima? ')
    resp.append(a)
    b=input('esteve no local do crime? ')
    resp.append(b)
    c=input('mora perto da vitima? ')
    resp.append(c)
    d=input('devia para a vitima? ')
    resp.append(d)
    e=input('ja trabalhou com a vitima? ')
    resp.append(e)
    
    qtd_sim = resp.count('s')
    
    if qtd_sim == 2:
        print(' suspeito')
    elif qtd_sim == 3 or 4:
        print('cumplice')
    elif qtd_sim == 5:
        print( 'assassino')
    
    else:
        print('inocente')


desvcrime()