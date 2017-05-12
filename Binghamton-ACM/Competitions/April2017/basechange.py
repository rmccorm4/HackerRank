"""
Author: Ryan McCormick
"""

numcases = int(input())
cases = []
for x in range(numcases):
    cases.append(input().split()[1])
    
octals=[0]*numcases
tens=[0]*numcases
hexs=[0]*numcases
i=0

for string in cases:
    badoctal=False
    ln = len(string)-1
    for x in range(len(string)):
        if int(string[ln]) > 7:
            badoctal=True
        else:
            octals[i] += (8**x)*int(string[ln])
            
        tens[i] += (10**x)*int(string[ln])
        hexs[i] += (16**x)*int(string[ln])
        ln-=1
    if (badoctal == True):
        octals[i]=0
    i+=1
        
for i in range(numcases):
    print(i+1, octals[i], tens[i], hexs[i])
    
