

#Export all layouts in a project as png files
import arcpy.mp

# Create an ArcGIS project object
project = arcpy.mp.ArcGISProject("Current")

# Assign the path for exports
output_path = r"C:\Users\YourUsername\Desktop\Folder"

# Export
for layout in project.listLayouts():
    # Export all pages for a map series, if there's a map series in the project
    if layout.mapSeries:
        if layout.mapSeries.enabled:
            layout.mapSeries.currentPageNumber = 1
            for num in range(1, layout.mapSeries.pageCount + 1):
                page_name = layout.mapSeries.pageRow[3]
                print(f"Exporting the layout for {page_name} to {output_path}")
                layout.exportToPNG(f"{output_path}\\{page_name}")
                print("Export Complete\n")

                if layout.mapSeries.currentPageNumber < layout.mapSeries.pageCount:
                    layout.mapSeries.currentPageNumber += 1

    # Export all other layouts
    else:
        layout_name = layout.name
        print(f"Exporting the layout for {layout_name} to the following folder: {output_path}")
        layout.exportToPNG(f"{output_path}\\{layout_name}")
        print("Export Complete\n")

print("All layouts have been exported")