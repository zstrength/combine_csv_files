import pandas as pd
import os
import chardet

#vars to fill out: 
    #cols_to_delete[]
    #ros_to_delete[]
    #final_file_name''

final_file_name = ''
cols_to_delete = []
rows_to_delete = []



folder_name = 'dataset/'
dir = os.listdir(folder_name)

#function to shape dataframe
def ShapeDataframe(file, cols_to_delete, rows_to_delete):
    df = pd.read_csv(file, engine='python')
    df_after_deleting_cols = df.drop(df.columns[cols_to_delete],axis=1)
    final_df = df_after_deleting_cols.drop(labels=rows_to_delete, axis=0)
    return final_df

#function to determine correct encoding type for reading the file
def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc

file_list = []
for file in dir:
    file_list.append(file)

frames = []
for file in file_list:
    try:
        x = ShapeDataframe(folder_name+file, cols_to_delete, rows_to_delete)
        frames.append(x)
    except:
        my_encoding = find_encoding(folder_name+file)
        df = pd.read_csv(folder_name+file, encoding=my_encoding)
        df_after_deleting_cols = df.drop(df.columns[cols_to_delete], axis=1)
        final_df = df_after_deleting_cols.drop(labels=rows_to_delete, axis=0)
        frames.append(final_df)

result = pd.concat(frames, ignore_index=True)

result.to_csv(final_file_name, encoding='utf-8', index=False)










