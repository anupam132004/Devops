#! /usr/bin/python3

fname = open("wordcount","r")
sentence = fname.read()

print(sentence)

words = sentence.split()
print(words)

counts = dict()
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)
fname.close()
