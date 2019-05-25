# A regular expression or regex for short is a way of searching text
# for a pattern.

# Import the 're' library:
import re

# Set pattern and text
pattern = "flag"
text = "The flag is: this is a fake flag: bajhdasdohaudsnasdaasd"

# Find every instance of 'flag' in the text
if re.findall(pattern, text):
    print("Found match!")

# In this case, we managed to extract the flag from the text provided.
pattern = "flag: (.*)"
data = re.findall(pattern, text)
print(data[0])


# The key is the pattern: flag: (.*).
# First we're looking for any text that starts with Flag:
# The brackets surround the bit we want to extract. We know the flag
# we want to get comes after flag: so the brackets are after flag:.
# The . inside the brackets means match any character.
# The * means any number of times.
# So put it together and you're extracting any series of characters
# after the word flag: .

# What re.findall returns is an array. That's because it find all
# possible matches, so if there was more than one match, it would
# put them in the other positions in the array.
# For example data[1] for the second match, data[2] for the third
# match and so on...
#
# You can find out how to do more things with it at:
# https://regexone.com/

html = """
<html>
<head>
    <title>Regex Demo</title>
</head>
<body>
    <div class='firstDiv'>Hello</div>
    <div class='secondDiv'>Hello</div>
</body>
</html>
"""

# Regex search that extracts all the classes from
# the divs and saves them into an array.

pattern = "<div class='(.*)'>"
classes = re.findall(pattern, html)

# Loop that goes through the array and prints the contents.

for c in range(0, len(classes)):
  print(classes[c])
