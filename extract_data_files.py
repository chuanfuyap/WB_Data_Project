import os
import pandas as pd
import shutil
import numpy as np

##### moving only data.csv files from zip outputs to a folder with everything else, leaving behind footnotes/legends

directories_in_curdir = filter(os.path.isdir, os.listdir(os.curdir))
directories_in_curdir.remove('.ipynb_checkpoints')

what_i_want = 'data.csv'
directories_with_csv = []
for folder in directories_in_curdir:
    for path, folders, files in os.walk(folder):
        #print path
        #print folders 
        for file_name in files:
            if file_name[-8:].lower()==what_i_want:
                directories_with_csv.append(folder)
                
for folder in directories_with_csv:
    new_name = folder.lower()+'.csv'
    target=directory+new_name
    for path, folders, files in os.walk(folder):
        for file_name in files:
            if file_name[-8:].lower()==what_i_want:
                file_to_move = folder+'/'+file_name
                shutil.copy(file_to_move, target)
                print file_to_move , 'moved'
                print 'to', target
                
