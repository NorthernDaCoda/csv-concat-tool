#!/usr/bin/env python
# -*- coding: utf-8 -*-

# combine all csv files with the same column structure to one big file

import os
import glob
import pandas as pd

# change to the current working directory

os.chdir(os.path.dirname(os.path.abspath(__file__)))

extension = "csv"
all_filenames = [i for i in glob.glob("*.{}".format(extension))]

# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, sep='\t', header=None) for f in all_filenames ])

# export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding="utf-8-sig")
