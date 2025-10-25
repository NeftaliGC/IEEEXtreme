n = int(input())
ns = []
for _ in range(n):
    ns.append(int(input()))

triplets = {}

for n in ns:
    if n % 2 != 0 or n & (n - 1) == 0:
        triplets[n] = -1
        continue

    x = n // 2
    _and = n & x

    if _and == 0:
        max_bit = 1 << (x.bit_length() - 1)
        a = max_bit
        b = x ^ max_bit
        c = n ^ x
    else:
        a = x
        b = _and
        c = (n ^ x) + _and
    triplets[n] = (a, b, c)

for triplet in triplets.values():
    if triplet == -1:
        print(-1)
    else:
        print(triplet[0], triplet[1], triplet[2])