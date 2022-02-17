test_case = int(input())

count = []
for i in range(test_case):
    friends = []
    network = int(input())
    for i in range(network):
        input_friend = input().split()
        friends += input_friend
        count.append(len(set(friends)))


for i in count: print(i)


