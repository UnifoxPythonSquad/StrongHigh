# about variable

'''
파이썬에서는 저장된 값을 판단하여 자료형을 알아낸다.
'''

a = [1,2,3]
b = a
print(a is b)
'''
두 변수의 메모리 주소가 같다.
즉 이름만 다르고 실질적으로 같은 메모리이다.
이를 해결하기 위해는 다음을 이용한다.
'''

#[:]를 이용한 값 복사
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(a is b)

#copy 모듈 이용
from copy import copy
b = copy(a)
print(a is b)

#변수를 만드는 방법
a, b = ('python', 'life')
[a,b] = ['python', 'life']
a = b = 'python'
