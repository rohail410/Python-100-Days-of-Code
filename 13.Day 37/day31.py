# cities3 = cities1.union(cities2)
# print(cities3)
# cities1.update(cities2)
# print(cities1)
# cities3 = cities1.intersection(cities2)
# print(cities3)
# cities1.intersection_update(cities2)
# print(cities1)
# cities3 = cities1.symmetric_difference(cities2)
# print(cities3)
# cities1.symmetric_difference_update(cities2)
# print(cities1)
# cities3 = cities1.difference(cities2)
# print(cities3)
# cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities1.difference_update(cities2)
# print(cities1)
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# print(cities.difference(cities2))
# cities1 = {"Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul"}
# print(cities1.isdisjoint(cities2))

# cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul"}
# print(cities1.issuperset(cities2))

# cities3 = {"Tokyo", "Madrid"}
# print(cities1.issuperset(cities3))
# print(cities3.issubset(cities1))
# print(cities1.issubset(cities3))
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.add("Islamabad")
# cities.add("Karachi")
# print(cities)
# cities2 = {"Warsaw", "Seoul", "Tokyo"}
# cities1.update(cities2)
# print(cities1)
# gone = cities1.pop()
# print(gone)
# cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi", "Seoul"}
# cities1.clear()
# print(cities1)

info = {"Carla", 19, 19, 5.9, False}

if "Carla" not in info:
    print("Yes")
else:
    print("No")
