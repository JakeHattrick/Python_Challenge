import os
import re

file = os.path.join("para2.txt")

#gets file text
a = open(file,"r")
contents = a.read()

#removes line breaks
contents = contents.replace('\n',' ')

#gets all words
words = contents.split()
#gets all sentences
sents = re.split("(?<=[.!?]) +", contents)

#averages letter count in words
aWord = sum(len(word)for word in words)/len(words)
#averages words count in sentences
aSent = sum(len(sent.split())for sent in sents)/len(sents)

print ("Paragraph Analysis")
print ("---------------------")
print (f"Approximate Word Count: {len(words)}")
print (f"Approximate Sentence Count: {len(sents)}")
print ("Average Letter Count: {:.1f}".format(aWord))
print ("Average Sentence Length: {:.1f}".format(aSent))