import os
import datetime
try: import simplejson as json
except ImportError: import json
from gps_fix import *

# dates = ['20110420', '20110421', '20110422', '20110423', '20110424', '20110425', '20110426', '20110427', '20110428', '20110429', '20110430']
# dates = ['20110421']
dates = ['20110422', '20110423', '20110424', '20110425', '20110426', '20110427', '20110428', '20110429', '20110430']
distances = ['0M', '5M', '10M', '15M']

threshold = 180 # attending venue if duration exceeds this threshold (in second)

def time_diff(s1, s2):
    start = datetime.datetime.strptime(s1[:6], '%H%M%S')
    end = datetime.datetime.strptime(s2[:6], '%H%M%S')
    delta = end - start
    return delta.seconds

class DeviceDatePair:

    def __init__(self, date, device, distance, gps_fixes):
        self.gps_fixes = gps_fixes
        self.date = date
        self.device = device
        self.distance = distance
        self.venues_attended = []

    def end_time_fixes_that_contains_the_same_venue(self, i, venue):
        if i >= len(self.gps_fixes) - 1: # second last gps_fix it is
            return i, self.gps_fixes[i].time

        while venue in self.gps_fixes[i+1].venues_inside:
            if i >= len(self.gps_fixes) - 2: # second last gps_fix it is
                return i+1, self.gps_fixes[i+1].time
            else:
                i = i+1
        return i, self.gps_fixes[i].time

    def remove_venues_in_a_range(self, start, end, venue):
        for i in range(start, end+1):
            self.gps_fixes[i].venues_inside.remove(venue)

    def parse_venue_attendance(self):
        # skip that gps fixes that are not inside any venue
        for i in range(len(self.gps_fixes)):
            if self.gps_fixes[i].venues_inside == []:
                continue

            for venue in self.gps_fixes[i].venues_inside:
                start_time = self.gps_fixes[i].time
                # find end time of consecutive fixes that contains the same venue
                end_i, end_time = self.end_time_fixes_that_contains_the_same_venue(i, venue)

                # if difference of start time, end time bigger than threshold, append to venues attended
                delta = time_diff(start_time, end_time)
                if delta > threshold:
                    self.venues_attended.append((venue, start_time, end_time))

                # remove current venue in all consecutive fixes for speed up
                # if duration doesn't exceed threshold, no need to search more, since it will only be shorter
                # if duration does exceed threshold, no need to search further, since only the longest one should be output
                self.remove_venues_in_a_range(i, end_i, venue)

    def output_venue_attendance(self):
        filename = 'VenueAttendance/%s/%s/%s.json' % (self.date, self.distance, self.device)
        with open(filename, 'w') as of:
            for venue in self.venues_attended:
                venue_fields = {'venue': venue[0], 'start': venue[1], 'end': venue[2]}
                of.write(json.dumps(venue_fields) + '\n')

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
    for date in dates:
        print 'date: %s' % date
        # get all the device id under the date
        date_folder = '%s/position/' % (date)
        files = [f for f in os.listdir(date_folder) if f.endswith('.tsv')]
        devices = [f[:-4] for f in files]
        for device in devices:
            print '     device: %s' % (device)
            for distance in distances:
                # read device date pair from file
                device_date_pair = read_device_date_pair_from_file(date, device, distance)
                # parse venue attendance
                device_date_pair.parse_venue_attendance()
                # output to file
                device_date_pair.output_venue_attendance()

