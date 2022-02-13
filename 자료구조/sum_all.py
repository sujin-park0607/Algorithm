#시간복잡도 


def sum_all(n):
    total = 0
    for num in range(1,n +1):
        total += num
    return total
#시간복잡도 n 
#O(n)

def sum_all(n):
    return int(n * (n + 1)/2)
#시간복잡도 1 
# O(1)

print(sum_all(100))
print(sum_all(100))