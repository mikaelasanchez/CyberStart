# Open a file called newfile.txt in /tmp. If no file exists it will be
# created.
# The "w" is the mode, in this case "w" is for write. You could use "r"
# for read.
myfile = open("/tmp/newfile.txt", "w")

# Write "Here is my message\n" to the file you opened. \n is a
# newline character.
myfile.write("Here is my message.\n")
myfile.write("Here is my second message.")

# Close the file
myfile.close()


# There are many different modes for opening a file in Python:
# w - Allows you to write to a file only. If the file exists, it will
# be overwritten.
# r - Allows you to read the file only.
# r+ - Allows you to read and write to the file.
# w+ - Allows you to read and write to the file, but if the file
# already exists it will overwrite it.
# a - Allows you to append to the file
# (write to the end of an existing file)
# a+ - Allows you to append to the file, and read from the file.

# Read the file and print to console
myfile = open("/tmp/newfile.txt", "r")
filecontents = myfile.read()
print(filecontents)
myfile.close()

# The major benefit of using 'with' is that it handles closing the
# file for you.
# For loop to read the file line by line.
with open("/tmp/newfile.txt", "r") as myfile:
    for line in myfile:
        print(line)


