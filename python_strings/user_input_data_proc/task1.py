# Task 1 input data processor
def validate_name(full_name):

    split_name = full_name.strip().split()
    
    if len(split_name) != 2:
        return "Oops! You need to enter exactly two names: a first name and a last name."
    
    first_name, last_name = split_name
    
    if len(first_name) < 2 or len(last_name) < 2:
        return "Uh-oh! Both your first and last names must have at least 2 characters each."
    
    return f"{first_name.title()} {last_name.title()}"

while True:
    your_full_name = input("Please type your first and last name (minimum 2 characters each): ")
    
    result = validate_name(your_full_name)
    
    if result.startswith("Oops") or result.startswith("Uh-oh"):
        print(result)
    else:
        print(f"Success! Your name is valid: {result}")
        break
