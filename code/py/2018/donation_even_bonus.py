a = int(input("a: "))
b = int(input("b: "))

# 짝수 입력값은 10배로 만든 뒤 두 값을 더합니다.
if a % 2 == 0:
    a *= 10
if b % 2 == 0:
    b *= 10

print(a + b)
