#Entrada estandar
n = int(input()) #caso de pruebas
for _ in range(n):
    t = input().split() #a, b, p, x1, y1, x2, y2
    t = [int(x) for x in t]

    #calculo de pendiente 
    #P = (x1, y1)
    #Q = (x2, y2)
    P = (t[3], t[4])
    Q = (t[5], t[6])

    # Caso especial: si P == Q pero y = 0 (punto en su inverso)
    if P[0] == Q[0] and (P[1] + Q[1]) % t[2] == 0:
        print("POINT_AT_INFINITY")
        continue

    if P != Q:
        lamb = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, t[2]) % t[2]
    else:
        lamb = (3 * P[0] ** 2 + t[0]) * pow(2 * P[1], -1, t[2]) % t[2]

    #calculo de R = P + Q
    x3 = (lamb ** 2 - P[0] - Q[0]) % t[2]
    y3 = (lamb * (P[0] - x3) - P[1]) % t[2]

    #Salida estandar
    print(f"{x3} {y3}")