##### <정규 표현식 Regular Expressions> #####
### 1. 살펴보기

# 정규식 미사용 (주민등록번호 마스킹 처리)
data = '''
park 800905-1049118
kim 700905-2059119
'''

result = []
for line in data.split("\n"):
    #print(line)
    word_result = []
    
    for word in line.split(" "): #공백으로 나누기
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:8]+"******"
        word_result.append(word)
        #print(word_result)
    result.append(" ".join(word_result))
print("\n".join(result))


# 정규식 사용
import re   #정규식 모듈 (regular expression)

data = '''
park 800905-1049118
kim 700905-2059119
'''

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))


### 2. 시작하기

# 메타문자(meta characters) = . ^ $ * + ? { } [ ] \ | ( )

# 문자 클라스(character class) []

# [abd] -> "a" match Yes, "before" match Yes, "dude" match No
# [a-c] = [abc]
# [0-5] = [012345]
# [a-zA-Z] = 알파벳 모두
# [0-9] = 모든 숫자

# ^ : 반대(not) 의미 ==>    [^0-9] = 숫자가 아닌 문자

# \d : 숫자와 매치 [0-9]와 동일
# \D : 숫자가 아닌 것과 매치 [^0-9]와 동일

# \s : whitespace 문자와 매치 [ \t\n\t\f\v]와 동일
# \S : whitespace 문자가 아닌 것과 매치 [^ \t\n\t\f\v]와 동일

# \w : 문자+숫자와 매치 [a-zA-Z0-9]와 동일
# \W : 문자+숫자가 아닌 것과 매치 [^a-zA-Z0-9]와 동일


# Dot(.) : 즐바꿈 문자인 \n을 제외한 모든 문자와 매치
# a.b -> a와 b 사이에 어떤 문자가 들어와도 매치 "a + 모든문자 + b"
# a[.]b -> a와 b 사이에 Dot(.) 문자가 있으면 매치 "a + Dot(.)문자 + b"

# 반복(*) : *바로 앞에 있는 문자가 0부터 무한대로 반복가능
# ca*t -> a가 0부터 무한대로 반복 "ct -> a가 0이 되어도 매칭"

# 반복(+) : +바로 앞에 있는 문자가 최소 1번 이상 반복
# ca+t -> a가 최소 1회 이상 반복   "c + a(1번이상 반복) + t"

# 반복({m,n},?) : 반복횟수가 m부터 n까지 매칭
# ca{2}t : a가 반드시 2번 반복    "c + a(2번 반복) + t" = " caat"
# ca{2, }t : a가 반드시 2번 이상 반복    "c + a(2번 이상 반복) + t"
# ca{2,5} : a가 2~5번 반복    "c + a(2번~5번 반복) + t"
# ca?t : a가 0~1번 반복     "c + a(있어도 되고 없어도 된다) + c"


import re

print("==== 정규식 사용하기 ====")

p = re.compile('[a-z]+')    # 정규식을 컴파일

m = p.match("python") # 컴파일과 매칭이 되는 것을 확인
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())
print("====")

m = p.match("123 python")
print(m)
print("====")
print("====")
print("====")

m = p.search("python") # 컴파일과 매칭이 되는 것을 찾아내기
print(m)
print("====")

m = p.search("123 python")
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())
print("====")
print("====")
print("====")

m = p.findall("life is too short") # 컴파일과 매칭해서 리스트로 돌려주기
print(m)
print("====")
print("====")
print("====")

m = p.finditer("life is too short") # 컴파일과 매칭해서 iterator object로 돌려주기
print(m)
print("====")

for r in m : print(r)

print("====\n\n\n\n\n\n")

# 컴파일과 매칭을 한번에 사용
# p = re.compile('[a-z]+')
# m = match("python")
# ==>
# m = re.match('[a-z]+', "python")

# DOTALL, S(약어) : dot(.)문자가 줄바꿈 문자를 포함하여 모든 문자와 매칭
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

# IGNORECASE, I(약어) : 대.소문자에 관계없이 매칭
p = re.compile('[a-z]', re.I)
m = p.match('python')
print(m)
m = p.match('Python')
print(m)
print("====\n")
# MULTILINE, M(약어) : 여러줄과 매칭
# ^python : 문자열의 처음은 항항 'python'으로 시작
# python$ : 문자열의 마지막은 항항 'python'으로 종료
p = re.compile("^python\s\w+", re.MULTILINE)  #python단어로 시작하고 그 뒤에 whitespace, 그 뒤에 단어가 와야함

data = '''python one
life is too short
python two
you need python
python three'''

print(p.findall(data))


# VERBOSE, X(약어) : berbose 모드 사용 (주석 등 사용)
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|[0-9]+|x[0-9a-fA-F]+);')
charref = re.compile(r'''
&[#] # Start of a numeric entity reference
(
    0[0-7]+ # Octal form
    |[0-9]+ # Decimal form
    |x[0-9a-fA-F]+ # Hexadecimal form
)
; # Trailing semicolon
''', re.VERBOSE)




### 3. 응용하기
# | : or  'A|b'

p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)
print("=====")

# ^ : 맨 앞 문자가 일치
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))
print("=====")

# \A : 전체 문자열의 처음과 매치

# $ : 문자 끝과 일치
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you neet python'))
print("=====")

# \Z : 전체 문자열의 끈과 매치

# \b :  단어 구분자(word boundary), 보통 단어는 whitespace에 의해 구분
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the dackassified algorithm'))
print("=====")

# \B : whitespace로 구분된 단어가 아닌 경우에 매칭

p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print(p.search('the daclassified algorithm'))

print("=============\n\n\n")

# Grouping (ABC)+
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group(0))
print("=====")

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print("=====")

p = re.compile(r"(\b\w+)\s+\1")
m = p.search('Paris in the the spring').group()
print(m)
print("=============\n\n\n")

# Grouping에 이름 붙이기
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(0))
print(m.group(1))
print(m.group('name'))
print("=============\n\n\n")


# 문자열 바꾸기 sub()
p = re.compile('(blue|white|red)')
m = p.sub('colour', 'blue socks and red shoes', count=1)
print("blue를 찾아서 colour로 변경 >>", m)
print("=====")

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
m = p.sub("\g<phone> 하하 \g<name>", "park 010-1234-1234")
print("이름과 전화번호 위치를 변경 >>", m)
