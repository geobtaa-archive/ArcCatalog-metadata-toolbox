# Custom ArcGIS Toolbox of Batch Metadata Scripts

Scripts Included:

Translate FGDC to ArcGIS for Standalone XML file
Calls the ESRI Translator tool to convert standalone XML files in FGDC CSDGM to the ArcGIS Metadata 1.0 Format. This tool should be used for standalone metadata files, because it does not perform any of the processes in the Upgrade Model, such as synchronization.


Synchronize ArcGIS Metadata for Feature Classes
Calls the Synchronize model to create or update a metadata file for a feature class in the ArcGIS Metadata 1.0 Format.

Upgrade FGDC to ArcGIS for Feature Classes
Calls the Upgrade Model to convert FGDC CSDGM to the ArcGIS Metadata 1.0 Format for a group of feature classes. This tool will also perform synchronization of metadata with the dataset.


Export to ArcGIS Metadata
Calls the batch export tool to create ArcGIS Metadata 1.0 Format as XML files. The export tool will run processes, such as synchronization, to the metadata before exporting it.