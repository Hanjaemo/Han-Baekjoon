a, b = input().split()

a_reverse = int(a[::-1])
b_reverse = int(b[::-1])

if a_reverse > b_reverse:
    print(a_reverse)
elif b_reverse > a_reverse:
    print(b_reverse)