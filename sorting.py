input = input("enter the words: ")

words = input.split()
words = [w.lower() + w for w in words]
words.sort()
words = [w[len(w)//2:] for w in words]
print(' '.join(words))
