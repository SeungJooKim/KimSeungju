# for문!

for i in range(100):
    print('hello world')


for i in range(5, 12):
    print('hello world', i)


for i in range(0, 10, 2):
    print('hello world', i)  # 증가폭 사용

for i in range(10, 0):
    print('동작 안함')  # 출력된 거 없음

for i in reversed(range(10)):   # range에 reversed를 사용하여 숫자의 순서를 반대로 뒤집음
    print('Hello, world!', i)


fruits = ('apple', 'orange', 'grape')

for fruit in fruits:
    print(fruit)

for letter in 'Python':
    print(letter, end=' ')
