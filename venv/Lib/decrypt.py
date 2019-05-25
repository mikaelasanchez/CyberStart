import zipfile
import itertools
import time

# Function for extracting zip files to test if the password work
def extractFile(zip_file, password):
    try:
        zip_file.extractall(pwd=password)
        return True
    except KeyboardInterrupt:
        exit(0)

# Main code starts here
# The file name of the zip file.
zipfilename = 'data.zip'

# The first part of the password.
first_half_password = 'Cola'

# These are the characters we will use for the brute force attack
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
zip_file = zipfile.ZipFile(zipfilename)

# We know they always have 3 characters after the first half of the password
# For every possible combination of 3 letters from alphabet,
for c in itertools.product(alphabet, repeat=3):

    # Add the three letters to the first half of the password.
    password = first_half_password+''.join(c)

    # Try to extract the file.
    print("Trying: %s" % password)

    # If the file was extracted, the right password was found
    if extractFile(zip_file, password):
        print('*' * 20)
        print('Password found: %s' % password)
        print('Files extracted...')
        exit(0)

# If no password was found by the end, let us know
print('Password not found.')
