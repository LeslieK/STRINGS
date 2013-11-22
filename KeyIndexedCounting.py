import StringUtils
import pdb

R = 10 # number of character values in alphabet

class KeyIndexedSort(object):
	'''sort a list of small integers'''
	def __init__(self, alist):
		self.count = [0] * (R + 1)
		self.aux = [0] * len(alist)

		# store the frequency of each key
		for i in alist:
			self.count[i + 1] += 1

		# store the cumulative total of keys
		# count[r + 1] contains the number of keys less than r
		# r is a character in alphabet
		for r in range(R):
			self.count[r + 1] += self.count[r]

		# distribute keys into aux list, in sorted order
		for i in range(len(alist)):
			self.aux[self.count[alist[i]]] = alist[i]
			self.count[alist[i]] += 1

	def sort(self):
		return self.aux

class LSDSort(object):
	'''sort a list of fixed-length integers'''

	def __init__(self, alist, W):
		'''sort a list of integers of width W'''
		self.alist = alist

		for d in range(W-1, -1, -1):
			count = [0] * (R + 1)
			aux = [0] * len(self.alist)

			# store the frequency of each key
			# key is dth character of integer n
			for i in self.alist:
				count[int(i[d]) + 1] += 1

			# store the cumulative total of keys
			# count[r + 1] contains the number of keys less than r
			# r is a character in alphabet
			for r in range(R):
				count[r + 1] += count[r]

			# move keys into aux list, in sorted order
			for i in range(len(self.alist)):
				aux[count[int(self.alist[i][d])]] = self.alist[i]
				count[int(self.alist[i][d])] += 1
			self.alist = aux[::]

	def sort(self):
		return self.alist

#alist = ['67890', '54321',  '45612', '12345']
#s = LSDSort(alist, 5)

class Quick3string(object):
	''' quick 3-way + MSD sort'''

	def __init__(self, alist):
		'''sort a list of integers'''
		self.alist = alist

	def _sort(self, lo, hi, d):
		'''sort a sequence of strings of unequal length'''

		if (hi <= lo):
			return
		lt = lo
		gt = hi
		i = lo + 1
		# set parition character
		v = self._charAt(self.alist[lo], d)

		# make 3 paritions
		while(i <= gt):
			curr_string = self.alist[i]
			t = self._charAt(curr_string, d)
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
		#pdb.set_trace()
		self._sort(0, len(self.alist) - 1, 0)
		return self.alist

class SuffixArray(object):
	def __init__(self, text):
		'''build a suffix array of (random) text'''
		self.N = len(text)
		self.suffixes = [1] * self.N

		for i in range(self.N):
			# build suffixes
			self.suffixes[i] = text[i:]
			#print self.suffixes[i]

		# sort suffix array (what sort algorithm is used?)
		#suffixes.sort
		# MSD radix sort + 3-way quicksort
		qs = Quick3string(self.suffixes)
		self.suffixes = qs.sort()

	def length(self):
		'''length of original text'''
		return self.N

	def select(self, i):
		'''return suffix array i'''
		return self.suffixes[i]

	def index(self, i):
		'''index in original text where suffix array i begins'''
		return self.N - len(self.suffixes[i])

	def lcp(self, i):
		'''return longest common prefix between suffix[i] and suffix[i-1]'''
		assert(i > 0)
		return StringUtils.lcp(self.suffixes[i], self.suffixes[i - 1])

	def rank(self, key):
		'''number of suffixes strictly less than key'''
		# binary search
		lo = 0
		hi = self.N - 1
		while (lo <= hi):
			mid = lo + (hi - lo)/2
			comp = StringUtils.compareTo(key, self.suffixes[mid])
			if comp < 0:
				hi = mid - 1
			elif comp > 0:
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







