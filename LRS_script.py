'''
parses filename, reads in text, then finds lrs
'''

import argparse
from KeyIndexedCounting import SuffixArray
import time

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

start = time.time()
maxlen = 0
indices = set()  # indexes into original string
counts = {}
for i in xrange(1, N):
	length = sa.lcp(i)
	if length > maxlen:
		maxlen = length
		indices.clear()
		counts.clear()
		lrs = sa.select(i)[:maxlen]
		counts[lrs] = 2
		indices.add(sa.index(i))
		indices.add(sa.index(i - 1))
	elif (length == maxlen):
		# another lrs with same length as earlier one found
		lrs = sa.select(i)[:maxlen]
		if lrs in counts:
			counts[lrs] = counts[lrs] + 1
			indices.add(sa.index(i))
		else:
			# add lrs to dict
			counts[lrs] = 2
			indices.add(sa.index(i))
			indices.add(sa.index(i - 1))
print time.time() - start
print len(lrs)
print counts
print indices