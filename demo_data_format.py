import csv

demo_reader = csv.reader(open('demographic/2011_am.csv'))
header = demo_reader.next() # skip header

resort_dic = {}
next_available_rid = 1

country_dic = {}
next_available_cid = 1

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

    r = row[6]
    if r == '':
        resort_living = 0
    elif r in resort_dic:
        resort_living = resort_dic[r]
    else:
        resort_dic[r] = next_available_rid
        next_available_rid += 1
        resort_living = resort_dic[r]
    fields.append(resort_living)

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

    c = row[10]
    if c == '':
        country_living = 0
    elif c in country_dic:
        country_living = country_dic[c]
    else:
        country_dic[c] = next_available_cid # add new country to country_dic
        next_available_cid += 1 # update next available country id
        country_living = country_dic[c]
    fields.append(country_living)

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

    if row[24] == 'Non-thrill rides':
        non_thrill_rides = 1
    else:
        non_thrill_rides = 0
    fields.append(non_thrill_rides)

    if row[25] == 'Indoor shows':
        indoor_shows = 1
    else:
        indoor_shows = 0
    fields.append(indoor_shows)

    if row[26] == 'Parades and fireworks':
        parades = 1
    else:
        parades = 0
    fields.append(parades)

    if row[27] == 'Meeting characters':
        characters = 1
    else:
        characters = 0
    fields.append(characters)

    if row[28] == 'Overall atmosphere':
        atmosphere = 1
    else:
        atmosphere = 0
    fields.append(atmosphere)

    if row[29] == 'Definitely':
        plan_for_day = 3
    elif row[29] == 'Somewhat':
        plan_for_day = 2
    elif row[29] == 'Not really':
        plan_for_day = 1
    else:
        plan_for_day = 0
    fields.append(plan_for_day)

    if row[30] == 'Y':
        dining_plan = 1
    else:
        dining_plan = 0
    fields.append(dining_plan)

    if row[31] == 'Y':
        must_see = 1
    else:
        must_see = 0
    fields.append(must_see)

    try:
        wait_must_see = int(row[33])
    except ValueError:
        wait_must_see = 0 # default value if no input or ill-format input
    fields.append(wait_must_see)

    try:
        wait_others = int(row[34])
    except ValueError:
        wait_others = 0 # default value if no input or ill-format input
    fields.append(wait_others)

    demo_groups.append(fields)

for group in demo_groups:
    print group

print resort_dic
print country_dic
