# 중첩 루프 사용하기

# 별 계단 식 출력
for i in range(5):
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print('i:', i, '\\n', sep='')


# 사각형으로 별 출력
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()


# 대각선으로 별 출력
for i in range(5):
    for j in range(5):
        if(j == i):
            print('*', end='')
        else:
            print('', end='')
    print()
