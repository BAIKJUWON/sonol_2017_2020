values = []

# 숫자 10개를 입력받아 리스트에 저장합니다.
for i in range(10):
    values.append(int(input("입력: ")))

# 뒤 인덱스부터 앞으로 이동하며 역순 출력합니다.
for i in range(9, -1, -1):
    print(values[i])
