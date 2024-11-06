for i in range(0,3):
    for j in range(0,3):
        
        print("valor do i = ",i)
        print("valor do j = ",j)


def vetor(x,y,z):
    vetor =[ x, y, z ]
    return vetor

def cria_matriz():
    matriz =[ [1,2,3],[4,5,6]]
    return matriz

def mostra_matriz(matriz):
    for i in range(0,2):  #linha 
        print("linha = ",i, end=',')
        for j in range(0,3): # coluna
            print(' coluna= ',j, end=', ')
            print('valor = ', matriz[i][j])
    return matriz

print(vetor(0,1,2))
matriz=cria_matriz()
mostra_matriz(matriz)
    