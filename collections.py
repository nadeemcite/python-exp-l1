t = (7,3,5)  # tuples are immutable, faster 
l = [9,4,2]  # lists are mutable

print(t[0])
print(l[1])

l[1] = 10


print(l[1])

l.append(67)

l.insert(0,45)

l.insert(1,50)



print(l)
l.append(35)
print(l)

# [45, 50, 9, 10, 2, 67, 35]

print(l)

print(l[-2])

# Slicing almost all python libraries

# [45, 50, 9, 10, 2, 67, 35]

# print(len(l))

# print(l[len(l) - 1])

# from 2nd index to 6th index

# loop

print(l[2:4]) # 2 and 3 

print(l[1:-2]) # start from 1st and end at second last

print(l[0:7:2])

# Tommorow
dat = {
    "pqr": 10,
    "mno": 15,
    "klp": "dsvs"
}