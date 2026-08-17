# 숫자 자료형
integer_value = 10
float_value = 10.2
complex_value = 2j
bool_value = True
print(type(integer_value), type(float_value), type(complex_value), type(bool_value))

# 문자열
text = "Hello"
print(text.count("l"))
print(text.startswith("He"))
print(text.endswith("lo"))
print(text.upper())
print(text.lower())
print("-".join(text))

# 리스트와 튜플
items = list("12345")
items.append("6")
items.sort(reverse=True)
print(items)
values = (1, 2, 3, 3)
print(values.count(3))

# 딕셔너리와 집합
data = {1: "a", 2: "b", 3: "c"}
print(data.get(2))
left = {1, 2, 3, 4, 5}
right = {4, 5, 6, 7}
print(left | right)
print(left & right)
