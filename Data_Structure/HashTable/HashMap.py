# Hasmaps - Dictionaries

d = {"Employee": 1, "Age": 23, "Status Point": 3}

# Adding key & value pair in dictionary: O(1)
d["arsh"] = 4

# Lookup for presence key in dictionary: O(1)
if "Employee" in d:
    print(True)

# Check the value corresponding to a key in the dictionary: O(1)
print(d['Age'])

# Loop over the key&value pairs of the dictionary: O(n)
for key, val in d.items():
    print(f'Key {key}: Val {val}')

# Defaultdict

from collections import defaultdict

default = defaultdict(int)

default[2]