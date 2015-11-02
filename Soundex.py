#
# Python Soundex Implementation
# 
# Version 1.0
# 
# Copyright 2015 Stefan Reich
#
# Licensed under the MIT license
#

import re

print("Enter string to index")

input_string = input()

# Initialize the end result with the first letter of the input string
soundex_result = input_string[0].upper()

# Remove all instances of h's and w's, since letters with like values
# are all treated similar when they are adjacent or separated only by
# h's and w's. This will make our later regex operations simpler.
input_string = re.sub('[hw]', '', input_string, flags=re.I)

# Replace all valued consonants with their respective values. Adjacent
# valued consonants are treated as one consonant.
input_string = re.sub('[bfpv]+', '1', input_string, flags=re.I)
input_string = re.sub('[cgjkqsxz]+', '2', input_string, flags=re.I)
input_string = re.sub('[dt]+', '3', input_string, flags=re.I)
input_string = re.sub('l+', '4', input_string, flags=re.I)
input_string = re.sub('[mn]+', '5', input_string, flags=re.I)
input_string = re.sub('r+', '6', input_string, flags=re.I)

# This transformed string still contains the first letter, so remove
# its value from the string.
input_string = input_string[1:]

# Now remove all vowels and y's from the string.
input_string = re.sub('[aeiouy]','', input_string, flags=re.I)

# Take the first 3 digits of the transformed string and append them to the result
soundex_result += input_string[0:3]

# Soundex results are supposed to have an opening letter followed by three digits.
# If there are less than 4 characters total, append with zeros until there are 4.
if len(soundex_result) < 4:
    soundex_result += '0'*(4-len(soundex_result))

print(soundex_result)

print("Press any key to exit")
input()