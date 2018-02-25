import pandas as pd
import os 

files = filter(os.path.isfile, os.listdir(os.curdir))
files.remove('cleaning.ipynb')

def get_index(data_list):
    index_list=[]
    for df_ in data_list:
        index_list.extend(df_["Country Name"].unique())
        #print len(df_["Country Name"].unique())
    index_list = list(set(index_list))
    return index_list

def get_indicators(data_list):
    indicators_list=[]
    for df_ in data_list:
        indicators_list.extend(df_["Indicator Name"].unique())
        #print len(df_["Indicator Name"].unique())
    indicators_list = list(set(indicators_list))
    return indicators_list

def wrap_data(data_list, go_here):
    for df_ in data_list:
        coverage_range = list(df_.columns[4:-1])
        #print coverage_range
        for row in df_.iterrows():
            indicator = row[1]['Indicator Name']
            go_here.at['Coverage_Range', indicator]=coverage_range
        for row in df_.iterrows():
            country = row[1]['Country Name']
            indicator = row[1]['Indicator Name']
            time_series = list(row[1].iloc[4:-1])
            go_here.at[country, indicator]=time_series            
            
topic = []
for file_ in files:
    print file_
    df_ = pd.read_csv(file_)
    topic.append(df_)
    
country_index = ['Coverage_Range']
country_index.extend(get_index(topic))

empty_df = pd.DataFrame(index=country_index, columns=get_indicators(health))

wrap_data(health, empty_df)

empty_df.to_csv('INSERT_TOPIC_NAME.csv')