#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import requests
import html5lib
import pandas as pd
import re


# In[5]:


q1=requests.get("https://en.wikipedia.org/wiki/Main_Page")
soup=BeautifulSoup(q1.content,"lxml")
hea=soup.find_all("span",class_="mw-headline")
page_header=[]
for i in hea:
    head=i.text
    page_header.append(head)
header_dataframe=pd.DataFrame(data=page_header,columns=['Page Header'])
header_dataframe


# In[6]:


header_dataframe.iloc[1]


# In[7]:


q2=requests.get("https://presidentofindia.nic.in/former-presidents")
soup=BeautifulSoup(q2.content,"lxml")
name=[]
term=[]
hea_name=soup.find_all('h3')
for i in hea_name:
    na=i.text
    name.append(na)
name=pd.DataFrame(name,columns=["Name"]) 
name


# In[8]:


name.loc[1]


# In[9]:


st=requests.get("https://presidentofindia.gov.in/"+str("name.iloc[1]"))


# In[10]:


st


# In[11]:


import pandas as pd


# In[12]:


x=pd.read_html("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")


# In[13]:


db=pd.DataFrame(x[0].head(10))


# In[14]:


db


# In[15]:


y=pd.read_html("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")


# In[16]:


y[0]


# In[17]:


z=y[0][["Pos","Player","Team","Rating"]]


# In[18]:


z.head(10)


# In[19]:


t=pd.read_html("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")


# In[20]:


v=t[0][['Pos','Player','Team','Rating']]


# In[21]:


v.head(10)


# In[22]:


q6=requests.get("https://www.cnbc.com/world/?region=world")


# In[23]:


soup=BeautifulSoup(q6.content,'lxml')


# In[24]:


hline=soup.find_all("a",class_="LatestNews-headline")


# In[25]:


head_line=[]
for i in hline:
    u=i.text
    head_line.append(u)


# In[26]:


time=soup.find_all("time",class_="LatestNews-timestamp")


# In[ ]:





# In[27]:


l_time=[]
for i in time:
    t=i.text
    l_time.append(t)


# In[28]:


link=[]
for i in soup.find_all("a",attrs={'href': re.compile("^https://")}):
    o=i.get("href")
    link.append(o)


# In[29]:


import numpy as np


# In[30]:


link=pd.DataFrame(link,columns=["News Link"])
head_line=pd.DataFrame(head_line,columns=["News Headline"])
l_time=pd.DataFrame(l_time,columns=['News Time'])


# In[31]:


pd.concat([link,head_line,l_time],axis=1)


# In[88]:


paper_tittle=[]
aut=[]
pub_date=[]
paper_url=[]


# In[89]:


j=requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")


# In[90]:


d=BeautifulSoup(j.content,"lxml")


# In[91]:


len(paper_url)


# In[92]:


for i in d.find_all("span",class_="sc-1w3fpd7-0 dnCnAO"):
    aut.append(i.text)
    


# In[93]:


for i in d.find_all("span",class_="sc-1thf9ly-2 dvggWt"):
    pub_date.append(i.text)


# In[94]:


for i in d.find_all("h2"):
    paper_tittle.append(i.text)


# In[95]:


for i in d.find_all("a",attrs={"href": re.compile("^https://www.sciencedirect.com/science/article/pii/")}):
    paper_url.append(i.get("href"))


# In[ ]:





# In[97]:


aut=pd.DataFrame({"Author":aut,"Publish Date":pub_date,'News Tittle':paper_tittle,"News Link":paper_url})


# In[41]:


v=requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")


# In[114]:


rest_name=[]
loc=[]
rat=[]
imgurl=[]


# In[115]:


soup=BeautifulSoup(v.content,'lxml')


# In[116]:


for i in soup.find_all("a",attrs={"href": re.compile("^/delhi/")}):
    rest_name.append(i.get_text("href"))
    
len(rest_name)


# In[117]:


for i in soup.find_all("div",class_="restnt-loc ellipsis"):
    loc.append(i.text)


# In[118]:


for i in soup.find_all("div",class_="restnt-rating rating-4"):
    rat.append(i.text)


# In[119]:


m=soup.find_all("img",class_="no-img")
for i in m:
    imgurl.append(i.get("data-src"))


# In[120]:


c=soup.find_all("span",class_="double-line-ellipsis")
cusine=[]
for i in c:
    t=i.text
    o=t.find("|")
    o=o+1
    #p=t[o:]
    cusine.append(t[o:])
    


# In[121]:


db=pd.DataFrame({"Cusine": cusine,"IMG URL": imgurl,"Rating": rat,"Location":loc,"Res name":rest_name})


# In[122]:


db


# In[ ]:




