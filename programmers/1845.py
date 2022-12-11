def solution(nums):
    pokemon = dict()
    max = len(nums)/2
    print(pokemon)
    for idx in nums:
        pokemon[idx] = 1
        
    print(len(pokemon))
    if max > len(pokemon):
        answer = len(pokemon)
    else:
        answer = max
    return answer

solution([3,1,2,3])