# 클래스 속성과 인스턴스 속성

# 클래스 속성
class Person:  # 클래스 속성은 모든 인스턴스에서 공유함!
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)


james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

# 인스턴스 속성


class Person:
    def __init__(self):
        self.bag = []  # 인스턴스 속성

    def put_bag(self, stuff):
        self.bag.append(stuff)


james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)


# 정적 메서드
class Calc:  # 정적 메서드는 @staticmethod 사용
    @staticmethod  # self가 붙지 않음
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)


Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)


# 클래스 메서드 #@classmethod 사용
class Person:
    count = 0    # 클래스 속성

    def __init__(self):
        Person.count += 1    # 인스턴스가 만들어질
        # 클래스 속성 count에 1을 더함

    @classmethod
    def print_count(cls):  # cls
        print('{0}명 생성되었습니다.'.format(cls.count))    # cls로 클래스 속성에 접근


james = Person()
maria = Person()

Person.print_count()    # 2명 생성되었습니다.
