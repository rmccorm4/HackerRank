#convert text to integer
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

#formatting input to a workable list
equation = input()
equation = equation.replace('plus', '+')
equation = equation.replace('divided by', '/')
equation = equation.replace('minus', '-')
equation = equation.replace('times', '*')

#regular expression module
import re
numbers = re.split('\+ |\- |\/ |\*', equation)
intnums=[text2int(num) for num in numbers]

eqlist = equation.split()
ops = []
for word in eqlist:
    if word == '+' or word == '*' or word == '-' or word == '/':
        ops.append(word)

#ops has the operations and its length is 1 less than the amount of numbers
#intnums has the actual integer numbers of the equation
intsAndOps = []
for x in range(len(intnums)):
    if x != len(intnums)-1:
               intsAndOps.append(intnums[x])
               intsAndOps.append(ops[x])
    else:
               intsAndOps.append(intnums[x])

#perform operations in PEMDAS order
while '*' in intsAndOps and '/' in intsAndOps:
    starIndex = intsAndOps.index('*')
    divIndex = intsAndOps.index('/')
    if(starIndex < divIndex):
        intsAndOps[starIndex-1] = intsAndOps[starIndex-1]*intsAndOps[starIndex+1]
        intsAndOps = intsAndOps[:starIndex]+intsAndOps[starIndex+2:]
    else:
        intsAndOps[divIndex-1] = intsAndOps[divIndex-1]/intsAndOps[divIndex+1]
        intsAndOps = intsAndOps[:divIndex]+intsAndOps[divIndex+2:]

while '/' in intsAndOps:
    divIndex = intsAndOps.index('/')
    intsAndOps[divIndex-1] = intsAndOps[divIndex-1]/intsAndOps[divIndex+1]
    intsAndOps = intsAndOps[:divIndex]+intsAndOps[divIndex+2:]

while '*' in intsAndOps:
    starIndex = intsAndOps.index('*')
    intsAndOps[starIndex-1] = intsAndOps[starIndex-1]*intsAndOps[starIndex+1]
    intsAndOps = intsAndOps[:starIndex]+intsAndOps[starIndex+2:]

while '+' in intsAndOps and '-' in intsAndOps:
    plusIndex = intsAndOps.index('+')
    minusIndex = intsAndOps.index('-')
    if(plusIndex < minusIndex):
        intsAndOps[plusIndex-1] = intsAndOps[plusIndex-1]+intsAndOps[plusIndex+1]
        intsAndOps = intsAndOps[:plusIndex]+intsAndOps[plusIndex+2:]
    else:
        intsAndOps[minusIndex-1] = intsAndOps[minusIndex-1]-intsAndOps[minusIndex+1]
        intsAndOps = intsAndOps[:minusIndex]+intsAndOps[minusIndex+2:]

while '+' in intsAndOps:
    plusIndex = intsAndOps.index('+')
    intsAndOps[plusIndex-1] = intsAndOps[plusIndex-1]+intsAndOps[plusIndex+1]
    intsAndOps = intsAndOps[:plusIndex]+intsAndOps[plusIndex+2:]

while '-' in intsAndOps:
    minusIndex = intsAndOps.index('-')
    intsAndOps[minusIndex-1] = intsAndOps[minusIndex-1]-intsAndOps[minusIndex+1]
    intsAndOps = intsAndOps[:minusIndex]+intsAndOps[minusIndex+2:]

print(int(intsAndOps[0]))


