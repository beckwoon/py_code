### <TIME> ###

import time

print(time.time())
print("==========")

print(time.localtime(time.time())) #튜플형태
print("==========")

print(time.asctime(time.localtime(time.time())))
print("==========")

print(time.ctime())
print("==========")

# time.strftime('출력할 형식 포멧 코드', (time.localtime(time.time()))
print(time.strftime('%x', time.localtime(time.time()))) #날짜
print(time.strftime('%X', time.localtime(time.time()))) #시간
print("==========")
print(time.strftime('%c', time.localtime(time.time()))) #날짜 시간
print("==========")
print(time.strftime('%a', time.localtime(time.time()))) #요일
print(time.strftime('%A', time.localtime(time.time())))
print(time.strftime('%b', time.localtime(time.time()))) #달
print(time.strftime('%B', time.localtime(time.time())))
print("==========")
print(time.strftime('%Y 년 %y Y %m %d', time.localtime(time.time()))) #year, month, dya
print("==========")
print(time.strftime('%H', time.localtime(time.time()))) #24시간
print(time.strftime('%I', time.localtime(time.time()))) #12시간(대문자 i)
print(time.strftime('%p', time.localtime(time.time()))) #AM PM
print(time.strftime('%M', time.localtime(time.time()))) #분
print(time.strftime('%S', time.localtime(time.time()))) #초
print("==========")
print(time.strftime('%Z', time.localtime(time.time()))) #기준시간대

# time.sleep
for i in range(5):
    print(i+1)
    time.sleep(0.5)

print("==========")
print("==========")
print("==========")


### <Calender> ###
import calendar

print(calendar.calendar(2019))
time.sleep(1)
print(calendar.prcal(2020))
time.sleep(1)
print("==========")

print(calendar.prmonth(2020,3))
print("==========")

# calendar.weekday
print(calendar.weekday(2020,3,1)) #일요일 = 6
print(calendar.weekday(2020,3,2)) #월요일 = 0
print(calendar.weekday(2020,3,7)) #토요일 = 5
print("==========")
# calendar.monthrange
print(calendar.monthrange(2020,2)) #2020년 2월 시작요일(토요일)과 끝(29일)
print("==========")

day = ['월', '화', '수', '목', '금', '토', '일']
year = int(input('년 입력>>'))
month = int(input('월 입력>>'))
s = calendar.monthrange(year, month)
print("%s년 %s월의 시작은 %s요일이고, %s일까지 있습니다."%(year, month, day[s[0]], s[1]))



