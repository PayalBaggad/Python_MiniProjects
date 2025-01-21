# A program to count words in a user-input sentence.

def word_counter():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print(f"Total words: {len(words)}")

word_counter()

'''
Explanation:
1. The program takes a sentence as input.
2. It splits the sentence into words using the split method.
3. The total number of words is calculated using len.
'''
