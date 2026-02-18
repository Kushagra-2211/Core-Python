#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 02:19:40 2026

@author: kush
"""

import pandas as pd
import numpy as np
import statistics
#%%
#%% General function on our primary dataframe
##
##
##
students = {
    "Aiden": {"Math": 85, "Science": 90, "History": 88, "English": 92},
    "Sophia": {"Math": 78, "Science": 82, "History": 80, "English": 79},
    "Liam": {"Math": 92, "Science": 94, "History": 89, "English": 96},
    "Isabella": {"Math": 70, "Science": 75, "History": 68, "English": 72},
    "Ethan": {"Math": 88, "Science": 85, "History": 90, "English": 87},
    "Maya": {"Math": 95, "Science": 93, "History": 97, "English": 96},
    "Noah": {"Math": 60, "Science": 65, "History": 58, "English": 62},
    "Olivia": {"Math": 83, "Science": 81, "History": 85, "English": 80}
}
students_df = pd.DataFrame(students).T
students_df
#%%