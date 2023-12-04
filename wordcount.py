"""Docstring (instructions/what it does): Count words in file. Count how many times the word appears in the file."""

data = open("test.txt")

word_counts = {}

for line in data:
    #strip then split, left to right in order - take off white space first and then split 
    words = line.rstrip().split(" ")
    for word in words:
       # word is in brackets, because it is pointing to the dictionary and dictionary do not have indices the same way as lists - instead of referencing an index, it is referencing element that it indirectly assigned to that variable in the for loop
       word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts.items())