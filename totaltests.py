# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:14:36 2021

@author: mikem
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

covidnyc = pd.read_csv("data-by-modzcta.csv")

def totaltests():
    sns.histplot(data=covidnyc["TOTAL_COVID_TESTS"],kde=True)
    plt.xlabel("Total number of COVID-19 tests per neighborhood")
    plt.ylabel("Frequency")
    plt.title("Frequency of number of COVID-19 tests per neighborhood")
'''shows freq of COVID tests per neighborhood'''

totaltests()
