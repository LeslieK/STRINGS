from KeyIndexedCounting import SuffixArray
from KnuthMorrisPratt import KMP
import StringUtils

def LRS(text, k=2, L=2):
	'''returns lrs that is repeated k or more times with length >= L'''
	N = len(text)
	sa = SuffixArray(text)

	maxlen = 0
	indices = set()  # indexes into original string
	counts = {}
	for i in range(1, N):
		length = sa.lcp(i)
		if length > maxlen:
			# found first lrs
			maxlen = length
			indices.clear()
			counts.clear()
			lrs = sa.select(i)[:maxlen]
			counts[lrs] = 2
			indices.add(sa.index(i))
			indices.add(sa.index(i - 1))
		elif (length == maxlen):
			# found another lrs with same length as current lrs
			lrs = sa.select(i)[:maxlen]
			if lrs in counts:
				counts[lrs] = counts[lrs] + 1
				indices.add(sa.index(i))
			else:
				# add lrs to dict
				counts[lrs] = 2
				indices.add(sa.index(i))
				indices.add(sa.index(i - 1))
	for key in counts:
		if counts[key] >= k:
			if len(key) >= L:
				print key, len(key)
	print counts
	print indices

def stringFreq(text, kgram):
	'''returns number of times the kgram (i.e., pattern) appears in text'''
	pass

def circularLinear(text):
	'''returns smallest circular string linearization of text'''
	sa = SuffixArray(text, rotated=True)
	return sa.select(0)

def ngram(text, n, maxfreq=True):
	'''find all frequency of all n-grams in text'''
	results = []
	n_dict = {}
	for i in range(len(text) - n + 1):
		pat = text[i:i + n]
		kmp = KMP(pat)
		results = kmp.findall(text)
		n_dict[pat] = (len(results), results)
	if maxfreq:
		return max(n_dict.items(), key=lambda (x, y): y)
	return n_dict

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
				length = StringUtils.lcp(str1[:j], str2)
				index1 = sa.index(i - 1)
				index2 = sa.index(i) - len(s) - 1
			else:
				j = str2.find(sentinel)
				length = StringUtils.lcp(str1, str2[:j])
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