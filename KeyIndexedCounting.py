import StringUtils

class KeyIndexedSort(object):
	'''sort keys of small integers'''
	def __init__(self, alist):
		self.count = [0] * (StringUtils.R + 1)
		self.aux = [0] * len(alist)

		# store the frequency of each key
		for i in alist:
			self.count[i + 1] += 1

		# store the cumulative total of keys
		# count[r + 1] contains the number of keys less than r
		# r is a character in alphabet
		for r in range(StringUtils.R):
			self.count[r + 1] += self.count[r]

		# distribute keys into aux list, in sorted order
		for i in range(len(alist)):
			self.aux[self.count[alist[i]]] = alist[i]
			self.count[alist[i]] += 1

	def sort(self):
		return self.aux

class LSDSort(object):
	'''sort a list of fixed-length strings'''

	def __init__(self, alist, W):
		'''sort a list of integers of width W'''
		self.alist = alist

		for d in range(W-1, -1, -1):
			count = [0] * (StringUtils.R + 1)
			aux = [0] * len(self.alist)

			# store the frequency of each key
			# key is dth character of integer n
			for i in self.alist:
				count[ord(i[d]) + 1] += 1

			# store the cumulative total of keys
			# count[r + 1] contains the number of keys less than r
			# r is a character in alphabet
			for r in range(StringUtils.R):
				count[r + 1] += count[r]

			# move keys into aux list, in sorted order
			for i in range(len(self.alist)):
				aux[count[ord(self.alist[i][d])]] = self.alist[i]
				count[ord(self.alist[i][d])] += 1
			self.alist = aux[::]

	def sort(self):
		return self.alist

#alist = ['67890', '54321',  '45612', '12345']
#s = LSDSort(alist, 5)

class Quick3string(object):
	''' quick 3-way + MSD sort'''

	def __init__(self, alist):
		'''sort a sequence of strings'''
		self.alist = alist

	def _sort(self, lo, hi, d):
		'''sort a sequence of strings of unequal length'''

		if (hi <= lo + StringUtils.CUTOFF):
			StringUtils.insertion(self.alist, lo, hi, d)
			return;

		# if (hi <= lo):
		# 	return

		lt = lo
		gt = hi
		i = lo + 1
		# set parition character
		v = self._charAt(self.alist[lo], d)

		# make 3 paritions
		while(i <= gt):
			curr = self.alist[i]
			t = self._charAt(curr, d)
			if t < v:
				StringUtils.exch(self.alist, lt, i)
				lt += 1
				i += 1
			elif t > v:
				StringUtils.exch(self.alist, i, gt)
				gt -= 1
			else:
				i += 1
		
		# sort the lower partition
		self._sort(lo, lt - 1, d)

		# sort the middle partition on the next character
		if v >= 0:
			self._sort(lt, gt, d + 1)

		# sort the upper partition
		self._sort(gt + 1, hi, d)

	def _charAt(self, astring, d):
		'''return the dth character in a string'''

		if d < len(astring):
			return ord(astring[d])
		else:
			return -1

	def sort(self):
		self._sort(0, len(self.alist) - 1, 0)
		return self.alist


class Suffix(object):
	'''a string suffix'''
	def __init__(self, s, offset, rotated):
		self.offset = offset
		self.N = len(s)
		self.s = s
		self.rotated = rotated

	def __getitem__(self, i):
		if not self.rotated:
			return self.s[i + self.offset]
		else:
			return self.s[(i + self.offset) % self.N]

	def __getslice__(self, i, j):
		if not self.rotated:
			return self.s[i + self.offset:j + self.offset]
		else:
			return self.s[(i + self.offset) % self.N: (j + self.offset) % self.N]

	def length(self):
		if not self.rotated:
			return self.N - self.offset
		else:
			return self.N

	def __len__(self):
		if not self.rotated:
			return self.N - self.offset
		else:
			return self.N

	def __cmp__(self, that):
		'''compare two suffix objects'''
		if not self.rotated:
			maxoffset = max(self.offset, that.offset)
			shortest_string = self.N - maxoffset
		else:
			shortest_string = self.N
		for i in range(shortest_string):
			if self[i] < that[i]:
				return -1
			elif self[i] > that[i]:
				return 1
		return 0

	def __repr__(self):
		if not self.rotated:
			return self.s[self.offset:]
		else:
			return self.s[self.offset:] + self.s[:self.offset]

class SuffixArray(object):
	''' an array of string suffixes'''
	def __init__(self, text, sort=True, rotated=False):
		'''build a suffix array of (random) text'''
		self.text = text
		self.N = len(text)
		self.suffixes = [Suffix(text, i, rotated=rotated) for i in range(self.N)]

		# sort suffix array (what sort algorithm is used?)
		#suffixes.sort
		# MSD radix sort + 3-way quicksort
		
		if sort:
			#self.suffixes.sort()
			q3 = Quick3string(self.suffixes)
			self.suffixes = q3.sort()


	def __getitem__(self, i):
		'''returns a suffix object'''
		return self.suffixes[i]

	def length(self):
		'''length of original text'''
		return self.N

	def select(self, i):
		'''return suffix string for suffix in suffixArray[i]'''
		return self.text[self[i].offset:]

	def index(self, i):
		'''index in original text where suffix i begins'''
		return self[i].offset

	def lcp(self, i):
		'''return longest common prefix between suffix[i] and suffix[i-1]'''
		assert(i > 0)
		# suffix objects
		min_length = min(self[i].length(), self[i - 1].length())
		for j in range(min_length):
			if self.select(i)[j] != self.select(i-1)[j]:
				return j
		return min_length

	def rank(self, key):
		'''number of suffixes strictly less than key'''
		# binary search
		lo = 0
		hi = self.N - 1
		while (lo <= hi):
			mid = lo + (hi - lo)/2
			if key < self.select[mid]:
				hi = mid - 1
			elif key > self.select[mid]:
				lo = mid + 1
			else:
				return mid
		# no match
		return lo



alist = [
"she",
"sells",
"seashells",
"by",
"the",
"sea",
"shore",
"the",
"shells",
"the",
"shells",
"she",
"sells",
"are",
"surely",
"seashells"
]







