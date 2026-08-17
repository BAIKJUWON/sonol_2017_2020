class Siri:
    # 질문과 답변을 각각 리스트에 저장합니다.
    Q_list = []
    A_list = []

    def getQ_list(self):
        return self.Q_list

    def getA_list(self):
        return self.A_list


s = Siri()
questions = s.getQ_list()
answers = s.getA_list()
running = True

# 기존 질문이면 답변하고, 모르는 질문이면 새 답변을 학습합니다.
while running:
    command = input("1.입력 , 2.종료: ")
    if command == "1":
        say = input("말을 입력하세요: ")
        for index, question in enumerate(questions):
            if question == say:
                print(answers[index])
                break
        else:
            answer = input("내용을 입력하세요: ")
            questions.append(say)
            answers.append(answer)
    elif command == "2":
        running = False
