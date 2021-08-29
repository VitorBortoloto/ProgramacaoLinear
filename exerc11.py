#FAÇA A AOPERAÇÃO (B+At)*(C^-1)-(3*Bt)

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
         print(matA[i][j], end = "\t")
    print()

print("\nDigite os valores da matriz B: ")

for i in range(l2):
    h = []
    for j in range(c2):
         h.append(int(input()))
    matB.append(h)

for i in range(l2):
    for j in range(c2):
         print(matB[i][j], end="\t")
    print()

print("\nDigite os valores da matriz C: ")

for i in range(l3):
    f = []
    for j in range(c3):
         f.append(int(input()))
    matC.append(f)

for i in range(l3):
    for j in range(c3):
         print(matC[i][j], end="\t")
    print()

#TRANSPOSTAS

print('Matriz At: \n')

matAt = []

for l in range(l3):
    e = []
    for s in range(c3):
        e.append(int(0))
    matAt.append(e)

for i in range(l3):
    for j in range(c3):
        matAt[i][j] = matA[j][i]
        print(matAt[i][j], end ='\t')
    print()
print()

print('Matriz Bt: \n')

matBt = []

for l in range(l3):
    m = []
    for s in range(c3):
        m.append(int(0))
    matBt.append(m)

for i in range(l3):
    for j in range(c3):
        matBt[i][j] = matB[j][i]
        print(matBt[i][j], end ='\t')
    print()
print()

#OPERAÇÃO DE SOMA

matSOM = []

for l in range(l3):
    k = []
    for s in range(c3):
        k.append(int(0))
    matSOM.append(k)

print('Matriz SOM: \n')

for i in range(l3):
    for j in range(c3):
        matSOM[i][j] = matB[i][j] + matAt[i][j]
        print(matSOM[i][j], end ='\t')
    print()
print()

#MULTIPLICAÇÃO 1

matM1 = []

for l in range(l3):
    u = []
    for s in range(c3):
        u.append(int(0))
    matM1.append(u)

print("\nA matriz M1 é: \n")

for i in range(len(matBt)):
    for j in range(len(matBt)):
         matM1[i][j] = 3 * matBt[i][j]
         print(matM1[i][j], end ='\t')
    print()

#INVERSA

a = int(matC[0][0])
b = int(matC[0][1])
c = int(matC[1][0])
d = int(matC[1][1])

z = ((-c)/(1+(c*b/a)))
w = (a/(a*d - b))
x = (((1-(b*z))/a))
y = ((-b*w)/a)

print()

matCi = [[x,y],[z,w]]

print('\nA Matriz Inversa é: ')

for i in range(l3):
    for j in range(c3):
        print(matCi[i][j], end ='\t\t')
    print()
print()

#MULTIPLICAÇÃO 2

matM2 = []

for l in range(l3):
    v = []
    for s in range(c3):
        v.append(int(0))
    matM2.append(v)

print("\nA matriz M2 é: \n")

for x in range(len(matSOM)):
    for y in range(len(matCi[0])):
        for z in range(len(matCi)):
            matM2[x][y] += matSOM[x][z] * matCi[z][y]

for l in matM2:
    print(l)

print()

#SUBTRAÇÃO

matSUB = []

for l in range(l3):
    n = []
    for s in range(c3):
        n.append(int(0))
    matSUB.append(n)

print('Matriz Resultado final: \n')

for i in range(l3):
    for j in range(c3):
        matSUB[i][j] = matM1[i][j] - matM2[i][j]
        print(matSUB[i][j], end ='\t\t')
    print()
print()