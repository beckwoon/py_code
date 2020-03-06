print("====")

try:
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

print("==Index에러==")

try:
    4/0
    a=[1,2]
    print(a[3])
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

print("==0 나누기 에러==")

try:
    4/0
    a=[1,2]
    print(a[3])
except (ZeroDivisionError,IndexError) as e:
    print(e)

print("==동시 작업==")

try:
    a=[1,2]
    print(a[3])
    4/0
except (ZeroDivisionError,IndexError) as e:
    print(e)

print("====")

try:
    f = open("없는파일",'r')
except FileNotFoundError:
    pass

print("==pass==")

# 오류 발생시키기 -> raise


class Bird:
    def fly(self):
        print("테스트 ㅋㅋ")
        raise NotImplementedError
class Eagle(Bird):  # Eagle클라스는 Bird 클라스를 상속받음
    pass

eagle = Eagle()
eagle.fly()
