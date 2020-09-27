#!/usr/bin/env python
# coding: utf-8

# ## BI Programming. Exam. Task 1 samples

# ### Sample 1
# Generate a random list of integer numbers. Number of elements and the generation range should
# be requested from the user. Print the generated list on the screen. Without using insertion or
# deletion, make a circular shift of all elements 1 step to the right, then print the modified list.

# #### WITHOUT NumPy

# In[3]:


import random

number_of_elements = 1
generation_range_l = 15
generation_range_r = 24

random.seed(1) # initialize internal state of the random number generator

random_list = []
for i in range(number_of_elements):
    random_list.append(random.randint(generation_range_l, generation_range_r))

print(random_list)
# shifting list
new_indexes = [-1]
new_indexes.extend(range(len(random_list)-1))
print(new_indexes)
shifted_list = []
for i in new_indexes:
    shifted_list.append(random_list[i])
    
print(shifted_list)


# #### WITH NumPy

# In[4]:


import numpy as np

number_of_elements = 15
generation_range_l = 15
generation_range_r = 24

random_list = np.random.randint(
    generation_range_l,
    generation_range_r,
    number_of_elements)

print(random_list)

shifted_list = np.roll(random_list, 1)

print(shifted_list)


# ### Sample 2
# Request a string, then two integer dimensions n (number of rows) and m (number of columns).
# Project the string onto the nxm matrix as shown in the example below (letter by letter, on the first
# column from top to bottom, then on the second column from top to bottom, etc.). If the number
# of characters in the string is not sufficient, fill the remaining elements of the matrix with “-”. If the
# number of characters in the string is larger than the number of cells in the matrix, take only the
# first nxm characters. The matrix does not have to be printed in the aligned way as in the example,
# use the standard “print” function to save time.

# In[5]:


our_str = 'Hello Python!'
rows = 5
cols = 4

if len(our_str) < rows*cols:
    our_str = our_str + '-'*(rows*cols - len(our_str))
elif len(our_str) > rows*cols:
    our_str = our_str[:rows*cols]
else:
    pass

# create matrix
msg = []
for i in range(rows):
    msg.append([])
    for j in range(cols):
        msg[i].append('-')

print(our_str)

# print matrix
print('Old matrix')
for i in range(rows):
    for j in range(cols):
        print(msg[i][j], end=' ')
    print()

# filling matrix

index_str = 0
for i in range(cols):
    for j in range(rows):
        msg[j][i] = our_str[index_str] 
        index_str += 1
        
# print matrix
print('New matrix')
for i in range(rows):
    for j in range(cols):
        print(msg[i][j], end=' ')
    print()


# ### Sample 3
# Request a matrix of integer numbers from the user and make sure it is a square one (number of rows
# = number of columns).
# + Print the matrix on the screen.
# + Find the sum of numbers on the main diagonal and on the antidiagonal.

# In[52]:


rows = 4
cols = 4

random_list = np.random.randint( -10, 10, rows*cols)
# create matrix

mrx = []
index_list = 0
for i in range(rows):
    mrx.append([])
    for j in range(cols):
        mrx[i].append(random_list[index_list])
        index_list += 1

for i in range(rows):
    for j in range(cols):
        print(mrx[i][j], end=' ')
    print()

#sum diagonal
sum_diagonal = 0
for i in range(rows):
    sum_diagonal += mrx[i][i]
    
sum_antidiagonal = 0
for i in range(rows):
    sum_antidiagonal += mrx[i][-i - 1]
    
print(sum_diagonal)
print(sum_antidiagonal)


# ### Sample 4
# Request a single string from the user. The string may contain any sequence of characters, which form
# words separated by one or many spaces. Select those words, which can be converted to floating point
# numbers and find the minimum among them. Note that words can end with one of the following
# four punctuation marks - dot(.), comma(,), colon(:), semicolon(;). But you can assume that there
# is always at least one space following it (with the exception of the last word in the sentence)
# If there are no floating point numbers in the string, print a corresponding message.
# 
# **Hint:** the simplest way to check whether some word is a floating point number is to try to
# convert it to a float, catching a potential error with a try-except block.

# In[14]:


our_string = '135.026 It can   be separate 3   by -132.546 Python. It. is, really 4658: cool; 69687.'
list_element = our_string.split(' ')
without_empty = [i for i in list_element if i]
without_marks = []
for item in without_empty:
    if item[-1] in [',', ':', ';']:
        without_marks.append(item[:-1])
    else:
        without_marks.append(item)
        
floats = []
for item in without_marks:
    try:
        floats.append(float(item))
    except ValueError:
        continue
print(min(floats))


# ### Sample 5
# Input a list of integer numbers from the user. Find the sum of numbers between the first and last
# occurrences of the minimal element, processing the following edge cases carefully:
# + If the last minimum comes directly after the first one, print a corresponding message.
# + If the minimal element is repeated only once, print another message.

# In[16]:


our_list = [6, 7, 1, 1, 9, 1, 1]

min_elem = min(our_list)
interested_index = []
for idx, item in enumerate(our_list):
    if item == min_elem:
        interested_index.append(idx)
    else:
        continue
print(interested_index)
if len(interested_index) == 1:
    print('The minimal element is repeated only once')
elif interested_index[-1] - interested_index[0] == 1:
    print('No elements between the first and last minimum')
else:
    sum_elems = 0
    for item in our_list[interested_index[0] + 1: interested_index[-1]]:
        sum_elems += item
    print(sum_elems)


# ### Sample 6
# 1. Generate a random list of integer numbers. The size of the list and the generation range are
# defined by the user.
# 2. Print the generated list on the screen.
# 3. Input an integer number k > 0.
# 4. Build a matrix (ragged array) of k rows that groups elements of the random list by the number
# of their repetitions: m-th row of the matrix (m = 1, 2, ... k) contains elements from the list
# that are repeated exactly m times
# 

# In[17]:


number_of_elements = 15
generation_range_l = 15
generation_range_r = 24

random_list = np.random.randint(
    generation_range_l,
    generation_range_r,
    number_of_elements)

random_list = list(random_list)

print(random_list)

k = 5

unique_numbers = set(random_list)

mtrx = []
reps = 1
for i in range(k):
    mtrx.append([])
    for num in unique_numbers:
        if random_list.count(num) == reps:
            mtrx[i].append(num)
        else:
            continue
    reps += 1
print('-/'*5)
for i in range(k):
    print(mtrx[i])


# In[87]:


list(random_list).count(15)


# In[ ]:




