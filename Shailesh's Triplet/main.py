n = int(input())
ns = []
for _ in range(n):
    ns.append(int(input()))

triplets = {}

for n in ns:
    if n % 2 == 1 or n & (n - 1) == 0:
        triplets[n] = -1
        continue

    x = n & -n
    a = n + x
    b = n - x
    c = x
    triplets[n] = (a, b, c)

for triplet in triplets.values():
    if triplet == -1:
        print(-1)
    else:
        print(triplet[0], triplet[1], triplet[2])