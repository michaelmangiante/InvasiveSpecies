#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mmangian
#
# Created:     28/02/2017
# Copyright:   (c) mmangian 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv
import os

# Data must be sorted from earliest year to latest year and then by earliest date to latest date.
data_type = 'plants'
debug = ''

if debug == 'Debug':
    inputdata = r'K:\InvasiveSpecies\FinalData\plantsDB\WorkingFolder\Test_Sqkm.csv'
    plantSpecies = open('K:\InvasiveSpecies\FinalData\plantsDB\WorkingFolder\PlantSpeciesList.txt', 'r')
    sciName = 5
    year = 8
    uniqueID = 0
    Huc12 = 13
    HucSqKm = 11
    Huc8 = 21
    Huc8SqKm = 23
else:
    inputdata = r'K:\InvasiveSpecies\FinalData\plantsDB\Plants_DB_conus_hucs_dated_LL.csv'
    plantSpecies = open('K:\InvasiveSpecies\FinalData\plantsDB\WorkingFolder\PlantSpeciesList.txt', 'r')
    sciName = 5
    year = 8
    uniqueID = 0
    Huc12 = 13
    HucSqKm = 11
    Huc8 = 21
    Huc8SqKm = 23
# Debugging

greatLakes = [40803000300,41202000300, 40203000300,40602000000,41502000200,90300091423] # Huron, Erie, Superior, Michigan, Ontario, lake of the woods
HUC8lakes = ['4020300', '4080300', '4060200', '4120200', '9030001', '9030009'] #Lake Superior, Lake Huron, lake Michigan, Lake Erie,Kabetogama Lake, lake of the woods
#########################################################################
# Start main script

# open empty string to add sciName to

# create stuff for output dataset
dirname = os.path.dirname(inputdata)
strName = str(data_type) + "_SumHucArea.csv"
outdata = os.path.join(dirname, strName)
if os.path.exists(outdata):
    os.remove(outdata)

# Read in plan species list

PlantSqKmList = []
HUC8sqkmlist = []
for plantline in plantSpecies:
    plantwhole = plantline.split()
    plant = str(plantwhole[0]) +" "+ str(plantwhole[1])
    HUClist = []
    sqkmlist = []
    HUC8list = []
    sqkmHUC8list = []
    print('Plant looking for is ' + str(plant))
    with open(inputdata, 'rb') as csvfile:
        spanreader = csv.reader(csvfile)
        headers = next(spanreader)[0:]
        # loop thruogh each species name
        for row in spanreader:
            inSciName = row[sciName]
            inYear = row[year]
            ID = row[uniqueID]
            #HUC = int(float(row[Huc12]))
            HUC = row[Huc12]
            sqkm = row[HucSqKm]
            HUC8 = row[Huc8]
            HUC8sqkm = row[Huc8SqKm]
            # check if huc is in huclist
            if inSciName == plant:
                if not any(HUC in s for s in HUClist):
                    if not (HUC == '40803000300' or HUC == '41202000300' or HUC == '40203000300' or HUC == '40602000000' or HUC == '41502000200' or HUC == '90300091423'): # last one is test or HUC == '10700061402'
                        HUClist.append(HUC)
                        sqkmlist.append(float(sqkm))
                        print(sqkm)
                        #print(HUC)
                    else:
                        print(str(HUC) + "DID NOT WORK")
                else:
                    print('HUC already exists')
            else:
                continue
            # for HUC 8
            if inSciName == plant:
                if not any(HUC8 in s for s in HUC8list):
                    if not any(HUC8 in s for s in HUC8lakes): # last one is test or HUC == '10700061402'
                        HUC8list.append(HUC8)
                        sqkmHUC8list.append(float(HUC8sqkm))
                        print(HUC8sqkm)
                        #print(HUC)
                    else:
                        print(str(HUC8) + "DID NOT WORK")
                        continue
                else:
                    continue
            else:
                continue
            # SUm the sq km and print result to output
    csvfile.close()
    plantsSqKm = sum(sqkmlist)
    nHuc12 = len(HUClist)
    PlantSqKmList.append(str(plant) + ";" + str(plantsSqKm) + ";" + str(nHuc12))
    # HUC 8 stuff
    Plants8SqKm = sum(sqkmHUC8list)
    nHuc8 = len(HUC8list)
    HUC8sqkmlist.append(str(plant)+ ";" + str(Plants8SqKm) + ";" + str(nHuc8))

with open(outdata, 'wb') as out:
    writer = csv.writer(out, lineterminator = '\n')
    writer.writerow(["SciName", "TotalHuc12SqKm", "CountofHUC12","SciName_HUC8", "TotalHuc8SqKm", "CountofHUC8"])
    for i, z in zip(PlantSqKmList, HUC8sqkmlist):
        pairData = i.split(";")
        HUC8data = z.split(";")
        outPlant = pairData[0]
        outSqKm = pairData[1]
        huc12count = pairData[2]
        HUC8plant = HUC8data[0]
        if HUC8plant == outPlant:
            huc8sqkm = HUC8data[1]
            nhuc8count = HUC8data[2]
        else:
            print('the species do not match')
            break
        writer.writerow([outPlant]+[outSqKm]+[huc12count]+[HUC8plant]+[huc8sqkm]+[nhuc8count])
out.close()

print('FinishedScript')

