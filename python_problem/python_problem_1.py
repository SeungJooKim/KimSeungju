# 예외 정의
class NotIn123(Exception):
    def __init__(self):
        super().__init__('1,2,3 중에 선택해주세요')


num = 0

while(True):
    while(True):
        try:
            player_num = int(input('부를 숫자의 개수를 입력하세요 (1,2,3 만 입력가능) : '))
            if 1 > player_num or player_num > 3:
                raise NotIn123
            else:
                break

        except NotIn123 as e:
            print(e)

        except ValueError:
            print('정수를 입력하세요')

    for i in range(player_num):
        num = num+1
        print('PlayerA : ', num)
        if num == 31:
            print('PlayerB win!')
            exit()

    while True:
        try:
            player_num = int(input('부를 숫자의 개수를 입력하세요 (1,2,3 만 입력가능) : '))
            if 1 > player_num or player_num > 3:
                raise NotIn123
            else:
                break

        except NotIn123 as e:
            print(e)

        except ValueError:
            print('정수를 입력하세요')

    for i in range(player_num):
        num = num+1
        print('PlayerB : ', num)
        if num == 31:
            print('PlayerA win!')
            exit()
