
#FAÇA A AOPERAÇÃO '[A+(B-Ct)]*B'

l1 = int(input("Digite o número de linhas da matriz A: "))
c1 = int(input("Digite o número de colunas da matriz A: "))

l2 = int(input("Digite o número de linhas da matriz B: "))
c2 = int(input("Digite o número de colunas da matriz B: "))

l3 = int(input("Digite o número de linhas da matriz C: "))
c3 = int(input("Digite o número de colunas da matriz C: "))

#entrada de dados das matrizes

matA = []
matB = []
matC = []

print("\nDigite os valores da matriz A: ")

for i in range(l1):
    g = []
    for j in range(c1):
        g.append(int(input()))
    matA.append(g)

for i in range(l1):
    for j in range(c1):
         print(matA[i][j], end = " ")
    print()

print("\nDigite os valores da matriz B: ")

for i in range(l2):
    h = []
    for j in range(c2):
         h.append(int(input()))
    matB.append(h)

for i in range(l2):
    for j in range(c2):
         print(matB[i][j], end=" ")
    print()

print("\nDigite os valores da matriz C: ")

for i in range(l3):
    f = []
    for j in range(c3):
         f.append(int(input()))
    matC.append(f)

for i in range(l3):
    for j in range(c3):
         print(matC[i][j], end=" ")
    print()

#TRANSPOSTA

print('Matriz Ct: \n')

matCt = []

for l in range(l3):
    e = []
    for s in range(c3):
        e.append(int(0))
    matCt.append(e)

for i in range(l3):
    for j in range(c3):
        matCt[i][j] = matC[j][i]
        print(matCt[i][j], end ='')
    print()
print()

#OPERAÇÕES DE SOMA E SUBTRAÇÃO

matSUB = []
matSOM = []

for l in range(l3):
    d = []
    for s in range(c3):
        d.append(int(0))
    matSUB.append(d)

for l in range(l3):
    k = []
    for s in range(c3):
        k.append(int(0))
    matSOM.append(k)

print('Matriz SUB: \n')

for i in range(l3):
    for j in range(c3):
        matSUB[i][j] = matB[i][j] - matCt[i][j]
        print(matSUB[i][j], end ='')
    print()
print()

print('Matriz SOM: \n')

for i in range(l3):
    for j in range(c3):
        matSOM[i][j] = matA[i][j] + matSUB[i][j]
        print(matSOM[i][j], end ='')
    print()
print()

#MULTIPLICAÇÃO

result = []

for l in range(l3):
    u = []
    for s in range(c3):
        u.append(int(0))
    result.append(u)

print("\nA matriz resultante é: \n")

for x in range(len(matSOM)):
    for y in range(len(matB[0])):
        for z in range(len(matB)):
            result[x][y] += matSOM[x][z] * matB[z][y]

for l in result:
    print(l)