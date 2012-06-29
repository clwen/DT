import csv

demo_reader = csv.reader(open('demographic/2011_am.csv'))
header = demo_reader.next() # skip header

demo_groups = []
for row in demo_reader:
    fields = []

    if row[3] == 'Y':
        hotel_guest = 1
    else:
        hotel_guest = 0
    fields.append(hotel_guest)

    if row[4] == 'Y':
        annual_pass = 1
    else:
        annual_pass = 0
    fields.append(annual_pass)

    if row[5] == 'Y':
        on_property = 1
    else:
        on_property = 0
    fields.append(on_property)

    if row[7] == 'Y':
        meal_plan = 1
    else:
        meal_plan = 0
    fields.append(meal_plan)

    if row[8] == '5+':
        num_trip = 5
    elif row[8] == '\'2-4': # compromise with weired input in the original xls
        num_trip = 3
    else:
        num_trip = 1
    fields.append(num_trip)

    if row[9] == 'Y':
        past_five_yr = 1
    else:
        past_five_yr = 0
    fields.append(past_five_yr)

    if row[11] == '':
        person_in_grp = 1 # fail safe: default by 1
    else:
        person_in_grp = int(row[11])
    fields.append(person_in_grp)

    if row[12] == 'Family':
        relationship = 0
    elif row[12] == 'Friends':
        relationship = 1
    elif row[12] == 'Couple':
        relationship = 2
    else:
        relationship = 3
    fields.append(relationship)

    if row[13] == 'F':
        p1_gender = 0
    else:
        p1_gender = 1 # default: M
    fields.append(p1_gender)

    try:
        p1_age = int(row[14])
    except ValueError:
        p1_age = 0 # default value if no input or ill-format input
    fields.append(p1_age)

    if row[15] == 'F':
        p2_gender = 0
    else:
        p2_gender = 1 # default: M
    fields.append(p2_gender)

    try:
        p2_age = int(row[16])
    except ValueError:
        p2_age = 0 # default value if no input or ill-format input
    fields.append(p2_age)

    if row[17] == 'F':
        p3_gender = 0
    else:
        p3_gender = 1 # default: M
    fields.append(p3_gender)

    try:
        p3_age = int(row[18])
    except ValueError:
        p3_age = 0 # default value if no input or ill-format input
    fields.append(p3_age)

    if row[19] == 'F':
        p4_gender = 0
    else:
        p4_gender = 1 # default: M
    fields.append(p4_gender)

    try:
        p4_age = int(row[20])
    except ValueError:
        p4_age = 0 # default value if no input or ill-format input
    fields.append(p4_age)

    if row[21] == 'F':
        p5_gender = 0
    else:
        p5_gender = 1 # default: M
    fields.append(p5_gender)

    try:
        p5_age = int(row[22])
    except ValueError:
        p5_age = 0 # default value if no input or ill-format input
    fields.append(p5_age)

    if row[23] == 'Thrill rides':
        thrill_rides = 1
    else:
        thrill_rides = 0
    fields.append(thrill_rides)

    demo_groups.append(fields)

for group in demo_groups:
    print group

