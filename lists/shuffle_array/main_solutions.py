# Sample solutions

# This is a simple solution that creates a brand new list and loops through
# the given list to append the elements in the correct order. The main trick
# here is to figure out how to append append the correct y elements. Drawing
# a diagram here can help.
def shuffle(nums, n):
    result = []
    for i in range(0, n):
        result.append(nums[i])
        result.append(nums[n+i])
    return result
    
# We've defined some simple test cases in the main function below for you to
# test your code. Feel free to edit the examples below and add your own.
def main():
    result = shuffle([1,2,3,4], 2)
    print(result) # Expected result: [1,3,2,4]

    result = shuffle([1,1,1,5,5,5], 3)
    print(result) # Expected result: [1,5,1,5,1,5]


# This 
if __name__ == "__main__":
    main()

