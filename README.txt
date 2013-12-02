KnuthMorrisPratt.py: implementation of the KMP algorithm to search for a string (the pattern) in a text without backing up in the text.

KeyIndexedCounting.py: 
implementation of radix sort algorithms
implementation of a Suffix Array from an input string (aka text)

StringUtils.py:
some general utility string functions

Some Client scripts:
LRS_script.py: 
1 arg: filename: parses filename, reads in text, then finds lrs

LongestRepeatedString.py:
1 arg: filename: parses filename, reads in text; client can call functions on text; ie LRS(text)

LRS_functions.py:
a module of various functions; functions require that data is preprocessed into 
a sorted suffix array

TwitterStrings.py:
a script that needs your twitter credentials and 
the twitter ids of people you follow and words/phrases that you track
This script demos KNUTH-MORRIS-PRATT matching algorithm in a streaming feed
update the script with your creds, enter your own pattern to search, and run the script!

KMPExperiments.py
calculates random number of compares for matching a random string in random text
