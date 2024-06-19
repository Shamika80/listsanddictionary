from collections import Counter

def square_dictionary_values(original_dict):
    
    for key in original_dict:
        original_dict[key] **= 2
    return original_dict

def find_path_to_value(nested_dict, target_value, current_path=None):
    
    if current_path is None:
        current_path = []

    for key, value in nested_dict.items():
        if value == target_value:
            return current_path + [key]
        elif isinstance(value, dict):
            result = find_path_to_value(value, target_value, current_path + [key])
            if result:
                return result

    return None

def count_frequencies(items):
    
    return Counter(items)

my_dict = {"a": 2, "b": 3, "c": 1}
squared_dict = square_dictionary_values(my_dict)
print("Task 4 - Squared Dictionary:", squared_dict)

my_nested_dict = {"a": {"b": {"c": 5, "d": 10}}, "e": 20}
path = find_path_to_value(my_nested_dict, 10)
print("Task 5 - Path to Value:", path)

my_numbers = [1, 2, 3, 1, 2, 4, 5, 1]
word_counts = count_frequencies(my_numbers)
print("Task 6 - Item Frequencies:", word_counts)