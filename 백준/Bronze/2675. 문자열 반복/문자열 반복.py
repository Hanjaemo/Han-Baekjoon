t= int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    for k in range(len(s)):
        # k번째 문자를 r번 반복하여 출력
        print(s[k] * r, end='')
    print() # 줄 넘김