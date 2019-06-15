import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
import datetime
#Load the data
from collections import Counter

# oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands=',')
# gdp_per_capita = pd.read_csv("gdp_per_capita.csv", thousands=',', delimiter='\t', encoding='latin', na_values='n/a')

# prepare the data
# country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
# x = np.c_[country_stats["GDP per capita"]]
# y = np.c[country_stats["Life satisfaction"]]


# data = np.genfromtxt("oecd_bli_2015.csv", dtype=None, delimiter=',')
# print(data[:, 1])

data = pd.read_csv("oecd_bli_2015.csv")
