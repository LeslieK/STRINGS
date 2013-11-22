from KeyIndexedCounting import SuffixArray
from KeyIndexedCounting import Quick3string

# texts = ["atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaac", 
# "ctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca",
#    "cggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgactt",
#    "gtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggatt",
#    "acgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttagga",
#    "tagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaat",
#    "tgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaag",
#    "atcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtt",
#    "tccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc",
# 	"atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaac"]

texts = ["ATCCATATTTGTCGTATGTATGTAATTTACGACGTGTATGTAAATCCATAATCCATAATCCATATGTATGTAATGTATGTAATTTACGACGATCCATATGTATGTAAATCCATAATCCATATTTACGACGTTTGTCGTAATCCATATGTATGTAAGGTTTGCGGTTTGCATCCATATGTATGTAATTTGTCGTAATCCATATGTATGTAAATCCATAGGTTTGCATCCATAATCCATATTTGTCGTAATCCATAATCCATATTTGTCGTATTTACGACGTTTACGACGATCCATAATCCATAATCCATATGTATGTAATTTGTCGTATGTATGTAAATCCATATTTGTCGTAGGTTTGCATCCATAATCCATAATCCATATTTACGACGTGTATGTAAATCCATATTTACGACGATCCATATTTGTCGTATTTGTCGTAATCCATAATCCATATTTGTCGTAATCCATATTTGTCGTATTTGTCGTATTTACGACGGGTTTGCTTTACGACGTTTGTCGTAGGTTTGCTTTACGACGTGTATGTAAATCCATATTTACGACGATCCATAGGTTTGCTTTGTCGTATTTACGACGTTTGTCGTATGTATGTAAATCCATATGTATGTAATTTACGACGATCCATAATCCATATTTACGACGGGTTTGCTTTACGACGTTTGTCGTAATCCATAATCCATATTTGTCGTATTTGTCGTAGGTTTGCGGTTTGCATCCATATTTGTCGTATTTGTCGTAATCCATATTTGTCGTAATCCATAGGTTTGCTTTGTCGTAGGTTTGCTTTGTCGTAGGTTTGCTTTACGACGGGTTTGCATCCATATTTGTCGTATTTGTCGTAGGTTTGCGGTTTGCGGTTTGCTTTGTCGTATGTATGTAAGGTTTGCTTTACGACGGGTTTGCTTTGTCGTATTTACGACGTGTATGTAATGTATGTAA"]

for text in texts:	
	N = len(text)
	sa = SuffixArray(text)
	q3 = Quick3string(sa.suffixes)
	sortedArray = q3.sort()

	lrs = ''
	maxlen = 0
	for i in range(1, N):
		length = sa.lcp(i)
		if (length > maxlen):
			maxlen = length
			lrs = sa.select(i)[0:maxlen]
	print 'longest repeated string: {}, {}'.format(lrs, len(lrs))



 #"ATCCATAATCCAT" . 12) ("TCCATAATCCATA" . 12)))
