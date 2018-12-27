"""
Function to create buffers for geometries

Inputs:
    - list that includes one or more geometry
    - buffer size in meters
    
Output:
    - list that includes all new geometries

"""

def getbuffers( geometry_list, buffer_size ):
    
    # Append the new buffers to this empty list
    buffer_geometries = []
    
    for geom in geometry_list:
        buffer_geometry = geom.Buffer(buffer_size, 1)
        buffer_geometries.append(buffer_geometry)

    return buffer_geometries