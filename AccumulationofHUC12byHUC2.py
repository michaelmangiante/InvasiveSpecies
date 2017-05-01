# Michael Mangiante
# 4/11/2017
# Accumulation of HUC12s per HUC2 over time.  If invasive species is observed in a HUC12, it is counted and is not counted again.

import csv
import os
import pandas as pd
import numpy as np

data_type = 'plants'
inputdata = r"K:\InvasiveSpecies\FinalData\plantsDB\SourceRegions\Plants_DB_conus_hucs_dated_LL_sourceLocations_4417UPDATED.csv"
outDir = r"H:\InvasiveSpecies\HUC2Analysis"

SciNameCol = 'sciName'
YearCol = 'year'
HUC8Col = 'HUC8'
HUC8sqkmCol = 'HUC8sKm'
HUC12Col = 'xHUC12'
HUC12sqkmCol = 'HUC12sqK'
IDcol = 'occurrence'
HUC2Col = 'HUC_2'
IDlocation = 0
RegionLocation = 'US_Region'


removedHUC12 = 'x40803000300', 'x41202000300', 'x40203000300', 'x40602000000', 'x41502000200', 'x90300091423'
removedHUC8 = '4020300', '4080300', '4060200', '4120200', '9030001', '9030009'


# create stuff for output dataset
dirname = os.path.dirname(inputdata)
strName = str(data_type) + "_AccumulationofHUC12sbyHUC2.csv"
outdata = os.path.join(outDir, strName)
if os.path.exists(outdata):
    os.remove(outdata)


data = pd.read_csv(inputdata, dtype={HUC12Col:'str', HUC8Col:'str', IDcol:'str'})
pd.DataFrame(data)

g = data.groupby([HUC2Col, YearCol]).xHUC12.nunique()

with open(outdata, 'wb') as out:
    writer = csv.writer(out, lineterminator = '\n')
    writer.writerow(["HUC2_Value", "Year", "CumulativePlantHUC12Count", "CumulativePlantHUC12SqKm"])
    for HUC2 in range(1,19):
        IDs = []
        areas = []
        for year in range(1700,2017):
            if ((data[HUC2Col] == HUC2) & (data[YearCol] == year)).any():
                ID_Values = data.loc[(data[HUC2Col] == HUC2) & (data[YearCol] == year), HUC12Col].values
                print(ID_Values)
                nonmatchlist = [x for x in ID_Values if x not in IDs]
                uniques = set(nonmatchlist)
                print(uniques)
                #usedID = str(ID_Values[0].split('.')[0])
                #print(usedID)
                for i in range(len(uniques)):
                    if list(uniques)[i] not in removedHUC12:
                        IDs.append(list(uniques)[i])
                        huc12area = data.loc[(data[HUC12Col] == list(uniques)[i]), HUC12sqkmCol].values
                        areas.append(huc12area[0])
                    else:
                        print(str(list(uniques)[i]) + " is in the removed HUC list.")
            else:
                print('no data in ' + str(year))
            # get the sqkm for each HUC and sum
            #for huc12s in IDs:
            #    huc12area = data.loc[(data[HUC12Col] == huc12s), HUC12sqkmCol].values
            #    areas.append(huc12area[0])
            listLength = len(IDs)
            totalArea = sum(areas)
            HUCName = 'HUC' + str(HUC2)
            writer.writerow([HUCName] + [year] + [listLength] + [totalArea])
            #del IDs
            #del areas
out.close()
print('done')

            #YearLengh = str(year) + ';' + str(listLength)
            #HUC{}.format(HUC2).append(YearLength)



#with open(outdata, 'wb') as out:
#    writer = csv.writer(out, lineterminator = '\n')

#eval.('HUC{},
# or a Dictionary
# HUCS = {}
#





