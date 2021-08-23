def gerar_matriz (i, j):
    matriz = []

    for i in range(1,i+1):
        for j in range(1,j+1):
            if i==j:
                matriz.append([1])
            else:
                matriz.append([i**2])

    return matriz

print(gerar_matriz(3,2))