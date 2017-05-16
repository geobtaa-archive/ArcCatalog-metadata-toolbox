import arcpy, sys, os
from arcpy import env

arcpy.env.workspace = sys.argv[1]


for isoFile in arcpy.ListFiles("*ISO.xml"):
    fileNameA = isoFile.split("_")[0]
    for arcFile in arcpy.ListFiles("*shp.xml"):
        fileNameB = arcFile.split("_")[0]

        if fileNameA == fileNameB:

            arcpy.ImportMetadata_conversion(isoFile, "FROM_ISO_19139", arcFile, "DISABLED")
                                         

            
    
