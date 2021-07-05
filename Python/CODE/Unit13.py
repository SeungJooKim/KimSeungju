x = 10

if x == 10:
    print('성공')


if x == 10:
    pass  # 코드 생략

# 들여쓰기 주의
if x == 10:
    print('x는')
    print('10입니다.')

# 중첩 if
x = 15
if x >= 10:
    print('10이상')
    if x >= 12:
        print('12이상')
    if x == 15:
        print('15임')


x = int(input()) 

if x == 10:            
    print('10입니다.')
