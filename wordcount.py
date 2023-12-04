"""Docstring (instructions/what it does): Count words in file. Count how many times the word appears in the file."""

data = open("test.txt")

word_counts = {}

for line in data:
    #strip then split, left to right in order - take off white space first and then split 
    words = line.rstrip().split(" ")
    for word in words:
       word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts.items())

#print(f"For {word}, the count, the amount of times this appears in the file is: {}")