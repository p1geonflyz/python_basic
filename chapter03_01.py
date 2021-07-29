# Chapter 03-1
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
*시퀀스 : 반복이나 순서가 있는 것
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = 'Anaconda'
float_v = 10.0 # 10 == 10.0 -> 다름, 한쪽을 int 또는 float 형으로 바꿔줘야함
int_v = 7
list = [str1, str2]
dict = {
    "name" : "machine learning",
    "version" : 2.0
}
tuple = (7, 8, 9) # 괄호 없이 사용 가능(only ,로만)
set = {7, 8, 9}

#데이터 타입 출력
print(list)
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

#숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) == x ** y
"""

#정수 선언
i = 77
i2 = -14
big_int = 77777777777999999999999999999999

#정수 출력
print(i)
print(i2)
print(big_int)

#실수 출력
f = 0.99999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)

#연산
i1 = 39
i2 = 939
big_int1 = 777777779999999923232424342
big_int2 = 999999991414919999134107510
f1 = 1.7777
f2 =  3.9339

# +
print(">>>>>>>+")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)

# -
print(">>>>>>>+")
print("i1 - i2 : ", i1 - i2)
print("f1 - f2 : ", f1 - f2)
print("big_int1 - big_int2 : ", big_int1 - big_int2)

# *
print(">>>>>>>*")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)

# +
print(">>>>>>>/")
print("i1 / i2 : ", i1 / i2)
print("f1 / f2 : ", f1 / f2)
print("big_int1 / big_int2 : ", big_int1 / big_int2)

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True : 1, Flase : 0
print(float(False))
print(complex(3))
print(complex('3'))
print(complex(False))

# 수치 연산 함수
print(abs(-7))
x, y =divmod(100, 8)
print(x, y)
print(pow(5, 3), 5 ** 3)

# 외부 모듈
import math

print(math.pi)
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
