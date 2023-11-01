set = {300,66,98,23,909,1200,225}
print(set)

set.add(100)
set.remove(300)
print("Set1:",set)

set2 = {100,478,200,300,1200,89,66}
print("Set2:",set2)

result = set - set2
union = set | set2
intersection = set & set2

print("Difference:",result)
print("Union:",union)
print("Intersection:",intersection)