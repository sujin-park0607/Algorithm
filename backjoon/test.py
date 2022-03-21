def grade(num):
    if num >= 90:
        grade = "수"
    elif num >= 80:
        grade = "우"
    elif num >= 70:
        grade = "미"
    elif num >= 60:
        grade = "양"
    else:
        grade = "가"
    
    return grade

while True:

    name = input("이름: ")
    kor = int(input("국어: "))
    eng = int(input("영어: "))
    mat = int(input("수학: "))
    sci= int(input("과학: "))


    sum = kor + eng + mat + sci
    ave = sum/4
    print(ave)
    grade_num = grade(ave)


    print("\n")
    print("     ###성적표###      ")
    print("\n")
    print("성명:",name)
    print("국어:",kor,"영어:",eng,"수학:",mat,"과학:",sci)
    print("총점:",sum,"평균:",ave,"등급:",grade_num)
    print("\n")



