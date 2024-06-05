# a = "Heart2_Valid_Var123 Invalid_Var 2abc_123 123_abc Heart_2"

# import re

# # Update the regex to match words with optional underscore and digits
# pattern = r"\A\b\w+_\d+\b|\b\w+\b"

# match = re.findall(pattern, a)

# print(match)


import re

a = "Heart2_Valid_Var123 Invalid_Var 2abc_123 123_abc Heart_2"

# Updated regex pattern
pattern = r'\A\w+(?:_\d+)?'

match = re.search(pattern, a)

if match:
    print(match.group(0))
