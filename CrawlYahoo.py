# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 10:21:14 2022

@author: charl
"""

import requests

r = requests.get('https://tw.yahoo.com/?guccounter=1')

if r.status_code == 200:
    print(r.text)