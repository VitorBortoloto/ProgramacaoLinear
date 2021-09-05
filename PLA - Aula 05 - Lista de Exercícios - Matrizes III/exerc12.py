def matriz_inversa (l1, c1, matA):

    if l1 == c1:

        a = int(matA[0][0])
        b = int(matA[0][1])
        c = int(matA[0][2])
        d = int(matA[1][0])
        e = int(matA[1][1])
        f = int(matA[1][2])
        g = int(matA[2][0])
        h = int(matA[2][1])
        k = int(matA[2][2])

        if True:

            try:

                r = (((k*a*d) - (g*a*f))/((-g*b*a*f)+(g*c*a*e)+((a**2)*h*f)-(a*h*d*c)+(k*a*d*b)-(k*(a**2)*e)))
                u = (((d*b*r) - (a*e*r) - d)/((a*f) - (d*c)))
                x = ((1 - (b*r) - (c*u))/a)

                s = (((d*c*g) - (d*k*a))/((-a*e*d*k)+(a*f*d*h)+((d**2)*b*k)-(d*b*g*f)+(d*c*g*e)-(h*(d**2)*c)))
                v = (((g*e*s) - (d*h*s) - g)/((d*k) - (g*f)))
                y = ((1 - (e*s) - (f*v))/d)

                t = (((g*f*a) - (d*g*c))/((-d*h*g*c)+(d*k*g*b)+((g**2)*e*c)-(g*e*a*k)+(g*f*a*h)-(f*(g**2)*b)))
                w = (((a*h*t) - (g*b*t) - a)/((g*c) - (a*k)))
                z = ((1 - (h*t) - (k*w))/g)

                matAi = [[x,y,z], [r,s,t], [u,v,w]]

                print('\nA Matriz Inversa é: ')

                for i in range(l1):
                    for j in range(c1):
                        print(matAi[i][j], end='\t\t')
                    print()

            except ZeroDivisionError:
                print('A Matriz não tem inversa!')
    print()

    if l1 != c1:
        return print('A matriz não tem inversa!')

print(matriz_inversa(3, 3, [[0, 1, 0], [1, 0, 0], [0, 0, 1]]))
print(matriz_inversa(3, 3, [[1, 1, 1], [0, 2, 3], [5, 5, 1]]))
print(matriz_inversa(3, 3, [[1, -2, -3], [0, -4, 4], [0, 0, 0]]))

print(matriz_inversa(3, 3, [[2, 0, 1], [1, 2, 1], [3, 2, 1]]))