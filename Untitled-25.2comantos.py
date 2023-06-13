#criando uma matriz: pedindo ao usuario para atribuir valores da linha e das colunas
import numpy as np
linha=int(input('digite valor linha da matriz: '))
coluna=int(input('digite valor coluna da matriz: '))
matriz = np.empty((linha,coluna))

#criar uma matriz vazia
matriz = [[0 for j in range (coluna)] for i in range (linha)]
#preenchendo a matriz com valores fornecidos
for i in range (linha):
    for j in range (coluna):
        valor = int(input(f"digite o valor para cada elemento [(i)][(j)]: "))
        matriz[i][j] = valor
        
# exibe a matriz na tela
for i in range (linha):
    for j in range (coluna):
        print(matriz[i][j], end = ' ')
        print(matriz)
        if matriz[i][j]==8:
            print(f'numero foi encontrado na linha: {i}, e coluna: {j}')    
print()          
        
####

#import numpy as np
#linha=int(input('digite valor linha da matriz: '))
#coluna=int(input('digite valor coluna da matriz: '))      
#prenchendo coluna manuamente   
#matriz= np.empty((linha,coluna))
#matriz[0][1]=3
#print(matriz)


#matriz[0][0]= 1
#matriz[0][1]= 2
#matriz[1][0]= 8
#matriz[1][1]= 3

#print(matriz)






#criando matriz so com zero esse tipo de matriz ja é pre definida
# np.Zeros
#import numpy as np
#m = np.zeros((5,5), dtype=float)

#print(m)

