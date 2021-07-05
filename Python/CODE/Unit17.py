import random
i = 0                     # 초기식
while i < 100:            # while 조건식
    print('Hello, world!')    # 반복할 코드
    i += 1                    # 변화식


count = int(input('반복할 횟수를 입력하세요: '))
i = 0
while i < count:
    print('Hello, world!', i)
    i += 1

random.randint(1, 6)


i = 0
while i != 3:
    i = random.randint(1, 6)
    print(i)


while 'Hello':
    print('Hello, world!')
