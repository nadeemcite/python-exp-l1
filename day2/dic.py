import datetime

def sample_fun(dob_arg):
    day = dob_arg["date"]
    month = dob_arg["month"]
    year = dob_arg["year"]
    calculated_date = datetime.datetime.strptime(f"{day} {month} {year}", "%d %b %Y")
    today = datetime.date.today()
    return today.year - calculated_date.year - ((today.month, today.day) < ( calculated_date.month, calculated_date.day))



dob = {
    "date": 13,
    "month": "feb",
    "year": 1991
}
print(sample_fun(dob))

for i in range(10):
    print(i)


for i in dob.keys():
    print(i)


for i in dob.values():
    print(i)


for i in dob.keys():
    print(f"{i} - {dob[i]}")

for k, v in dob.items():
    print(f"{k} {v}")


print(dob.keys())
print(dob.items())

tup = (55,96,"hello")

# v1 = tup[0]
# v2 = tup[1]
# v3 = tup[2]
# print(v1)
# print(v2)
# print(v3)

(v1, v2, v3) = tup
print(v1)
print(v2)




person = {
    "name": "Xyz",
    "address": {
        "address_line_1" :"some place",
        "zip": 123343,
        "country" :"Bahrain",
        "details": {
                "a":1,
                "b":1
        }
    }
}

person["address"]["details"]["a"]


def sample_fun_args(day, month, year):
    calculated_date = datetime.datetime.strptime(f"{day} {month} {year}", "%d %b %Y")
    today = datetime.date.today()
    return today.year - calculated_date.year - ((today.month, today.day) < ( calculated_date.month, calculated_date.day))


# unpacking can only be done if a function is accepting arguments and you need to pass a dictionary with exact same keys

new_dob = {
    "day": 13,
    "month": "feb",
    "year": 1991
}
print(sample_fun_args(**new_dob))


# kwarguments in function

# format string

test_dict = {
    "name": "My Name",
    "age": 12
}

a_str = "hello {name} how are you? and {age} is your age".format(**test_dict)

print(a_str)

# Set

my_random_list = set([5,8,6,3,8,9,2,3,4,0,1,2])
print(my_random_list)