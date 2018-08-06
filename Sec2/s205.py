# Dictionary type

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

#딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b'
print(a)

#딕셔너리 요소 삭제
del a[1]
print(a)

#딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'],grade['julliet'])

'''
동일한 key가 여러개 존재할 경우 하나를 제외한 나머지가 모두 무시된다.
'''

#딕셔너리 함수
#key 리스트 만들기
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())

#Value 리스트 만들기
print(a.values())

#요소 모두 지우기
a.clear
print(a)

#Key로 Value얻기(get)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))

#key가 딕셔너리에 있는지 조사하기
print('name' in a)
