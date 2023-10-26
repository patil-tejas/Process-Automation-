# Process-Automation-
This contains some scripts for automating my manual tasks for screening, filtering or managing stocks.
Code processes all the CSV files for each sector and gets an filtered output in excel for organized access of all the list of stocks related to each sector and industry sorted by their market capitalization.

Futher Additions Coming:
1.Get an ID columns in output tagging stocks belonging to the NSE 750 - Consisting IDs ["NSE 50" , "Next 50" , "MidCap 50" , "MidCap next 100" , "SmallCap 50" , "SmallCap Next 200", "MicroCap 250"]
2.Web Scraping Script: (Not Defined Structure yet for execution as this scripts will have to run daily)
          a: Scrape prices and get AVG[Volume X Price] for regular use.
          b. Scrape prices and get stocks above 50-100-200 EMA.


Folder Structure:

SE/
  output/
  resources/
  main.py
  main.bat
  .gitignore
README.md


I have not included files in resources folder which I process . They are all the CSVs for stocks in each sector. Around 50 files
Also not included the output file - the generated sheet.

I do want to make it more modular but having some SettingwithCopy warning in pandas.
In main.py
    
 # if the code is in below order then i causes a Settingwithcopywarning 
    #dataframe['Symbol'] = dataframe['Symbol'].str.replace('-', '_').str.replace('&', '_')          /This causes the warning. Here for str replace it uses chaining.
    #dataframe = dataframe[~dataframe['Symbol'].str.isnumeric()]
    
    dataframe = dataframe[~dataframe['Symbol'].str.isnumeric()]                                    /If used in this order it goes away as the dataframe object is created
    dataframe['Symbol'] = dataframe['Symbol'].str.replace('-', '_').str.replace('&', '_')
