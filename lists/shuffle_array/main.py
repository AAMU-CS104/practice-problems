# You can run this code from the directory containing the main.py file
# by running `python main.py`. This is a template file for Leetcode #1470.
# We'll use this as a practice problem to learn about lists. 

# The shuffle function takes a list of integers consisting of 2n elements of
# the form [x1,x2,...,xn,y1,y2,...,yn] and an integer n. It returns a list
# of integers in the form [x1,y1,x2,y2,...,xn,yn]. 
# For a detailed explanation, see:
# https://leetcode.com/problems/shuffle-the-array/

def shuffle(nums, n):
    # The `pass` keyword is used as a placeholder for future code. It means
    # do nothing, somebody will add code here in the future.
    # TODO: remove the pass statement below and actually implement the
    # shuffle function.
    pass
    

# We've defined some simple test cases in the main function below for you to
# test your code. Feel free to edit the examples below and add your own.
def main():
    result = shuffle([1,2,3,4], 2)
    print(result) # Expected result: [1,3,2,4]

    result = shuffle([1,1,1,5,5,5], 3)
    print(result) # Expected result: [1,5,1,5,1,5]

# This line of code doesn't really do anything other than call the main
# function. It ensures that your code actually runs when you execute: 
# `python main.py`. 
# See this stackoverflow post for a detailed explanation:
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    main()

