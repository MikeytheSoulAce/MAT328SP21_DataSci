# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:08:37 2021

@author: mikem
"""

import matplotlib.pyplot as plt
import seaborn as sns

from Milestone_1 import covidnyc


def pctpos():
    """shows freq of percentages of residents per neighborhood who tested positive"""
    sns.histplot(data=covidnyc["PERCENT_POSITIVE"], kde=True)
    plt.xlabel("Percent of residents per neighborhood tested positive for COVID-19")
    plt.ylabel("Frequency")
    plt.title("Frequency of percentages of residents in each neighborhood who tested positive for COVID-19")


if __name__ == '__main__':
    pctpos()
