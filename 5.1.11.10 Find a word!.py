word = input("Enter the word: ").upper()
text = input("Enter the text: ").upper()

found = True
start = 0

for char in word:
    pos = text.find(char, start)
    if pos < 0:
        found = False
        break
    start = pos + 1
if found:
    print("Yes")
else:
    print("No")
