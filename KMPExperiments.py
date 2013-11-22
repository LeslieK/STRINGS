import random
import string
from KnuthMorrisPratt import KMP

R = 256
alphabet = string.ascii_uppercase

def KMPExperiment(pat_len, text_len, times):
	'''look for random pattern in random text t times

	return avg number of compares
	'''
	pattern = []
	text = []
	

	# generate random pattern
	for i in range(pat_len):
		c = random.choice(alphabet)
		pattern.append(c)
	pattern = ''.join(pattern)

	# generate random text
	for i in range(text_len):
		c = random.choice(alphabet)
		text.append(c)
	text = ''.join(text)

	kmp = KMP(pattern)
	print pattern
	count = 0  # counts character compares
	for trial in range(times):
		offset = kmp.search(text)
		count += kmp.count
		kmp.count = 0
	print '{}, avg number of compares: {}'.format(offset, float(count)/times)
	#print text
	return text





