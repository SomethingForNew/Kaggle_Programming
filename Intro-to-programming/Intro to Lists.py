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


