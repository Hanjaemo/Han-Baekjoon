# 입력받은 알파벳을 대문자로 변환
s = input().upper()
# 입력받은 변수 s를 중복 제거하여 리스트에 추가
s_list = list(set(s))
cnt = []

for i in s_list:
    # 문자열 s 내 i의 개수를 count에 저장
    count = s.count(i)
    # count를 cnt라는 빈 리스트에 추가
    cnt.append(count)
    
# cnt의 요소 중 최대값이 2개 이상이면 '?' 출력
if cnt.count(max(cnt)) >= 2:
    print('?')
# 아니라면 cnt의 요소 중 최대값에 해당하는 알파벳 출력
else:
    print(s_list[cnt.index(max(cnt))])