# Importing the os module
import os

# Creating a directory called data (if not already created)
if (not os.path.exists("data")):
    os.mkdir("data")

# Creating 100 directory from Day1 to Day100 for 100 Days of Code Tutorials
for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")

# Renaming all the 100 directory to Tutorial 1 to Tutorial 100
for i in range(0, 100):
    os.rename(f"data/Day{i+1}", f"data/Tutorial {i+1}")
    
# Listing all the directories and files in the data folder
folders = os.listdir("data")

# Printing our current working directory
print(os.getcwd())

# Changing our current working directory
os.chdir("C:/Users/intag/Desktop")

# Printing our latest current working directory
print(os.getcwd())


