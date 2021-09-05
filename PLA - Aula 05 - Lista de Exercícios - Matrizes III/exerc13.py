l3 = int(input("Digite o número de linhas da matriz A: "))
c3 = int(input("Digite o número de colunas da matriz A: "))

matA = []

print("\nDigite os valores da matriz A: ")

for r in range(l3):
    f = []
    for s in range(c3):
         f.append(int(input()))
    matA.append(f)

for i in range(l3):
    for j in range(c3):
         print(matA[i][j], end=" ")
    print()

a = int(matA[0][0])
b = int(matA[0][1])
c = int(matA[1][0])
d = int(matA[1][1])

z = ((-c)/(1+(c*b/a)))
w = (a/(a*d - b))
x = (((1-(b*z))/a))
y = ((-b*w)/a)

print()

matAi = [[x,y],[z,w]]

print('\nA Matriz Inversa é: ')

for i in range(l3):
    for j in range(c3):
        print(matAi[i][j], end ='\t\t')
    print()
print()

print('\nA*1/9:\n ')

matB = [[0,0],[0,0]]

for i in range(l3):
    for j in range(c3):
         matB[i][j] = 1/9*(matA[i][j])
         print(matB[i][j], end ='\t')
    print()

for i in range(l3):
    for j in range(c3):
        if matB[i][j] == matAi[i][j]:
            pass
        else:
            break
print()
print('A matriz A inversa não é igual a 1/9*A')