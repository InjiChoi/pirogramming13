height = int(input())
blank = height -1
for i in range(height):
    for j in range(height+i):
        if j<blank:
            print(' ',end='')
        else:
            print('*',end='')
    print()
    blank= blank-1
