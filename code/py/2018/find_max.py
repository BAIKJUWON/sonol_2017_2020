def find_max(values):
    # 첫 번째 값을 최댓값으로 두고 나머지 값과 비교합니다.
    max_value = values[0]
    for i in range(1, len(values)):
        if values[i] > max_value:
            max_value = values[i]
    return max_value


values = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(values))
