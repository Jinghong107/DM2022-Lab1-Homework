import nltk
from nltk.corpus import stopwords

"""
Helper functions for data mining lab session 2018 Fall Semester
Author: Elvis Saravia
Email: ellfae@gmail.com
"""

def format_rows(docs):
    """ format the text field and strip special characters """
    D = []
    for d in docs.data:
        temp_d = " ".join(d.split("\n")).strip('\n\t')
        D.append([temp_d])
    return D

def format_labels(target, docs):
    """ format the labels """
    return docs.target_names[target]

def check_missing_values(row):
    """ functions that check and verifies if there are missing values in dataframe """
    counter = 0
    for element in row:
        if element == True:
            counter+=1
    return ("The amoung of missing records is: ", counter)

def tokenize_text(text, remove_stopwords=False):
    """
    Tokenize text using the nltk library
    """
    tokens = []
    for d in nltk.sent_tokenize(text, language='english'):
        for word in nltk.word_tokenize(d, language='english'):
            # filters here
            tokens.append(word)
    return tokens
def tokenize_text_stopwords(Y):
    """
    Delete Tokenize stop-words text using the nltk library
    """
    stops = stopwords.words('english')
    new_array = []

    for i in range(len(Y)):
        tokens = []
        for d in nltk.sent_tokenize(Y.iloc[i], language='english'):
            for word in nltk.word_tokenize(d, language='english'):
                if word not in stops:
                    # print(word)
                    tokens.append(word)
                new = ' '.join(tokens)
        new_array.append(new)
    return new_array