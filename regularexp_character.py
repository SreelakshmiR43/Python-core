import re
pattern = "[A-Z][0-9][a-z]"  # we can use any pattern like Aa1,a1A,1Aa etc.,can use any number of patterns
if re.search(pattern,A3s):
    print("matched")
else:
    print("not matched")