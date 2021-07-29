# Chapter 03 - 2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "i am python"
str2 = "python"
str3 = """How are you?"""
str4 = '''Thanky You!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = '' # 따옴표로 열고 닫고(아무것도 없이)
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
# I'm Boy

print("i'm boy")
print('i\'m boy') # 특수 기호 뒤에 그대로 표시(escape 형식)

print('a \t b')
print('a \n b')
print('a \"\" b')

# 이스케이프 예시
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = "What\'s on TV?"
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)

# Raw String
raw_s1 = r'D:\python\test' #드라이브 경로 알려줄 때
raw_s2 = r'D:\t python\test'
print(raw_s1)
print(raw_s2)

#멀티라인 입력
#역슬래시 사용
multi_str_1 = \
'''
String
Multi Line
Test
'''

multi_str_2 = '''
String
Multi Line
Test
'''

print(multi_str_1)
print(multi_str_2)

#문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('p' not in str_o2)

#문자열 형 변환
print(str(66), type(str(66))) #66은 문자열임
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...) -> 그때그때 필요한 거 구글링해서 사용할 것
print("Capitalize : ", str_o1.capitalize())
print("endswith? : ", str_o1.endswith("n"))
print("endswith? : ", str_o2.endswith("s"))
print("endswith? : ", str_o3.endswith("?"))
print("replace", str_o1.replace("thon", ' good'))
print("sorted: ", sorted(str_o1)) #정렬에서 리스트 형태로 변환
print("split: ", str_o4.split(' ')) #단어나 문장 단위 분리시킬 때

#반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str))  #__iter__ -> 시퀀스 반복됨을 알 수 있다

#출력
for i in im_str:
    print(i)

# 슬라이싱 연습
str_s1 = "Nice Python"

# 슬라이싱 연습
print(str_s1[:4])
print(str_s1[5:])
print(str_s1[:len(str_s1)]) #str_s1[:11]과 동일 -> 끝부분 모를 때 사용하면 됨
print(str_s1[1:4:2])    #순서 1부터 4전까지 2칸씩 출력
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])

#아스키 코드
a = 'Z'
print(ord(a))   #문자를 아스키 코드로
print(chr(122)) #아스키 코드를 문자로
