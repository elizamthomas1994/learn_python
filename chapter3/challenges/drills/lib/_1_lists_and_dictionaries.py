# == INSTRUCTIONS ==
#
# In these exercises you will recap basic dictionary and list operations, then
# go deeper on both topics.
#
# The requirements will always start with the name of the function. Use this
# name exactly or the tests won't be able to find it.
#
# Then there will be a description of what the function should do. Note that
# some solutions will require more than one line of code.
#
# You won't find everything that you need in our materials. Use the Python Docs
# and Google liberally if you get stuck.

# == LIST EXERCISES ==

# Method name: fourth_element
# Purpose: returns the fourth element of the given list
# Arguments: one list
# Example:
#   Call:    fourth_element([1, 2, 3, 4, 5])
#   Returns: 4
def fourth_element(list):
  return list[3]

# Method name: average
# Purpose: returns the average (the mean) of the given list
# Arguments: one list
# Example:
#   Call:    average([3, 1, 44, 1])
#   Returns: 12.25
def average(list):
  sum = 0 

  for i in list:
    sum += i

  return (sum / len(list))

# Method name: lowest_squared
# Purpose: returns the lowest number squared
# Arguments: one list
# Example:
#   Call:    lowest_squared([5, 3, 44, 7])
#   Returns: 9
def lowest_squared(list):
  list.sort()
  num = list[0]
  return num ** 2

# Method name: highest_squared
# Purpose: returns the highest number squared
# Arguments: one list
# Example:
#   Call:    highest_squared([5, 3, 44, 7])
#   Returns: 1936
def highest_squared(list):
  list.sort()
  num = list[-1]
  return num ** 2

# Method name: starts_with_a
# Purpose: returns only elements starting with 'a'
# Arguments: one list
# Example:
#   Call:    starts_with_a(['banana', 'apple', 'orange', 'avocado'])
#   Returns: ['apple', 'avocado']
def starts_with_a(list):
  filtered_list = []

  for i in list:
    if i.startswith('a'):
      filtered_list.append(i)
    else:
      None

  return filtered_list

# Method name: starts_with_a_vowel
# Purpose: returns only the elements that start with a vowel
# Arguments: one list
# Example:
#   Call:    starts_with_a_vowel(['banana', 'apple', 'orange', 'avocado'])
#   Returns: ['apple', 'orange', 'avocado']
def starts_with_a_vowel(list):
  filtered_list = []

  for i in list:
    if i.startswith('a') or i.startswith('e') or i.startswith('i') or i.startswith('o') or i.startswith('u'):
      filtered_list.append(i)
    else:
      None

  return filtered_list

# Method name: reverse_each_element
# Purpose: reverses each sting in the given list
# Arguments: one list
# Example:
#   Call:    reverse_each_element(['one', 'two'])
#   Returns: ['eno', 'owt']
def reverse_each_element(list):
  filtered_list = []

  for i in list:
    filtered_list.append(i[::-1])

  return filtered_list

# Method name: sort_by_last_letter
# Purpose: returns the list, sorted by the last letter alphabetically
# Arguments: one list
# Example:
#   Call:    sort_by_last_letter(['banana', 'apple', 'carrot', 'avocado'])
#   Returns: ['banana', 'apple', 'avocado', 'carrot']
def sort_by_last_letter(list):
  return sorted(list, key=lambda x: x[-1])

# Method name: greater_than_5
# Purpose: returns only numbers greater than 5
# Arguments: one list
# Example:
#   Call:    greater_than_5([9, 3, 44, 7])
#   Returns: [9, 44, 7]
def greater_than_5(list):
  filtered_list = []

  for i in list:
    if i > 5:
      filtered_list.append(i)

  return filtered_list

# Method name: greater_than
# Purpose: returns only the elements that are greater than the number provided
# Arguments: one list and one number
# Example:
#   Call:    greater_than([9, 3, 6, 44, 7, 7], 6)
#   Returns: [9, 44, 7, 7]
def greater_than(list, num):
  filtered_list = []

  for i in list:
    if i > num:
      filtered_list.append(i)

  return filtered_list

