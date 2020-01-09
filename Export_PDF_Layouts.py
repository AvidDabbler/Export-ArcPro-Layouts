import arcpy
import os

pdf_path = input('Where would you like to save the pdf documents? ' )or 'W:\\Research&Development\\Data-Share\\analysis-fin\\TitleVI\\TitleVI\\MR\\'
aprx_loc= input('Where is the arcgis pro projecct? ') or r'W:\Research&Development\Data-Share\analysis-dev\TitleVI\MetroReimagined_190917\MR_TitleVI_Analysis_190917\MR_TitleVI_Analysis_190917.aprx'

aprx = aprx_loc.split('\\')[-1]
print(aprx)

os.path.dirname(pdf_path)
proj_path = os.path.dirname(aprx_loc)

project = arcpy.mp.ArcGISProject(proj_path + aprx)

list = project.listLayouts()


for item in list:
    item.exportToPDF(pdf_path + item.name, resolution=300)
    print(pdf_path + item.name + " created")

