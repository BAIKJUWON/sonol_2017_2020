number = int(input("숫자를 입력하세요: "))

# 1부터 입력값까지 나누어 떨어지는 수를 출력합니다.
for i in range(1, number + 1):
    if number % i == 0:
        print(i)
