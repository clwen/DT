import os

dates = ['20110420', '20110421', '20110422', '20110423', '20110424', '20110425', '20110426', '20110427', '20110428', '20110429', '20110430']
distances = ['0M', '5M', '10M', '15M']

for date in dates:
    for distance in distances:
        dir_name = 'VenueAttendance/%s/%s' % (date, distance)
        print dir_name
        os.system('mkdir -p %s' % dir_name)
