import arcpy, sys
arcpy.env.workspace = sys.argv[1]

fcList = arcpy.ListFeatureClasses()

for fc in fcList:
   arcpy.UpgradeMetadata_conversion (fc, "FGDC_TO_ARCGIS")
