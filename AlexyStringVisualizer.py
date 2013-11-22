import json
 
class RecString(str):
    def __init__(self, text):
        self.steps = [text]
        self.index = 0
    
    def __eq__(self, other):
        if other is '':
            return not len(self)
        
        if len(self) != 1 or len(other) != 1 or not isinstance(other, RecString):
            self.error()
        
        equal = str.__eq__(self, other)
        self.steps.append(['c', self.index, other.index, 1 if equal else 0])
        return equal
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __getitem__(self, *args):
        if (len(args) > 1):
            self.error()
        else:
            return self.baby(str.__getitem__(self, *args), args[0])
            
    def __getslice__(self, *args):
        self.error()
        
    def lower(self):
        return self.baby(str.lower(self), self.index)
        
    def upper(self):
        return self.baby(str.upper(self), self.index)
    
    def baby(self, text, index):
        baby = RecString(text)
        baby.steps = self.steps
        baby.index = index
        return baby
    
    def error(self):
        raise Exception("""
        Please access only individual characters: e.g. text[a]
        Comparisons such as text == text[::-1] are O(n),
        do them explicitly one character at a time.
        """)
    
    def get_recording_link(self):
        return ('http://explored.tk/experiments/palindrome#[%s]' %
                json.dumps(self.steps, separators=(',',':')))

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    text, N = text.lower(), len(text)
    pals = [(i,i) for i in range(N+1)] + [(i,i+1) for i in range(N)]
    while True:
        new_pals = [(i-1, j+1) for i, j in pals
                    if 0 < i and j < N and text[i-1] == text[j]]
        if not new_pals: break
        pals = new_pals
    return max(pals, key=lambda (i, j): j - i)

text = RecString('RacecarX')
longest_subpalindrome_slice(text)
print text.get_recording_link()

http://explored.tk/experiments/palindrome#[["RacecarX",["c",0,1,0],["c",1,2,0],["c",2,3,0],["c",3,4,0],["c",4,5,0],["c",5,6,0],["c",6,7,0],["c",0,2,0],["c",1,3,0],["c",2,4,1],["c",3,5,0],["c",4,6,0],["c",5,7,0],["c",1,5,1],["c",0,6,1]]]