# else사용

x = 5

if x == 10:
    print('10이다')
else:
    print('10아니다')


if x == 10:
    y = x
else:
    y = 0


# 들여쓰기 주의
if x == 10:
    print('10임!!')

else:
    print('x에 들어있는 것은')
    print('10이 아님!!')

# 동작 방식

if 0:
    print('참')

else:
    print('거짓')

if 1:
    print('참')
else:
    print('거짓')  # 참 출력


if None:  # none은 거짓
    print('참')
else:
    print('거짓')


if not 0:
    print('참')  # not 0은 참

if not None:
    print('참')  # None은 참

if not '':
    print('참')  # not 빈 문자열은 참
