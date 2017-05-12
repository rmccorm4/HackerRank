"""
Author: Ryan McCormick
"""

num = int(input())
if num == 1:
    print(0)
elif num == 2:
    print(1)
else:
    it = 0
    while num != 1:
        if num%2 == 0:
            num = num / 2
        else:
            num = 3*num+1
        it+=1
    print(it)
