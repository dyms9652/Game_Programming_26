# 함수 - 인자값을 받아, 그에 따른 결과값을 반환한다.
# 필요할 때마다 호출이 가능하고, 코드의 중복을 최소화, 재사용성을 높인다.

# 1) 반환(return)이 없는 함수
def fire() :
    print("미사일 발사!")

fire()

def fire(n=3) :
    for i in range(n) :
        print("안녕")

print('\n')

fire()
print('\n')
fire(5)

def fire(kind, n) :
    for i in range(0, n) :
        if kind == 'machine_gun' :
            print('기관총 발사')
        elif kind == 'missile' :
            print('미사일 발사')
        elif kind == 'bomb' :
            print("폭탄 발사")
        else :
            print("무기 없음")

fire('machine_gun', 5)
fire('missile', 3)

# 2) 반환[return]이 있는 함수
def add(n1, n2) :
    return n1 + n2

r = add(100, 200)
print(r)

# 가변 인자 : 인자의 개수를 정하지 않을 때
def add(*li) :
    sum = 0
    for i in li :
        sum = sum + i

    return sum

a = add(1, 2, 3, 4, 5)
print(a)
b = add(1, 2, 3, 4, 5, 6, 7)
print(b)