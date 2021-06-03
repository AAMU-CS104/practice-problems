# Shuffle Array

This is a real interview question from Leetcode #1470:
https://leetcode.com/problems/shuffle-the-array/

## Review Concepts

### For loops
How to loop from 0 to 5 (inclusive)? 
```
for i in range(0, 6):
    print(i)
```

How to loop through the indexes of the list `foo`? 
```
for i in range(0, len(foo)):
    print(i)
```
Note that for the ith element in a list, we say that it's index is i-1. Remember lists are indexed from zero, not one.

How to loop through all the elements in the list `foo`?
```
for i in foo:
    print(foo)
```

When do you want to loop through the elements of a list vs. the indexes of a list?

### Lists
How do we initialize (create) a new empty list? Use square brackets.
```
new_list = []
```

How do we add items to the end of a list? Use the `append` function. 
```
new_list = []
# This adds the integer 1 to the end of the list. 
new_list.append(1)
print(new_list) # Expect: [1]

new_list.append(2)
print(new_list) # Expect: [1,2]
```
How do I use an index to access a list element? In other words, how do I get the element in the list at index 0 (or the first item in the list)? 
```
new_list = [1,2,3]
print(new_list[0]) # Expect: 1
print(new_list[1]) # Expect: 2
print(new_list[2]) # Expect: 3
```

### Math Operations
How do we divide things in python? 
```
n/2
```

How do we do floor division? What is floor division? 
```
n//2
```
