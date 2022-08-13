# sys 모듈 불러오기
import sys

# 숫자의 개수 입력
n = int(input())

# n개의 숫자를 공백없이 리스트에 추가
n_list = list(map(int, sys.stdin.readline().rstrip()))

# 반복문 계산을 위한 초기값 설정
sum = 0

for i in n_list:
    sum += i
    
print(sum)