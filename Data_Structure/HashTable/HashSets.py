# Hashset

# Creating set
s = set()

# Adding on set - O(1)
s.add(1)
s.add(2)
s.add(3)

# Lookup if item in Set - O(1)
if 1 in s:
    print("Exists")
else:
    print("N/A")

# Removing item from the set
s.remove(3)

# Set construction - O(s) - S is the lenght of the string
# Checking if the data exixst in a long string
string = 'aaaabbbbccccccddddeeee'
sett = set(string) 
print(sett)