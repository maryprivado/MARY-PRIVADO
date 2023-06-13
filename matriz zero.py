#
import numpy as np
#cont= 0
matriz_varia =  np.empty((2,2))
for i in range(2):
    for j in range(2):
        valor = int(input("digite os valores do elementos [(i)][(j)]: "))
        matriz_varia[i][j] = valor
        if matriz_varia[i][j]:
            cont= 0
            cont= cont + 1
print(cont)
        
#print(matriz_varia)