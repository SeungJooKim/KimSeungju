student_list = []


class Student:
    def __init__(self, name, mid, fin):
        self.name = name
        self.mid = mid
        self.fin = fin
        self.grade = 0


def Menu1(name, mid_s, fin_s):
    student_list.append(Student(name, mid_s, fin_s))


def Menu2():
    for stu in student_list:
        if stu.grade == 0:
            avg = int((stu.mid+stu.fin) / 2)
            if avg >= 90:
                stu.grade = 'A'
            elif avg >= 80:
                stu.grade = 'B'
            elif avg >= 70:
                stu.grade = 'C'
            else:
                stu.grade = 'D'


def Menu3():
    print('------------------------------------------------')
    print('%-10s %-10s %-10s %-10s' % ('name', 'mid', 'final', 'grade'))
    print('------------------------------------------------')
    for stu in student_list:
        print('%-10s %-10d %-10d %-5s' %
              (stu.name, stu.mid, stu.fin, stu.grade))


def Menu4(name):
    for stu in student_list:
        if stu.name == name:
            student_list.remove(stu)


def checkIsExist(name):
    for stu in student_list:
        if stu.name == name:
            return True
    return False


def checkGrade_All():
    for stu in student_list:
        if stu.grade == 0:
            return False
    return True


class AlreadyInStudent(Exception):
    def __init__(self):
        super().__init__('Already Exist Name!')


class WrongScore(Exception):
    def __init__(self):
        super().__init__('Score is not positive integer!')


print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

while True:
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            stu_name, mid_s, fin_s = input(
                'Enter name, mid-score, final-score : ').split()

            if not mid_s.isdigit() or not fin_s.isdigit():
                raise WrongScore

            mid_s = int(mid_s)
            fin_s = int(fin_s)

            if mid_s < 0 or fin_s < 0:
                raise WrongScore

            if checkIsExist(stu_name):
                raise AlreadyInStudent

            Menu1(stu_name, mid_s, fin_s)

        except WrongScore as e:
            print(e)
        except ValueError:
            print("Num of data is not 3!")
        except AlreadyInStudent as e:
            print(e)

    elif choice == "2":
        if not student_list:
            print('No Student Data!')
            continue
        else:
            Menu2()
            print('Grading to All students.')

    elif choice == "3":
        if not student_list:
            print('No Student Data!')
            continue

        if not checkGrade_All():
            print('There is a student who didn''t get grade !')
            continue

        Menu3()

    elif choice == "4":
        if not student_list:
            print('No Student Data!')
            continue
        else:
            name = input('Enter the name to delete : ')

            if not checkIsExist(name):
                print('Not exist name!')
                continue
            else:
                Menu4(name)
                print(name, 'Student information is deleted !')

    elif choice == "5":
        print('EXIT PROGRAM!')
        break

    else:
        print('Wrong Number. Choose Again !')
        continue
