# Question 1
# In the House Prices - Advanced Regression Techniques competition, you need to use information like the number of bedrooms and bathrooms to predict the price of a house. Inspired by this competition, you'll write your own function to do this.

# In the next code cell, create a function get_expected_cost() that has two arguments:

# beds - number of bedrooms
# baths - number of bathrooms
# It should return the expected cost of a house with that number of bedrooms and bathrooms. Assume that:

# the expected cost for a house with 0 bedrooms and 0 bathrooms is 80000.
# each bedroom adds 30000 to the expected cost
# each bathroom adds 10000 to the expected cost.
# For instance,

# a house with 1 bedroom and 1 bathroom has an expected cost of 120000, and
# a house with 2 bedrooms and 1 bathroom has an expected cost of 150000.

# TODO: Complete the function
def get_expected_cost(beds, baths):
    value = 80000 + beds * 30000 + baths * 10000
    return value

print(get_expected_cost(2, 3))


# Question 2
# You are thinking about buying a home and want to get an idea of how much you will spend, based on the number of bedrooms and bathrooms. You are trying to decide between four different options:

# Option 1: house with two bedrooms and three bathrooms
# Option 2: house with three bedrooms and two bathrooms
# Option 3: house with three bedrooms and three bathrooms
# Option 4: house with three bedrooms and four bathrooms
# Use the get_expected_cost() function you defined in question 1 to set option_1, option_2, option_3, and option_4 to the expected cost of each option.

# TODO: Use the get_expected_cost function to fill in each value
option_one = get_expected_cost(2, 3)
option_two = get_expected_cost(3, 2)
option_three = get_expected_cost(3, 3)
option_four = get_expected_cost(3, 4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)


# Question 3
# You're a home decorator, and you'd like to use Python to streamline some of your work. Specifically, you're creating a tool that you intend to use to calculate the cost of painting a room.

# As a first step, define a function get_cost() that takes as input:

# sqft_walls = total square feet of walls to be painted
# sqft_ceiling = square feet of ceiling to be painted
# sqft_per_gallon = number of square feet that you can cover with one gallon of paint
# cost_per_gallon = cost (in dollars) of one gallon of paint
# It should return the cost (in dollars) of putting one coat of paint on all walls and the ceiling. Assume you can buy the exact amount of paint that you need, so you can buy partial gallons (e.g., if you need 7.523 gallons, you can buy that exact amount, instead of needing to buy 8 gallons and waste some paint). Do not round your answer.

# TODO: Finish defining the function
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = cost_per_gallon * gallons_needed
    return cost


# Question 4
# Use the get_cost() function you defined in Question 3 to calculate the cost of applying one coat of paint to a room with:

# 432 square feet of walls, and
# 144 square feet of ceiling.
# Assume that one gallon of paint covers 400 square feet and costs $15. As in Question 3, assume you can buy partial gallons of paint. Do not round your answer.

# TODO: Set the project_cost variable to the cost of the project
project_cost = get_cost(432, 144, 400, 15)
print(project_cost)