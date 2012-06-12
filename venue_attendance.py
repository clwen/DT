
# read gps fixes from a file first, say 20110421/99.tsv
gps_fixes = []
# open file
lines = open('20110421/position/99.tsv').readlines()
# discard first two lines, which is comment
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
# open file
