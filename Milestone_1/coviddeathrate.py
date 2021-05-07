# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:39:42 2021

@author: mikem
"""

import matplotlib.pyplot as plt
import seaborn as sns

from Milestone_1 import covidnyc


def coviddeaths():
    """shows distribution of COVID-19 deaths in each neighborhood"""
    sns.histplot(data=covidnyc["COVID_DEATH_RATE"], kde=True)
    plt.xlabel("Number of deaths from COVID-19 per neighborhood")
    plt.ylabel("Frequency")
    plt.title("Frequency of deaths from COVID-19 in each neighborhood")


if __name__ == '__main__':
    coviddeaths()
