# Import/download that only needs to be run once
# import nltk
# nltk.download('stopwords')
#####################################
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.util import ngrams
import re


def tokenize_words(row_dict):
    """Function that takes a dictionary of summary and description strings. Converts the strings to lowercase. Then
    splits the strings on white space to tokenize into words. Using the nltk library it also removes all stopwords from
    the words."""

    tokenized_dict = {}
    stop_words = set(stopwords.words('english'))
    porter_stemmer = SnowballStemmer("porter")

    for row_key in row_dict:
        summary = row_dict[row_key][0].lower().split() #split the sentences into word tokens
        description = row_dict[row_key][1].lower().split()
        summary_filtered = []
        description_filtered = []
        for word in summary:
            if word not in stop_words: #check if the word is an unwanted stop word
                stem_word = porter_stemmer.stem(word).encode('ascii', 'ignore') #stem the word
                if re.match('^[\w-]+$', stem_word) is not None: summary_filtered.append(stem_word) #rematch to check for non alphanumeric characters, append if none

        for word in description:
            if word not in stop_words:
                stem_word = porter_stemmer.stem(word).encode('ascii', 'ignore')
                if re.match('^[\w-]+$', stem_word) is not None: description_filtered.append(stem_word)

        tokenized_dict[row_key] = (summary_filtered, description_filtered)
    return tokenized_dict

def ngram_generator(wordList, n):
    """ngram generater, currently unused code"""
    outputSet= set()
    createdNgrams = ngrams(wordList, n)
    for i in createdNgrams:
        outputSet.add(i)

    return outputSet
