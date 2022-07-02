def solution(record):
    answer = []
    names = dict() #[id, nickname]

    for i in range(len(record)):
        comment = record[i].split()
                
        if comment[0] == "Enter":
            names[comment[1]] = comment[2]
                
        elif comment[0] == "Change":
            names[comment[1]] = comment[2]

            
    for i in range(len(record)):
        comment = record[i].split()
        
        if comment[0] == "Enter":
            answer.append(names[comment[1]]+"님이 들어왔습니다.")
        
        elif comment[0] == "Leave":
            answer.append(names[comment[1]]+"님이 나갔습니다.")
        
    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])