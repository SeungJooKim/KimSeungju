a = 10
b = 20
c = a+b
c

a = 10
a+20

a

# 6-3
x = input()
x

x = input('문자열을 입력하세요: ')


a = input('첫 번째 숫자를 입력하세요: ')
b = input('두 번째 숫자를 입력하세요: ')

print(a + b)


a = input()
type(a)

a = int(input('첫 번째 숫자를 입력하세요: '))
b = int(input('두 번째 숫자를 입력하세요: '))
print(a + b)


# 6.4
a, b = input('문자열 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리

print(a)
print(b)


a, b = input('숫자 두 개를 입력하세요: ').split()  ㅑ
print(a + b)


a, b = input('숫자 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리
a = int(a)
b = int(b)
print(a + b)


a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
print(a + b)


# 6.8
a, b, c, d = map(int, input().split())
print(int((a+b+c+d)/4))
