from KnuthMorrisPratt import KMP

def isRotated(string1, string2):
	'''returns True if string2 is a rotation of string1, else False'''
	N = len(string1)
	if N != len(string2):
		return False
	index = 1 # index into string1; length of pattern from string1
	while index < N - 1:
		pat = string1[:index]
		kmp = KMP(pat)
		offset = kmp.search(string2)
		if (offset + index) == N:
			suffix1 = string1[index:]
			prefix2 = string2[:offset]
			return suffix1 == prefix2
		else:
			index += 1
	return False