import re
pattern = "python"
if re.match(pattern,"python hello how are you?"):
    print("matched")
else:
    print("not matched")

# its only matched when the string contains the word python at 1st
# if the word python is in the middle or after its not matched