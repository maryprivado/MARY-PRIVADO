import numpy as np
linha=int(input('digite valor linha: '))
coluna=int(input('digite valor coluna: '))
#matriz = np.empty((linha,coluna))

#preenchendo a matriz com valores fornecidos 
matriz = [[0 for j in range (coluna)] for i in range (linha)]
for i in range (linha):
    for j in range (coluna):
        valor = int(input(f"digite o valor para cada elemento [(i)][(j)]: "))
        matriz[i][j] = valor
# exibe a matriz na tela
for i in range (linhas):
    for j in range (colunas):
        print(matriz[i][j], end = ' ')
print()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

