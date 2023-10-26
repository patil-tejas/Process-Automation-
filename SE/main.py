import os
import pandas as pd
import numpy as np
import json

with open('config.json', 'r') as file:
    config = json.load(file)

PATH = config['resources']['path']
OP_PATH = config['output']['output_file']
SHEET_1 = config['output']['sheet_1']
SHEET_2 = config['output']['sheet_2']


all_files = os.listdir(PATH)
#count_all_files= len(all_files)   #Total count of all the files

def write_to_excel(path, df1,df2, sheet1, sheet2):
    """
    Used to write the ouput df to excel
    """
    with pd.ExcelWriter(path) as writer:
        df1.to_excel(writer, sheet_name=sheet1, index=False)
        df2.to_excel(writer, sheet_name=sheet2, index=False)
        
    print("Excel File Created")

def process_file(dataframe , sec):
    dataframe = dataframe.iloc[:,[1,2,3]]

    dataframe.insert(1,"Sector",sec)

    # if the code is in below order then i causes a Settingwithcopywarning 
    #dataframe['Symbol'] = dataframe['Symbol'].str.replace('-', '_').str.replace('&', '_')
    #dataframe = dataframe[~dataframe['Symbol'].str.isnumeric()]
    dataframe = dataframe[~dataframe['Symbol'].str.isnumeric()]
    dataframe['Symbol'] = dataframe['Symbol'].str.replace('-', '_').str.replace('&', '_')
   
    dataframe['Trading View Symbol'] = 'NSE:' + dataframe['Symbol'] + ','
    return dataframe

def merge_output(o_df , df2):
    return pd.concat([o_df, df2], ignore_index = True)

def main():
    
    #Get Output DF
    output_df = pd.DataFrame()

    for file_name in all_files:
        print(file_name)
        df = pd.read_csv(PATH+"/"+ file_name,skiprows=4)
        sector = file_name.split("_")[0]

        df = process_file(df , sector)
        output_df = merge_output(output_df , df)
  
    output_df = output_df.sort_values(['Sector', 'Industry','Market Cap(Rs. Cr.)'], ascending=[True, True, False]).reset_index(drop=True)
    

    #Get Map
    sector_counts = output_df.groupby('Sector').size().reset_index(name='Total Stocks')
    industry_counts = output_df.groupby(['Sector', 'Industry']).size().reset_index(name='Stocks in Industry')
    map_df = pd.concat([sector_counts, industry_counts],axis=1)
        
    write_to_excel(OP_PATH,output_df,map_df,SHEET_1,SHEET_2)
    print("Completed")



if __name__ == "__main__":
    main()