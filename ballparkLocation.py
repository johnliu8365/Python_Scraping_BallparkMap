
# coding: utf-8

# In[38]:

import requests
from bs4 import BeautifulSoup

r = requests.get("http://mlb.mlb.com/team/index.jsp")
c = r.content

soup = BeautifulSoup(c,"html.parser")

alteam = soup.find_all("ul",{"class":"al team"})
nlteam = soup.find_all("ul",{"class":"nl team"})


# In[67]:

l = []

for item in alteam:
    d={}
    d["teamname"]=item.find("h5").text
    d["ballpark"]=item.find_all("li")[1].text
    d["address"]=item.find_all("li")[2].text
    d["location"]=item.find_all("li")[3].text
    l.append(d)
    
for item in nlteam:
    d={}
    d["teamname"]=item.find("h5").text
    d["ballpark"]=item.find_all("li")[1].text
    d["address"]=item.find_all("li")[2].text
    d["location"]=item.find_all("li")[3].text
    l.append(d)


# In[191]:

base_url="https://maps.googleapis.com/maps/api/geocode/json?address="
import urllib, json

for item in range(0,30):
    r=(base_url+l[item]['address']+l[item]['location']+"&key=AIzaSyCR4MM2pjCyMlU4G29vEEo8LRZAfKLuOeU")
    response = urllib.urlopen(r)
    data = json.loads(response.read())
    l[item]["lng"] = data['results'][0]['geometry']['location']['lng']
    l[item]["lat"] = data['results'][0]['geometry']['location']['lat']


# In[188]:

import pandas
df = pandas.DataFrame(l)


# In[189]:

df


# In[190]:

df.to_csv("ballparkLocation.csv")


# In[ ]:



