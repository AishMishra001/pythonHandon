# Counter : 

from collections import Counter 

string = "adfdastfewagdsadsdadfadsfsrdasDSA"

counts = Counter(string) 


print(counts)  # output : Counter({'d': 7, 'a': 6, 's': 6, 'f': 5, 't': 3, 'r': 3, 'w': 2, 'g': 1, 'A': 1, 'S': 1, 'D': 1})
print(counts['a']) # output : 6
print(counts.most_common(5)) # output : [('d', 7), ('a', 6), ('s', 6), ('f', 5), ('t', 3)]




# When to use it: Anagram problems (e.g., Counter(s) == Counter(t) checks if two strings are anagrams in a single line) or whenever you immediately need the frequency of every element in an array.