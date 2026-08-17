count = 0
limit = int(input("숫자를 입력하세요: "))

# 10부터 입력값까지 일의 자리가 1인 수의 개수를 셉니다.
for number in range(10, limit + 1):
    if number % 10 == 1:
        count += 1

print(count)
