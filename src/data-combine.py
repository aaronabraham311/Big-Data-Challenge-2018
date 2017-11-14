import pandas as pd
import numpy as np

"""
Merge datasets: https://pandas.pydata.org/pandas-docs/stable/merging.html
"""

# Reading in csv files and cleaning 
alberta = pd.read_csv("../data/raw/Alberta Disaster Data.csv", sep = '\t');
cleanAlberta = alberta[alberta["Fatalities"] != "Unknown"]

bc = pd.read_csv("../data/raw/BC Disaster Data.csv")
cleanBC = bc.dropna()

international = pd.read_csv("../data/raw/International Disaster Data.csv")
cleanInter = international.dropna()

manitoba = pd.read_csv("../data/raw/Manitoba Disaster Data.csv", sep = '\t')
cleanManitoba = manitoba.dropna()

NB = pd.read_csv("../data/raw/New Brunswick Disaster Data.csv", sep = '\t')
cleanNB = NB.dropna()

NL = pd.read_csv("../data/raw/Newfoundland and Labrador Disaster Data.csv", sep = '\t')
cleanNL = NL.dropna()

NWT = pd.read_csv("../data/raw/Northwest Territories Disaster Data.csv", sep = '\t')
cleanNWT = NWT.dropna()

NS = pd.read_csv("../data/raw/Nova Scotia Disaster Data.csv", sep = '\t')
cleanNS = NS.dropna()

nunavut = pd.read_csv ("../data/raw/Nunavut Disaster Data.csv")
cleanNunavut = nunavut.dropna()

ontario = pd.read_csv("../data/raw/Ontario Disaster Data.csv")
cleanOntario = ontario.dropna()

PEI = pd.read_csv("../data/raw/PEI Disaster Data .csv")
cleanPEI = PEI.dropna()

quebec = pd.read_csv("../data/raw/Quebec Disaster Data .csv")
cleanQuebec = quebec.dropna()

SK = pd.read_csv("../data/raw/Saskatchewan Disaster Data.csv")
cleanSK = SK.dropna()

yukon = pd.read_csv("../data/raw/Yukon Disaster Data.csv")
cleanYukon = yukon.dropna()