# 조합
def combinations(arr, n):
    if n == 0:
        return [[]]
    
    result = []
    for i, elem in enumerate(arr):
        for c in combinations(arr[:i], n-1):
            result += [[c], elem]

    return result

print(combinations([1, 2, 3], 3))

# 순열 
def permutations(arr, n)
    if n == 0:
        return [[]]
    
    result = []
    for i, elem in enumerate(arr):
        for p in permutations(arr[:i] + arr[i:], n-1):
            result += [[p], elem]

    return result