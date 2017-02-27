def ransom_note(magazine, ransom):
    #dictionary is O(1) because you can just access value using key immediately
    myMagazine = {word: 0 for word in magazine}

    for word in magazine:
        myMagazine[word] += 1
    
    for word in ransom:
        #have to use .get() with default value of -1 if not found 
        #because you'll get a key error otherwise
        if myMagazine.get(word, -1) > 0:
                myMagazine[word] -= 1
        else:
            return False
    return True


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
