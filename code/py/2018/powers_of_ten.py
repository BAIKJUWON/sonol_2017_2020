# 10의 거듭제곱을 출력합니다.
for i in range(7):
    print(pow(10, i))

print()

# 1, 11, 111, ... 형태의 누적값을 출력합니다.
total = 0
for i in range(7):
    total += pow(10, i)
    print(total)
