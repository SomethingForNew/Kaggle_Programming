# 1.
# Select the description column from reviews and assign the result to the variable desc.

#  My Solution:
# desc = reviews.description
# desc = reviews["description"]


# 2.
# Select the first value from the description column of reviews, assigning it to variable first_description.

# My Solution:
# first_description = reviews.description.iloc[0]


# 3.
# Select the first row of data (the first record) from reviews, assigning it to the variable first_row.

# My Solution:
# row number로 원하는 row 를 선택
# first_row = reviews.iloc[0]


# 4.
# Select the first 10 values from the description column in reviews, assigning the result to variable first_descriptions.
# Hint: format your output as a pandas Series.

# My Solution:
# first_descriptions = reviews.description.iloc[:10]

# Other Solution:
# first_descriptions = reviews.description.head(10)
# reviews.loc[:9, "description"]


# 5.
# Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.

# In other words, generate the following DataFrame:


# 6.
# Create a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels 0, 1, 10, and 100.
# In other words, generate the following DataFrame:

# My Solution:
# df = reviews.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]

# Kaggle's Solution:
# cols = ['country', 'province', 'region_1', 'region_2']
# indices = [0, 1, 10, 100]
# df = reviews.loc[indices, cols]