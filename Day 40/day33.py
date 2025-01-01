# print(info["name"])
# print(info.get("name2"))
# print("Hello World")
# print(info.values())

# for value in info.values():
#     print(value)
    
# print(type(info.values()))

# print(info.keys())

# for key in info.keys():
#     print(key)
    
# print(type(info.keys()))


info = {"name":"Rohail", "age": 23, "eligible":True}

print(info)


print(info.items())

for key,value in info.items():
    print(f"This is key => {key} and it's value => {value}")
    
print(type(info.items()))
