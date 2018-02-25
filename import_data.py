import pandas as pd
import requests
import zipfile
import io
import re
import os

def get_data_from_url(url, name):
    url=url.strip()
    url_data = requests.get(url)    
    extension = url[-4:]
    print(extension)
    if extension == '.zip':
        z = zipfile.ZipFile(io.BytesIO(url_data.content))
        directory_name = 'data/'+name.replace(' ','_')
        os.makedirs(directory_name)
        z.extractall(directory_name)
    elif extension == '.csv':
        try:
            df = pd.read_csv(io.StringIO(url_data.content.decode('utf-8')))
        except:
            df = pd.read_csv(io.StringIO(url_data.content.decode('latin-1')))
        name = name.replace('/', '_')
        output_path = 'data/'+name.lower().replace(' ','_')+extension        
        df.to_csv(output_path)
    else:
        file_name= 'data/'+name.lower().replace(' ','_')+'.xls'
        output = open(file_name, 'wb')
        output.write(url_data.content)
        output.close()
        
        
def get_url(bulk_download): 
    if r'(CSV)' in bulk_download:
        output =re.search(r'(CSV).*(https*://.*[.zip|.csv])',bulk_download).group()
        output=re.search(r'https*://.*[zip|xls|xlsx|csv](?!;)',output).group()
        output=output.split(';')
        output=output[0]
        print('csv')
    elif r'(Excel)' in bulk_download:
        output=re.search(r'(Excel).*(https*://.*[.zip|.xls|.xlsx])',bulk_download).group()
        output=re.search(r'https*://.*[.zip|.xls|.xlsx|.csv]',output).group()
        output=output.split(';')
        output=output[0]
        print('xls')
    else:
        output=re.search(r'https*://.*[.zip|.xls|.xlsx|.csv]',bulk_download).group()
        output=output.split(';')
        output=output[0]
        print('random')
    unwanted = ['=csv','=xml','=excel','=zip']
    for i in unwanted:
        if i in output.lower():
            output=output.replace(i,'')
    return output

catalog = pd.read_excel('world_bank_data_catalog.xls')
current =catalog[catalog['Last Revision Date'] =='Current']
for index, series in enumerate(current.iterrows()):
    name = series[1]['Name']
    link = series[1]['Bulk Download']
    download_link = get_url(link)
    print(index, series[0],download_link,name) ##prints index to track links are faulty
    get_data_from_url(download_link, name)
    
tmp_catalog = catalog[catalog['Last Revision Date'] !='Current']
index_2017 = [i for i in tmp_catalog.index if tmp_catalog['Last Revision Date'] [i].year==2017]
updated_2017 = catalog.iloc[index_2017]
links_2017 = updated_2017[['Name','Bulk Download']].dropna()
links_2017.drop(66, inplace=True) ##dropping data i don't want
links_2017.drop(153, inplace=True)##dropping data i don't want

for index, series in enumerate(links_2017.iterrows()):
    name = series[1]['Name']
    link = series[1]['Bulk Download']
    download_link = get_url(link)
    print(index, series[0],download_link,name) ##prints index to track links are faulty
    get_data_from_url(download_link, name)