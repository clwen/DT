import os

def point_in_polygon(x, y, poly):
    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x, p2y = poly[i % n]
        # print '==========================='
        # print 'y: ' + y
        # print 'min y: ' + min(p1y, p2y)
        # print 'max y: ' + max(p1y, p2y)
        # print 'x: ' + x
        # print 'max x: ' + max(p1x, p2x)
        # print '==========================='
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y-p1y) * (p2x-p1x) / (p2y-p1y) + p1x
                        print x, xinters
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

if __name__ == '__main__':
    # read gps fixes from a file first, say 20110421/99.tsv
    gps_fixes = []
    # open file
    lines = open('20110421/position/94.tsv').readlines()
    # discard first two lines, which are comments
    lines = lines[2:]
    # for each line
    for line in lines:
        # parse lat, long pair
        tokens = line.split()
        lon, lat = tokens[3], tokens[4]
        gps_fixes.append((lon, lat))
    print len(gps_fixes), gps_fixes

    geofile_prefix = 'Geofences/15M/'
    geofiles = [f for f in os.listdir(geofile_prefix) if f.endswith('.mif')]
    print geofiles

    for geofile in geofiles:
        # read all vertex from a specific geofences file first, say 15M Alladin
        poly = []
        # open file
        lines = open(geofile_prefix + geofile).readlines()
        # discard first 15 lines, which are comments
        lines = lines[15:]
        # for each line
        for line in lines:
            # parse longitude, latitude pair
            tokens = line.split()
            lon, lat = tokens[0], tokens[1]
            poly.append((lon, lat))
        print len(poly), poly

        # for each gps fixes
        for gps_fix in gps_fixes:
            x, y = gps_fix[0], gps_fix[1]
            # test whether its inside the poly
            inside = point_in_polygon(x, y, poly)
            print x, y, inside
