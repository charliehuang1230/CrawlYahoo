# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 10:21:14 2022

@author: charl
"""

import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.google.com.tw/')

if r.status_code == 200:
    # print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    print(soup.title)