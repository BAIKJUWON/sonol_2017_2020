values = [1, 2, 3]

# 리스트의 주요 메서드를 차례대로 실행합니다.
values.append(4)
values.extend([5, 6])
values.insert(1, 10)
print(len(values))
print(values.index(10))
print(10 in values)
print(values.count(3))
values.remove(10)
del values[0]
values.sort()
print(values)
values.sort(reverse=True)
print(values)
