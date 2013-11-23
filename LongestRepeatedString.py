from KeyIndexedCounting import SuffixArray

texts = [
"atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaac", 
 "ctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca",
   "cggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgactt",
   "gtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggatt",
   "acgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttagga",
   "tagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaat",
   "tgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaag",
   "atcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtt",
   "tccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc"]

#texts = ["ATCCATATTTGTCGTATGTATGTAATTTACGACGTGTATGTAAATCCATAATCCATAATCCATATGTATGTAATGTATGTAATTTACGACGATCCATATGTATGTAAATCCATAATCCATATTTACGACGTTTGTCGTAATCCATATGTATGTAAGGTTTGCGGTTTGCATCCATATGTATGTAATTTGTCGTAATCCATATGTATGTAAATCCATAGGTTTGCATCCATAATCCATATTTGTCGTAATCCATAATCCATATTTGTCGTATTTACGACGTTTACGACGATCCATAATCCATAATCCATATGTATGTAATTTGTCGTATGTATGTAAATCCATATTTGTCGTAGGTTTGCATCCATAATCCATAATCCATATTTACGACGTGTATGTAAATCCATATTTACGACGATCCATATTTGTCGTATTTGTCGTAATCCATAATCCATATTTGTCGTAATCCATATTTGTCGTATTTGTCGTATTTACGACGGGTTTGCTTTACGACGTTTGTCGTAGGTTTGCTTTACGACGTGTATGTAAATCCATATTTACGACGATCCATAGGTTTGCTTTGTCGTATTTACGACGTTTGTCGTATGTATGTAAATCCATATGTATGTAATTTACGACGATCCATAATCCATATTTACGACGGGTTTGCTTTACGACGTTTGTCGTAATCCATAATCCATATTTGTCGTATTTGTCGTAGGTTTGCGGTTTGCATCCATATTTGTCGTATTTGTCGTAATCCATATTTGTCGTAATCCATAGGTTTGCTTTGTCGTAGGTTTGCTTTGTCGTAGGTTTGCTTTACGACGGGTTTGCATCCATATTTGTCGTATTTGTCGTAGGTTTGCGGTTTGCGGTTTGCTTTGTCGTATGTATGTAAGGTTTGCTTTACGACGGGTTTGCTTTGTCGTATTTACGACGTGTATGTAATGTATGTAA"]

#texts = ["ACAACTATGCATACTATCGGGAACTATCCT"] # lrs: "ACTAT", count = 3  kmp = KMP("ACTAT") kmp.findall(texts)

#texts = ["CGATATATCCATAG"]  # lrs: "ATA", count = 3

#texts = ["AAABBAAAABCAA"]
text = ''.join(texts)

N = len(text)
sa = SuffixArray(text)

# maxlen = 0
# for i in range(1, N):
# 	length = sa.lcp(i)
# 	if length > maxlen:
# 		maxlen = length
# 		lrs = sa.select(i)[:maxlen]
# 		indices = (sa.index(i), sa.index(i-1))
# print 'longest repeated string: {}, len: {}, indices: {}'.format(lrs, len(lrs), indices)
# print text

maxlen = 0
indices = set()  # indexes into original string
counts = {}
for i in range(1, N):
	length = sa.lcp(i)
	if length > maxlen:
		maxlen = length
		indices.clear()
		counts.clear()
		lrs = sa.select(i)[:maxlen]
		counts[lrs] = 1
		indices.add(sa.index(i))
		indices.add(sa.index(i - 1))
	if (length == maxlen):
		# another lrs with same length as earlier one found
		lrs = sa.select(i)[:maxlen]
		if lrs in counts:
			counts[lrs] = counts[lrs] + 1
			indices.add(sa.index(i))
			indices.add(sa.index(i - 1))
		else:
			# add lrs to dict
			counts[lrs] = 1
			indices.add(sa.index(i))
			indices.add(sa.index(i - 1))
print len(lrs)
# sort by counts
print counts.items()
print indices