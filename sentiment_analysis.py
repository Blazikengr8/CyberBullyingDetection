import pickle
import os
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem import PorterStemmer
import pandas as pd

# responses = ['']

def analyze(text):
    vectorizer = pickle.load(open('vectorizer.sav', 'rb'))
    classifier = pickle.load(open('classifier.sav', 'rb'))
    # text=input()
    tokens = word_tokenize(text)
    tag = pos_tag(tokens)
    flag=False #if pronoun other than I, me, mine etc (first person pronouns)
    print(tag)
    ps=PorterStemmer()
    words=pd.read_csv('Excel_Swear_dic.csv')
    word=words['word']
    #print(word[0])
    res = any(ele in text for ele in word) #profanity check (checks for slurs)
    for i in tag:
        if i[1] == 'PRP':
            if not ps.stem(i[0]) == 'i' or ps.stem(i[0]) == 'me' or ps.stem(i[0]) == 'my':
                flag=True
    vector_text=vectorizer.transform([text])
    result=classifier.predict(vector_text) #checks if the sentence is positive or negative
    if flag==True and result==['neg'] and res == True:
        return 0
        print(flag,result,res)
    else:
        return 1
        print(flag,result,res)
#print(result)