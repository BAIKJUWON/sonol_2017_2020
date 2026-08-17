class Siri:
    # 입력된 문장에 따라 미리 정한 답변을 출력합니다.
    def speaking(self, speak):
        if speak == "뭐해":
            print("그냥집에서 놀고있어요")
        elif speak == "랩해봐":
            print("너와나의 연결고리")
        elif speak == "뭐먹고싶어?":
            print("채소 많이 먹으라는 모든어머님말씀이 진리인것 같습니다.")


s = Siri()
running = True

# 1을 입력하면 대화하고 2를 입력하면 종료합니다.
while running:
    command = input("1.입력 , 2.종료: ")
    if command == "1":
        say = input("말을 입력하세요: ")
        s.speaking(say)
    elif command == "2":
        running = False
