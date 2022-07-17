# Homework 1- Caesar Cipher Code Breaker
# CSCI 4742
# Sebastian Barry

# main function requests user input as ciphertext, and begins to generate cipher
# possibilities and guess them until the user identifies it is correct
def main():
    guessed = "n"
    shift = 0
    
    ciphertext = input("Enter ciphertext: ").lower()
    print("Output (y for yes, n for no)")
    while(guessed != "y"):
        shift += 1
        nextGuess = shift_text(ciphertext, shift)
        print("Is it \"" + nextGuess + "\"?")
        guessed = input(">> ").lower()
    print(nextGuess)
    return nextGuess

# shift_text function takes in a string and an int shift value and returns a string
# that is the equivalent string with all characters shifted the requested amount
# (z goes back around to a) (non-characters stay as non-characters)
def shift_text(text, shift_value):
    textarray = list(text)
    newtextarray = []
    for c in textarray:
        cc = ord(c) + shift_value
        if cc > 122:
            cc = 96 + (cc - 122)
        elif cc < 97:
            cc = ord(c)
        newtextarray.append(chr(cc))
    newtext = "".join(newtextarray)
    return newtext

main()