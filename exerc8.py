matrizA = [[0,0],[0,0]]
matrizB = [[0,0],[0,0]]
matrizC = [[0,0],[0,0]]
op = [[0,0],[0,0]]

for l in range(0,2):
    for c in range(0,2):
        matrizA[l][c] = int(input(f'Matriz A - Digite um valor para o elemento [{l},{c}]:'))
print('-='*30)

print('Matriz A: \n')

for l in range(0,2):
    for c in range(0,2):
        print(f'[{matrizA[l][c]}]', end ='')
    print()
print()

for l in range(0,2):
    for c in range(0,2):
        matrizB[l][c] = int(input(f'Matriz B - Digite um valor para o elemento [{l},{c}]:'))
print('-='*30)

print('Matriz B: \n')
for l in range(0,2):
    for c in range(0,2):
        print(f'[{matrizB[l][c]}]', end ='')
    print()
print()

for l in range(0,2):
    for c in range(0,2):
        matrizC[l][c] = int(input(f'Matriz C - Digite um valor para o elemento [{l},{c}]:'))
print('-='*30)

print('Matriz C: \n')
for l in range(0,2):
    for c in range(0,2):
        print(f'[{matrizC[l][c]}]', end ='')
    print()
print()

print('-='*30)

print('Faça a seguinte operação: A + B - 4C \n')

print('Resultado: \n')

op[l][c] = (matrizA[l][c]) + (matrizB[l][c]) - (4*(matrizC[l][c]))

for l in range(0,2):
    for c in range(0,2):
        print(f'[{op[l][c]}]', end ='')
    print()
print()