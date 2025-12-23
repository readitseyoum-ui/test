#1
# for i in range(5):
#     for j in range(5):
#         print('*', end=' ')
#     print()  # move to the next line

# rows = 5

# for i in range(1, rows + 1):
#     print('*' * i)
# w = "maldon"
# c = 0
# while c < len(w):
#     print(w[c])
#     c += 1
# for i in range(len(w)):
#     print(w[i])
# sum = 0
# for i in range(1, 11):
#     sum += i
#     print(sum)
# print(sum)

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

# i = 1
# while i < 11:
#     if i%2 == 0:
#         print(i)
#     i += 1


## 1. Ask the user to input a sentence and count how many words it contains. Assume a word is separated by 
# exactly one space.

# user = input("Enter a sentence: ")
# word = user.split(" ")
# count = len(word)
# print("Number of words:", count)

## 2. Write a program that takes a word as input and asks the user how many times they want the word to be 
# repeated. Then, the program should print the word that many times, with each repetition separated by 
# a space, all on the same line.

# word = input("Enter a word: ")
# times = int(input("How many times do you want it repeated? "))

# for i in range(times):
#     print(word, end=" ")

# print("")

## 3. Write a program that counts how many vowels are in a given string. Make sure to get the 
# string from the user

# user = input("Enter a text: ")
# user2 = user.lower()
# count = 0
# v = "aeiou"
# for i in range(len(user2)):
#     if user2[i] in v:
#         count += 1
# print(count)


## 4. Ask the user to input a password. Print whether it is "Weak", "Medium", or "Strong" based on the following rules:
#     Weak: Less than 6 characters
#     Medium: 6-10 characters, only letters
#     Strong: More than 10 characters and contains letters and numbers
#password = input("Enter your password: ")

# if len(password) < 6:
#     print("Weak")
# elif len(password) > 10:
#     for i in password:
#         if i.isdigit():
#             print("Strong")          
# else:
#     print("Medium") 

# x = True
# while x:
#     if len(password) < 6:
#         print("Weak")
#         x = False
#     elif len(password) > 6 and len(password) < 10:
#         print("medium")
#         x = False
#     else:
#         print("Strong")
#         x = False
#6:
# Ask the user for the start and end of the range
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

total = 0  # variable to hold the sum

for num in range(start, end + 1):
    if num % 4 == 0:        # skip numbers divisible by 4
        continue
    if total + num > 100:   # stop if sum would exceed 100
        break
    print("Adding:", num)   # show each number being added
    total += num

print("Final sum:", total)
# Added for Git purpose
