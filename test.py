my_dict = {
    "January" : "2200",
    "February" : "2350",
    "March" : "2600",
    "April" : "2130",
    "May" :" 2190"
}

heros=['spider man','thor','hulk','iron man','captain america']

value1 = int(my_dict["February"]) - int(my_dict["January"])
value2 = int(my_dict["February"]) + int(my_dict["January"]) + int(my_dict["March"])

print (value1)
print (value2)

for key, value in my_dict.items():
    if value == "2000":
        print(key, value)

my_dict['June'] = '1980'
for key, value in my_dict.items():
    print(key, value)

my_dict['April'] = int(value) + 200
for key, value in my_dict.items():
    print(key, value)

length = len(heros)
print(length)
heros.append("Black Panther")
for n in heros:
    print(n)

heros.remove("Black Panther")
heros.insert(2,"black panther")
for n in heros:
    print(n)