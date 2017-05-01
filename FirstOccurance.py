#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Samantha
#
# Created:     21/02/2017
# Copyright:   (c) Samantha 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv
import os

# Data must be sorted from earliest year to latest year and then by earliest date to latest date.
data_type = 'plants'
debug = ''

if debug == 'Debug':
    inputdata = r'E:\MikesData_2162017\InvasiveSpecies\FinalData\plantsDB\WorkingFolder\Test_FirstOccurance.csv'
    uniqueID = 0
    sciName = 1
    year = 2
else:
    inputdata = r'E:\MikesData_2162017\InvasiveSpecies\FinalData\plantsDB\Plants_DB_conus_hucs_dated_LL.csv'
    sciName = 5
    year = 8
    uniqueID = 0
# Debugging


#########################################################################
# Start main script

# open empty string to add sciName to

# create stuff for output dataset
dirname = os.path.dirname(inputdata)
strName = str(data_type) + "_FirstOccurances.csv"
outdata = os.path.join(dirname, strName)
if os.path.exists(outdata):
    os.remove(outdata)

dataList = []
with open(inputdata, 'rb') as csvfile:
    spanreader = csv.reader(csvfile)
    headers = next(spanreader)[0:]
    for row in spanreader:
        inSciName = row[sciName]
        inYear = row[year]
        ID = row[uniqueID]
        if any(inSciName in s for s in dataList):
            matching = [s for s in dataList if inSciName in s]
            inListdata = matching[0].split(";")
            if int(inListdata[1]) > int(inYear):
                dataList = [w.replace(matching[0], str(inSciName) + ";" + str(inYear) + ";" + str(ID)) for w in dataList]
            else:
                continue
        else:
            dataList.append(str(inSciName) + ";" + str(inYear) + ";" + str(ID))

print(dataList)

# get the unique names in a single list
uniqueID_list = []

for i in dataList:
    indata = i.split(";")
    uniqueID_list.append(indata[2])

#writer = csv.writer(open(outdata, 'wb'), lineterminator = '\n')
with open(outdata, 'wb') as out:
    writer = csv.writer(out, lineterminator = '\n')
    writer.writerow(headers)
    with open(inputdata, 'rb') as read_data:
        dataRead = csv.reader(read_data)
        skipped = next(dataRead)[0:]
        for row in dataRead:
            #if any(row[uniqueID] in s for s in uniqueID_list):
            for s in uniqueID_list:
                if row[uniqueID] == s:
                    writer.writerow(row)
                else:
                    continue

print('finished script')

#with open(outdata, 'w') as f:
#     write = csv.writer(f, lineterminator = '\n')
#     write.writerow(["SpeciesName", "Year"])
#     for i in dataList:
#        outListData = i.split(";")
#        SpcName = outListData[0]
#        YearName = outListData[1]
#        write.writerow([SpcName] + [YearName])

#print('finished script')


