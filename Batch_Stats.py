# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 10:52:46 2017

@author: mmangian
"""

# Import things you will need
import csv, os
import pandas as pd
import numpy as np

# Input Working Directory

dirname = r'H:\InvasiveSpecies\HUC2Analysis\HUCSummary'
plantSpeciesIn = r'H:\InvasiveSpecies\HUC2Analysis\HUCSummary\PlantSpeciesList.txt'

# names of columns

SciNameCol = 'sciName'
YearCol = 'year'
HUC8Col = 'HUC8'
HUC8sqkmCol = 'HUC8sKm'
HUC12Col = 'xHUC12'
HUC12sqkmCol = 'HUC12sqK'

# HUCs not to use
removedHUC12 = 'x40803000300', 'x41202000300', 'x40203000300', 'x40602000000', 'x41502000200', 'x90300091423'
removedHUC8 = '4020300', '4080300', '4060200', '4120200', '9030001', '9030009'

# loop through the number of HUC2s there are i.e (1 to 18)
for i in range(1,19):
    print('HUC running is: ' + str(i))
    inFile = os.path.join(dirname, "HUC{}".format(i), "HUC{}_OccuranceTable.csv".format(i))
    outFile = os.path.join(dirname, "HUC{}".format(i), "HUC{}_OutputStats.csv".format(i))
    if os.path.exists(outFile):
        os.remove(outFile)
    data = pd.read_csv(inFile, dtype={HUC12Col:'str', HUC8Col:'str'})
    pd.DataFrame(data)

    minYear = data[YearCol].min()
    # change the HUC12 column to string
    #data[HUC12Col] = data[HUC12Col].astype('str')
    #data[HUC8Col] = data[HUC8Col].astype('str')
    #print(data[HUC12Col])
    with open(outFile, 'w') as out_v:
        write = csv.writer(out_v, lineterminator = '\n')
        write.writerow(["Year", "Annual_Occurances", "Cumulative_Occurances", "Annual_Species_Count", "Number_First_Occurances", "Cumulative_First_Occurance", "HUC12_Occurances", "AnnualHUC12_sqkm", "HUC8_Occurances", "AnnualHUC8_sqkm"])
        # open empty lists
        # occurance Year
        plantSpecies = open(plantSpeciesIn, 'r')
        firstOccuranceList = []
        for plantline in plantSpecies:
            print('the plant line is: ' + plantline)
            plantwhole = plantline.split()
            try:
                plant = str(plantwhole[0]) +" "+ str(plantwhole[1]) + " " + str(plantwhole[2])
            except:
                plant = str(plantwhole[0]) +" "+ str(plantwhole[1])
            print('plant used is: ' + plant)
            if any(data[SciNameCol] == plant):
                firstOccurYear = data.loc[data[SciNameCol] == plant, YearCol].min()
                firstOccuranceList.append(firstOccurYear)
            else:
                continue
        plantSpecies.close()

        CumOccuranceList = []
        CumFirstOccur = []
        for year in range(minYear, 2017):
            # Total Occurance
            TotalOccurance = data.loc[data[YearCol] == year, YearCol].count()
            #df.loc[df['a'] == 1, 'b'].sum()
            CumOccuranceList.append(TotalOccurance)

            # cumulative number of occurances
            CumulativeOccurances = sum(CumOccuranceList)

            # number of species per year
            speciesList = data.loc[data[YearCol] == year, SciNameCol].unique()
            SpeciesCount = np.count_nonzero(speciesList)

            # First Occurance
            FirstOccuranceCount = sum(int(num) == year for num in firstOccuranceList)
            CumFirstOccur.append(FirstOccuranceCount)
            # cumulative first occurances
            CumFirstOccuranceCount = sum(CumFirstOccur)

            # count unique HUC12s
            HUC12List = data.loc[data[YearCol] == year, str(HUC12Col)].unique()
            HUC12Count = np.count_nonzero(HUC12List)
            # remove the bad HUCs listed above
            usable_HUC12 = []
            for e in HUC12List:
                if e not in (removedHUC12):
                    usable_HUC12.append(str(e))
            # calculate total sq km covered for that year
            HUC12sumList = []
            for HUC12 in usable_HUC12:
                # get the minimum value of the HUC12 (they all should be the same so min shouldnt matter)
                outHUC12 = data.loc[data[HUC12Col] == str(HUC12), HUC12sqkmCol].min()
                HUC12sumList.append(float(outHUC12))
            # sum the entier list of HUC12s to get total area of that year
            HUC12sqkmOut = sum(HUC12sumList)

            # Count unique HUC8s
            HUC8List = data.loc[data[YearCol] == year, HUC8Col].unique()
            HUC8Count = np.count_nonzero(HUC8List)
            # remove the bad HUCs listed above
            usable_HUC8 = []
            for e in HUC8List:
                if e not in (removedHUC8):
                    usable_HUC8.append(e)
            # calculate total sq km covered for that year
            HUC8sumList = []
            for HUC8 in usable_HUC8:
                # get the minimum value of the HUC8 (they all should be the same so min shouldnt matter)
                outHUC8 = data.loc[data[HUC8Col] == str(HUC8), HUC8sqkmCol].min()
                HUC8sumList.append(float(outHUC8))
            # sum the entier list of HUC12s to get total area of that year
            HUC8sqkmOut = sum(HUC8sumList)

            # append the document with all values
            write.writerow([year] + [TotalOccurance] + [CumulativeOccurances] + [SpeciesCount] + [FirstOccuranceCount] + [CumFirstOccuranceCount] + [HUC12Count] + [HUC12sqkmOut] + [HUC8Count] +[HUC8sqkmOut])

    out_v.close()
    print('finished running: ' + str(i))
print('finished running all HUCs')