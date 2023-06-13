#import numpy as np

#m = np.empty(2,2)

#criando uma matriz
m = [[1,2,3],[4,5,6],[7,8,9]]
#calcular a soma de todso os elementos da matriz
soma = 0
for linhas in range(len(m)):
    for colunas in range(len(m [linhas])):
        soma += m [linhas][colunas]
print(f"a som de todos os elementos da matriz é {soma}. ")