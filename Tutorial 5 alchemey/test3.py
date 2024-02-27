import json

# Sample tuple
sample_tuple = ('key1', 'value1', 'key2', 'value2')

print(sample_tuple[::2])
print(sample_tuple[1::2])
# Convert tuple to dictionary
data_dict = dict(zip(sample_tuple[::2], sample_tuple[1::2]))

# Serialize dictionary to JSON
json_data = json.dumps(data_dict)

print(json_data)