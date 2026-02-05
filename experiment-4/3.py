#Input a sentence and print words in separate lines.

sentence = input("Enter a sentence: ")
word = sentence.split()
for word in word:
  print(word)