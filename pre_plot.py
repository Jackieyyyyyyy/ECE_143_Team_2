# Author: James Choi (JC)
# Last Edited: JC, 5/13/19

import numpy as np
import pandas as pd

def xy (fname, x, y):
    """
    y column elements that correspond to the x column elements are summed up
    outputs a new DataFrame
    :param fname: .csv file name
    :param x: x column string, e.g., "Year"
    :param y: y column string, e.g., "Kills"
    :return: DataFrame
    """
    assert isinstance(fname, str) and isinstance(x, str) and isinstance(y, str)
    assert fname[-4:] == '.csv'

    df = pd.read_csv(fname)

    to_drop = []
    for i in range(df.shape[0]):
        if df.loc[df.index[i], x] == 'Missing' or df.loc[df.index[i], y] == 'Missing':
            to_drop.append(i)
    df = df.drop(to_drop)
    df = df.sort_values(x)
    df[y] = df[y].astype(int)

    x_arr = df[x].unique()  # numpy array of all unique values in x
    df_xy = pd.DataFrame({x: x_arr, y: 0})  # new dataset of x

    ind = 0
    for element in x_arr:
        y_sum = df.query("%s=='%s'" % (x, element))[y].sum()
        df_xy.loc[df_xy.index[ind], y] = y_sum
        ind += 1
    return df_xy

df_new = xy('PakistanSuicideAttacks_modified.csv', 'Year', 'Kills')