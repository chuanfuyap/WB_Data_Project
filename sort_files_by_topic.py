import os
import pandas as pd
import shutil
import numpy as np


###### now files are moved based on their categories/topics
files = filter(os.path.isfile, os.listdir(os.curdir))

files.remove('Data_Sort.ipynb')
files.remove('govdata360.csv')
files.remove('world_bank_data_catalog-Copy1.xls')

catalog = pd.read_excel('world_bank_data_catalog.xls')

all_the_topics = catalog['Topics']

topics = set()
for topic in all_the_topics:
    [topics.add(top.strip()) for top in topic.split(',')]
    
current =catalog[catalog['Last Revision Date'] =='Current']
tmp_catalog = catalog[catalog['Last Revision Date'] !='Current']
index_2017 = [i for i in tmp_catalog.index if tmp_catalog['Last Revision Date'] [i].year==2017]
updated_2017 = catalog.iloc[index_2017]

df = pd.concat([current, updated_2017])
df = df[pd.notnull(df['Bulk Download'])]

what_i_want = df[['Name','Economy Coverage', 'Coverage', 'Topics']]
what_i_want = what_i_want[what_i_want['Topics']!='World Bank Group Projects & Finances']
what_i_want.dropna(inplace=True)

what_i_want.drop([2,5,52,133,135,137,142,152], axis=0, inplace = True)

topics = list(topics)
topics.remove('World Bank Group Projects & Finances')

for topic in topics:
    new_dir = topic
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        
for row in what_i_want.iterrows():
    topic_list = row[1]['Topics'].split(',')
    topic_list = [ topic.strip().lower().replace(' ' , "_") for topic in topic_list]
    name = row[1]['Name'].lower().replace(' ', '_')+'.csv' 
    [shutil.copy(name, topic) for topic in topic_list]