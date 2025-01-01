# generate a list of cubes using list comprehension
cubeList = [num**3 for num in range(1, 11)]

print(cubeList)

# Generate a list of positive numbers from a list of numbers using list comprehension

sampleList = [1, -2, 4, 1, 0, 23, -23, -54]

positiveNumList = [num for num in sampleList if num >= 0]
print(positiveNumList)


# Generating a list of first letter of list items
names = ["Rohail", "Haddiya", "Ayaan"]
firstLetterList = [name[0] for name in names]
print(firstLetterList)