# a: 고정 비용, b: 가변 비용, c: 노트북 가격
a, b, c = map(int, input().split())

if b >= c:
    print(-1) # 손익분기점 존재 X
else:
    print(int((a / (c - b)) + 1)) # 손익분기점