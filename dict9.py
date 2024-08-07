# Define a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Key to access in the dictionary
key_to_access = 'country'

try:
    # Attempt to access a non-existent key
    value = my_dict[key_to_access]
except KeyError:
    # Handle the KeyError exception with a custom error message
    print(f"Error: The key '{key_to_access}' does not exist in the dictionary.")
else:
    # If no exception occurred, print the value
    print(f"The value for the key '{key_to_access}' is: {value}")
