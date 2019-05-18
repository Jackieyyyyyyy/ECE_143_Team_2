#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:22:37 2019

@author: jerrychen
"""

import pandas as pd
import seaborn as sns

pakistan_data = pd.read_csv('/Users/jerrychen/Documents/GitHub/ECE_143_Team_2/data clean up/PakistanSuicideAttacks_modified.csv')
pakistan_data_dict = dict(pakistan_data)

y_axis = 'Targeted Relgion'

heatmap_data_dict = {}
heatmap_data_dict['Year'] = pakistan_data_dict['Year']
heatmap_data_dict[y_axis] = pakistan_data_dict[y_axis]
heatmap_data_dict['Kills'] = pakistan_data_dict['Kills']

heatmap_data_dict_cleaned = {'Year':[],y_axis:[],'Kills':[]}

year_list = list(heatmap_data_dict['Year'])
loc_type_list = list(heatmap_data_dict[y_axis])
kill_list = list(heatmap_data_dict['Kills'])    

year_loc_pair_list = []

row = 0
'''while row < len(loc_type_list):
    #print(loc_type_list[row])
    if '/' in str(loc_type_list[row]):
        slash_index = loc_type_list[row].index('/')
        loc_type_list.append(loc_type_list[row][slash_index+1:])
        year_list.append(year_list[row])
        kill_list.append(kill_list[row])
        loc_type_list[row] = loc_type_list[row][0:slash_index]
    row += 1'''

for row in range(len(year_list)):
    #print(loc_type_list[row])
    loc_type_list[row] = str(loc_type_list[row])[0].upper() + str(loc_type_list[row])[1:]
    if loc_type_list[row] == 'Nan':
        loc_type_list[row] = 'None/Unknown'
    else:
        if not loc_type_list[row][0].isupper():
            loc_type_list[row] = 'None/Unknown'
        if loc_type_list[row] == 'None':
            loc_type_list[row] = 'None/Unknown'
    if not loc_type_list[row] == 'None/Unknown': #comment out to include 'None/Unknown'
        if [year_list[row],loc_type_list[row]] not in year_loc_pair_list:
            year_loc_pair_list.append([year_list[row],loc_type_list[row]])
            heatmap_data_dict_cleaned['Year'].append(year_list[row])
            heatmap_data_dict_cleaned[y_axis].append(loc_type_list[row])
            for char in kill_list[row]:
                isnum = True
                if not char.isdigit():
                    isnum = False
            if isnum:
                heatmap_data_dict_cleaned['Kills'].append(int(kill_list[row]))
            else:
                heatmap_data_dict_cleaned['Kills'].append(0)
        else:
            index = year_loc_pair_list.index([year_list[row],loc_type_list[row]])
            for char in kill_list[row]:
                isnum = True
                if not char.isdigit():
                    isnum = False
            if isnum:
                heatmap_data_dict_cleaned['Kills'][index] += int(kill_list[row])

heatmap_data_frame = pd.DataFrame(heatmap_data_dict_cleaned)

heatmap_data_frame_pivoted = heatmap_data_frame.pivot("Year", y_axis, "Kills")

ax = sns.heatmap(heatmap_data_frame_pivoted,annot=True,fmt='.1f',linewidths=.5)