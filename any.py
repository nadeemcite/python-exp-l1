num = 8

a = 'hi ' + str(num)
print(a)

# Formatting in string
num2 = 10
b = f'hi {num2}'  # fstring in python
print(b)

# Hello <person name>  how are you?

person_name = "Nadeem"

message = f"Hello {person_name} how are you?"

print(message)

k = "mno"
n = 99

i  =45

mesage_format = "{value_of_k} {value_of_i} {value_of_n}".format(
    value_of_k=k.upper(),value_of_i=i,value_of_n=n
)

print(mesage_format)

# Multiline String

a = """
            "hello"
            bye
            vdsvds
            vdsv
"""
print(a)

b = 'kfllg "kgf" '  # workaround

c = "kfllg \\\"kgf\" \\ / " # solution

print(c)

# tuples () and lists [] (collections) something where we have multiple items

t = (1,2,3)
l = [1,2,3]

print(t)
print(l)