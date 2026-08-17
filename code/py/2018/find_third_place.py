scores = []
count = int(input("사람 수(3~10): "))

# 점수를 입력받아 내림차순 정렬 후 3등 점수를 찾습니다.
for i in range(count):
    scores.append(int(input("성적: ")))

scores.sort(reverse=True)
third = scores[2]
print("3등 점수는", third)

# 3등 점수가 전체 평균보다 높은지 확인합니다.
if third > sum(scores) / count:
    print("평균 이상")
else:
    print("평균 이하")
