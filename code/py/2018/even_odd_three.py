a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

# 세 수를 각각 짝수와 홀수로 판별합니다.
for name, value in (("a", a), ("b", b), ("c", c)):
    if value % 2 == 0:
        print(name + "짝")
    else:
        print(name + "홀")
