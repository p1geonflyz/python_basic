# Chapter 03 - 5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용(웹에서는 json 형태로 사용되기도 함)
# 딕셔너리 자료형(순서x, 키 중복 허용x, 수정O, 삭제O)

# 선언
# () - > 튜플
# [] - > 리스트
# {} - > 딕셔너리 (or 집합)
a = {'name' : 'kim', 'phone' : '010333377777', 'birth' : '870514'} # key와 value로 이루어짐
#a = {'name' : 'kim', 'name' : 'Lee'} -> 중복 안됨
b = {0 : 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 33,
    'Grade' : 'A',
    'Status' : True
}

# 또 다른 dict의 선언 방법 -> list 안의 tuple
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

#딕셔너리 -> 구조적, 정보를 효율적으로 저장가능

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 출력
print('a - ', a['name']) # 속성으로 사용 시, 존재 x-> 에러발생
print('a - ', a.get('name1')) # 없을 경우를 대비해서 get을 더 많이 사용함 -> 프로그램 끊기지 않고 잘 돌아감
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 길이
a['address'] = 'seoul'
print('a - ', a)
a['name'] = 'lee'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

print('a - ', len(a))
print('a - ', len(b))
print('a - ', len(c))
print('a - ', len(d))

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))

print()

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))

print()

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))

print()

print('a - ', a.pop('name'))
print('a - ', a)

print('c - ', c.pop('arr'))
print('c - ', c)

print()

print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)

print()

print('a - ', 'birth' in a)
print('d - ', 'city' in d)

# 수정
a['test'] = 'test_dict'
print('a - ', a)

a['address'] = 'dj'
print('a - ', a)

a.update(birth = '910904')
print('a - ', a)

temp = {'address' : 'busan'}
a.update(temp)
print('a - ', a)
