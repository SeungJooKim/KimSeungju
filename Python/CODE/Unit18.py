# break

i = 0
while True:    # 무한 루프
    print(i)
    i += 1
    if i == 100:
        break

i = 0
for i in range(10000):
    print(i)
    if i == 100:
        break


# continue
for i in range(100):
    if i % 2 == 0:
        continue
    print(i)


count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count + 1):
    if i % 2 == 0:
        continue
    print(i)
