from KnuthMorrisPratt import KMP

# def isRotated(string1, string2):
# 	'''returns True if string2 is a rotation of string1, else False'''
# 	N = len(string1)
# 	if N != len(string2):
# 		return False
# 	index = 1 # index into string1; length of pattern from string1
# 	while index < N - 1:
# 		pat = string1[:index]
# 		kmp = KMP(pat)
# 		offset = kmp.search(string2)
# 		if (offset + index) == N:
# 			suffix1 = string1[index:]
# 			prefix2 = string2[:offset]
# 			return suffix1 == prefix2
# 		else:
# 			index += 1
# 	return False

def isRotated(string1, string2):
	'''returns True if string2 is a rotation of string1, else False'''
	if len(string1) != len(string2):
		return False
	text = string1 + string2
	N = len(text)
	kmp = KMP(string1)
	offset = kmp.search(text)
	if offset < N:
		return True
	else:
		False

