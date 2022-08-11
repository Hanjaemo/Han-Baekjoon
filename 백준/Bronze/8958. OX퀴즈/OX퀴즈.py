t = int(input())

for i in range(t):
    # 입력 받은 문자열을 리스트 형식으로 저장
    ox_list = list(input())
    # 반복문 계산을 위한 초기값 설정
    score = 0
    sum_score = 0
    for ox in ox_list: 
        if ox == 'O':
            score += 1
            sum_score += score
        elif ox == 'X':
            score = 0
    print(sum_score)