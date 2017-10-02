# What is the smallest number such that every number after it
# can be represented as a sum of 6, 9, and 20 (chicken nuggets)
# AKA
# What is the largest number of chicken nuggets that you CAN'T 
# buy when they're sold as 6, 9, or 20 pieces

bools = []
# Initialize first few known numbers
for i in range(10):
	if i == 6 or i == 9:
		bools.append(True)
	else:
		bools.append(False)
		
i = 10
while 
