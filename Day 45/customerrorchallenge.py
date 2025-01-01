# The register_user function takes username, password, and email as parameters.

def register_user (username, password, email):
    try:
        if len(username) < 5:
            raise ValueError("Username should be 5 characters or more.")
        elif len(password) < 8:
            raise ValueError("Password should be 8 characters or more.")
        elif "@" not in email:
            raise ValueError("Email should have an @ symbol.")
    except ValueError as v:
        return f"Error : {v}"
    else:
        return f"{username} is successfully created with email : {email}"

print(register_user("Roha", "rohail123", "rohail@gmail.com")) # Error : Username should be 5 characters or more.

print(register_user("Rohail", "rohail1", "rohail@gmail.com")) # Error : Password should be 8 characters or more.

print(register_user("Rohail", "rohail123", "rohailgmail.com")) # Error : Email should have an @ symbol.

print(register_user("Rohail", "rohail123", "rohail@gmail.com")) # Rohail is successfully created with email : rohail@gmail.com
