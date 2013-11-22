import argparse
from KnuthMorrisPratt import KMP

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="filename of text", type=str)
parser.add_argument("pattern", help="pattern string", type=str)
args = parser.parse_args()

pat = args.pattern
kmp = KMP(pat)

with open(args.filename) as f:
	# set initial index into pattern
	pattern_index = 0
	offset = 0
	while True:
		c = f.read(1)
		if not c:
			print "End of file"
			break
		else:
			offset += 1
			pattern_index = kmp.stream(c, pattern_index)
			if pattern_index == len(pat):
				print "match found  offset: {}".format(offset)
				break

