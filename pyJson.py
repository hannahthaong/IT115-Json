#

import json

#

data1 = {
    'name': 'Hannah Nguyen',
    'age': 28,
    'city': 'Seattle',
    'interests': ['Traveling', 'Beauty', 'Hiking', 'Eating Out'],
    'is_student': True
}

#creating json file with key pairs

with open('data1.json', 'w') as json_file:
    #Dump the Data Dictionary into the json file
    json.dump(data1, json_file, indent=4)

print("You have succesfully written to data1.json")

#opening json file and load data
with open('data1.json', 'r') as json_file:

    loaded_data = json.load(json_file) 

print("Successfully able to read file")
print(loaded_data)

#load more data and append to the list
loaded_data['age'] = 30
loaded_data['interests'].append('Researching')

# 

with open('data1.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

print('Modified data written to data.json')

