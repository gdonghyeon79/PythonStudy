vowels = set('aeiou')
word = input("Provide a word to search for vowels :")
i = vowels.intersection(set(word))
for vowel in i:
    print(vowel)