# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:25:21 2021

@author: mikem
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

covidnyc = pd.read_csv("data-by-modzcta.csv")

def totalcases():
    sns.histplot(data=covidnyc["COVID_CASE_COUNT"],kde=True)
    plt.xlabel("Total number of COVID-19 cases per neighborhood")
    plt.ylabel("Frequency")
    plt.title("Frequency of total number of COVID-19 cases per neighborhood")
'''shows freq of total number of COVID-19 cases per neighborhood'''

totalcases()
