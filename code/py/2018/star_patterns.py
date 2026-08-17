# 별 개수가 1개씩 증가합니다.
for i in range(1, 6):
    print("*" * i)

print()

# 별 개수가 1개씩 감소합니다.
for i in range(5, 0, -1):
    print("*" * i)

print()

# 가운데 정렬된 홀수 개수 별을 출력합니다.
for i in range(1, 5):
    print(" " * (4 - i) + "*" * (i * 2 - 1))
