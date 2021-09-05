def matriz_solucao (matX, matA, matB):

    a = int(matA[0][0])
    b = int(matA[0][1])
    c = int(matA[1][0])
    d = int(matA[1][1])
    e = int(matB[0][0])
    f = int(matB[1][0])

    y = (((a*f) - (c*e))/((a*d) - (c*b)))
    x = ((e - (b*y))/a)

    matX[0][0] = x
    matX[1][0] = y

    print('A matriz X é: \n')

    return matX

print(matriz_solucao([[0],[0]],[[3,4],[2,3]],[[-1],[-1]]))