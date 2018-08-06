#String type

#문자열을 만드는 법
'''
1. 큰따옴표로 둘러싸기
2. 작을따옴표로 둘러싸기
3. 큰따옴표 3개로 둘러싸기
4. 작은따옴표 3개로 둘러싸기
'''

#문자열 안에 작은따옴표나 큰따옴표를 포함할때

food = "Python's favorite food is perl"
say = '"Python is very easy." he says.'
print(food,say)
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

print(food,say)

#여러 줄인 문자열을 변수에 대입하고 싶을 때
multiline='''
Life is too short
You need python
'''
print(multiline)
multiline="""
Life is too short
You need python
"""
print(multiline)

#문자열 연산하기
#덧셈
head = "Python"
tail = " is fun!"
print(head + tail)

#곱셈
a = "python"
print(a*2)

#문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3])
print(a[-2])


#문자열 슬라이싱
print(a[0:4])
print(a[19:])
print(a[:17])
print(a[:])
print(a[19:-7])

#문자열 포매팅
number = 3
day = "three"
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
print("I eat %d apples." % number)
print("I ate %d apples. so I was sick for %s days." % (number, day))

#문자열 정렬 
print("%10s" % "hi")
print("%-10sjane." % 'hi')

#문자열 실수형 포매팅 소수점
y = 3.42134234
print("%0.4f" % 3.42134234)

#format 함수를 이용한 포매팅
number = 3
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
print("I eat {0} apples".format(number))
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:10.4f}".format(y))

#문자열 함수

#문자 개수 세기
a = "hobby"
print(a.count('b'))

#위치 알려주기
a = "Python is the best choice"
print(a.find('b'))
print(a.index('t'))

#문자열 삽입 
print(a.join('abcd'))

#대소문자 변환 
print(a.upper())
print(a.lower())

#문자열 교체 
a = "Life is too short"
print(a.replace("Life", "Your leg"))

#문자열 분리
a = "Life is too short"
print(a.split())
