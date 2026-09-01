# 제어문 : 조건문, 반복문
# 1) 조건문(if문) - 특정 조건에 따라 코드가 수행되도록 한다.

fire = True
if fire :
    print("미사일 발사!")

fire = False
if fire :
    print("미사일 발사!")



key = 'LEFT'

if key == 'LEFT' :
    print("왼쪽으로 이동")

elif key == 'RIGHT' :
    print("오른쪽으로 이동")

else :
    print("정지")

# 반복문 - for문, while문
for i in range(0, 5) :      # 범위가 (0, 3)이면, (0부터 2까지의 수이다)
    print(i)
    print("적 등장!")
    print('\n')

# 리스트 만들기
enemy = ['적1', '적2', '적3']

for e in enemy :
    print(e)
    print('\n')

# while 문
i = 0
while i < 3 :
    print("미사일 발사!")
    i = i + 1










