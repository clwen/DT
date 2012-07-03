import csv
import re
import os
try: import simplejson as json
except ImportError: import json

distance = '15M'
venues = []
venue_dic = {}

demo_reader = csv.reader(open('demographic/2011_am.csv'))
header = demo_reader.next() # skip header

def read_venue_names(distance):
    venues = []
    geofile_prefix = 'Geofences/%s/' % distance
    geofiles = [f for f in os.listdir(geofile_prefix) if f.endswith('.mif')]
    for geofile in geofiles:
        venues.append(geofile[len(distance)+1:-4]) # remove 'xxM' and '.mif'
    return venues

def read_attendance(date, device):
    attendance = [0] * len(venues)
    # try to read the file, for ill format or non-exist, return 0 vector
    att_filename = 'VenueAttendance/%s/%s/%s.json' % (date, distance, device)
    atts = []
    try:
        with open(att_filename) as f:
            # for each line, collect all the venues attended
            lines = f.readlines()
            for line in lines:
                fields = json.loads(line)
                att = fields['venue']
                atts.append(att)
    except IOError:
        return attendance # return zero vector

    # for each venue attended, mark them in corresponding position in the vector
    for a in atts:
        idx = venue_dic[a]
        attendance[idx] = 1
    return attendance

if __name__ == '__main__':
    venues = read_venue_names(distance)
    # construct venue index dictionary
    for i in range(len(venues)):
        venue_dic[venues[i]] = i

    attendances = []
    for row in demo_reader:
        # parse date
        try:
            match = re.search(r'(\d+)/(\d+)/(\d+)', row[0])
            month = match.group(1) if len(match.group(1)) == 2 else '0' + match.group(1) # padding zero for single digit month such as 4 or 5
            day = match.group(2)
            year = match.group(3)
            date = year + month + day
        except AttributeError: # blank or ill format date
            date = 77770707

        device = row[2]

        print date, device
        attendance = read_attendance(date, device)
        attendances.append(attendance)

    # output attendances data to file
    att_writer = csv.writer(open('demographic/2011_att.csv', 'w'))
    for att in attendances:
        print att
        att_writer.writerow(att)
