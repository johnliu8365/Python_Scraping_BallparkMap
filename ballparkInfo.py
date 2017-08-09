
# coding: utf-8

# In[17]:

import requests
from bs4 import BeautifulSoup

r = requests.get("https://en.wikipedia.org/wiki/List_of_current_Major_League_Baseball_stadiums")
c = r.content.decode('utf-8')

soup = BeautifulSoup(c,"html.parser")
for row in soup.find_all("sup",{"class":"reference"}):
    cells = row.find('a')
    cells.replace_with('')

print soup.prettify()


# In[18]:

right_table=soup.find("table", {"class":"wikitable sortable plainrowheaders"})
right_table


# In[19]:

l=[]

for row in right_table.find_all("tr"):
    d={}
    cells = row.find_all('td')
    states = row.find_all('th') #To store second column data
    if len(cells)==8: #Only extract table body not heading
        d["Name"]=states[0].text
        d["Seating capacity"]=cells[1].text
        d["Location"]=cells[2].text
        d["Playing surface"]=cells[3].text
        d["Team"]=cells[4].text
        d["Opened"]=cells[5].text
        d["Distance to center field"]=cells[6].text
        d["Ballpark typology"]=cells[7].text
        
    elif len(cells)==9:
        d["Name"]=cells[1].text
        d["Seating capacity"]=cells[2].text
        d["Location"]=cells[3].text
        d["Playing surface"]=cells[4].text
        d["Team"]=cells[5].text
        d["Opened"]=cells[6].text
        d["Distance to center field"]=cells[7].text
        d["Ballpark typology"]=cells[8].text
        
    l.append(d)
    
l


# In[20]:

import pandas
df = pandas.DataFrame(l).drop([0])


# In[21]:

df


# In[23]:

df.to_csv("BallparkInfo.csv", encoding='utf-8')


# In[ ]:



