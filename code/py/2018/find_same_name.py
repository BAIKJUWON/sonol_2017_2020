def find_same_name(names):
    # 모든 이름 쌍을 비교해 중복 이름을 집합에 저장합니다.
    result = set()
    for i in range(0, len(names) - 1):
        for j in range(i + 1, len(names)):
            if names[i] == names[j]:
                result.add(names[i])
    return result


names = ["Tom", "Jelly", "Mike", "Tom"]
print(find_same_name(names))
