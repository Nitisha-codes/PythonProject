# To check if the given string or word is palindrome or not

word = input("Enter a word: ")
rev = word[::-1]
print(f"Since, the reverse of {word} is {rev} ")
if word == rev:
    print("Your word is  a palindrome.")
else:
    print("Your word is not a palindrome.")


