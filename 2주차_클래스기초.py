# p.319
# 클래스 정의
class Car :
    color = ""
    speed = 0

    def upSpeed(self, value) :
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

# 인스턴스 만들기
myCar = Car()
print(myCar.speed)

myCar.upSpeed(30)
print(myCar.speed)

myCar.upSpeed(40)
print(myCar.speed)

myCar.color = "red"
print(myCar.color)

myCar.downSpeed(15)
print(myCar.speed)

# p.323 기본 생성자
class Car :
    color = ""
    speed = 0

    def __init__(self) :
        self.color = "빨강"
        self.speed = 0

