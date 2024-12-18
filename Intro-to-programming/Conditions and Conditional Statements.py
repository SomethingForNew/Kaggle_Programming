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


