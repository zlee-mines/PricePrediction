# PricePrediction
Written by Zachary Lee, Jared Schneider, and Yujin Kim

The following is a small price prediction algorithm written as a final project for CSCI 470 - Intro to Machine Learning.

The code uses an LSTM model, datasets gathered from the coindesk api (https://www.coindesk.com/coindesk-api) and bitcoin mentions on twitter (https://bitinfocharts.com/comparison/tweets-btc.html) to predict if the price of bitcoin will increase or decrease, and by how much it will do so.

The model is able to predict up to multiple days in advance on trends, and has been shown to be fairly accurate in practice.
