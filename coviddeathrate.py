# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:39:42 2021

@author: mikem
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

covidnyc = pd.read_csv("data-by-modzcta.csv")

def coviddeaths():
    sns.histplot(data=covidnyc["COVID_DEATH_RATE"],kde=True)
    plt.xlabel("Number of deaths from COVID-19 per neighborhood")
    plt.ylabel("Frequency")
    plt.title("Frequency of deaths from COVID-19 in each neighborhood")
'''shows distribution of COVID-19 deaths in each neighborhood'''

coviddeaths()
