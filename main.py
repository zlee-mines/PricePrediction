import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow.keras.layers import LSTM, Embedding, Dense, Dropout, Activation
from tensorflow.keras.losses import BinaryCrossentropy
from math import log, log10
import math
from get_data import get_btc_prices, get_tweets_df
import datetime


def get_all_data():
    tweets = get_tweets_df()
    prices = get_btc_prices(tweets.index[0], tweets.index[-1])

    prices = prices[datetime.datetime(2017, 1, 1):]
    data = prices.merge(tweets, left_index=True, right_index=True)
    return data

def normalize(column, method):
    if method == 'normal':
        return (column - np.mean(column)) / np.std(column)
    else:
        return column.apply(method)


def percentages(column):
    ser = column.copy()
    ser[ser.index[0]] = 1
    for i in range(len(column) - 1):
        ser[ser.index[i+1]] = column[column.index[i+1]] / column[column.index[i]]

    return ser

def binary_increase(column):
    ser = column.copy()
    ser[ser.index[0]] = 1
    for i in range(len(column) - 1):
        ser[ser.index[i+1]] = 1 if column[column.index[i+1]] > column[column.index[i]] else 0

    return ser


def make_model(output_activation):
    layers = [
        LSTM(32),
        Dense(15, activation='relu'),
        Dense(1, activation=output_activation)
    ]

    model = Sequential(layers)

    return model


a = get_all_data()

print(np.mean(binary_increase(a['price'])))
make_model('linear')
