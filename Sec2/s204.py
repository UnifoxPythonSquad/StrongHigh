# Tuple type
'''
리스트는 [과 ]으로 둘러싸지만 튜플은 (과 )으로 둘러싼다.
리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
'''
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

#튜플의 인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0],t1[3])

#튜플의 슬라이싱
print(t1[1:])

#튜플의 덧셈
t2 = (3, 4)
print(t1 + t2)

#튜플의 곱셈
print(t2 * 3)
