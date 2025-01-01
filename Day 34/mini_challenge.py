
def person_info(name, age, city):
    """
    Generate and print a sentence containing the person's information.

    Parameters:
    name (str): The name of the person.
    age (int): The age of the person.
    city (str): The city where the person lives.

    Returns:
    None
    """
    print(f"Hello. My name is {name}. I am {age} years old and live in {city}.")
    

# Calling the function
person_info("Rohail", 23, "Islamabad")
# Output => Hello. My name is Rohail. I am 23 years old and live in Islamabad.

# Printing Docstring of the function 
print(person_info.__doc__)

