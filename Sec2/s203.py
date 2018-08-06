#List type

a = [ ]
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

#리스트 인덱싱
a = [1, 2, 3]
print(a[0])
print(a[0]+a[2])
print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[-1][0])

#리스트 연산자
#덧셈
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

#곱셈
a = [1, 2, 3]
print(a * 3)

#리스트 수정, 삭제
#수정 
a = [1, 2, 3]
print(a)
a[2] = 4
print(a)
a[1:2] = ['a', 'b', 'c']
print(a)

#삭제 
a[1:3] = [ ]
print(a)
del a[1]
print(a)

#리스트 함수
#추가
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5,6])
print(a)

#정렬 
a = [1, 4, 3, 2]
a.sort()
print(a)

#리스트 반전
a = ['a', 'c', 'b']
a.reverse()
print(a)

#위치 반환
a = [1,2,3]
print(a.index(3))

#삽입
a = [1, 2, 3]
a.insert(0, 4)
print(a)

#제거
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

#pop
a = [1,2,3]
print(a.pop())
print(a)

#요소 개수 새기
a = [1,2,3,1]
print(a.count(1))
