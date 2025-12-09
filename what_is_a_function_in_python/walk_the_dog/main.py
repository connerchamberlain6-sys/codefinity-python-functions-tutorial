def describe_dog(name, breed, age):
    # Check if the age is valid
    if age < 0:
        statement= f"Invalid age for {name}. Age cannot be negative." 
        return statement
    # Check if the dog is a newborn
    elif age == 0:
        statement = f"{name} is a newborn {breed}. A bundle of joy!"
        return statement
    # Check if the dog is 1 year old
    elif age == 1:
        statement = f"{name} is a 1-year-old {breed}. A great companion!"
        return statement
    # For all other ages, including plural years
    else:
        statement = f"{name} is a {age}-year-old {breed}. An old dog with much wisdom!"
        return statement

# Test the function with various scenarios
description = describe_dog("Buddy", "Labrador", 3)
print(description)