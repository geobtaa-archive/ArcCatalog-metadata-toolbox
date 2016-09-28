import arcpy, sys
sources = sys.argv[1]
translator = "export2arc.xml"
output_folder = sys.argv[2]

arcpy.ExportMetadataMultiple_conversion (sources, translator, output_folder)


