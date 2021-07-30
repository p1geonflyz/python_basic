# Chapter 03 - 4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서 O, 중복 O, 수정 X, 삭제 X) -> del, remove, insert 안됨 # 불변
# 중요한 데이터들, 변하면 안되는 정보들을 튜플로 저장

# 선언

a = ()
b = (1,) #하나일 때는 , 찍어야 튜플로 사용 가능
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))

print(type(a), type(b))

# 인덱싱
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('d - ', e[-1])
print('d - ', e[-1][1])
print('d - ', list(e[-1][1]))

# 수정  X
#d[0] = 1500 -> 안됨

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])

# 튜플 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a.index(3))
print('a - ', a.count(2))

# 팩킹 & 언팩킹(Packing and Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux') # -> 원소를 묶은 것: 패킹

print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t # 묶여있던 것을 풀어서 각각 맞는 순서의 원소에 대입 #가로가 있어도 없어도 무관

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