# Method name: less_than
# Purpose: returns only the elements that are less than the number provided
# Arguments: one list and one number
# Example:
#   Call:    less_than([9, 3, 6, 44, 1, 7, 7], 6)
#   Returns: [3, 1]
def less_than(list, num):
  filtered_list = []

  for i in list:
    if i < num:
      filtered_list.append(i)

  return filtered_list

# Method name: words_shorter_than
# Purpose: returns only the elements than have fewer characters than the number provided
# Arguments: one list and one number
# Example:
#   Call:    words_shorter_than(['banana', 'apple', 'orange', 'nut', 'avocado'], 6)
#   Returns: ['apple', 'nut']
def words_shorter_than(list, num):
  return [i for i in list if len(i) < num]

# Method name: all_above
# Purpose: returns true if all elements are greater than the number provided
# Arguments: one list and one number
# Example:
#   Call:    all_above([9, 3, 6, 44, 1, 7, 7], 6)
#   Returns: False
#   Call:    all_above([9, 3, 6, 44, 1, 7, 7], 0)
#   Returns: True
def all_above(list, num):
  return all(i > num for i in list)

# Method name: all_below
# Purpose: returns true if all elements are less than the number provided
# Arguments: one list and one number
# Example:
#   Call:    all_below([9, 3, 6, 44, 1, 7, 7], 6)
#   Returns: False
#   Call:    all_below([9, 3, 6, 44, 1, 7, 7], 100)
#   Returns: True
def all_below(list, num):
  return all(i < num for i in list)

# Method name: multiply_each_by
# Purpose: returns a new list with each element multiplied by the number provided
# Arguments: one list and one number
# Example:
#   Call:    multiply_each_by([9, 3, 6, 44, 1, 7, 7], 2)
#   Returns: [18, 6, 12, 88, 2, 14, 14]
def multiply_each_by(list, num):
  filtered_list = []
  for i in list:
    filtered_list.append(i * num)

  return filtered_list


# == DICTIONARY EXERCISES ==

# Method name: values_summed
# Purpose: returns the total of all the values in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    values_summed({'cat': 4, 'person': 2, 'centipede': 100})
#   Returns: 106
def values_summed(dict):
  values = dict.values()
  return sum(values)

# Method name: add_key_value_pair
# Purpose: returns a the dictionary with the new key and value added
# Arguments: one dictionary, one key and one value
# Example:
#   Call:    add_key_value_pair({'cat': 4, 'person': 2, 'centipede': 100}, 'dog', 4)
#   Returns: {'cat': 4, 'person': 2, 'centipede': 100, 'dog': 4}
def add_key_value_pair(dict, key, value):
  dict[key] = value
  return dict

# Method name: remove_key_value_pair
# Purpose: returns a the dictionary with the key and value removed
# Arguments: one dictionary, one key
# Example:
#   Call:    remove_key_value_pair({'cat': 4, 'person': 2, 'centipede': 100}, 'cat')
#   Returns: {'person': 2, 'centipede': 100}
def remove_key_value_pair(dict, key):
  del dict[key]
  return dict

# Method name: where_value_below
# Purpose: returns key value pairs where the value is less than the number provided
# Arguments: one dictionary and one number
# Example:
#   Call:    where_value_below({'cat': 4, 'person': 2, 'centipede': 100}, 5)
#   Returns: {'cat': 4, 'person': 2}
def where_value_below(dict, num):
  return {key: value for key, value in dict.items() if value < num}

# Method name: where_key_starts_with
# Purpose: returns key value pairs where the key starts with the letter provided
# Arguments: one dictionary and one letter
# Example:
#   Call:    where_key_starts_with({'cat': 4, 'person': 2, 'centipede': 100}, 'c')
#   Returns: {'cat': 4, 'centipede': 100}
def where_key_starts_with(dict, letter):
  return {key: value for key, value in dict.items() if key.startswith(letter)}

