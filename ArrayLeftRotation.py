def array_left_rotation(a, n, k):
    return a[k:] + a[:k]

#This part was given by hackerrank to pass the input and print output
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
