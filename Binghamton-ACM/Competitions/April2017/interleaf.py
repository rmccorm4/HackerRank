"""
Author: Ryan McCormick
"""

numorgs = int(input())
#org list
orgs = input().split()
#veg list
veg = input().split()
#~20
numveg = int(len(veg)/2)

#list of orgs' veggies
orgveg = []
for y in range(numorgs):
    orgveg.append([])

i=0
for x in range(0, len(veg), 2):
    if (veg[x+1]=='1'):
        orgveg[i].append(veg[x])
        if i == numorgs-1:
            i=0
        else:
            i+=1

both = []
for z in range(numorgs):
    both.append([])
for z in range(numorgs):
    both[z].append(orgs[z])
    both[z].append(orgveg[z])


both = sorted(both)

for x in range(numorgs):
    out = ""
    both[x][1] = sorted(both[x][1])
    for item in both[x][1]:
        out += item + " "

    print(both[x][0], out)

