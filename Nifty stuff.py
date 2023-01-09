# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 01:15:50 2022

@author: GH382TL
"""
import datetime as dt
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt 
import mplfinance as mpf

stocks = ['^NSEI']
start = dt.datetime.today()-dt.timedelta(3650)
end = dt.datetime.today()
cl_price = pd.DataFrame()
#ohlcv_data = {}
type(end)
df = yf.download(stocks,start,end)
# =============================================================================
# indexx = 'Indexx'
# df.set_index("Indexx",inplace = True, append= True)
# =============================================================================
df.reset_index(inplace = True)
n = len(df)
# =============================================================================
# englufing = pd.DataFrame(columns=['a'])
# =============================================================================
englufing2 = []
end.weekday()
def Bullish_eng():
   
    for i in range (1,len(df),1):
        n = len(df)- i
        current_date = df.iloc[n]
        Previous_date = df.iloc[n-1]
        if current_date['Close']>Previous_date['Open'] and current_date['Close']>Previous_date['Close']\
            and current_date['Open']<Previous_date['Close'] and current_date['Open']<Previous_date['Open']:
                p = current_date['Date']
                englufing2.append(p)
# =============================================================================
#                 val = current_date['Close']                   
#                 later_date = df.iloc[n+9]
#                 later_date_cl = later_date['Close']
#                 return10 = (later_date_cl-val)/val
#                 
#                 englufing2['enf_10_d_ret'] = englufing2['enf_10_d_ret'].append('return10')
# =============================================================================
                print (p,"is bullish engulfing")
                
        else:
            q = current_date['Date']
            print (q, "is not B engulfing")
        
        
        
Bullish_eng()
enfulfPDF = pd.DataFrame(englufing2)  
# =============================================================================
# enfulfPDF.reset_index(0, inplace = True)
# =============================================================================
enfulfPDF.columns = ["Date"]
#enfulfPDF["Returns"] = ''
later_dateZ = []
for i in range (0, len(enfulfPDF),1):   
       later_date =  enfulfPDF["Date"].iloc[i]+dt.timedelta(days = 10)
       if later_date.weekday() > 4 and later_date.weekday() < 6:
           later_date =  enfulfPDF["Date"].iloc[i]+dt.timedelta(days = 12)
       elif later_date.weekday() > 5:
           later_date =  enfulfPDF["Date"].iloc[i]+dt.timedelta(days = 11)
       else :
           later_date = later_date
       later_dateZ.append(later_date)



       
enfulfPDF["Later_date"] = later_dateZ



# =============================================================================
# Merging df and enfulpdf table to get the returns  

enfulfPDF1 = pd.merge(df,enfulfPDF, on ='Date', how = 'inner' )

enfulfPDF2 = enfulfPDF1[['Date','Close','Later_date']]
enfulfPDF2.rename(columns = {'Close':'CLOSE1','Date':'date_enf'}, inplace = True)
enfulfPDF2 = pd.merge(df[['Date','Close']],enfulfPDF2,left_on='Date',right_on='Later_date', how = 'right')
enfulfPDF3 = enfulfPDF2[['date_enf','CLOSE1','Later_date','Close']]
enfulfPDF3['Returnss'] = (enfulfPDF3['Close']-enfulfPDF3['CLOSE1'])/enfulfPDF3['CLOSE1']
enfulfPDF3.dropna(inplace=True)


trueenf_dateZ = []
for i in range (0, len(enfulfPDF3),1):   
       trueenf_date =  enfulfPDF3["date_enf"].iloc[i]+dt.timedelta(days = -20)
       if trueenf_date.weekday() > 4 and trueenf_date.weekday() < 6:
           trueenf_date =  enfulfPDF3["date_enf"].iloc[i]+dt.timedelta(days = -22)
       elif trueenf_date.weekday() > 5:
           trueenf_date =  enfulfPDF3["date_enf"].iloc[i]+dt.timedelta(days = -21)
       else :
           trueenf_date = trueenf_date
       trueenf_dateZ.append(trueenf_date)
       
enfulfPDF3["trueenf_date"] = trueenf_dateZ

enfulfPDF3.rename(columns = {'Close':'Close_later_date'}, inplace = True)
enfulfPDF6 = pd.merge(df[['Date','Close']],enfulfPDF3,left_on='Date',right_on='trueenf_date', how = 'right')
enfulfPDF6.drop(['Date'], axis = 1, inplace = True)
enfulfPDF7 =enfulfPDF6.iloc[:,[1,2,3,4,5,6,0]]

#checking if the previous trend was a down trend or not
enfulfPDF7['Trend_return'] = (enfulfPDF7['CLOSE1'] - enfulfPDF7['Close']) / enfulfPDF7['Close']
enfulfPDF7.dropna(inplace=True)
enfulfPDF8 = enfulfPDF7[enfulfPDF7['Trend_return'] < -0.01] 
enfulfPDF8['Returnss'].mean()
enfulfPDF8.describe()
#plotting the returns 

bargraph = enfulfPDF8.plot.bar(x = 'date_enf', y = 'Returnss', fontsize = 19)
# =============================================================================
# =============================================================================
# def is_bearish_candlestick(df):
#     return df['Close']<df['Open']
# def is_bullish_candles(df,p):
#     current_day = df[]
#     previous_day = df[p-1]
#     
#     if is_bearish_candlestick(previous_day)\
#         and current_day['Close']>previous_day['Open']\
#         and current_day['Open']<previous_day['Close']:
#         return True
#     return False
# 
# for i in range(1,len(df)):
#     print(df[i])
#     
#     if is_bullish_candles(df,i):
#         print("{}is a bullish engulfing".format(df[i]['Date']))
# 
#         
# mpf.plot(df,type='candle')
# 
# bullish_engulfing = pd.DataFrame()
# =============================================================================

