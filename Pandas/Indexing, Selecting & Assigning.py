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

# 7.
# Create a variable df containing the country and variety columns of the first 100 records.

# Hint: you may use loc or iloc. When working on the answer this question and the several of the ones that follow, keep the following "gotcha" described in the tutorial:

# iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. loc, meanwhile, indexes inclusively.

# This is particularly confusing when the DataFrame index is a simple numerical list, e.g. 0,...,1000. In this case df.iloc[0:1000] will return 1000 entries, while df.loc[0:1000] return 1001 of them! To get 1000 elements using loc, you will need to go one lower and ask for df.iloc[0:999].

# My Solution:
# cols = ['country', 'variety']
# df = reviews.loc[:99, cols]


# 8.
# Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?

# italian_wines = reviews[reviews.country == 'Italy']


# 9.
# Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.

# top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand'])) & (reviews.points >= 95)]