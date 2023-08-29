"""
Exercise 1:
Write a program that takes a list of numbers and prints the sum of all the numbers in the list.
"""
numbers = [5, 4, 9, 10, 3, 10, 5, 2]
numbers_total = 0
for number in numbers:
    numbers_total += number
print(numbers_total)

"""
Exercise 2:
Write a program that takes a list of strings and prints the length of each string in the list.
"""
list_of_words = ["aap", "noot", "mies", "school"]
for word in list_of_words:
    print(len(word))

"""
Exercise 3:
Write a program that prompts the user to enter 5 names and stores them in a list. Then, print the list in alphabetical order.
HINT: Use a range(5) with a for loop to loop 5 times
HINT: To get user input and store it in a variable: name = input("Enter a name: ") 
"""
# names_collected = []
# for number in range(1, 6):
#     name = input(f"Please enter name {number}:" )
#     names_collected.append(name)
# print(sorted(names_collected))
"""
Exercise 4:
Write a program that takes a list of numbers and prints the largest and smallest numbers in the list.
HINT: min and max are built-in Python functions
"""
print(min(numbers))
print(max(numbers))
"""
Exercise 5:
Write a program that takes a list of integers and prints the average of the numbers in the list.
"""
print(numbers)
numbers_length = len(numbers)
print(f"the average of {numbers_total} / {numbers_length} is: ")
print(numbers_total / numbers_length)

"""
Exercise 6:
Write a program that takes a list of integers and removes all the duplicates, printing the updated list.
HINT: Python's in-built set function will remove duplicates from a list
"""
print(set(numbers))

"""
Exercise 7:
Write a program that prompts the user to enter a sentence and prints the sentence in reverse order.
"""
sentence = input("Please give me a sentence ")
words_in_sentence = sentence.split()
words_in_sentence.reverse()
print(words_in_sentence)
"""
BONUS CHALLENGE!
Write a program that prompts the user to enter a sentence and counts the frequency of each word in the sentence using a dictionary.
HINT: Python's split() method will turn a set into a List
"""
sentence2 = input("Please give me another sentence ")
words = sentence2.split()
unique_words = set(words)
for word in unique_words:
    word_count = words.count(word)
    print(f"You used {word} {word_count} times")