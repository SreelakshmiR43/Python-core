import re
pattern = "python"

if re.search(pattern,"hai hello i am python"):
    print("matched")
else:
    print("not matched")