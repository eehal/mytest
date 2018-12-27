"""
Function computes NDVI values when given lists of reflectances from red and near infrared (NIR) bands.

OUTPUT:
Function returns list of NDVI values.

"""

def getndvi( red_band_list , nir_band_list ):
    
    # Append new NDVI values into a list
    NDVI_list = []
    
    for j in range(len(red_band_list)):
        RED  = red_band_list[j]
        NIR  = nir_band_list[j]
        NDVI = (NIR-RED) / (NIR+RED)
        NDVI_list.append(NDVI)

    return NDVI_list