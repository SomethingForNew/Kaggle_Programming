# 1.
# Have you ever felt debugging involved a bit of luck? The following program has a bug. Try to identify the bug and fix it.

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        # else:
        #     return False
    return False

    # one-line version using a list comprehension with Python's any function
    # return any([num % 7 == 0 for num in nums])

# 2.
# Look at the Python expression below. What do you think we'll get when we run it?
# When you've made your prediction, uncomment the code and run the cell to see if you were right

# R and Python have some libraries (like numpy and pandas) compare each element of the list to 2
# (i.e. do an 'element-wise' comparison) and give us a list of booleans like [False, False, True, True].

# Implement a function that reproduces this behaviour, returning a list of booleans corresponding to whether the corresponding element is greater than n.

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    pass

    res = []

    for num in L:
        res.append(num > thresh)

    return res

    # list comprehension version:
    # return [ele > thresh for ele in L]


# 3.
# Complete the body of the function below according to its docstring.

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    pass
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False