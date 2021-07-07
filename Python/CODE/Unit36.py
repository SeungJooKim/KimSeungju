# 클래스 상속 이용하기

from abc import *


class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):  # 상속받아 생성
    def study(self):
        print('공부하기')


james = Student()
james.greeting()    # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.study()       # 공부하기: 파생 클래스 Student에 추가한 study 메서드

# issubclass 상속관계 확인하기
issubclass(Student, Person)  # 파생클래스 / 기반 클래스 순으로 작성


# 포함 관계

class Person:
    def greeting(self):
        print('안녕하세요.')


class PersonList:
    def __init__(self):
        self.person_list = []    # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person):    # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)


# super()로 기반 클래스 초기화 하기

class Person:
    def __init__(self):  # 생성자가 있으므로 상속받는 애한테서 호출 필요
        print('Person __init__')
        self.hello = '안녕하세요.'


class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()                # super()로 기반 클래스의 __init__ 메서드 호출
        self.school = '파이썬 코딩 도장'


james = Student()
print(james.school)
print(james.hello)


# 메서드 오버라이딩

class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')


james = Student()
james.greeting()  # student 형식 출력

# 부모꺼도 같이 출력


class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def greeting(self):
        super().greeting()  # super()사용
        print('저는 파이썬 코딩 도장 학생입니다.')


james = Student()
james.greeting()


# 다중 상속 사용하기
class Person:
    def greeting(self):
        print('안녕하세요.')


class University:
    def manage_credit(self):
        print('학점 관리')


class Undergraduate(Person, University):
    def study(self):
        print('공부하기')


james = Undergraduate()
james.greeting()         # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.manage_credit()    # 학점 관리: 기반 클래스 University의 메서드 호출
james.study()            # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드


# 추상클래스 사용


class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass  # 빈 메서드로 만들기

    @abstractmethod
    def go_to_school(self):
        pass


class Student(StudentBase):
    def study(self):
        print('공부하기')


james = Student()
james.study()
