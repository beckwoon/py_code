# import <모듈이름>
# from <모듈이름> import <함수>

# module.py

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

if __name__ == "__main__":
    print(add(1,4))
    print(sub(4,2))
    

# __name__ == "__main__" 은 직접 모듈을 실행할 경우 True, 모듈을 import할 경우 False
# 모듈을 import할 경우, __name__ 변수에는 모듈의 이름값이 저장된다.





PI = 3.141592

class Math:
    def sov(self,r):
        return PI*(r**2)



