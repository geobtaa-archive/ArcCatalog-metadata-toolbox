import arcpy, sys
arcpy.env.workspace = sys.argv[1]

fcList = arcpy.ListFeatureClasses()

for fc in fcList:
   arcpy.SynchronizeMetadata_conversion(fc,"ALWAYS")
