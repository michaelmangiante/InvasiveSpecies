# Michael Mangiante
# 4/24/2017
# Count the number of animal, plant, and total species within each HUC12 for every time period

import csv
import os
import pandas as pd
import numpy as np

# Breaks

brk1 = 1900
brk2 = 1930
brk3 = 1950
brk4 = 1970
brk5 = 1990
brk6 = 2016

HUC12List = r'H:\InvasiveSpecies\HUC2Analysis\HUC12List.txt'

# Plants
inputPlants = r"K:\InvasiveSpecies\FinalData\plantsDB\SourceRegions\Plants_DB_conus_hucs_dated_LL_sourceLocations_4417UPDATED.csv"
outDir = r"H:\InvasiveSpecies\HUC2Analysis"

SciNameCol_P = 'sciName'
YearCol_P = 'year'
HUC8Col_P = 'HUC8'
HUC8sqkmCol_P = 'HUC8sKm'
HUC12Col_P = 'xHUC12'
HUC12sqkmCol_P = 'HUC12sqK'
IDcol_P = 'occurrence'
HUC2Col_P = 'HUC_2'
IDlocation_P = 0
RegionLocation = 'US_Region'
x0HUC12LOC_P = 'x0HUC12'

# Animals

inputAnimals = r"K:\InvasiveSpecies\FinalData\animalsDB\WorkingFolder_Animals\Animals31417_final_albers_HUC2.csv"

SciNameCol_A = 'sciName'
YearCol_A = 'year_'
HUC8Col_A = 'xHUC8'
HUC8sqkmCol_A = 'HUC8areaSq'
HUC12Col_A = 'xHUC12'
HUC12sqkmCol_A = 'HUC12areaS'
IDcol_A = 'occurrence'
HUC2Col_A = 'HUC_2'
IDlocation_A = 4


# create stuff for output dataset
dirname = os.path.dirname(inputPlants)
strName = "CountofSpeciesperHUC12_TimeSteps.csv"
outdata = os.path.join(outDir, strName)
if os.path.exists(outdata):
    os.remove(outdata)


plantsdata = pd.read_csv(inputPlants, dtype={HUC12Col_P:'str', HUC8Col_P:'str', IDcol_P:'str'})
pd.DataFrame(plantsdata)

animaldata = pd.read_csv(inputAnimals, dtype={HUC12Col_A:'str', HUC8Col_A:'str', IDcol_A:'str'})
pd.DataFrame(animaldata)

with open(outdata, 'wb') as out:
    writer = csv.writer(out, lineterminator = '\n')
    writer.writerow(["HUC12_Value", "P_1600to1900", "P_1901to1930", "P_1931to1950","P_1951to1970","P_1971to1990","P_1991to2016", "A_1600to1900", "A_1901to1930", "A_1931to1950","A_1951to1970","A_1971to1990","A_1991to2016","Total_1600to1900", "Total_1901to1930", "Total_1931to1950","Total_1951to1970","Total_1971to1990","Total_1991to2016"])
    HUC12s = open(HUC12List, 'r')
    for line in HUC12s:
        inHUC12 = line.split()[0]
        print(inHUC12)
        # Break 1
        P_brk1 = plantsdata.loc[(plantsdata[x0HUC12LOC_P] == inHUC12) & (plantsdata[YearCol_P] <= brk1), SciNameCol_P].nunique()
        A_brk1 = animaldata.loc[(animaldata[HUC12Col_A] == inHUC12) & (animaldata[YearCol_A] <= brk1), SciNameCol_A].nunique()
        Total_brk1 = P_brk1 + A_brk1
        # Break 2
        P_brk2 = plantsdata.loc[(plantsdata[x0HUC12LOC_P] == inHUC12) & (plantsdata[YearCol_P] <= brk2), SciNameCol_P].nunique()
        A_brk2 = animaldata.loc[(animaldata[HUC12Col_A] == inHUC12) & (animaldata[YearCol_A] <= brk2), SciNameCol_A].nunique()
        Total_brk2 = P_brk2 + A_brk2
        # Break 3
        P_brk3 = plantsdata.loc[(plantsdata[x0HUC12LOC_P] == inHUC12) & (plantsdata[YearCol_P] <= brk3), SciNameCol_P].nunique()
        A_brk3 = animaldata.loc[(animaldata[HUC12Col_A] == inHUC12) & (animaldata[YearCol_A] <= brk3), SciNameCol_A].nunique()
        Total_brk3 = P_brk3 + A_brk3
        # Break 4
        P_brk4 = plantsdata.loc[(plantsdata[x0HUC12LOC_P] == inHUC12) & (plantsdata[YearCol_P] <= brk4), SciNameCol_P].nunique()
        A_brk4 = animaldata.loc[(animaldata[HUC12Col_A] == inHUC12) & (animaldata[YearCol_A] <= brk4), SciNameCol_A].nunique()
        Total_brk4 = P_brk4 + A_brk4
        # Break 5
        P_brk5 = plantsdata.loc[(plantsdata[x0HUC12LOC_P] == inHUC12) & (plantsdata[YearCol_P] <= brk5), SciNameCol_P].nunique()
        A_brk5 = animaldata.loc[(animaldata[HUC12Col_A] == inHUC12) & (animaldata[YearCol_A] <= brk5), SciNameCol_A].nunique()
        Total_brk5 = P_brk5 + A_brk5
        # Break 6
        P_brk6 = plantsdata.loc[(plantsdata[x0HUC12LOC_P] == inHUC12) & (plantsdata[YearCol_P] <= brk6), SciNameCol_P].nunique()
        A_brk6 = animaldata.loc[(animaldata[HUC12Col_A] == inHUC12) & (animaldata[YearCol_A] <= brk6), SciNameCol_A].nunique()
        Total_brk6 = P_brk6 + A_brk6
        writer.writerow([inHUC12] + [P_brk1] + [P_brk2] + [P_brk3]+ [P_brk4] + [P_brk5] + [P_brk6] + [A_brk1] + [A_brk2] + [A_brk3]+ [A_brk4] + [A_brk5] + [A_brk6] + [Total_brk1] + [Total_brk2] + [Total_brk3]+ [Total_brk4] + [Total_brk5] + [Total_brk6])
    HUC12s.close()
out.close()

print('finished script')

