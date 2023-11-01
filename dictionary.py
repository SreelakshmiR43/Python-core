x = {
    "name":"zry",
    "class":"rmca",
    "roll no":41,
    "college":"ajce"
}
print(x)
print(x["name"])
print(len(x))
x["cgpa"] = 6.17
print(x)
x.update({"subject":"python"})
print(x)
x.pop("cgpa")
print(x)
x.popitem()
print(x)

for i in x.values():
    print(i)

print("\n")

for i in x.keys() :
    print(i)

print("\n")

for i in x.items():
    print(i)

num = {

    1:"one",
    2:"two",
    3:"three"
}
print(num.get(3,"key not found"))
print(num.get(4,"key not found"))