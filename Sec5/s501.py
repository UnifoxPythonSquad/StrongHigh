# Class

#사칙연산 클래스
class FourCal:
    # 세터 
    def setdata(self, first, second):
        self.first = first
        self.second = second
    # 메소드
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

    
a = FourCal()
a.setdata(4, 2)
print(a.first)
print(a.second)

b = FourCal()
b.setdata(3, 7)
print(b.first)
print(a.first)

a = FourCal()
a.setdata(4, 2)
print(a.sum())

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())
print(b.sum())
print(b.mul())
print(b.sub())
print(b.div())


class FourCal2:
    # 생성자 
    def __init__(self, first, second):
        self.first = first
        self.second = second
    # 메소드
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal2(4, 2)
print(a.sum())
print(a.div())

    
# 상속 
class MoreFourCal(FourCal2):
    def pow(self):
        result = self.first ** self.second
        return result

    
a = MoreFourCal(4, 2)
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())


# 메소드 오버로딩 
class SafeFourCal(FourCal2):
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())

# 클래스 변수
class Family:
    lastname = "김"

a = Family()
b = Family()

print(Family.lastname)
print(a.lastname)
print(b.lastname)

Family.lastname = "박"

a = Family()
b = Family()
