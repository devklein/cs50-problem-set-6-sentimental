import sys
from cs50 import get_string

# Check user if user provided exactly one argument
if len(sys.argv) == 1:
    print("You did not enter an argument for the encryption key.")
    print("Please restart the program with one non negative integer in the command-line-argument.")


elif len(sys.argv) > 2:
    print("You did enter more than one argument for the encryption key.")
    print("Please restart the program with one non negative integer in the command-line-argument.")


# declare key variable as an int from string provided as command-line-argument
key = int(sys.argv[1])

# prompt user for plaintext string
plain = get_string("plaintext: ")

# print ciphertext
print("ciphertext: ", end="")

for char in plain:
    # check vor uppercase letter
    if char.isupper():
        print("{}".format(chr((ord(char) - ord("A") + key) % 26 + ord("A"))), end="")
    # check vor uppercase letter
    elif char.islower():
        print("{}".format(chr((ord(char) - ord("a") + key) % 26 + ord("a"))), end="")
    # print all other input
    else:
        print("{}".format(char), end="")
print()