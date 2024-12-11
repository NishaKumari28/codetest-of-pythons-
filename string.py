#1. Write a Python program to count the occurrences of each word in a given sentence string = “To change the overall look of your document. To change the look available in the gallery”
def count_word_occurrences(sentence):
    words = sentence.split()
    word_counts = {}
    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

sentence = "To change the overall look of your document. To change the look available in the gallery"
word_counts = count_word_occurrences(sentence)
for word, count in word_counts.items():
    print(f"{word}: {count}")

    

#2. Write a Python program to remove a newline in Python String = "\nBest \nDeeptech \nPython \nTraining\n"
def remove_newlines(input_string):
    return input_string.replace("\n", "")

input_string = "\nBest \nDeeptech \nPython \nTraining\n"
output_string = remove_newlines(input_string)
print(output_string)



#3. Write a Python program to reverse words in a string String = “Deeptech Python Training”
def reverse_words(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

input_string = "Deeptech Python Training"
output_string = reverse_words(input_string)
print(output_string)


#4. Write a Python program to count and display the vowels of a given text String=”Welcome to python Training
def count_vowels(input_string):
    vowels = "aeiou"
    input_string = input_string.lower()
    vowel_counts = {}
    for vowel in vowels:
        vowel_counts[vowel] = input_string.count(vowel)
    return vowel_counts

input_string = "Welcome to python Training"
vowel_counts = count_vowels(input_string)
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")





