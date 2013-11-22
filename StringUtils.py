def exch(a_sequence, i, j):
	'''exchange values a_sequence[i] and a_sequence[j]'''
	swap = a_sequence[i]
	a_sequence[i] = a_sequence[j]
	a_sequence[j] = swap
	return a_sequence

def lcp(text1, text2):
	'''return longest common prefix'''
	length = min(len(text1), len(text2))
	for i in range(length):
		if text1[i] != text2[i]:
			return i
	return length

def compareTo(string1, string2):
	'''compare string1 to string2'''
	if string1 < string2:
		return -1
	elif string1 > string2:
		return 1
	else:
		return 0





