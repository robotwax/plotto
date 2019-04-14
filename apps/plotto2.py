import datetime
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame
import numpy as np
import json

d = datetime.datetime.now()
f = []
f.append(d)
f = str(f)
g = f.replace('[datetime.datetime(', '')
k = g[:4]
m = int(k)
bk = []
for i in range(1988, m):
    bk.append(i)
z = len(bk)
bz = []
i = 0
for i in bk:
    while len(bz) <= z:
        gb = "https://www.irishlottery.com/archive-"
        kz = gb + str(i)
        bz.append(kz)
        i += 1
x = []
for i in range(0, z):
    x.append(i)
c = 0
def plotto_2():
    gg = []
    sky = []
    for c in x:
        while len(gg) <= len(bz)-1:
            url = bz[c]
            print(url)
            html = urlopen(url)
    
            soup = BeautifulSoup(html, 'lxml')
    
            # Get the title
            table = soup.findAll('table')[0] 
            df = pd.read_html(str(table))
            df= (df[0].to_json(orient='split'))
    
            df = pd.read_json(df, orient='split')
            lendf = (len(df)-1)
            gg.append(lendf)
    
            i = 2
            while i <= lendf:
                df1 = df.loc[[i], 'Draw Result:'].tolist()
                clean = str(df1)
                clean = clean.replace("\'", "")
                clean = clean.replace(" ", ", ")
                clean = clean.replace("list(", "")
                clean = clean.replace(")", "")
                newlist = 'clean = ' + clean
                exec(newlist)
                sky.append(clean)
                i += 1
            c += 1
            if len(gg) == len(bz):
                with open('gg.txt', 'w') as outfile:
                    json.dump(gg, outfile)
                with open('sky.txt', 'w') as outfile:
                    return json.dump(sky, outfile)
                
