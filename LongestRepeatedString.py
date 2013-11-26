from KeyIndexedCounting import SuffixArray
import StringUtils
from KnuthMorrisPratt import KMP
import time
import argparse

'''
parses filename arg, reads it in

includes methods that take text param
'''

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="text file of string data", type=str)
args = parser.parse_args()

with open(args.filename) as f:
	t = f.read()

text = t
N = len(text)
print 'done reading file', N

start = time.time()
sa = SuffixArray(text, sort=True)
elapsed = time.time() - start
print elapsed

def LRS(text, k=2, L=2):
	'''returns lrs that is repeated k or more times with length >= L'''
	N = len(text)
	start = time.time()
	sa = SuffixArray(text)
	print time.time() - start

	maxlen = 0
	indices = set()  # indexes into original string
	counts = {}
	for i in xrange(1, N):
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

