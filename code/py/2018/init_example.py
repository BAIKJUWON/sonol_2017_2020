class Ex:
    # 객체를 만들 때 두 값을 받아 저장합니다.
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("저는 " + str(b) + "입니다.")

    def disp(self, value):
        print(value)

    def disp2(self):
        return 20


example = Ex("안녕하세요", "카인")
example.disp(example.a)
print(example.disp2())
