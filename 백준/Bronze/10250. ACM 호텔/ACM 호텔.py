t = int(input())

for p in range(t):
    # 호텔의 층 수, 각 층의 방 수, n 번째 손님
    h, w, n = map(int, input().split())
    height = n % h
    width = n // h + 1
    if n % h == 0:
        height = h
        width = n // h
    print(height * 100 + width)