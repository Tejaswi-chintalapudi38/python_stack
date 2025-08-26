# Dictionary: is a collection of key-value pairs, where each key is unique
example = {'name':'Alice', 'age':25, 'city':'New York'}

#get(key, default=None) - Returns value for the key if it exists; otherwise returns default.
print(example.get('name'))
print(example.get('gender', 'N/A'))

#keys() - Returns a view object of dictionary keys
print(list(example.keys()))

# values() - Returns a view object of dictionary values.
print(list(example.values()))

# items() - Returns a view object of (key, value) tuples.
for k,v in example.items():
    print(k,v)   
print(example.update({'gender':'male'}))

# pop(key, default) - Removes specified key and returns its value
print(example.pop('mobile','N/A'))

# popitem() - deletes the last item
print(example.popitem())

# clear() - clears all the elements in dictionary
print(example.clear())

# update([for multiple items]) - update the data if the data not in the original dictionary it adds that data 
example.update([('a',7)  , ('d', 4),  ('e', 5)]) 
print(example)

# .copy() => is also said as shallow copy it opies entire data but when you update the copied data the original one also change
shallow = example.copy()
shallow.append('pincode',522318)
print(example)

# copy.deepcopy() => deepcopy just copies the entire data but when you update the copy the original one didn't change 
import copy
shallow = copy.deepcopy(example)
shallow.append('id',1)
print(shallow)
print(example)

# fromkeys(keys, value=None) =>Creates a new dictionary from keys and a common value. If value is mutable (like a list), all keys share the same object.
keys = ['a', 'b']
new_d = dict.fromkeys(keys, 0)
print(new_d)  

# Zip(keys, values) pairs up items from both lists. dict(zip(...)) converts those pairs into key-value pairs.
keys = ['a', 'b']
values = [1, 2, 3]
print(dict(zip(keys, values))) 