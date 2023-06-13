senha = input('digite sua senha:')
tentativas = 0

while senha != '123' and tentativas < 1:
    tentativas += 1
    #tentativa + tentativa + 1 =  tentativas += 1
    print( 'senha incorreta, tente novamente!!!')
    senha = input ('digite sua senha: ')
    
if senha == '123':
    print('senha correta:')
else:
    print('numero de tentativas excedeu')