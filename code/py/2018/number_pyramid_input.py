height = int(input("숫자를 입력하세요: "))

# 입력받은 높이만큼 숫자 피라미드를 만듭니다.
for i in range(1, height + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
