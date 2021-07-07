import random

# 예외 정의


class NotIn123(Exception):
    def __init__(self):
        super().__init__('1,2,3 중에 선택해주세요')


def brGame(player, num):
    player_num = 0

    while(True):
        if player == 'player':
            try:
                player_num = int(input('부를 숫자의 개수를 입력하세요 (1,2,3 만 입력가능) : '))
                next_turn_player = 'computer'
                if 1 > player_num or player_num > 3:
                    raise NotIn123
                else:
                    break

            except NotIn123 as e:
                print(e)

            except ValueError:
                print('정수를 입력하세요')

        elif player == 'computer':
            next_turn_player = 'player'
            player_num = random.randint(1, 3)
            break

    for i in range(player_num):
        num = num+1
        print(player, ' : ', num)

        if num == 31:
            print(next_turn_player, ' win!!')
            exit()
    return num


num = 0

while(True):
    num = brGame("computer", num)
    num = brGame("player", num)
