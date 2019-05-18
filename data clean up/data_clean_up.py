#!/usr/bin/env python3

# Started by TSun May5/2019, last edited by TSun May8/2019.
# This python3 script was created for cleaning up the raw data set for the ECE143_19SP Porject of team 2.

import csv
from datetime import date
new_year = []
new_month = []
new_day = []
new_daytype = []
new_time = []
new_city = []
new_province = []
new_locationtype = []
new_location_density = []
new_target = []
new_kills = []
new_injures = []
new_temperature = []
with open('PakistanSuicideAttacks_raw.csv', encoding="utf8", errors='ignore') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for i,row in enumerate(csv_reader,-1):
        length = i
        if i>=0:

            # Modify Date into year-month-day-dayName
            new_year.append(int(row[1][-4:]))
            new_day.append(row[1][-7:-5])
            if new_day[i][0] == ' ' or new_day[i][0] == '-':
                new_day[i] = new_day[i][1]
            new_day[i] = int(new_day[i])
            if 'January' in row[1] or 'Jan' in row[1]:
                new_month.append(1)
            elif 'February' in row[1] or 'Feb' in row[1]:
                new_month.append(2)
            elif 'March' in row[1] or 'Mar' in row[1]:
                new_month.append(3)
            elif 'April' in row[1] or 'Apr' in row[1]:
                new_month.append(4)
            elif 'May' in row[1] or 'May' in row[1]:
                new_month.append(5)
            elif 'June' in row[1] or 'June' in row[1]:
                new_month.append(6)
            elif 'July' in row[1] or 'July' in row[1]:
                new_month.append(7)
            elif 'August' in row[1] or 'Aug' in row[1]:
                new_month.append(8)
            elif 'September' in row[1] or 'Sep' in row[1]:
                new_month.append(9)
            elif 'October' in row[1] or 'Oct' in row[1]:
                new_month.append(10)
            elif 'November' in row[1] or 'Nov' in row[1]:
                new_month.append(11)
            elif 'December' in row[1] or 'Dec' in row[1]:
                new_month.append(12)
            else:
                assert False, row[1]
            if date(new_year[i],new_month[i],new_day[i]).weekday() > 4 or row[3] == 'Holiday':
                new_daytype.append('Weekend or Holiday')
            else:
                new_daytype.append('Working Day')

            # Modify Time
            Missing = ['N/A','NA','NA ','','Half hour after aftar','aftar time','5 min befor aftar']
            if row[5] in Missing:
                new_time.append('Missing')
            elif ':' in row[5] or '.' in row[5] or 'pm' in row[5]:
                if row[5][0:7] == 'between':
                    temp = int(row[5][8:10] if row[5][9].isdigit() else row[5][8])
                elif row[5][0:6] == 'around':
                    temp = int(row[5][7:9] if row[5][8].isdigit() else row[5][7])
                elif row[5][0:5] == 'About':
                    temp = int(row[5][6:8] if row[5][7].isdigit() else row[5][6])
                else:
                    temp = int(row[5][0:2] if row[5][1].isdigit() else row[5][0])
                if temp < 12 and ('PM' in row[5] or 'pm' in row[5]):
                    temp += 12
                new_time.append(temp)
            elif 'evening' in row[5] or 'Night' in row[5] or 'Evening' in row[5] or 'night' in row[5]:
                new_time.append([18,19,20,21,22])
            elif 'Morning' in row[5] or 'MORNING' in row[5]:
                new_time.append([7,8,9,10])
            elif row[5] == 'About 12pm' or 'after noon' in row[5].lower() or 'Noon' in row[5]:
                new_time.append(12)
            elif 'maghrib' in row[5] or 'Maghrib' in row[5]:
                new_time.append(18)
            elif 'Jummah prayer' in row[5] or 'Friday prayers' in row[5] or 'Friday prayer' in row[5]:
                new_time.append(12)
            else:
                assert False, row[5]

            # Modify Location
            if False:
                pass
            else:
                new_city.append(row[6])
                
            if row[9] == 'KPK':
                new_province.append('Khyber-Pakhtunkhwa')
            elif row[9] == 'Baluchistan':
                new_province.append('Balochistan')
            else:
                new_province.append(row[9])

            if row[11] == '' or row[11] == ' ':
                new_locationtype.append('Missing')
            elif row[11].lower() in ['foreign','foreigner']:
                new_locationtype.append('Foreign Area')
            elif row[11] in ['Office', 'Office Building','Government','Government/Office Building','Government Official']:
                new_locationtype.append('Office Building')
            elif row[11] in ['Hotel', 'Hospital']:
                new_locationtype.append('Hotel and Hospital')
            elif row[11] in ['Religious']:
                new_locationtype.append('Religious Area')
            elif row[11] in ['Mobile']:
                new_locationtype.append('Vehicle')
            elif row[11] in ['Military','Police']:
                new_locationtype.append('Military or Police Area')
            elif row[11] in ['Residence','Park/Ground','Market','Educational','Civilian','Bank','Residential Building','Commercial/residence']:
                new_locationtype.append('Commercial and Residence Area')
            elif row[11] in ['Airport', 'Transport','Highway']:
                new_locationtype.append('Transport')
            else:
                assert False, row[11]

            if row[12] == '' or row[12] == ' ':
                new_location_density.append('Missing')
            else:
                new_location_density.append(row[12])

            # Modify Target Type
            if row[15] in ['',' ','Unknown','None']:
                new_target.append('Missing')
            elif row[15].lower() in ['foreigner']:
                new_target.append('Tourist')
            elif row[15].lower() in ['civilian','children/women']:
                new_target.append('Civilian')
            elif row[15].lower() in ['media', 'government official','advocates (lawyers)','civilian judges','judges & lawyers']:
                new_target.append('Government, Media and Officer')
            elif row[15].lower() in ['shia sect','election candidate','prominent political leaders']:
                new_target.append('Party and Election')
            elif row[15].lower() in ['religious']:
                new_target.append('Religious')
            elif row[15].lower() in ['military','police','anti-militants','rangers','police & rangers','civilian & police','army','frontier corps ']:
                new_target.append('Police and Military')
            else:
                assert False, row[15]

            # Modify Kills and Injures
            if row[17] in ['',' '] and row[18] in ['',' ']:
                new_kills.append('Missing')
            elif row[17] in ['',' ']:
                new_kills.append(int(row[18]))
            elif row[18] in ['',' ']:
                new_kills.append(int(row[17]))
            else :
                new_kills.append(int((int(row[17])+int(row[18]))/2))
                
            if row[19] in ['',' '] and (row[20] in ['',' '] or row[20][0:4] == 'http'):
                new_injures.append('Missing')
            elif row[19] in ['',' ']:
                new_injures.append(int(row[20]))
            elif row[20] in ['',' ']:
                new_injures.append(int(row[19]))
            else :
                if row[20][-1] == '+':
                    new_injures.append(int((int(row[19])+int(row[20][0:-1]))/2))
                else:
                    new_injures.append(int((int(row[19])+int(row[20]))/2))

            # Modify Temperature(F)
            if row[25] in ['',' ']:
                new_temperature.append('Missing')
            else:
                new_temperature.append(int(float(row[25])//1))

with open('PakistanSuicideAttacks_modified.csv', mode='w',newline ='') as writer_file:
    writer = csv.writer(writer_file, delimiter=',')
    writer.writerow(['Year', 'Month', 'Day','Daytype','Time','City','Province','LocationType','Density','Target','Kills','Injures','Temperature(F)'])
    for i in range(length+1):
        writer.writerow([new_year[i],new_month[i],new_day[i],new_daytype[i],new_time[i],new_city[i],new_province[i],new_locationtype[i],new_location_density[i],new_target[i],new_kills[i],new_injures[i],new_temperature[i]])
