# Question 1
# You have seen how to convert a float to an integer with the int function. Try this out yourself by running the code cell below

# Uncomment and run this code to get started!
# print(int(1.2321))
# print(int(1.747))
# print(int(-3.94535))
# print(int(-2.19774))


# Question 2
# In the tutorial, you learned about booleans (which can take a value of True or False), in addition to integers, floats, and strings. For this question, your goal is to determine what happens when you multiply a boolean by any of these data types. Specifically,

# What happens when you multiply an integer or float by True? What happens when you multiply them by False? How does the answer change if the numbers are positive or negative?
# What happens when you multiply a string by True? By False?
# Use the next code cell for your investigation.

# Uncomment and run this code to get started!
# print(3 * True)
# print(-3.1 * True)
# print(type("abc" * False))
# print(len("abc" * False))


# Question 3
# In this question, you will build off your work from the previous exercise to write a function that estimates the value of a house.

# Use the next code cell to create a function get_expected_cost that takes as input three variables:

# beds - number of bedrooms (data type float)
# baths - number of bathrooms (data type float)
# has_basement - whether or not the house has a basement (data type boolean)
# It should return the expected cost of a house with those characteristics. Assume that:

# the expected cost for a house with 0 bedrooms and 0 bathrooms, and no basement is 80000,
# each bedroom adds 30000 to the expected cost,
# each bathroom adds 10000 to the expected cost, and
# a basement adds 40000 to the expected cost.

# TODO: Complete the function
def get_expected_cost(beds, baths, has_basement):
    """Returns the sum of base_cost, beds, baths, has_basement

    Args:
        base_cost        (int): First number to add
        beds             (int): Second number to add
        baths            (int): Third number to add
        has_baseMent (boolean): Last number to add
    
    Returns:
        int: Sum of 'base_cost', 'beds', 'baths', 'has_baseMent'
    """
    base_cost = 80000
    beds_cost = 30000 * beds
    baths_cose = 10000 * baths
    basement_cost = 40000 * int(has_basement)
    value = base_cost  + beds_cost + baths_cose + basement_cost
    return value