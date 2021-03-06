### Practicing using Functions and method in a string data types
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
print("The length of the string of the variable verse is {}".format(len(verse)))
print("The index of the first 'and' can be found in the {}th position".format(verse.find("and")))
print("The index of the last 'and' can be found in the {}th position".format(verse.rfind("you")))

### Practicing Ordering and Indexing of Data Types
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month

num_days = days_in_month[month-1]
print(num_days) 


### Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
#Modify this line so it prints the last three elements of the list
eclipse_dates = eclipse_dates[-3:]
print(eclipse_dates)

### A Basic Split Method

new_str = "The cow jumped over the moon."
print(new_str.split(" "))

### what would this script produce as a result
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

#Result 4,2

### What would be the output of this code
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))
#Result Albert & Ben & Carol & Donna

### Choose the correct syntax to slice each of the following elements from the list
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

arr[:2]

### Doing Exercise with Turples
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

# The Result to this code is that it would produce 13.4125 for latitude and 103.866667 for longitude


### An Error code that would produce that the key in the dictionary are unhashable because they mutable
"""
room_numbers = {
    ['Freddie', 'Jen']: 403,
    ['Ned', 'Keith']: 391,
    ['Kristin', 'Jazzmyne']: 411,
    ['Eugene', 'Zach']: 395
}

print(room_numbers)
"""

### Another Dictionary element

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He',}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas']= True
print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])

### Practice Question

"""
Your task for this quiz is to find the number of unique words in the text. In the code editor below,
complete these three steps to get your answer.
1. Split verse into a list of words. Hint: You can use a string method you learned in the previous lesson.
2. Convert the list into a data structure that would keep only the unique elements from the list.
3. Print the length of the container.

"""
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique =  len(verse_set)
print(num_unique, '\n')

### Practise Question to used Dictionary Data Structures 
"""
Try to answer these using code, rather than inspecting the dictionary manually!
1. How many unique words are in verse_dict?
2. Is the key "breathe" in verse_dict?
3. What is the first element in the list created when verse_dict is sorted by keys?
Hint: Use the appropriate dictionary method to get a list of its keys, and then sort that list. 
Use this list of keys to answer the next two questions as well.
4. Which key (word) has the highest value in verse_dict?

"""

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = 'breathe' in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
keys_list = verse_dict.keys()
print(keys_list)
sorted_keys = sorted(verse_dict.keys())
print(sorted_keys)

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1])

### Using for loop to iterate through a dictionary
# whenever you iterate through a dictionary, the outputs
# are usually the keys, to obtain the key and values, you
# use the item method to bring it out

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

for keys in cast:
    print(keys)

print("\n Iterating through the Dictionary for the keys and  the values")

for keys,values in cast.items():
    print ("Actor: {}  Roles: {} ".format(keys, values))

### Fruit-Basket Task
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Solution of the problem
for key, values in basket_items.items():
    if key in fruits:
        result += int(values)

print(result)

'''
Our sensor technology has received a major upgrade, and now 
provides two-dimensional images using nested arrays.

- Every pixel is still a 1 or a 0.
- The image will contain exactly one rectangle of 0s on a 
  background of 1s.
- We consider the top left corner to be 0,0

Write a function that takes the image as input and returns 
the row and column indices of the rectangle's top-left corner.

You can choose to reuse or modify first_zero or get_width, 
or start over.

For complexity analysis, the dimensions of the input are 
width(w) and height(h)
'''

def find_rectangle(image):
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            if image[i][j] == 0 :
                return i,j 

image1 = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1],
]
print(find_rectangle(image1)) # (2,3)  row, column

image2 = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0],
]
print(find_rectangle(image2)) # (4,6)

image3 = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 0, 0],
  [1, 1, 1, 1, 1, 0, 0],
]
print(find_rectangle(image3)) # (3,5)
  
image4 = [
  [0, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
]
print(find_rectangle(image4)) # (0,0)

image5 = [
  [0],
]
print(find_rectangle(image5)) # (0,0)


def first_zero(image1):
    for i in range(0,len(image1)):
        if (image1[i]) == 0:
            return i
def get_width(image1):
    result = 0
    for i in range(0, len(image1)):
        if (image1[i]) == 0:
            result += 1
    return (result)


#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for key, values in basket_items.items():
    if key in fruits:
        result += int(values)

print(result)

#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for key, values in basket_items.items():
    if key in fruits:
        result += int(values)

print(result)


#Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for key, values in basket_items.items():
    if key in fruits:
        result += int(values)

print(result)

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for keys, values in basket_items.items():
#if the key is in the list of fruits, add to fruit_count.
    if keys in fruits:
        fruit_count += values
#if the key is not in the list, then add to the not_fruit_count
    if keys not in fruits:
        not_fruit_count += values

print("The number of fruits is {}.  There are {} objects \
     that are not fruits.".format(fruit_count, not_fruit_count))


# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= 6:
    
    # multiply the product so far by the current number
    product *= current
    
    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)

### Factorial Question Using For Loop

# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
for num in range(2, number + 1):
    product *= num


# print the factorial of number
print(product)

## Count By Quiz

start_num = 5
end_num = 100
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)

### Count By Check Quiz

start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)

### Nearest Square Quiz 

limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)

