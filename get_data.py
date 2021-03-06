import requests 
import pandas as pd
import re
import datetime

def get_website_source(url):
    response = requests.get(url)
    return response.text

def get_raw_pairs(doc):
    start = doc.find('[[new Date')
    doc = doc[start+1:]
    end = doc.find(']]')
    doc = doc[:end+1]

    doc = re.sub(r"new Date\((.{12})\)", "\g<1>", doc)
    doc = re.sub("null", "-1", doc)

    doc=str(doc)

    return eval(doc)

def get_tweets_df():
    text = get_website_source('https://bitinfocharts.com/comparison/tweets-btc.html')
    pairs = get_raw_pairs(text)
    for count in range(len(pairs)):
        if pairs[count][1] == -1:
            pairs[count][1] = pairs[count-1][1]
        
    dates = []
    num_tweets = []

    for pair in pairs:
        dates.append(pair[0])
        num_tweets.append(pair[1])
    
    for i in range(len(dates)):
        dates[i] = datetime.datetime.strptime(dates[i],"%Y/%m/%d")
    

    df = pd.DataFrame()
    df["date"] = dates
    df["tweets"] = num_tweets
    return df

def get_btc_prices(start, end):
    if isinstance(start, datetime.datetime):
        start = start.strftime('%Y-%m-%d')
    if isinstance(end, datetime.datetime):
        end = end.strftime('%Y-%m-%d')
    
    response = requests.get(f"https://api.coindesk.com/v1/bpi/historical/close.json?start={start}&end={end}")
    raw = response.json()['bpi']
    dates = []
    prices = []
    for date_str in raw:
        dates.append(date_str)
        prices.append(raw[date_str])
        
    for i in range(len(dates)):
        dates[i] = datetime.datetime.strptime(dates[i], "%Y-%m-%d")
    
    df = pd.DataFrame()
    df['date'] = dates
    df['price'] = prices
    
    return df
