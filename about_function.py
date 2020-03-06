################## 내장함수
print("")
print("")
print(" -3의 절대값 : ", abs(-3))
print("====")
print("모두가 참인가? [1,2,3] : ", all([1,2,3]))
print("모두가 참인가? [1,2,3,0] : ", all([1,2,3,0]))
print("====")
print("any 참이 있는가? [1,2,3,0] : ", all([1,2,3,0]))
print("any 참이 있는가? [0,""] : ", all([0,""]))
print("====")
print("a와 b를 나눈 값과 나머지를 튜플로 (a=7, b=2) : ", divmod(7,2))
print("====")
print("")
print("")
# filter와 lamdba 활용
a = list(filter(lambda x:x>0, [1,-3,2,0,-5,6]))
print(a)

print("====")
print("")
print("")
print("python의 문자길이는?? ", len("python"))
print("====")
print("python의 각 문자를 리스트로 : ", list("python"))
print("====")

print(max([1,2,3]))
print(min([1,2,3]))
print(sum([1,2,3]))
print(pow(2,4))  # 2의 4 제곱

# open 함수 = opne(filename, [mode])
# w(쓰기), r(읽기), a(추가), b(바이너리 모드)

# round(number,[ndigits])

print("====================")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")



################## 외장함수 (파이썬 라이브러리)

# sys - 파이선이 제공하는 변수와 함수를 직접 제어
import sys
print(sys)
print("====")

# sys.argv
print(sys.argv)
print("====")

# sys.path
print(sys.path)
print("====")
print("")
print("")

# os - OS 자원을 제어
import os
print(os)
print("====")

# os.environ (현재 시스템의 환경변수 값 - 시스템 정보, 딕셔너리로 보여줌)
print(os.environ)
print("====")
print(os.environ['path'])
print("====")
print("")
print("")

# os.chdir - 디렉토리 위치 변경
# os.chdir("C:\WINDOWS")
# os.getcwd - 디렉토리 위치 확인
# os.getcwd()

# os.system - 시스템 명령어 실행
# os.system("dir")

# os.popen - 시스템 명령의 결과 받기
f = os.popen("dir")
print(f)
print(f.read()) # object값 읽는 방법

print("====")
print("")
print("")

# os.mkdir(디렉토리) - 디렉토리 생성
# os.rmdir(디렉토리) - 디렉토리 삭제 (데이터가 비워 있어야 삭제 가능)
# os.unlink(파일이름) - 파일 지우기
# os.rename(src, dst) - 파일이름 변경 (src를 dat로 변경)



# shutil - 파일을 복사해주는 파이썬 모듈
# import shutil
# shutil.copy("src.txt", "dst.txt")



# glob(pathname) - 특정 디렉토리에 있는 파일이름을 불러오기(메타문자 활용)
# import glob
# glob.glob("c:/dpot/mark*")
# => ['c:/dpot/marks1.py', 'c:/dpot/marks2.py', ...]



# tempfile - 파일을 임시로 만들어 사용
import tempfile
filename = tempfile.mktemp()
print(filename)
print("====")
print("")
f = tempfile.TemporaryFile()
print(f)
print(f.read())
print("====")
f.close()

print("====")
print("")
print("")
print("")
print("")

# random
import random
print(random.random())
print(random.randint(1,10))
print(random.randint(1,100))
print("====")

def random_pop(data):
    number = random.randint(0, len(data)-1) #randint
    return data.pop(number)

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data : print(random_pop(data))
    
print("====")

def random_pop2(data):
    number = random.choice(data) #choice
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data : print(random_pop2(data))

print("====")

data = [1,2,3,4,5]
random.shuffle(data)  #shuffle
print(data)


#webbrowser
import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com")


