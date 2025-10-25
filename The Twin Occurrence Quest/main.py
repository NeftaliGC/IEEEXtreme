n, q = input().split()
n = int(n)
q = int(q)

array = input().split()
array = [int(x) for x in array]

results = []

for _ in range(q):
    x = int(input())
    try:
        first_index = array.index(x) + 1
        last_index = len(array) - 1 - array[::-1].index(x) + 1
        results.append((first_index, last_index))
    except ValueError:
        results.append((-1, -1))

for result in results:
    print(str(result[0]), str(result[1]))