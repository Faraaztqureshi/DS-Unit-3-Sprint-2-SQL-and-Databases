#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install psycopg2-binary


# In[1]:


import psycopg2


# In[2]:


dir(psycopg2)


# In[3]:


## Set up steps

dbname = 'qdesulho'
user = 'qdesulho'
password = 'JGeDV6muogRvBZvrAfYst69Yeb9mQlBg'
host = 'rajje.db.elephantsql.com'


# In[13]:


pg_conn = psycopg2.connect(dbname=dbname, user=user, 
                           password=password, host = host)


# In[14]:


## check to see if we have a connection object
pg_conn


# In[15]:


## make a cursor
pg_curs = pg_conn.cursor()


# In[16]:


## structure of the table you want to create
create_table_statement = """
CREATE TABLE test_table (
  id        SERIAL PRIMARY KEY,
  name  varchar(40) NOT NULL,
  data    JSONB
);
"""

## code to create the table you wanted
pg_curs.execute(create_table_statement)

## commiting the changes
pg_conn.commit()


# In[17]:


## data for the table you created

insert_statement = """
INSERT INTO test_table (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
"""

## puts the data into the table
pg_curs.execute(insert_statement)

## commits the changes you made
pg_conn.commit()


# In[18]:


## SQL search
query = 'SELECT * FROM "public"."test_table" LIMIT 100'

## do the search
pg_curs.execute(query)

##s show the results
pg_curs.fetchall()


# ## RPG Data

# In[22]:


import sqlite3


# In[26]:


sl_conn = sqlite3.connect('rpg_db.sqlite3')


# In[27]:


sl_curs = s1_conn.cursor()


# In[28]:


row_count = 'SELECT COUNT(*) FROM charactercreator_character'
sl_curs.execute(row_count).fetchall()


# In[31]:


## we want to move characters from sqlite3 to postgres
## select the characters
get_characters = '''SELECT * FROM charactercreator_character'''

## execute search and save results
characters = sl_curs.execute(get_characters).fetchall()


# In[33]:


## examine first 5 results
characters[:5]


# In[34]:


## count how many results
len(characters)


# In[35]:


## since we are moving from sqlite3 to postgreSQL we need to see how data was structured
sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()


# In[36]:


## we now need to create a table to put this information into
create_character_table = '''
CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
);
'''


# In[38]:


## I got an error so I re-established the connection
pg_conn = psycopg2.connect(dbname=dbname, user=user, 
                           password=password, host = host)
## make a cursor
pg_curs = pg_conn.cursor()


# In[39]:


## create the table using the pg_cursor
pg_curs.execute(create_character_table)

## save changes
pg_conn.commit()


# In[40]:


## look at tables
show_tables = """
SELECT
   *
FROM
   pg_catalog.pg_tables
WHERE
   schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""
pg_curs.execute(show_tables)
pg_curs.fetchall()


# In[46]:


## in case you make a mistake you can delete all the rows
delete_table_rows = '''DELETE FROM charactercreator_character
'''
pg_curs.execute(delete_table_rows)
pg_conn.commit()


# In[47]:


## execute and commit deletion of rows
pg_curs.execute('SELECT * FROM charactercreator_character')
pg_curs.fetchall()


# In[48]:


for character in characters:
    insert_character = '''
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES ''' + str(character[1:]) + ";"
    
    pg_curs.execute(insert_character)
    pg_conn.commit()


# In[50]:


pg_curs.execute('SELECT * FROM charactercreator_character')
len(pg_curs.fetchall())


# ## TITANIC

# ### Create new tables for database

# In[51]:


## create a table for passengers
passengers_table = '''
CREATE TABLE passengers (
id SERIAL PRIMARY KEY,
name TEXT,  
sex TEXT, 
age FLOAT,
sibsp INT,
parch INT
)
'''
pg_curs.execute(passengers_table)
pg_conn.commit()


# In[52]:


## create a survival table
survival_table = '''
CREATE TABLE survival (
id SERIAL PRIMARY KEY,
survived INT
)
'''
pg_curs.execute(survival_table)
pg_conn.commit()


# In[54]:


## create a fare info table
fare_info = '''
CREATE TABLE fare_info (
id SERIAL PRIMARY KEY,
pclass INT,
ticket TEXT,
fare FLOAT,
cabin TEXT,
embarked TEXT
)
'''
pg_curs.execute(fare_info)
pg_conn.commit()


# ### Move data from CSV to Database

# In[59]:


## re-establish connection
pg_conn = psycopg2.connect(dbname=dbname, user=user, 
                           password=password, host = host)
## make a cursor
pg_curs = pg_conn.cursor()


# In[60]:


with open('passengers.csv', 'r') as row:
    next(row)# Skip the header row.
    pg_curs.copy_from(row, 'passengers', sep=',')
    
with open('survival.csv', 'r') as row:
    next(row) 
    pg_curs.copy_from(row, 'survival', sep=',')

with open('trip_info.csv', 'r') as row:
    next(row)
    pg_curs.copy_from(row, 'fare_info', sep=',')
    
pg_conn.commit()    


# ## Run a query to show that it works

# In[64]:


query = '''
SELECT * FROM "public"."fare_info" LIMIT 100
'''
pg_curs.execute(query)
pg_curs.fetchall()


# In[ ]:




