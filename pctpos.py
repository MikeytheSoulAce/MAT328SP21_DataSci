# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:08:37 2021

@author: mikem
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

covidnyc = pd.read_csv("data-by-modzcta.csv")

def pctpos():
    sns.histplot(data=covidnyc["PERCENT_POSITIVE"],kde=True)
    plt.xlabel("Percent of residents per neighborhood tested positive for COVID-19")
    plt.ylabel("Frequency")
    plt.title("Frequency of percentages of residents in each neighborhood who tested positive for COVID-19")
'''shows freq of percentages of residents per neighborhood who tested positive'''

pctpos()
