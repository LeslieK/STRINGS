import argparse
from KnuthMorrisPratt import KMP

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="filename of text", type=str)
parser.add_argument("pattern", help="pattern string", type=str)
args = parser.parse_args()

# read text from file
with open(args.filename) as f:
	text = f.read()

#print "text:    ", text
pat = args.pattern
# preprocess pattern
#pat = pat.lower()
#pat = ' '.join(pat.split())

kmp = KMP(pat)
offset = kmp.search(text)
print offset
#print "pattern: ",
if offset < len(text):
	print text[offset - 500], pat, text[offset + 20 + len(pat) + 500]
else:
	print pat, 'not found'

# find all occurrences
offsets = kmp.findall(text)