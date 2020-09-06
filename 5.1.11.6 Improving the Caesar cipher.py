
def encrypt(text, key):

    try:
        Encoded_Text = ""
        for i in range(len(text)):
            char = text[i]
    # Encrypt uppercase characters in text
            if (char.isupper()):
                Encoded_Text += chr((ord(char) + int(key) - 65) % 26 + 65)

            elif char.isdigit() or char == " ":
                Encoded_Text += chr(ord(char))
            # Encrypt lowercase characters in text
            else:

                Encoded_Text += chr((ord(char) + int(key) - 97) % 26 + 97)
    except ValueError:
        print("the shift key must be an integer number ")
        # Recall the function..
        encrypt(input("Enter the text : "), input(
            "Enter a valid shift value : "))

    # prints out the encoded text.
    print(Encoded_Text)


# call the function
encrypt(input("Enter the text : "), input("Enter the shist value : "))
