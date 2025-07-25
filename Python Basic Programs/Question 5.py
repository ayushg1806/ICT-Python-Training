#Reverse the word
word = input("Enter a word: ")
reversedWord = ''
for ch in word:
    reversedWord = ch + reversedWord
print("Reversed word:", reversedWord)