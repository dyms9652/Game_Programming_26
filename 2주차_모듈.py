# 모듈(module)
# 모듈이란 : 함수, 변수, 클래스 등의 집합으로 내장된 표준 모듈도 있고, 외부모듈도 가져올 수 있다.

# 시간 모듈(Time Module)
import time

# 1970년 1월 1일 ~ 경과된 초 시간
print(time.time())

# 현재 지역의 시간대의 날짜와 시간 형태를 변환하기
now = time.localtime(time.time())
print(now)

year = str(now.tm_year)
month = str(now.tm_mon)
day = str(now.tm_mday)
print(year + "년 " + month + "월 " + day + "일")

hour = str(now.tm_hour)
minute = str(now.tm_min)
sec = str(now.tm_sec)
print(hour + "시 " + minute + "분 " + sec + "초" )

# 랜덤 모듈
import random
print(random.random())   # 0~1 미만의 실수값
print(random.randint(1, 10))    # 정수 랜덤
print(random.randrange(0, 10, 2))   # 0~10 사이의 2간격 수 중에서 선택하기

# 리스트
li = [10, 20, 30, 40, 50]
print(li)

print(random.choice(li))
print(random.sample(li, 2))

random.shuffle(li)      # 내부 값들을 랜덤으로 셔플함.
print(li)



