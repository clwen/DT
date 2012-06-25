import os
import sys
try: import simplejson as json
except ImportError: import json
from gps_fix import *

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

def read_gps_fixes_from_file(date, device):
    gps_file = '%s/position/%s.tsv' % (date, device)
    # read gps fixes from the file
    gps_fixes = []
    # open file
    with open(gps_file) as f:
        lines = f.readlines()
    # discard first two lines, which are comments
    lines = lines[2:]
    # for each line
    for line in lines:
        # parse lat, long pair
        tokens = line.split()
        time, lon, lat = str(tokens[0]), float(tokens[3]), float(tokens[4])
        gps_fix = GPSFix(time, lon, lat)
        gps_fixes.append(gps_fix)
    return gps_fixes

def read_times_from_file(date, device):
    gps_file = '%s/position/%s.tsv' % (date, device)
    # read gps fixes from the file
    times = []
    # open file
    with open(gps_file) as f:
        lines = f.readlines()
    # discard first two lines, which are comments
    lines = lines[2:]
    # for each line
    for line in lines:
        # parse lat, long pair
        tokens = line.split()
        time = str(tokens[0])
        times.append(time)
    return times

def read_venue_names(distance):
    venues = []
    geofile_prefix = 'Geofences/%s/' % distance
    geofiles = [f for f in os.listdir(geofile_prefix) if f.endswith('.mif')]
    for geofile in geofiles:
        venues.append(geofile[len(distance)+1:-4]) # remove 'xxM' and '.mif'
    return venues

def read_polys_from_files(distance):
    polys = []
    geofile_prefix = 'Geofences/%s/' % distance
    geofiles = [f for f in os.listdir(geofile_prefix) if f.endswith('.mif')]
    for geofile in geofiles:
        # read all vertex from the geofences file
        poly = []
        # open file
        lines = open(geofile_prefix + geofile).readlines()
        # discard first 15 lines, which are comments
        lines = lines[15:]
        # for each line
        for line in lines:
            # parse longitude, latitude pair
            tokens = line.split()
            lon, lat = float(tokens[0]), float(tokens[1])
            poly.append((lon, lat))
        polys.append(poly)
    return polys

def gps_in_venue(date, device, distance):
    gps_fixes = read_gps_fixes_from_file(date, device)
    polys = read_polys_from_files(distance)
    venues = read_venue_names(distance)

    output_file = 'GPSInsideVenue/%s/%s/%s.json' % (date, distance, device)
    with open(output_file, 'w') as of:
        # for each gps fixes
        for i in range(len(gps_fixes)):
            gps_fix = gps_fixes[i]
            time = gps_fix.time
            x, y = gps_fix.lon, gps_fix.lat
            # test whether its inside the poly
            venues_inside = []
            for j in range(len(polys)):
                assert len(polys) == len(venues)
                poly = polys[j]
                venue = venues[j]
                inside = point_in_polygon(x, y, poly)
                if inside:
                    venues_inside.append(venue)
            # update venues inside information in object
            gps_fields = {'time': time, 'lon': x, 'lat': y, 'venues_inside': venues_inside}
            of.write(json.dumps(gps_fields) + '\n')

if __name__ == '__main__':
    path = sys.argv[1]
    tsv_files = [f for f in os.listdir(path) if f.endswith('.tsv')]
    devices = [f[:-4] for f in tsv_files]
    for device in devices:
        print device
