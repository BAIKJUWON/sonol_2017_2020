name = input("이름을 입력하세요: ")
school = input("학교를 입력하세요: ")
age = int(input("나이를 입력하세요: "))

# format 함수를 사용해 입력값을 한 문장으로 출력합니다.
print("나이가 {0}살이고 이름은 {1}이다 학교는 {2} 다닌다.".format(age, name, school))
