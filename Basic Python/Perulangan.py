for i in range(1, 10):
    a = "*"
    print(a * i)

for i in range(10, 0, -1): 
    a = " "
    print(a * (10 - i) + "*" * i)

height = 7
for row in range(height):
    for col in range(height):
        if col == 0 or col == height - 1 or (row == col and col <= height // 2) or (row + col == height - 1 and col >= height // 2):
            print('*', end='')
        else:
            print(' ', end='')
    print()
    