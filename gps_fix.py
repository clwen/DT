class GPSFix:

    def __init__(self, time, lon, lat, venues_inside = []):
        self.time = time
        self.lon = lon
        self.lat = lat
        self.venues_inside = venues_inside

    def update_venues_inside(self, venue_lst):
        self.venues_inside = venue_lst

    def __str__(self):
        return "%s  %s  %s  %s" % (self.time, self.lon, self.lat, self.venues_inside)

