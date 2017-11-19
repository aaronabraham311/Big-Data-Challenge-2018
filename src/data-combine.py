import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Reading in csv files and cleaning 
df = pd.read_csv("../data/raw/glaciers.csv")

# Looking at data
df.head()

# NaN values
nanSums = df.isnull().sum() #132890 rows

# Drop columns with more than 110000 NaN values, and drop all rows with NaN
df = df.dropna(thresh = len(df) - 110000, axis = 1)
df = df.dropna()

# Rows left: 627

# Drop outliers?
df.info() # Every column aside from Glacier ID --> Glacier Name is a float. Boxplots or violin to see variance

# Writing csv
df.to_csv("../data/processed/cleaned_glaciers.csv")

## Outlier detection using violin plots
min_el_vp = sns.violinplot(x = df["Minimum Elevation"]) # Insights: Values below 0 can be dropped
min_el_ex_vp = sns.violinplot(x = df["Minimum Elevation Exposed"]) # Same as above
max_el_vp = sns.violinplot(x = df["Maximum Elevation"])