# split up the dataset by HUC2
import os, sys
import arcpy
from arcpy import env

#HUC 2 location
HUC2 = r'K:\InvasiveSpecies\FinalData\plantsDB\plantsDB.gdb\EnviroAtlas_HUC2_augmentedarea'
# in plant or animal data to be split by huc 2
inData = r'K:\InvasiveSpecies\FinalData\animalsDB\AnimalsDB.gdb\Animals31417_final_albers'
# the output folder to hold the shapefiles of the split operation
shpLoc = r'H:\InvasiveSpecies\HUC2Analysis\AnimalsByHUC2shp'
# the output folder that will hold the sub folders of all the stats/dbf files
outputFiles = r'H:\InvasiveSpecies\HUC2Analysis\Aniamsl_HUCSummary'
# the field that you split everything with from the HUC data
splitField = 'HUC_2_'

# split analysis

arcpy.Split_analysis(inData, HUC2, splitField, shpLoc)

# make DBF files from input shapefile

fcList = arcpy.ListFeatureClasses(shpLoc)

for i in range(1,19):
    print('current run is ' + str(i))
    inFile = os.path.join(shpLoc, "{}.shp".format(i))
    outws = os.path.join(outputFiles, "HUC{}".format(i))
    outFile = "HUC{}.dbf".format(i)
    arcpy.TableToTable_conversion(inFile, outws, outFile)
    print('finished running ' + str(i))
