# checks whether the entered text is a palindrome, and prints result.

text0 = input("Enter text, please: ")
text1 = text0.replace(' ', '').upper()

if (text1 == text1[::-1]):
    print("It's palindrome")
else:
    print("It's not a palindrome")
