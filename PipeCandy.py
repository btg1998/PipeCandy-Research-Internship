#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 17:14:38 2017

@author: bhargav
"""

# Importing the required packages and functions
from urlparse import urlparse
#import yaml
import string as str

# List of key-words which we want for it to be a Product URL
key=['shop','book','product','products','id','ids','item','items',
     'pid','deals','store']

# List of Domain Names which if present in a URL we don't want to explore further
do=['linkedin','facebook','twitter','youtube','instagram','pinterest','plus_google',
     'angel','google'] 

# List of non key-words which we want for it to be a non-Product URL
nkey=['service', 'contact', 'support', 'exchange', 'return', 'help', 'wallet', 'balance', 'dashboard',
     'jobs', 'sell', 'customer', 'location', 'services', 'about', 'about-us', 'welcome', 'our-story',
     'story', 'stories', 'helpcentre', 'help', 'contact', 'contact us', 'shipping', 'handling', 'ordering',
     'delivery', 'order', 'track', 'policy', 'policies', 'privacy', 'security', 'question', 'questions', 'cancellation',
     'returns', 'return', 'exchange', 'cancel', 'press', 'blog', 'terms', 'conditions', 'faq', 'join', 'join-us', 'team',
     'teams', 'careers', 'career', 'payments', 'pricing', 'payment', 'price', 'about', 'about-us', 'welcome',
     'our-story', 'story', 'stories', 'helpcentre', 'help', 'contact', 'contact us', 'shipping', 'handling', 'ordering',
     'delivery', 'order', 'track', 'policy', 'policies', 'privacy', 'security', 'question', 'questions', 'cancellation',
     'returns', 'return', 'exchange', 'cancel', 'press', 'blog', 'terms', 'conditions', 'faq', 'join', 'join-us', 'team',
     'teams', 'careers', 'career', 'payments', 'pricing', 'payment', 'contact', 'contact-us', 'helpcentre', 'help',
     'about', 'about-us', 'welcome', 'our story', 'stories', 'story', 'linkedin', 'facebook', 'twitter', 'youtube',
     'instagram', 'pinterest', 'plus_google', 'angel', 'faq', 'terms', 'conditions', 'terms-conditions',
     'privacy', 'policy', 'policies', 'question', 'questions', 'security', 'press', 'blog', 'careers', 'career', 'join-us',
     'join', 'team', 'teams', 'payments', 'pricing', 'payment', 'shipping', 'handling', 'delivery-order', 'track',
     'ordering', 'exchange', 'return', 'cancellation', 'cancel', 'returns','store','store-locator']
'''
# Loading and importing more non key-words from an external .yaml file
with open("keywords.yaml", 'r') as stream:
    out = yaml.load(stream)

# A list to store all the non key-words from the external file
nk=[]

# Converting the non key-words to a list
for i in out.keys():
    if type(out[i])==list:
        nk=nk+out[i]

# Removing the unneccesary / if it is present 
for i in range(len(nk)):
    if nk[i][0]=='/':
        nk[i]=nk[i][1:]

# Creating the final non key-words list
nkey=nkey+nk

print nkey

# To remove duplicates if any
nkey=list(set(nkey))
'''
# Function to check if there are n-grams present in the given URL
def ngram(st):
    a=0
    b=0
    for i in st:
        a=max(a,i.count('-'))
    if a==0:
        for i in st:
            b=max(b,i.count('_'))        
    return a+b


# Function to check if there are key-words for a Product URL in the given URL
def keys(st):
    c=0
    for i in st:
        i=str.lower(i)
        for j in key:
            if i.find(j)!=-1:
                c=c+1
    return c


# Function to check if there are non key-words for a non-Product URL in the given URL
def nkeys(st):
    c=0
    for i in st:
        i=str.lower(i)
        for j in nkey:
            if i.find(j)!=-1:
                c=c+1
    return c

# Function to check if the URL contains Domain Names which if present in a URL we don't want to explore further
def dom(st):
    for i in do:
        if i in st:
            return True
    return False


# The Final Function which takes any URL as an input and combines the usage of the above functions and
# returns -1: if it's a non product URL
# reurns 1: if it's a product URL
# returns 0: if the URL when further explored will lead to Product URLs like a product Listing Page
def pipe(url):
    parse_object = urlparse(url)
    domn=parse_object.netloc
    comp=parse_object.path.rsplit('/')
    comp.append(domn)
    ng=ngram(comp)
    k=keys(comp)
    nk=nkeys(comp)
    if nk>=1:
        return -1
    elif dom(domn):
        return -1
    elif (ng>=1 or k>=1):
        return 1
    else:
        return 0

# Usage note: This script can easily be integrated to any crawler by just importing this Python Scipt File
# and using the Function pipe which i have defined here to judge if the given URL is a Product one or not.
# An example usage:

print pipe('https://www.oliversweeney.com/store-locator/')

    
    
        
    
    


        

    
    
