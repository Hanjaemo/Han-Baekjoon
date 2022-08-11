n_list = []

for i in range(10):
    a = int(input())
    # 입력 받은 a를 42로 나눈 나머지를 리스트에 추가
    n_list.append(a % 42)

# set(): 중복 제거
s = set(n_list)
print(len(s))