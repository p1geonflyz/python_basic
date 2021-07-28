# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

# 기본 출력
# 주로 작은 따옴표 사용
# 기본적으로 enter 포함
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")
print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('P', 'Y', 'T', 'H', 'O', 'N', sep=' ')
print('P', 'Y', 'T', 'H', 'O', 'N', sep=',')
# 원하는 format으로 출력할 수 있음

print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

# end 옵션 -> 하나로 연결할 수 있음
print('Welcome to', end=' ')
print('IT News', end='')

# file 옵션
import sys
print('Learn Python', file=sys.stdout)

# format 사용(d, s, f)(d : 3, s : 'python', f : 3.1414)
print('%s' '%s' %('one', 'two'))
print('{} {}' .format('one', 'two'))
print('{1} {0}' .format('one', 'two'))

# %Ns -> N개의 자리 수
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice')) #중앙정렬

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) #절삭
print('{:10.5}'.format('pythonstudy')) #총 10글자 중 5글자 출력

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))
print('{:<4d}'.format(42))

# %f
print('%f' % (3.1434343434343434))
print('%1.10f' % (3.1434343434343434))
print('{:f}'.format(3.1434343434343434))
print('%06.2f' % (3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))

#정수나 실수일 때는 %d, %f를 넣어줘야함
#% 또는 format 사용
