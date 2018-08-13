#file I/O

#파일 생성 
f = open("f401.txt", 'w')
f.close()

'''
r	읽기모드 - 파일을 읽기만 할 때 사용
w	쓰기모드 - 파일에 내용을 쓸 때 사용
a	추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
'''


# 출력값 파일에 저장
f = open("f401.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


# 파일 내용 읽어오기
f = open("f401.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("f401.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close

# readlines func
f = open("f401.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()


# read func
f = open("f401.txt", 'r')
data = f.read()
print(data)
f.close()


# 파일에 내용 추가하기
f = open("f401.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


# with keyword
with open("f402.txt", "w") as f:
    f.write("Life is too short, you need python")
''' 자동으로 close '''
