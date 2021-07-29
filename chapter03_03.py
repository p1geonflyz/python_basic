# Chapter 03 - 3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [70, 75, 80, 85] # 0번 1번 2번 3번
print(len(c))
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'footbar', 3, 4, False, 3.14159]

# 인덱싱 -> 원하는 데이터 가져오기
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', type(e[-1][1]))
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('e - ', e[-1][1:3])

# 리스트 연산
print('>>>>>')
print('c + d', c + d)
print('c * d', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# Identity(id)

temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # 원소로 들어감
print('c - ', c)
c[1:2] = [['a', 'b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c'] # 리스트로 들어감
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2]    #삭제
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10)    #끝에 추가
print('a - ', a)
a.sort()
print('a - ', a)    #순서대로 정렬
a.reverse()
print('a - ', a)    #역순으로 정렬
#sort, reverse는 데이터가 많아진다면 매우 오래걸림
print('a - ', a.index(3), a[3])
a.insert(2, 7)
print('a - ', a)
a.reverse()
print('a - ', a)

a.remove(10)    #불필요한 데이터를 제거할 때
print('a - ', a)
print('a - ', a.pop())  #마지막 원소 꺼내고 리스트에서 없애기
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))   # 개수 세기
ex = [8, 9]
a.extend(ex)
print('a - ', a)

#삭제 : remove, pop, del

#반복문 활용
while a:
    data = a.pop()
    print(data)
