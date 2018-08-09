# contro keyword

money = 1
if money:
     print("택시를 타고 가라")
else:
     print("걸어 가라")
     
'''
들여쓰기에 조심해서 코딩을 해야한다.
'''

# 비교 연산자
x = 3
y = 2
print(x > y)
print(x < y)
print(x == y)
print(x != y)

money = 2000
if money >= 3000:
     print("택시를 타고 가라")
else:
     print("걸어가라")
     
money = 2000
card = 1
if money >= 3000 or card:
     print("택시를 타고 가라")
else:
     print("걸어가라")
    
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
     print("택시를 타고 가라")
else:
     print("걸어가라")

'''
아무일도 하지 않게 설정하려면 pass를 사용한다.
'''

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
     pass 
else:
     print("카드를 꺼내라")

#elif 
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
     print("택시를 타고가라")
elif card: 
     print("택시를 타고가라")
else:
     print("걸어가라")

#조건부 표현식
score = 60
message = "success" if score >= 60 else "failure"
print(message)
