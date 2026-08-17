# 1부터 10까지의 합
result = 0
for number in range(1, 11):
    result += number
print(result)

# 1부터 49까지 홀수의 합
result = 0
for number in range(1, 50, 2):
    result += number
print(result)

# 1/2 + 2/3 + ... + 9/10
result = 0
for number in range(1, 10):
    result += number / (number + 1)
print(result)
