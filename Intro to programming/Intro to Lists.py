# Question 1
# You own a restaurant with five food dishes, organized in the Python list menu below. One day, you decide to:

# remove bean soup ('bean soup') from the menu, and
# add roasted beet salad ('roasted beet salad') to the menu.
# Implement this change to the list below. While completing this task,

# do not change the line that creates the menu list.
# your answer should use .remove() and .append().

# Do not change: Initial menu for your restaurant
menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp',
       'fish soup with cream and onion', 'gyro']

# TODO: remove 'bean soup', and add 'roasted beet salad' to the end of the menu
menu.remove('bean soup')
menu.append('roasted beet salad')


# Question 2
# The list num_customers contains the number of customers who came into your restaurant every day over the last month (which lasted thirty days). Fill in values for each of the following:

# avg_first_seven - average number of customers who visited in the first seven days
# avg_last_seven - average number of customers who visited in the last seven days
# max_month - number of customers on the day that got the most customers in the last month
# min_month - number of customers on the day that got the least customers in the last month
# Answer this question by writing code. For instance, if you have to find the minimum value in a list, use min() instead of scanning for the smallest value and directly filling in a number.

# Do not change: Number of customers each day for the last month
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

# TODO: Fill in values for the variables below
avg_first_seven = sum(num_customers[:7]) / 7
avg_last_seven = sum(num_customers[-7:]) / 7
max_month = max(num_customers)
min_month = min(num_customers)


# Question 3
# Now it is your turn to try this out! Create two Python lists:

# letters should be a Python list where each entry is an uppercase letter of the English alphabet. For instance, the first two entries should be "A" and "B", and the final two entries should be "Y" and "Z". Use the string alphabet to create this list.
# address should be a Python list where each row in address is a different item in the list. Currently, each row in address is separated by a comma.

# DO not change: Define two Python strings
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"

# TODO: Convert strings into Python lists
letters = alphabet.split('.')
formatted_address = address.split(',')

# Question 4

def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    # TODO: Complete the function
    return sum(list_liked) / len(list_liked)

# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])


# 🌶️ Question 5
 
# Say you're doing analytics for a website.  You need to write a function that returns the percentage growth in the total number of users relative to a specified number of years ago.

# Your function `percentage_growth()` should take two arguments as input:
# - `num_users` = Python list with the total number of users each year.  So `num_users[0]` is the total number of users in the first year, `num_users[1]` is the total number of users in the second year, and so on.  The final entry in the list gives the total number of users in the most recently completed year.
# - `yrs_ago` = number of years to go back in time when calculating the growth percentage

# For instance, say `num_users = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]`.
# - if `yrs_ago = 1`, we want the function to return a value of about `0.036`. This corresponds to a percentage growth of approximately 3.6%, calculated as (2001078 - 1930992)/1930992.
# - if `years_ago = 7`, we would want to return approximately `0.66`.  This corresponds to a percentage growth of approximately 66%, calculated as (2001078 - 1204334)/1204334.

# Your coworker sent you a draft of a function, but it doesn't seem to be doing the correct calculation.  Can you figure out what has gone wrong and make the needed changes?

# TODO: Edit the function
# my solution:
def percentage_growth(num_users, yrs_ago):
    base_year_of_users = num_users[-1:][0]
    reference_year_of_users = num_users[-(yrs_ago + 1):][0]
    return (base_year_of_users - reference_year_of_users) / reference_year_of_users

# Kaggle's solution:
def percentage_growth(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]
    return growth

# Do not change: Variable for calculating some test examples
num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

# Do not change: Should return .036
print(percentage_growth(num_users_test, 1))

# Do not change: Should return 0.66
print(percentage_growth(num_users_test, 7))