class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
        # self : 첫번째 매개변수로 객체를 호출한 객체 자신
        # >>> a = FourCal()
        # >>> FourCal.setdata(a, 4, 2)
        # >>> a.setdata (4, 2)

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / sellf.second
        return result

class MoreFourCal(FourCal):
    # 클래스 상속(Inheritance)

    def pow(self):
        result = self.first**self.second
        return result

class SafeFourCal(FourCal):
    def div(self):
        # 메서드 오버라이딩(overriding)

        if self.second == 0:
            return 0
        else:
            return self.first / self.second
