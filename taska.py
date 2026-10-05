
y = int(input())

if y%400==0 or ( y%4==0 and y%100!=0):
    print('YES')
else:
    print('NO')

'''
if y % 4 == 0:
    if y%100 == 0:
        if y%400 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
else:
    print('NO')
'''