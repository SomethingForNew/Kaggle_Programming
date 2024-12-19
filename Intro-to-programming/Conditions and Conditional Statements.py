# Question 1
# You work at a college admissions office. When inspecting a dataset of college applicants, you notice that some students have represented their grades with letters ("A", "B", "C", "D", "F"), whereas others have represented their grades with a number between 0 and 100.

# You realize that for consistency, all of the grades should be formatted in the same way, and you decide to format them all as letters. For the conversion, you decide to assign:

# "A" - any grade 90-100, inclusive
# "B" - any grade 80-89, inclusive
# "C" - any grade 70-79, inclusive
# "D" - any grade 60-69, inclusive
# "F" - any grade <60
# Write a function get_grade() that takes as input:

# score - an integer 0-100 corresponding to a numerical grade
# It should return a Python string with the letter grade that it corresponds to. For instance,

# A score of 85 corresponds to a B grade. In other words, get_grade(85) should return "B".
# A score of 49 corresponds to an F grade. In other words, get_grade(49) should return "F".
# Make sure that when supplying the grade that is returned by the function, it is enclosed in quotes. (For instance, if you want to return "A", you should write return "A" and not return A.)

# TODO: Edit the function to return the correct grade for different scores
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Question 2
# In the exercise for the previous lesson, you wrote a function cost_of_project() that estimated the price of rings for an online shop that sells rings with custom engravings. This function did not use conditional statements. In this exercise, you will rewrite the function to use conditional statements. Recall that the online shop has the following price structure:

# Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
# Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
# Spaces and punctuation are counted as engraved units.

def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        return 100 + 10 * len(engraving)
    else:
        return 50 + 7 * len(engraving)


# Question 3
# You are a programmer at a water agency. Recently, you have been tasked to write a function get_water_bill() that takes as input:

# num_gallons = the number of gallons of water that a customer used that month. (This will always be an integer with no decimal part.)
# It should output the water bill.

# The water agency uses this pricing structure:

# Tier	Amount in gallons	Price per 1000 gallons
# Tier 1	0 - 8,000	$5
# Tier 2	8,001 - 22,000	$6
# Tier 3	22,001 - 30,000	$7
# Tier 4	30,001+	$10

# TODO: Edit the function to return the correct bill for different
# values of num_gallons
def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        return 5 * num_gallons / 1000
    elif num_gallons <= 22000:
        return 6 * num_gallons / 1000
    elif num_gallons <= 30000:
        return 7 * num_gallons / 1000
    else:
        return 10 * num_gallons / 1000


# Question 4
# You work for a company that provides data services. For $100/month, your company provides 15 gigabytes (GB) of data. Then, any additional data is billed at $0.10/MB (or $100/GB, since 1,000 MB are in 1 GB).

# Use the next code cell to write a function get_phone_bill() that takes as input:

# gb = number of GB that the customer used in a month
# It should return the customer's total phone bill.

# For instance:

# A customer who uses 10 GB of data in one month is billed only $100, since the usage stayed under 15 GB. In other words, get_phone_bill(10) should return 100.
# A customer who uses 15.1 GB (or 15 GB + 100 MB) of data in one month has gone over by .1 GB, so they must pay $100 (cost of plan), plus $0.10 * 100 = $10, for a total bill of $110. In other words, get_phone_bill(15.1) should return 110.

# TODO: Edit the function to return the correct bill for different
# values of GB
def get_phone_bill(gb):    
    if gb <= 15:
        return 100
    else:
        return 100 + 100 * (gb - 15)


