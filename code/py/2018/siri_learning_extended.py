class Siri:
    Q_list = ["안녕", "뭐해", "잘가", "ㅂㅇㄹ"]
    A_list = ["안녕하세요", "놀고있었어요", "안녕히가세요", "보겸은 도덕책"]

    def getQ_list(self):
        return self.Q_list

    def getA_list(self):
        return self.A_list


s = Siri()
questions = s.getQ_list()
answers = s.getA_list()
running = True

# 질문을 찾지 못하면 새 답변을 입력받아 리스트에 추가합니다.
while running:
    command = input("1.컴퓨터랑 대화하기 , 2.종료: ")
    if command == "1":
        say = input("내용을 입력하세요: ")
        for index, question in enumerate(questions):
            if question == say:
                print(answers[index])
                break
        else:
            answer = input("원하는 답변을 입력하세요: ")
            questions.append(say)
            answers.append(answer)
    elif command == "2":
        running = False
