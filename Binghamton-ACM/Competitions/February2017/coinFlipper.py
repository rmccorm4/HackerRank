""" Author: Ryan McCormick """

numsets = int(input())
strings=[]

for x in range(1, numsets+1):
    sets.append(input())
    strings.append(input())

j=1
for string in strings:
    sub=[]
    TTT=0
    TTH=0
    THT=0
    THH=0
    HTT=0
    HTH=0
    HHT=0
    HHH=0
    for i in range(len(string)):
        if i+3 <= len(string):
            sub.append(string[i:i+3])
    for triple in sub:
        if(triple == "TTT"): TTT+=1
        elif(triple == "TTH"): TTH += 1
        elif(triple == "THT"): THT+=1
        elif(triple == "THH"): THH+=1
        elif(triple == "HTT"): HTT+=1
        elif(triple == "HTH"): HTH+=1
        elif(triple == "HHT"): HHT+=1
        elif(triple == "HHH"): HHH+=1
    print(j, TTT, TTH, THT, THH, HTT, HTH, HHT, HHH)
    j+=1
