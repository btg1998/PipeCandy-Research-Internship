#!/usr/bin/env python

# coding: utf-8

# Importing the necessary Packages and functions
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import os
import math
import sklearn
from collections import Counter
from sklearn.linear_model import LogisticRegression

# A function to tokenize the URLs
def getTokens(input):
	tokensBySlash = str(input.encode('utf-8')).split('/')	#get tokens after splitting by slash
	allTokens = []
	for i in tokensBySlash:
		tokens = str(i).split('-')	#get tokens after splitting by dash
		tokensByDot = []
		for j in range(0,len(tokens)):
			tempTokens = str(tokens[j]).split('.')	#get tokens after splitting by dot
			tokensByDot = tokensByDot + tempTokens
		allTokens = allTokens + tokens + tokensByDot
	allTokens = list(set(allTokens))	#remove redundant tokens
	if 'com' in allTokens:
		allTokens.remove('com')	#removing .com since it occurs a lot of times and it should not be included in our features
	if 'www' in allTokens:
		allTokens.remove('www')	#removing www since it occurs a lot of times and it should not be included in our features
	if 'http' in allTokens:
		allTokens.remove('http')	#removing http since it occurs a lot of times and it should not be included in our features
	if 'https' in allTokens:
		allTokens.remove('https')        #removing .com since it occurs a lot of times and it should not be included in our features
  
	return allTokens



def TL():
                #Enter the path to our all urls file, I have used the path where the file is in my System.
	allurls = 'Sheet containing URLs for training ML Model.csv'
	
	allurlscsv = pd.read_csv(allurls,',',error_bad_lines=False)	#reading file
	
	allurlsdata = pd.DataFrame(allurlscsv)	#converting to a dataframe

	allurlsdata = np.array(allurlsdata)	#converting it into an array
	random.shuffle(allurlsdata)	#shuffling

	y = [d[1] for d in allurlsdata]	#all labels 
	corpus = [d[0] for d in allurlsdata]	#all urls corresponding to a label (either product or non-product)
	vectorizer = TfidfVectorizer(tokenizer=getTokens)	#get a vector for each url but use our customized tokenizer which we defined above
	X = vectorizer.fit_transform(corpus)	#get the X vector
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=108)	#split into training and testing set 80/20 ratio
    
                 # Here I have used Logistic Regression as the Algo for Classification as it gave me the highest accuracy
                 # but we can also try various models as our Data Set Evolves 
	lgs = LogisticRegression()	#using logistic regression
	lgs.fit(X_train, y_train)
	print(lgs.score(X_test, y_test)) 	#Printing the accuracy score
	return vectorizer, lgs # Here we are returning the function used to Vectorize the URL as well as the model to be used for prediction


# Running the model and getting the vectorizer and the model to be used for prediction from TL function
vec,mod =  TL()

# URLs that we have to predict
X_predict = ['https://faucetface.com/pages/stores']

# Transforming the URLs
X_predict = vec.transform(X_predict)

# Predicting based on the model
y_Predict = mod.predict(X_predict)

# Printing the results
print(y_Predict)

