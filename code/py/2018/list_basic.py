# 리스트 합치기
first = [1, 2, 3]
second = [3, 4, 5]
print(first + second)

# 리스트 반복
numbers = [1, 2, 3]
print(numbers * 3)

# 요소 추가와 삽입
numbers.append(15)
numbers.insert(2, 20)
print(numbers)

# 값과 위치를 이용한 삭제
if 15 in numbers:
    numbers.remove(15)
del numbers[0]
print(numbers)
