import arcpy, sys
arcpy.env.workspace = sys.argv[1]
dir = arcpy.GetInstallInfo("desktop")["InstallDir"]
translator = dir + "Metadata/Translator/FGDC2ESRI_ISO.xml"
for file in arcpy.ListFiles("*.xml"):
   outfile = file.replace('.xml','_arc.xml')
   arcpy.ESRITranslator_conversion(file,translator,outfile)
