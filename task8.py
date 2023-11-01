# regula exp - character

import re

pattern = "[A-Z][a-z][0-9][a-z][A-Z][0-9]"
if re.search(pattern,"Zy4sA3"):
    print("matched")
else:
    print("not matched")