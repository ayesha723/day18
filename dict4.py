line=input("Enter a line i will count how many times a word is repeating")

words=line.split()
word_count={}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word]=1

print(word_count)