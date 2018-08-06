#Number type

'''
변수의 선언은 따로 없으며,
정수형, 실수형 값을 대입하여 타입을 정한다.
'''

#정수형 변수
a = 123
a = -178
a = 0
print(a)

#실수형 변수
a = 1.2
a = -3.45
print(a)

#16진수와 8진수 변수
'''
8진수는 숫자 앞에 0o 또는 0O 접두어가 붙는다.
16진수는 숫자 앞에 0x 접두어가 붙는다.
'''
a = 0o177
b = 0xABC
print(a,b)


#사칙 연산자
'''
사칙연산은 파이썬에서 그대로 수행된다.
'''
a=3
b=4
print(a+b,a*b,a/b)


#x의 y제곱 연산자
print(3**4)

#나머지 연산자
print(7%3)
print(3%7)

#가우스 연산자
'''
나눗셈 후 소숫점 아랫자리를 버린다.
'''
print(7//4)
