import csv
import os
import pandas as pd
import numpy as np

data_type = 'animals'
plantSpeciesIn = r'K:\InvasiveSpecies\FinalData\animalsDB\WorkingFolder_Animals\AnimalSpeciesList.txt'
inputdata = r"K:\InvasiveSpecies\FinalData\animalsDB\SourceRegions\Animals31417_final_albers_HUC2_SourceRegions.csv"
outDir = r"K:\InvasiveSpecies\FinalData\animalsDB\CircularFlow"

SciNameCol = 'sciName'
YearCol = 'year_'
HUC8Col = 'xHUC8'
HUC8sqkmCol = 'HUC8areaSq'
HUC12Col = 'xHUC12'
HUC12sqkmCol = 'HUC12areaS'
IDcol = 'occurrence'
HUC2Col = 'HUC_2'
IDlocation = 4
RegionLocation = 'US_Region'

#########################################################################
# Start main script

# open empty string to add sciName to

# create stuff for output dataset
dirname = os.path.dirname(inputdata)
strName = str(data_type) + "_USRegions_FirstOccurances.csv"
outdata = os.path.join(outDir, strName)
if os.path.exists(outdata):
    os.remove(outdata)

data = pd.read_csv(inputdata, dtype={HUC12Col:'str', HUC8Col:'str', IDcol:'str'})
pd.DataFrame(data)

US_regions = ["1;2;4;5;7;9", "3;8;6", "10;11;12", "13;15", "14;16", "18", "17"]
Region_name= ["North.East", "South.East", "Great.Plains", "South.West", "Mountain.West", "Californian", "Pacific.North.West"]

IDs = []
# get ID values
# loop for each HUC
for i in Region_name:
    plantspecies = open(plantSpeciesIn, "r")
    for plantline in plantspecies:
        print('the plant line is: ' + plantline)
        plantwhole = plantline.split()
        try:
            plant = str(plantwhole[0]) +" "+ str(plantwhole[1]) + " " + str(plantwhole[2])
        except:
            plant = str(plantwhole[0]) +" "+ str(plantwhole[1])
        print('plant used is: ' + plant)
        if ((data[SciNameCol] == plant) & (data[RegionLocation] == i)).any():
            # select ID where HUC2 = i and plant = plantCOl
            minYear = data.loc[(data[RegionLocation] == i) & (data[SciNameCol] == plant), YearCol].min()
            ID_Values = data.loc[(data[RegionLocation] == i) & (data[SciNameCol] == plant) & (data[YearCol]==minYear), IDcol].values
            print(ID_Values)
            usedID = str(ID_Values[0].split('.')[0])
            print(usedID)
            IDs.append(usedID)
        else:
            continue
    plantspecies.close()

with open(outdata, 'wb') as out:
    writer = csv.writer(out, lineterminator = '\n')
    with open(inputdata, 'rb') as read_data:
        spanreader = csv.reader(read_data)
        headers = next(spanreader)[0:]
        writer.writerow(headers)
        for row in spanreader:
            if str(row[IDlocation].split('.')[0]) in IDs:
                writer.writerow(row)
            else:
                continue
read_data.close()
out.close()
print('script is done')




