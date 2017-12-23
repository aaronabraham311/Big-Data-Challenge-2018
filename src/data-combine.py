import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""def violinVisualization (df):
    for i in len(df.columns):
        plot = sns.violinplot(df[:,i])
        print(plot) """

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

#violinVisualization(df)

## Outlier detection using violin plots. All have bimodal distributions
#sns.violinplot(x = df["Minimum Elevation"]) # Insights: Values below 0 can be dropped
#sns.violinplot(x = df["Minimum Elevation Exposed"]) # Same as above
#sns.violinplot(x = df["Maximum Elevation"]) # No outliers
#sns.violinplot(x = df["Mean Elevation"]) # No outliers
#sns.violinplot(x = df["Maximum Elevation"]) # No outliers
#sns.violinplot(x = df["Snow Line Elevation"]) # Drop everything below 2000
#sns.violinplot(x = df["Snow Line Accuracy"]) # Drop accuracy 
#sns.violinplot(x = df["Area Accuracy"]) # Skipped Glacier Area as that is the variable we are looking at
#sns.violinplot(x = df["Mean Width"]) # Drop everything above 10
#sns.violinplot(x = df["Mean Length"]) # Drop everything above 35
#sns.violinplot(x = df["Maximum Length"]) # Drop everything above 40
#sns.violinplot(x = df["Maximum Length Exposed"]) # Same as above
#sns.violinplot(x = df["Mean Depth"]) # Drop everything above 300
#sns.violinplot(x = df["Depth Accuracy"])# Drop accuracy """
### The rest of the variables are not needed for outlier detection. They are either numbers or objects


#Outlier drop

df= df[df["Minimum Elevation"] >= 0 ]
df = df[df["Minimum Elevation Exposed"] >= 0]
df = df[df["Snow Line Elevation"] >= 2000]
df = df.drop("Snow Line Accuracy", 1)
df = df.drop("Area Accuracy", 1)
df = df.drop("Depth Accuracy", 1)
df = df[df["Mean Width"] <= 10]
df = df[df["Mean Length"] <= 35]
df = df[df["Maximum Length"] <= 40]
df = df[df["Maximum Length Exposed"] <= 40]
df = df[df["Mean Depth"] <= 300]

#Rows left: 610

# Writing csv
df.to_csv("../data/processed/cleaned_glaciers.csv")