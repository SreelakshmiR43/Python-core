# Write Python code which Accept the student name and in turn returns their respective Mark.
# Make sure to use dictionaries to store
# student name and their respective mark. The dictionary should
# include at least 7 elements

students = {
    "Libiya":80,
    "Sreekutty":75,
    "Zry":55,
    "Athira":85,
    "Vyshnavi":100,
    "Manya":95,
    "Athul":101
}
name = input("Enter the student name : ")
print("The mark obtained by "+name,"is",students.get(name))