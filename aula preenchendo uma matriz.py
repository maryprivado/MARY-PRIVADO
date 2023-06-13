import numpy as np

m= np.empty((2, 2), dtype= float)
cont = 0
listapares = []
for linhas in range(2):# percorre a  linha da matriz 
    for colunas in range(2): # percorre a coluna da matriz
        numero = float(input('digite um numero: ['+str(linhas)+'] '+ '['+str(colunas)+']')) #nesse caso o numero vai ser adcionado pelo usuario na matriz tanto na linha e na coluna, o que
#foi adicinado dentro do coxete foi transformadas em str
        m[linhas][colunas] = numero #  numero vai ser adcionada na matriz
        if m[linhas][colunas]==0:
            cont = cont + 1
            
            #criando uma lista vazia para verificar os numero pares dentro da matriz
            
        if m[linhas][colunas] % 2==0:# esse comando fica fora do if
                
            listapares.append(numero)# adiciona o valor dentro da lista vazia
print(m)
print(cont)
print(listapares)



#criando uma matriz
#m = [[1,2,3],[4,5,6],[7,8,9]]
#calcular a soma de todso os elementos da matriz
#soma = 0
#for linhas in range(len(m)):
#    for colunas in range(len(m [linhas])):
#        soma += m [linhas][colunas]
#print(f"a som de todos os elementos da matriz é {soma}. ")