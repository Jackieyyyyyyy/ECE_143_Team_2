#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:28:23 2019

@author: jerrychen
"""

import pandas as pd
import seaborn as sns

pakistan_data = pd.read_csv('/Users/jerrychen/Downloads/PakistanSuicideAttacks_modified.csv')
pakistan_data_dict = dict(pakistan_data)

y_axis = 'LocationType'

heatmap_data_dict = {}
heatmap_data_dict['Year'] = pakistan_data_dict['Year']
heatmap_data_dict[y_axis] = pakistan_data_dict[y_axis]
heatmap_data_dict['Kills'] = pakistan_data_dict['Kills']

heatmap_data_dict_cleaned = {'Year':[],y_axis:[],'Kills':[]}

year_list = list(heatmap_data_dict['Year'])
loc_type_list = list(heatmap_data_dict[y_axis])
kill_list = list(heatmap_data_dict['Kills'])    

year_loc_pair_list = []

for row in range(len(year_list)):
    for char in kill_list[row]:
        isnum = True
        if not char.isdigit():
            isnum = False
    if [year_list[row],loc_type_list[row]] not in year_loc_pair_list:
        year_loc_pair_list.append([year_list[row],loc_type_list[row]])
        heatmap_data_dict_cleaned['Year'].append(year_list[row])
        heatmap_data_dict_cleaned[y_axis].append(loc_type_list[row])
        if isnum:
            heatmap_data_dict_cleaned['Kills'].append(int(kill_list[row]))
        else:
            heatmap_data_dict_cleaned['Kills'].append(0)
    else:
        index = year_loc_pair_list.index([year_list[row],loc_type_list[row]])
        if isnum:
            heatmap_data_dict_cleaned['Kills'][index] += int(kill_list[row])
    
heatmap_data_frame = pd.DataFrame(heatmap_data_dict_cleaned)

heatmap_data_frame_pivoted = heatmap_data_frame.pivot("Year", y_axis, "Kills")

ax = sns.heatmap(heatmap_data_frame_pivoted,annot=True,fmt='.1f',linewidths=.5)