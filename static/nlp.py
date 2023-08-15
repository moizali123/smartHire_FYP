##Importing NLTK Libraries
import nltk
#nltk.download("stopwords")
#nltk.download('wordnet')
#nltk.download('omw-1.4')
#nltk.download('punkt')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer , WordNetLemmatizer
import pandas as pd

def give_keywords(strng_ans):
    #This will tokenize the answer and returns the list of tokens
    tokens_lst = word_tokenize(strng_ans)

    #This will remove the stop words
    stop_words = set(stopwords.words('english'))
    without_sw = []
    for i in tokens_lst:
        if i not in stop_words:
            without_sw.append(i)
    tok_sw = without_sw

    #This will do lemmatizing
    def do_lemmatizing(data,pos):
       lemmatizer = WordNetLemmatizer()
       lemmatized= []
       for j in data:
            lem = lemmatizer.lemmatize(j , pos)
            lemmatized.append(lem)
       return lemmatized
    
    verb_lemmatized = do_lemmatizing(tok_sw,'v')
    adj_lemmatized = do_lemmatizing(verb_lemmatized,'a')
    noun_lemmatized = do_lemmatizing(adj_lemmatized,'n')
    lemmatized_ans = do_lemmatizing(noun_lemmatized,'r')

    tok_sw_lem = lemmatized_ans

    return tok_sw_lem

#example = "This is Operating System apples"

#print(give_keywords(example))


