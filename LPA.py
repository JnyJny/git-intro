import arcpy
import arcpy.da

def main():
    # arcpy.env.workspace = r"D:\ArcGIS\Projects\LPA\ArcGIS Pro Files\LPA.gdb"
    # moveit()
    # spatjoin()
    calclatlong()
    excel()


def moveit():
    arcpy.env.workspace = r"D:\ArcGIS\Projects\Geocode_October_2020\ArcGIS Pro Files\Geocode_Ocotober_2020\Geocode_Ocotober_2020.gdb"
    outpath = r"D:\ArcGIS\Projects\LPA\ArcGIS Pro Files\LPA.gdb"
    rawgeo = r"D:\ArcGIS\Projects\Geocode_October_2020\ArcGIS Pro Files\Geocode_Ocotober_2020\Geocode_Ocotober_2020.gdb\Student_Geocoded_20201019_Extra"
    geof = "Student_Geocoded_20201019_Extra"

    arcpy.FeatureClassToFeatureClass_conversion(rawgeo, outpath, geof)


def spatjoin():
    arcpy.env.workspace = r"D:\ArcGIS\Projects\LPA\ArcGIS Pro Files\LPA.gdb"
    geof = "Student_Geocoded_20201019_Extra"
    lpazone = "LPA_Zone"
    lpa = "LPA_Geocoded_Extra"
    fieldmap = arcpy.FieldMappings()
    fieldmap.addTable(geof)
    arcpy.SpatialJoin_analysis(geof, lpazone, lpa, "JOIN_ONE_TO_ONE", "KEEP_COMMON", fieldmap, "INTERSECT", None, '')


def excel():
    arcpy.env.workspace = r"D:\ArcGIS\Projects\LPA\ArcGIS Pro Files\LPA.gdb"
    lpa = "LPA_Geocoded_Extra"
    outpath = r"D:\ArcGIS\Projects\LPA\Documents\LPA.XLSX"
    arcpy.TableToExcel_conversion(lpa, outpath)


def calclatlong():
    arcpy.env.workspace = r"D:\ArcGIS\Projects\Geocode_October_2020\ArcGIS Pro Files\Geocode_Ocotober_2020\Geocode_Ocotober_2020.gdb"
    # lpa = "LPA_Geocoded_Extra"
    lpa = "Student_Geocoded_20201019_SAZ"
    arcpy.AddField_management(lpa, "Latitude", "FLOAT", field_alias="Latitude")
    arcpy.AddField_management(lpa, "Longitude", "FLOAT", field_alias="Longitude")
    arcpy.CalculateGeometryAttributes_management(lpa, "Latitude POINT_Y;Longitude POINT_X", '', '',
                                                 None, "DD")


if __name__ == '__main__':
    main()
