import os
import simplejson as json
from gps_fix import *

# dates = ['20110420', '20110421', '20110422', '20110423', '20110424', '20110425', '20110426', '20110427', '20110428', '20110429', '20110430']
dates = ['20110420']
# dates = ['20110421', '20110422', '20110423', '20110424', '20110425', '20110426', '20110427', '20110428', '20110429', '20110430']
distances = ['0M', '5M', '10M', '15M']

class DeviceDatePair:

    def __init__(self, date, device, distance, gps_fixes):
        self.gps_fixes = gps_fixes
        self.date = date
        self.device = device
        self.distance = distance
        self.venues_attended = []

    def parse_venue_attendance(self):
        print 'parse venue attendance'

    def output_venue_attendance(self):
        print 'output venue attendance'

def read_device_date_pair_from_file(date, device, distance):
    filename = 'GPSInsideVenue/%s/%s/%s.json' % (date, distance, device)
    gps_fixes = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            gps_fields = json.loads(line)
            # print gps_fields
            gps_fix = GPSFix(gps_fields['time'], gps_fields['lon'], gps_fields['lat'], gps_fields['venues_inside'])
            gps_fixes.append(gps_fix)
    device_date_pair = DeviceDatePair(date, device, distance, gps_fixes)
    return device_date_pair

if __name__ == '__main__':
    # read device date pair from file
    device_date_pair = read_device_date_pair_from_file('20110421', '17', '15M')
    # parse venue attendance
    device_date_pair.parse_venue_attendance()
    # output to file
    device_date_pair.output_venue_attendance()

