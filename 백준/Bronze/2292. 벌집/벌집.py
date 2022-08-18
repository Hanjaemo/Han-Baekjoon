n = int(input())

room = 1 # 벌집의 개수, 1개부터 시작
cnt = 1 # 반복 횟수, 반복문을 통해 1씩 증가

while n > room:
    room += 6 * cnt
    cnt += 1

print(cnt)