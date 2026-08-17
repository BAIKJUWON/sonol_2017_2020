values = [100, 92, 98, 18, 78]
max_value = 0
min_value = 9999

# 리스트를 한 번 순회하며 최댓값과 최솟값을 찾습니다.
for value in values:
    if max_value < value:
        max_value = value
    if min_value > value:
        min_value = value

print(max_value)
print(min_value)
