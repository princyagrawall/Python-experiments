#Program to count number of unique words in a given sentence using sets.

sentence = input("enter a sentence: ")
word = sentence.lower().split()
unique_words=set(word)

print("unique words",unique_words)

print("number of unique words: ",len(unique_words))
