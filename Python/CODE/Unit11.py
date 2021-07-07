a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

30 in a  # true

100 in a  # false

43 in (38, 76, 43, 62, 16)  # true

100 not in a  # true

'P' in 'Hello Python'  # true

range(0, 10) + range(10, 20)  # 오류! 이렇게 쓸 수 없음


list(range(0, 10)) + list(range(10, 20))

'Hello, ' + str(10)  # Hello 10

[0, 10, 20, 30] * 3  # 3번 반복됨


a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
len(a)  # 길이 구하기


a = [38, 21, 53, 62, 19]
a[0]
a[2]  # 인덱스 사용
a.__getitem__(1)

b = (38, 21, 53, 62, 19)
b[0]
b[-1]  # 뒤에서부터
del b[2]  # 삭제

# 슬라이스
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[1:1]
a[4:7]

a[4:-1]  # 인덱스 4부터 -2까지 요소 5개를 가져옴

a[2:8:3]  # 증가폭

a[:7]  # 리스트 처음부터
a[:]  # 리스트 전체

b = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
b[4:7]


a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a']    # 인덱스 2부터 4까지에 값 1개를 할당하여 요소의 개수가 줄어듦


del a[2:5]