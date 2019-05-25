# As you know, computers only think in numbers. That means, when it
# comes to dealing with text, the computer has to have some way of
# converting numbers into letters. This is a form of encoding.

# The most common form of encoding is ASCII. In ASCII, a specific
# number maps to a letter. So for example, the number 65 is a capital
# A.

# Sometimes we need to be able to convert between the number a letter
# represents and the letter itself.

num = 65

# chr allows us to convert a decimal number to it's ASCII value.
char = chr(num)
# ord allows us to convert the ASCII character to it's decimal value.
dec = ord(char)

print("Character: " + char + ", Decimal: " + str(dec))

# CHALLENGE 1: Write a loop that prints the ASCII characters of all
#              the decimal values between the range 49 and 127

for x in range(49, 128):
    print(chr(x))
