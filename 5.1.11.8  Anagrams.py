# checks whether, the entered texts are anagrams and prints the result
text1 = input("Enter the first text: ")
text2 = input("Enter the second string: ")
ls_text1 = list(text1.replace(' ', '').upper())
ls_text1.sort()
ls_text2 = list(text2.replace(' ', '').upper())
ls_text2.sort()

if (ls_text1 == ls_text2):
    print("Anagrams")
else:
    print("Not anagrams")
