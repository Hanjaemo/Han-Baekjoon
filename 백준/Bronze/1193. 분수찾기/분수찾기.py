x = int(input())

line = 0
max_x = 0

while x > max_x:
    line += 1
    max_x += line
    
gap = max_x - x

if line % 2 == 0:
    top = line - gap
    under = gap + 1
else:
    top = gap + 1
    under = line - gap
    
print(f'{top}/{under}')