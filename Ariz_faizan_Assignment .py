#!/usr/bin/env python
# coding: utf-8

# In[741]:


import numpy as np
import pandas as pd
import re


# In[742]:


pat='Python Exercises, PHP exercises.'


# In[743]:


re.sub('[\s,.]',":",pat)


# In[744]:


pat1='australia germany england america ariz nagaland new'


# In[745]:


print(re.findall(r'\b[a|n]\w*\b',pat1,flags=re.I))


# In[746]:


pat2="i am a Data Scien Ariz rehan"


# In[747]:


reg_pat=r'\b\w{4}\b'


# In[748]:


pat_com=re.compile(reg_pat)


# In[749]:


type(pat_com)


# In[750]:


pat_com.findall(pat2)


# In[751]:


reg1_pat=r'\b\w{3,5}\w\b'


# In[752]:


pat1_com=re.compile(reg1_pat)


# In[753]:


pat1_com.findall(pat2)


# In[754]:


q5="example (.com) hr@fliprobo (.com) github (.com) Hello (Data Science World) Data (Scientist)"


# In[755]:


re.sub(r'[()+\s]', ' ',q5)


# In[756]:


q6= "example (.com) hr@fliprobo (.com) github (.com) Hello (Data Science World) Data (Scientist)"


# In[757]:


re.findall(r'[a-zA-Z]+\s',q6)


# In[758]:


q8="RegularExpression1IsAn2ImportantTopic3InPython"


# In[759]:


re.sub(r'([nc])(\d{1,2,})', r'\1 \2', q8)


# In[760]:


q9="RegularExpression1IsAn2ImportantTopic3InPython"


# In[761]:


re.sub(r'(\w)([A-Z])', r'\1 \2',q9)


# In[762]:


q7="ImportanceOfRegularExpressionsInPython"


# In[763]:


re.sub(r'(\w)([A-Z])',r'\1 \2',q7)


# In[764]:


q10='''Hello my name is Data Science and my email address is xyz@domain.com and alternate email
address is xyz.abc@sdomain.domain.com. 
Please contact us at hr@fliprobo.com for further information.'''


# In[765]:


re.findall('\S+@\S+',q10)


# In[787]:


q14='''On August 15th 1947 that India was declared independent from British colonialism 
and the reins of control were handed over to the leaders of the Country’.'''


# In[788]:


re.sub(r'(\s)','',q14)


# In[909]:


re.findall(r'[A][a-z]+\s[a-z0-9]+\s[0-9]+',q14)


# In[895]:


q30='''The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added 
to the ArrayList and the ArrayList is trimmed accordingly.'''


# In[ ]:





# In[770]:


pat30=r'\b\w{2,4}\b'


# In[771]:


re.sub(pat30,"",q30)


# In[772]:


q29="Ron was born on 12-09-1992 and he was admitted to school 15-12-1999"


# In[773]:


re.findall(r'\S*[0-9]',q29)


# In[774]:


q28='''@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>
Those who  are protesting #demonetization  are all different party leaders'''


# In[775]:


re.sub(r'[+U00ABD8]',"",q28)


# In[776]:


q27='''RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS 
<ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo'''


# In[777]:


re.findall(r'#\S+',q27)


# In[778]:


q22='My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'


# In[779]:


v=re.findall(r'\d+',q22)


# In[780]:


v=map(int,v)


# In[781]:


max(v)


# In[782]:


q25="Hello hello world world"


# In[783]:


re.sub(r'\b(\w+)( \1\b)+', r'\1',q25)


# In[ ]:




