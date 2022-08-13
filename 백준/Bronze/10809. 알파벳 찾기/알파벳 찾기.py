# string 모듈에서 ascii_lower 가져오기
from string import ascii_lowercase

# 문자열 입력
s = input()

# 알파벳 소문자를 리스트에 추가
a_list = list(ascii_lowercase)

n_list = []


for i in a_list:
    # i가 s에 포함되면 s 문자열 내 i의 위치 출력
    if i in s:
        print(s.find(i), end=' ')   # end=' '를 이용해 공백과 같이 출력
    # 포함되지 않는다면 -1 출력
    else:
        print(-1, end=' ')