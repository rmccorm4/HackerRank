#This was my first attempt, it passes 7/9 test cases, the other 2 timeout so
#there must be some sort of infinite loop happening
def array_left_rotation(a, n, k):
    b = [0]*n
    for shift in range(k):
        for index in range(n):
            b[index-1] = a[index]
        a = b[:]
    return a

#This part was given by hackerrank to pass the input and print output
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
