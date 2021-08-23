matriz = []

def gerar_matriz (i, j):

    for i in range(1,i+1):
        for j in range(1,j+1):
            if i==j:
                matriz.append([i+j])
            else:
                matriz.append([(2*i)-(2*j)])

    return matriz

def soma_elementos (a,b):

    soma = matriz[a] + matriz[b]
    soma_final = sum(soma)
    return soma_final

print('A Matriz 3x4 é: ', gerar_matriz(3,4))

print ('A soma do a22 e a34 é: ', soma_elementos(3,11))

