#greedy algorithm 탐욕알고리즘
#최적의 해에 가까운 값을 구하기 위해 사용됨
#여러 경우 중 하나를 결정해야할 때마다, 매순간 최적이라고 생각되는 
# 경우를 선택하는 방식으로 진행해서, 최종적인 값을 구하는 방식 




coin_list = [500,100,50,1]
#동전문제
def min_coin_count(value,coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        value -= coin_num * coin
        details.append([coin,coin_num])

    return total_coin_count, details

data_list = [(10,10),(15,12),(20,10),(25,8),(30,5)]


def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key = lambda x:x[1]/ x[0], reverse=True)
    total_value = 0
    details = list()

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append(data[0],data[1],1)
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0],data[1],fraction])
            break
    return total_value,details

get_max_value(data_list,capacity=30)


