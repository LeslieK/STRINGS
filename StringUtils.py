R = 4 # number of character values in alphabet
CUTOFF = 0 # length of string when insertion sort is used (instead of some other string sorting method)

from KeyIndexedCounting import SuffixArray

def exch(a_sequence, i, j):
	'''exchange values a_sequence[i] and a_sequence[j]'''
	swap = a_sequence[i]
	a_sequence[i] = a_sequence[j]
	a_sequence[j] = swap
	return a_sequence

# def exch(alist, i, j):
# 	'''exchange alist[i] and alist[j]'''
# 	swap = alist[i].offset
# 	alist[i].offset = alist[j].offset
# 	alist[j].offset = swap
# 	return alist

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

def insertion(a, lo, hi, d):
	'''sort from a[lo] to a[hi], starting from the dth character'''
	for i in range(lo, hi + 1):
		# a[i] is a string
		for j in range(i, lo, -1):
			# j is an index into the string a[i]
			if less(a[j], a[j - 1], d):
				exch(a, j, j - 1)

def less(string1, string2, d):
	return string1[d:] < string2[d:]


def charsfromfile(f):
	'''a generator for reading a buffered file'''
	while True:
		a = array.array('c')
		a.fromstring(f.read(1000))
		if not a:
			break
		for x in a:
			yield x

def LCS(file1, file2):
	'''returns longest common substring between the files'''
	with open(file1) as f1:
		s = f1.read()

	with open(file2) as f2:
		t = f2.read()

	sentinel = chr(24)
	st = s + sentinel + t  # chr(24) is ascii CAN (Cancel)
	sa = SuffixArray(st)

	maxlen = 0
	indices = set()  # indexes into original string
	counts = {}
	for i in xrange(2, len(st)):
		str1 = sa.select(i-1)
		str2 = sa.select(i)
		b1 = sentinel in set(str1)
		b2 = sentinel in set(str2)
		if (b1 or b2) and (not (b1 and b2)):
			if b1:
				# get index of sentinel in string1
				j = str1.find(sentinel)
				length = lcp(str1[:j], str2)
				index1 = sa.index(i - 1)
				index2 = sa.index(i) - len(s) - 1
			else:
				j = str2.find(sentinel)
				length = lcp(str1, str2[:j])
				index1 = sa.index(i - 1) - len(s) - 1
				index2 = sa.index(i)

			# process length
			if length > maxlen:
				# found first lrs
				maxlen = length
				indices.clear()
				counts.clear()
				lrs = sa.select(i)[:maxlen]
				counts[lrs] = 2
				indices.add(index1)
				indices.add(index2)
			elif (length == maxlen):
				# found another lrs with same length as current lrs
				lrs = sa.select(i)[:maxlen]
				if lrs in counts:
					# another repeat of current lrs
					counts[lrs] = counts[lrs] + 1
					indices.add(index1)
					indices.add(index2)
				else:
					# add lrs to dict
					counts[lrs] = 2
					indices.add(index1)
					indices.add(index2)
	print counts
	print indices