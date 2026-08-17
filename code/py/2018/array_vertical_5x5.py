# 세로 방향 규칙을 가진 5x5 숫자 배열을 출력합니다.
for i in range(5, 0, -1):
    for j in range(5):
        print(5 * i - j, end=" ")
    print()
