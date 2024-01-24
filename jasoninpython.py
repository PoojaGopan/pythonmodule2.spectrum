# import json

# # Create a Python dictionary
# data = {
#     "name": "John Doe",
#     "age": 25,
#     "city": "Example City",
#     "is_student": False,
#     "hobbies": ["reading", "coding", "hiking"],
#     "address": {
#         "street": "123 Main St",
#         "city": "Sampletown",
#         "zip": "12345"
#     }
# }

# # Encode the Python dictionary to a JSON-formatted string
# json_data = json.dumps(data, indent=2)  # indent for pretty printing

# # Print the JSON data
# print(json_data)

# # Write JSON data to a file
# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=2)

# with open('data.json', 'r') as file:
#     loaded_data = json.load(file)

# # Print the loaded data
# print(loaded_data)