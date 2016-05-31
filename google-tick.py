import urllib
import time
import os
import re
import csv
import string

def get_quotes(googleticker):
    url="http://www.google.com/finance?&q="
    txt = urllib.urlopen(url + googleticker).read()
    k = re.search('id="ref_(.*?)">(.*?)<', txt)
    if k:
        tmp = k.group(2)
        q = tmp.replace(',', '')
    else:
        q = "Nothing found for: " + googleticker
    return q

if __name__ == '__main__':
    print (str(get_quotes("TSE:TD")))