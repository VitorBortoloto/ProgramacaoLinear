matrizA = [[0,0,0],[0,0,0],[0,0,0]]
matrizAt = [[0,0,0],[0,0,0],[0,0,0]]
matrizB = [[0,0,0],[0,0,0],[0,0,0]]

def somarMatriz(matrizA, matrizAt):
    soma = 0
    for l in range(len(matrizA)):
        for c in range(len(matrizAt)):
            soma += matrizA[l][c] + matrizAt[l][c]
    return soma

for l in range(0,3):
    for c in range(0,3):
        matrizA[l][c] = int(input(f'Matriz A - Digite um valor para o elemento [{l},{c}]:'))
print('-='*30)

print('Matriz A: \n')

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matrizA[l][c]}]', end ='')
    print()
print()
print('-='*30)

print('Matriz At: \n')

for l in range(0,3):
    for c in range(0,3):
        matrizAt[l][c] = matrizA[c][l]
        print(f'[{matrizAt[l][c]}]', end ='')
    print()
print()
print('-='*30)

print('Faça a seguinte operação: B = A + At \n')

print('Resultado:')

matrizB[l][c] = somarMatriz(matrizA,matrizAt)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matrizB[l][c]}]', end ='')
    print()
print()