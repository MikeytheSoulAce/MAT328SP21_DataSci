# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 00:26:27 2021

@author: mikem
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

covidnyc = pd.read_csv("data-by-modzcta.csv")

def borodeaths():
    
    a = sns.catplot(x = "BOROUGH_GROUP", y = "COVID_DEATH_COUNT", kind = "box", data = covidnyc)
    a.fig.set_size_inches(6,6)
    plt.title("Boxplot of deaths from COVID-19 by borough")
    plt.xlabel("Borough")
    plt.ylabel("Number of deaths")

borodeaths()
