def point_in_polygon(x, y, poly):
    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y-p1y) * (p2x-p1x) / (p2y-p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

# read gps fixes from a file first, say 20110421/99.tsv
gps_fixes = []
# open file
lines = open('20110421/position/99.tsv').readlines()
# discard first two lines, which are comments
lines = lines[2:]
# for each line
for line in lines:
    # parse lat, long pair
    tokens = line.split()
    lon, lat = tokens[3], tokens[4]
    print lon, lat
    gps_fixes.append((lon, lat))
print gps_fixes

# read all vertex from a specific geofences file first, say 15M Alladin
poly = []
# open file
lines = open('Geofences/15M/15M Aladdin The Flying Carpet Over Agrabah.mif').readlines()
# discard first 15 lines, which are comments
lines = lines[15:]
# for each line
for line in lines:
    # parse longitude, latitude pair
    tokens = line.split()
    lon, lat = tokens[0], tokens[1]
    print lon, lat
    poly.append((lon, lat))
print poly
