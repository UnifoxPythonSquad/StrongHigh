# function

# 함수의 구조
'''
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
'''

def sum(a, b): 
    return a + b
    
a=3
b=4
c = sum(a,b)
print(c)


# 입력값이 없는 함수
def say(): 
    return 'Hi' 
a= say()
print(a)


# 입력값도 결과값도 없는 함수
def hello(): 
    print('Hi')
hello()

print(sum(a=3, b=7))
print(sum(b=5, a=3))


# 입력값이 여러개인 함수
def sum_many(*args): 
    sum = 0 
    for i in args: 
        sum = sum + i 
    return sum

print(sum_many(1,2,3))
print(sum_many(1,2,3,4,5,6,7,8,9,10))


# 전역변수 변경 
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)


# lambda
sum = lambda a, b: a+b
print(sum(3,4))

