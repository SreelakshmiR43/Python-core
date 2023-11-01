import re
pattern ="r.d" #1 dot one character
if re.match(pattern,"red"):  # if the string contains more than characters the incorect.
    print("correct")
else:
    print("incorrect")