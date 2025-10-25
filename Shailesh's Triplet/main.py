def construct_with_c(n, c):
    S = 2 * n - c
    X = n ^ c
    if S <= 0 or S < X: 
        return None
    if (S - X) % 2 != 0:
        return None
    half = (S - X) // 2
    if (half & X) != 0:
        return None
    a = half
    b = half ^ X
    # necesidades: positivos y distintos entre sí y distintos de c
    if a <= 0 or b <= 0 or a == b or a == c or b == c:
        return None
    return (a, b, c)

def find_triplet(n):
    # casos imposibles: n impar o potencia de dos
    if n % 2 == 1 or (n & (n - 1)) == 0:
        return None

    bl = n.bit_length()
    candidates = set()

    # 1) números "todos unos" cercanos: (1<<t)-1, (1<<t)-1 - d (d pequeño)
    for t in range(1, bl + 3):
        base = (1 << t) - 1
        # probamos base, base-1, base-2, ... hasta algunos decrementos
        for d in range(0, min(1 << 6, base + 1)):  # d hasta 63
            c = base - d
            if 0 < c < 2 * n:
                candidates.add(c)

    # 2) pequeños c (siempre útiles)
    for c in range(1, min(1000, 2 * n)):
        candidates.add(c)

    # 3) potencias de dos multiplicadas por pequeños coeficientes
    for t in range(0, bl + 3):
        for m in range(1, 6):
            c = (1 << t) * m
            if 0 < c < 2 * n:
                candidates.add(c)

    # probar candidatos ordenados (más pequeños primero)
    for c in sorted(candidates):
        res = construct_with_c(n, c)
        if res:
            return res

    # fallback (raro): intento exhaustivo (no recomendado para n muy grande)
    # for c in range(1, 2*n):
    #     res = construct_with_c(n, c)
    #     if res:
    #         return res

    return None

# entrada/uso tal como tu programa
t = int(input().strip())
ns = [int(input().strip()) for _ in range(t)]

for n in ns:
    trip = find_triplet(n)
    if trip is None:
        print(-1)
    else:
        print(trip[0], trip[1], trip[2])
