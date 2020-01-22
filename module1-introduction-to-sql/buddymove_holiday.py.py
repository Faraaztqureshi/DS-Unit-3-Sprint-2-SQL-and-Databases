#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

# make a connection
conn = sqlite3.connect('/Users/faraazqureshi/repos/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3')


# In[2]:


# make a cursor
curs = conn.cursor()


# ## Total Characters

# In[3]:


# determine how many total characters
curs.execute('SELECT count(*) FROM charactercreator_character')
print(curs.fetchall())


# ## Total characters of each subclass

# In[6]:


# how many characters of each subclass
curs.execute('SELECT count(*) FROM charactercreator_cleric')
print("Cleric count: " + str(curs.fetchall()))


# In[8]:


curs.execute('SELECT count(*) FROM charactercreator_fighter')
print("Fighter count: " + str(curs.fetchall()))


# In[9]:


curs.execute('SELECT count(*) FROM charactercreator_mage')
print("Mage count: " + str(curs.fetchall()))


# In[10]:


curs.execute('SELECT count(*) FROM charactercreator_necromancer')
print("Necromancer count: " + str(curs.fetchall()))


# In[11]:


curs.execute('SELECT count(*) FROM charactercreator_thief')
print("Thief count: " + str(curs.fetchall()))


# ## How many total items

# In[12]:


curs.execute('SELECT count(*) FROM armory_item')
print("Total Items: " + str(curs.fetchall()))


# ## Of the total items how many are weapons

# In[22]:


# total number of items
curs.execute('SELECT count(*) FROM armory_item')
curs.fetchall()


# In[19]:


# total number of items that are weapons method 1
curs.execute('SELECT count(*) FROM armory_item, armory_weapon WHERE armory_item.item_id = armory_weapon.item_ptr_id')
print("Number of items that are weapons: " + str(curs.fetchall()))


# In[17]:


# total nmber of items that are weapons method 2
curs.execute('SELECT count(*) FROM armory_item JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id')
print("Number of items that are weapons: " + str(curs.fetchall()))


# ## How many items does each character have

# In[24]:


'''SELECT charactercreator_character.character_id, charactercreator_character.name,  count(armory_item.item_id)
FROM charactercreator_character, armory_item, charactercreator_character_inventory
WHERE charactercreator_character.character_id = charactercreator_character_inventory.character_id
AND armory_item.item_id = charactercreator_character_inventory.item_id
GROUP BY charactercreator_character.character_id
ORDER BY count(armory_item.item_id) DESC
LIMIT 20;
'''
curs.execute('SELECT charactercreator_character.character_id, charactercreator_character.name,  count(armory_item.item_id) FROM charactercreator_character, armory_item, charactercreator_character_inventory WHERE charactercreator_character.character_id = charactercreator_character_inventory.character_id AND armory_item.item_id = charactercreator_character_inventory.item_id GROUP BY charactercreator_character.character_id ORDER BY count(armory_item.item_id) DESC LIMIT 20;')
curs.fetchall()


# ## How many weapons does each character have?

# In[25]:


query = '''
SELECT charactercreator_character.character_id, charactercreator_character.name,  count(armory_weapon.item_ptr_id)
FROM charactercreator_character, armory_weapon, charactercreator_character_inventory
WHERE charactercreator_character.character_id = charactercreator_character_inventory.character_id
AND armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
GROUP BY charactercreator_character.character_id
ORDER BY count(armory_weapon.item_ptr_id) DESC
LIMIT 20;
'''


# In[27]:


curs.execute(query)
curs.fetchall()


# ## AVG Number of Items

# In[31]:


((58 * 5) +(62 * 4) + (64 * 3) + (50* 2) + (68 * 1)) / 302


# In[28]:


58 + 62 + 64 +50


# In[29]:


302-234


# In[32]:


import pandas as pd


# In[34]:


query = '''SELECT charactercreator_character.character_id, charactercreator_character.name,  count(armory_item.item_id)
FROM charactercreator_character, armory_item, charactercreator_character_inventory
WHERE charactercreator_character.character_id = charactercreator_character_inventory.character_id
AND armory_item.item_id = charactercreator_character_inventory.item_id
GROUP BY charactercreator_character.character_id
ORDER BY count(armory_item.item_id) DESC;
'''
curs.execute(query)
items_data = curs.fetchall()


# In[35]:


df1 = pd.DataFrame(items_data)


# In[38]:


df1.head()


# In[41]:


import numpy as np
np.mean(df1[2])


# ## AVG Number of weapons

# In[42]:


query = '''
SELECT charactercreator_character.character_id, charactercreator_character.name,  count(armory_weapon.item_ptr_id)
FROM charactercreator_character, armory_weapon, charactercreator_character_inventory
WHERE charactercreator_character.character_id = charactercreator_character_inventory.character_id
AND armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
GROUP BY charactercreator_character.character_id
ORDER BY count(armory_weapon.item_ptr_id) DESC;
'''
curs.execute(query)
weapons_data = curs.fetchall()


# In[44]:


df2 = pd.DataFrame(weapons_data)
np.mean(df2[2])


# # Assignment Part 2

# In[45]:


df = pd.read_csv('buddymove_holidayiq.csv')
df.head()


# In[46]:


df.isnull().sum()


# In[47]:


df.shape


# In[58]:


conn = sqlite3.connect('buddymove_holidayiq.sqlite3')


# In[ ]:


c = conn.cursor()


# In[59]:


from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)


# In[60]:


df.to_sql("Reviews", con = engine)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[61]:


conn = sqlite3.connect('/Users/faraazqureshi/repos/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv')


# In[62]:


curs = connection.cursor()


# In[63]:


type(curs)


# In[ ]:


query = 


# In[ ]:





# In[50]:


connection = conn = sqlite3.connect('/Users/faraazqureshi/repos/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.sqlite3')


# In[ ]:




