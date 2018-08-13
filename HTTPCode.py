#!/usr/bin/env python
import requests
import urllib.request
app=['/shop1','/products','/categories','/collections','/catalog',
     'catalog/products','catalog/product_list']
def func(domn):
    try:
        t="http://"+domn
        dom=domn[0:domn.find('.')]
        for i in app:
            url=t+i
            r = requests.head(url)
            print(r.status_code)
            if r.status_code==200:
                print(url)
                return url
            elif r.status_code==302 or r.status_code==301:
                try:
                    resp=urllib.request.urlopen(url)
                    finalurl=resp.geturl()
                    print('Final URL:') 
                    print(finalurl)
                    if dom in finalurl:
                        return finalurl
                except:
                    return None
        return None
    except requests.ConnectionError:
        print("failed to connect")
func('shop.panthers.com')

