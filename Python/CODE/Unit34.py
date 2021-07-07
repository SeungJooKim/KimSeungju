# 클래스
class Person:
    def greeting(self):
        print('hello')


james = Person()
james.greeting()


a = int(10)
b = list(range(10))

c = dict(x=10, y=20)


# 특정 클래스의 인스턴스 인지 확인하기
isinstance(james, Person)


class Person2:
    def __init__(self):
        self.hello = '안녕하세요'

    def greeting(self):
        print(self.hello)


ksj = Person2()
ksj.greeting()


class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age


sj = Person3('ksj', 23)
print(sj.name)

# 비공개 속성 __


class Person4:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.__wallet = wallet  # 변수 앞에 __ 를 붙이면 비공개 속성


maria = Person4('maria', 33, 10000)
# maria.__wallet=-10000 #에러 발생 / 접근 불가

# 비공개 메서드 __


class Person5:
    def __greeting(self):
        print('Hello')

    def hello(self):
        self.__greeting()


james = Person5()
# james.__greeting() #에러발생 / 사용 불가
