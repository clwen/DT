import os
from gps_fix import *

class DeviceDatePair:
    def __init__(self):
        self.gps_fixes = []

def read_device_date_pair_from_file(date, device, distance):
    filename = 'GPSInsideVenue/%s/%s/%s.txt' % (date, distance, device)
    with open(filename) as f:
        lines = f.readlines()
        lines = lines[1:] # discard first line, which is comment
        tokens = lines[711].split(' ')
        # print tokens[0]
        # print tokens[1]
        # print tokens[2]
        print tokens[3]
        # for token in tokens:
        #     print token

def parse_venue_attendance(date, device, distance):
    pass

if __name__ == '__main__':
    # read device date pair from file
    read_device_date_pair_from_file('20110421', '17', '15M')

    # parse venue attendance from 
    # parse_venue_attendance('20110421', '17', '15M')


