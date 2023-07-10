import random
names = input("Enter the names")
names1 = names.split(", ")
names2 = len(names1)
names3 = random.randint(0,names2-1)
names4 = names1[names3]
print(names4)