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
