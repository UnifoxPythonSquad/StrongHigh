# Set type

s1 = set([1,2,3])
print(s1)
'''
집합 자료형의 특징
중복을 허용하지 않는다.
순서가 없다(Unordered).
'''

#집합의 이용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

#교집합
print(s1 & s2)

#gkq집합
print(s1 | s2)

#차집합
print(s1 - s2)

#함수
#값 하나 추가
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

#값 여러 개 추가
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

#특정 값 제거
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)
