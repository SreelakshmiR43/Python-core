#exceptional handling

try:
    a=10
    b="zry"
    print(a + b)

except:
    print("There is an Error")
finally:
    print("Finished")
