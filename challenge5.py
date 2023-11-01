# Write Python code to open a file named Fileprogram.txt and write some random data into it.
file = open("Fileprogram.txt",'w')
file.write("Hai,i am Zry")

# Open the file, read the contents and display them as output.
file = open("Fileprogram.txt", 'r')
sentence = file.read()
print(sentence)

# Write python code to add additional text to the existing file on a new line without deleting the previous contents.
file=open("Fileprogram.txt", 'a')
file.write(" \ni am fine here...")
file.close()