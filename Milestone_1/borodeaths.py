# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 00:26:27 2021

@author: mikem
"""

import matplotlib.pyplot as plt
import seaborn as sns

from Milestone_1 import covidnyc


def borodeaths():
    a = sns.catplot(x="BOROUGH_GROUP", y="COVID_DEATH_COUNT", kind="box", data=covidnyc)
    a.fig.set_size_inches(6, 6)
    plt.title("Boxplot of deaths from COVID-19 by borough")
    plt.xlabel("Borough")
    plt.ylabel("Number of deaths")


if __name__ == '__main__':
    borodeaths()
