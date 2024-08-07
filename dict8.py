def merge_dicts(dict1, dict2):
    # Create a new dictionary that starts with dict1
    merged_dict = dict1.copy()
    # Update it with dict2, which will overwrite any existing keys from dict1
    merged_dict.update(dict2)
    return merged_dict

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

# Merge the dictionaries
result = merge_dicts(dict1, dict2)

# Print the resulting dictionary
print(result)
