x = int(input())    # 영수증에 적힌 총 금액
n = int(input())    # 구매한 물건의 종류의 수
sum = 0

for i in range(0, n):
    # 물건의 가격 a와 개수 b 입력
    a, b = map(int, input().split())
    sum += (a * b)

if sum == x:
    print('Yes')
else:
    print('No')