from typing import get_args
from bs4 import BeautifulSoup
import requests
url,see,rank= 'https://www.imdb.com/india/top-rated-indian-movies/',[],0
res=requests.get(url)
soup=BeautifulSoup(res.text,'html.parser')
tbody=soup.find('tbody', class_='lister-list')
trs=tbody.find_all('tr')
for i in trs:
    rank+=1
    tds,movies=i.find('td', class_='titleColumn'),{}
    ran,nam,link=tds.find('span'),tds.find('a'),'https://www.imdb.com/'+tds.a['href']
    rating=i.find('td',class_='ratingColumn imdbRating').strong
    movies['Rank'],movies['Name'],movies['Year'],movies['Rating'],movies['Link']=rank,nam.text,ran.text,rating.text,link
    see.append(movies)
task={}
for i in see:
    c=''
    for s in i['Year']:
        if s.isnumeric():
            c+=s
    b=int(c)//10
    b*=10
    if b not in task:
        task[b]=[]
for j in task:
    for i in see:
        c=''
        for s in i['Year']:
            if s.isnumeric():
                c+=s
        if j<=int(c)<(j+10):
            task[j].append(i)
print(task)