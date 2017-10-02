if len(s) == 0:
	return 0
	
	maxlen = 0
	# Up to half the string is possible length of repeating substr
	for i in range(1, (len(s)+1)//2):
		length = i
		for k in range(0, len(s), length):
			if s[k : k+length] == s[k+length : k+2*length]:
				maxlen = length
	
	return maxlen
