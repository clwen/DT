import os
import sys
import datetime
try: import simplejson as json
except ImportError: import json
from gps_fix import *

path = ''
distance = '15M'
threshold = 180 # attending venue if duration exceeds this threshold (in second)

def time_diff(s1, s2):
    start = datetime.datetime.strptime(s1[:6], '%H%M%S')
    end = datetime.datetime.strptime(s2[:6], '%H%M%S')
    delta = end - start
    return delta.seconds

class DeviceDatePair:

    def __init__(self, device, distance, gps_fixes):
        self.gps_fixes = gps_fixes
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
        filename = '%s/%s_venue.json' % (path, device)
        with open(filename, 'w') as of:
            for venue in self.venues_attended:
                venue_fields = {'venue': venue[0], 'start': venue[1], 'end': venue[2]}
                of.write(json.dumps(venue_fields) + '\n')

def read_device_date_pair_from_file(device):
    filename = '%s/%s_pip.json' % (path, device)
    gps_fixes = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            gps_fields = json.loads(line)
            # print gps_fields
            gps_fix = GPSFix(gps_fields['time'], gps_fields['lon'], gps_fields['lat'], gps_fields['venues_inside'])
            gps_fixes.append(gps_fix)
    device_date_pair = DeviceDatePair(device, distance, gps_fixes)
    return device_date_pair

if __name__ == '__main__':
    path = sys.argv[1]
    tsv_files = [f for f in os.listdir(path) if f.endswith('.tsv')]
    devices = [f[:-4] for f in tsv_files]
    for device in devices:
        print device
        # read device date pair from file
        device_date_pair = read_device_date_pair_from_file(device)
        # parse venue attendance
        device_date_pair.parse_venue_attendance()
        # output to file
        device_date_pair.output_venue_attendance()
