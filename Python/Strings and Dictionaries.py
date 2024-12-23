# 0a.
a = ""
length = len(a)


# 0b.
b = "it's ok"
length = len(b)

# 0c.
b = "it's ok"
length = len(b)


# 0d.
d = """hey"""
length = len(d)


# 0e.
e = '\n'
length = len(e)


# 1.
# There is a saying that "Data scientists spend 80% of their time cleaning data, and 20% of their time complaining about cleaning data."
# Let's see if you can write a function to help clean US zip code data.
# Given a string, it should return whether or not that string represents a valid zip code. For our purposes, a valid zip code is any string consisting of exactly 5 digits.

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    pass
    return len(zip_code) == 5 and zip_code.isdigit()


# 2.
# A researcher has gathered thousands of news articles.
# But she wants to focus her attention on articles including a specific word. Complete the function below to help her filter her list of articles.

# Your function should meet the following criteria:

# Do not include documents where the keyword string shows up only as a part of a larger word.
# For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.”
# She does not want you to distinguish upper case from lower case letters.
# So the phrase “Closed the case.” would be included when the keyword is “closed”
# Do not let periods or commas affect what is matched.
# “It is closed.” would be included when the keyword is “closed”. But you can assume there are no other types of punctuation.


def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    pass
    indices = [] 
    
    for i, doc in enumerate(doc_list):
        words = doc.split()
        temp = [word.rstrip('.,').lower() for word in words]

        if keyword.lower() in temp:
            indices.append(i)
            
    return indices


# 3.
# Now the researcher wants to supply multiple keywords to search for. Complete the function below to help her.

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    pass
    keyword_to_indices = {}
    
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(doc_list, keyword)
    return keyword_to_indices