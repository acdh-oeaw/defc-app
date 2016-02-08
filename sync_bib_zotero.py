
# coding: utf-8

# In[96]:

import requests, json, sys
from bib.models import Book
from orea.settings.ksenia_local import Z_USER_ID, Z_COLLECTION, Z_API_KEY


# In[97]:

root = "https://api.zotero.org/users/"
params = "{}/collections/{}/items/top?v=3&key={}".format(Z_USER_ID,
                                                         Z_COLLECTION,
                                                         Z_API_KEY)
url = root+params+"&sort=dateModified&limit=100"


# In[98]:

try:
    r = requests.get(url)
except:
    sys.exit("aa! errors!")


# In[86]:

response = r.json()


# In[95]:

failed = []
saved = []
for x in response:
    NewBook = Book(zoterokey = x["data"]["key"],
                      item_type =x["data"]["itemType"],
                      author=x["data"]["creators"][0]["name"],
                      title =x["data"]["title"],
                      short_title = x["data"]["shortTitle"])
    try:
        NewBook.save()
        saved.append(x['data'])
    except:
        failed.append(x['data'])
print('saved: {} objects \nfailed: {} objects'.format(len(saved), len(failed)))


# In[53]:

datalist = response[1]


# In[54]:

type(datalist)


# In[57]:

c = 0
failed = []
saved = []
for row in datalist.items:
    print(row)
print('saved: {} objects \n failed: {} objects'.format(len(saved), len(failed)))


# In[47]:

failed


# In[37]:

for row in response:
    print(row["data"])


# In[ ]:



