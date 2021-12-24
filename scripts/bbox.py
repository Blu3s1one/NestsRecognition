def world2Pixel(geoMatrix, x , y):
    u1X = geoMatrix[0]
    u1Y = geoMatrix[3]
    xDist = geoMatrix[1]
    yDist = geoMatrix[5]
    rtnX = geoMatrix[2]
    rtnY = geoMatrix[4]
    pixel = int((x - u1X) / xDist)
    line = int((y - u1Y) /yDist)
    return (pixel, line)

def get_tif_path_ptw(json):
    rad=json.stem
    tif='pixel_to_world/tifs/'+rad+'.tif'
    return tif
def get_tif_path_wtp(json):
    rad=json.stem
    tif='world_to_pixel/tifs/'+rad+'.tif'
    return tif

def get_pixel_coordinates(coordinates,geotrans):
    xmin,ymin = world2Pixel(geotrans,coordinates[0][0],coordinates[0][1])
    xmax, ymax = world2Pixel(geotrans,coordinates[0][0],coordinates[0][1])
    for i in coordinates:
        x,y= world2Pixel(geotrans,i[0],i[1])
        if x>xmax:
            xmax=x
        if y>ymax:
            ymax=y
        if x<xmin:
            xmin=x
        if y<ymin:
            ymin=y
    return([xmin,ymin,xmax,ymax])

def get_label(objectif, properties):
    if objectif == 'oiseau':
        if properties['GA']==1 or properties['GM']==1 or properties['GB']==1:
            return 'bird'
        else:
            return None


    elif objectif == 'nid':
        if properties['Pas de nid']==None:
            return 'nest'
        else:
            return None
    elif objectif == 'espèce':
        if properties['GA'] == 1:
            return 'GA'
        if properties['GM']==1:
            return 'GM'
        if properties['GB'] == 1:
            return 'GB'


    else:
        print('Objectif invalide. Les objectifs valides sont oiseau, nid ou espèce')


