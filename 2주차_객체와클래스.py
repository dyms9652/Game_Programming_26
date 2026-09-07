# 객체(object)와 클래스(class)
# 객체 : 현실 세계는 객체들로 이루어져 있다. 객체들간의 상호작용으로 사건들이 발생한다.
# 클래스 : 객체의 구성 요소를 담는 개념이다. 객체를 정의하는 설계도와 같다.

# (전투기) 클래스 정의
class Fighter(object) :
    def __init__(self, model, missile):
        self.model = model
        self.missile = missile

    def attack(self): # 메서드 정의
        print(self.model + "출격!")

    def fire(self): # 메서드 정의
        print(self.missile + "발사!")

fighter = Fighter("F-22", "공대공 미사일")    # 인스턴스 만들기
fighter.attack()
fighter.fire()