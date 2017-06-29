import pandas as pd
import os
import time
from datetime import datetime

path = "/Users/richardsaville/documents/LifeIQ/intraQuarter"

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    #insert data frame
    df = pd.DataFrame(columns = ['Date','Unix','Ticker','DE Ratio','Price'])
    #print(stock_list)
    sp500_df = pd.DataFrame.from_csv("SP500.csv")

    for each_dir in stock_list[1:2]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("_KeyStats/")[1]
        if len(each_file) > 0:
            for file in each_file:

                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                #print(date_stamp, unix_time)
                full_file_path = each_dir+'/'+file
                #save full source code HTML to "source" variable.
                source = open(full_file_path,'r').read()
                #print(source)

                try:
                    #split by the opening of the table data tag and the table data closing tag to find the value we're hunting for.
                    value = source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]

                    # try:
                    #     sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                    #     row = sp500_df[(sp500_df.index == sp500_date)]
                    #     sp500_value = float(row["Adjusted Close"])
                    # except:
                    #     sp500_date = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                    #     row = sp500_df[(sp500_df.index == sp500_date)]
                    #     sp500_value = float(row["Adjusted Close"])

                    stock_price = float(source.split('</small><big><b>')[1].split('</b></big>')[0])
                    #print("stock_price:",stock_price,"ticker:", ticker)

                    #re-defining our DataFrame object as the previous DataFrame object with the new data appended to it
                    df = df.append({'Date':date_stamp,
                                    'Unix':unix_time,
                                    'Ticker':ticker,
                                    'DE Ratio':value,
                                    'Price':stock_price}, ignore_index = True)
                except Exception as e:
                    pass

    #specifying a custom name for the csv file, then using pandas to_csv capability to output the Data Frame to an actual CSV file.
    save = gather.replace(' ','').replace(')','').replace('(','').replace('/','')+('.csv')
    print(save)
    df.to_csv(save)



Key_Stats()
