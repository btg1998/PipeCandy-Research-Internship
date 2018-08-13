#!/usr/bin/env python
import requests
import urllib2
app=['/categories','/shop','/products','/collections','/catalog',
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
                ans=[]
                ans.append(url)
                if i=='/categories':
                    ans.append('BigCommerce')
                if i=='/shop' or i=='/products':
                    ans.append('WooCommerce')
                    ans.append('Shopify')
                if i=='/collections':
                    ans.append('Shopify')
                if i=='/catalog' or i=='/catlog/products' or i=='catalog/product_list':
                    ans.append('OpenCart')
                    ans.append('PrestaShop')
                print(ans)
                return ans
            elif r.status_code==302 or r.status_code==301:
                try:
                    resp=urllib2.urlopen(url)
                    finalurl=resp.geturl()
                    print('Final URL:') 
                    print(finalurl)
                    ans=[]
                    if dom in finalurl:
                        ans.append(finalurl)
                        if i=='/categories':
                            ans.append('BigCommerce')
                        if i=='/shop' or i=='/products':
                            ans.append('WooCommerce')
                            ans.append('Shopify')
                        if i=='/collections':
                            ans.append('Shopify')
                        if i=='/catalog' or i=='/catlog/products' or i=='catalog/product_list':
                            ans.append('OpenCart')
                            ans.append('PrestaShop')
                        print(ans)
                        return ans
                    else:
                        return None
                except:
                    continue
        return None
    except requests.ConnectionError:
        print("failed to connect")
func('shultzilla.com')

