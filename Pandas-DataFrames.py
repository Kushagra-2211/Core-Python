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
students_df.columns
students_df.describe()  #You can get mean/std/max etc by just using the describe() function
#%% Getting Subject Averages
students_stats = students_df.describe()
subject_mean_1 = students_stats.loc["mean"]
subject_mean_1
#%% Selecting Columns
students_df["Math"]
students_df[["Math","History"]]
#%% Using the .loc (labels)function --> .loc(x,y)
#students_df.loc["Aiden"]                 # full row for Aiden
#students_df.loc["Aiden", "Math"]         # Aiden's Math score → 85
#students_df.loc["Aiden":"Liam"]          # Aiden, Sophia, Liam (inclusive)
#students_df.loc[["Aiden", "Maya"]]       # specific students
#%% Selecting Rows and specfic data points
students_df.loc["Liam"]
students_df.loc[:,"History"]
students_df.loc[["Liam","Maya"],["Math","History"]]
#%% Using the .iloc (index)function --> .iloc(index x,index y)
float(students_df.iloc[0,3])   #English Score for Aiden
students_df.iloc[[2,5],[0,2]]  #Math and History score for Liam and Maya
students_df.iloc[1:4,:]
#%% Basic Statistics
students_df.mean()
students_df.mean(axis=1)
#%% Calculate mean of a column
students_df["Math"].mean()
#%% Get mean of all the subjects (columns)
subjects = ["Math","Science","History","English"]
subject_mean = {subject : float(students_df[subject].mean()) for subject in subjects}
subject_mean    #{'Math': 81.375, 'Science': 83.125, 'History': 81.875, 'English': 83.0}
#%% Get mean of all the students (rows) - Method 1
student_avg = students_df.mean(axis=1).to_dict()
student_avg  #{'Aiden': 88.75,'Sophia': 79.75,'Liam': 92.75,'Isabella': 71.25,'Ethan': 87.5,'Maya': 95.25,'Noah': 61.25,'Olivia': 82.25}
#%% Get mean of all the students (rows) - Method 2 
student_avg_2 = {name : rows.mean() for name, rows in students_df.iterrows()}
student_avg_2
#%% Creating a grades column based on student's average marks
students_avg_df = students_df.mean(axis=1)
students_avg_df
students_df["Average"] = students_avg_df
students_df
def grades(x):
    if x > 90:
        return "A"
    elif 80 < x <= 90:
        return "B"
    elif 70 < x <= 80:
        return "C"
    elif 50 < x <= 70:
        return "D"
    else:
        return "F"
students_df["Grade"] = students_df["Average"].apply(grades)
students_df
#%% Sorting a data frame using sort_values, rem .sorted() is used for list,dic but not df
students_df.sort_values(by = "Average", ascending = False, inplace= True)
students_df
#%% Drop a column
stu_df = students_df.copy()
stu_df.drop(columns = ["Grade"],inplace=True)
stu_df
#%% Rename a column
stu_df.rename(columns = {"Math":"Mathematics"}, inplace= True)
stu_df
#%% Removing all students with less than 80 average
stu_test_1 = students_df[students_df["Average"] > 80]
stu_test_1
#%% Removing all students with grade D
stu_test = students_df[students_df["Grade"] != "D"]
stu_test
#%% Operations on our primary data frame
## These operation are similar to what we performed in our dictionary (see : ListDictionaryFinal.py)
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
##
#%% Add operation on a column
test_df = students_df.copy()
test_df["Math"] += 5
test_df
#%% Getting a row which shows Subject Average
subjects = ["Math", "Science", "History", "English"]
students_df.loc["Subject Average"] = [students_df[subject].mean() for subject in subjects]
students_df
#%% Alternate Method - Best
# student_df.loc["Subject Average"] = student_df.mean()
#%% Getting a column which shows Student Average
students_df["Student Average"] = round(students_df.mean(axis= 1),2)
students_df
#%% Sorting whole df by column = Student Average
students_df.sort_values(by = "Student Average", ascending= False, inplace= True)
students_df
#%% Getting top math student and score
top_math_score = students_df["Math"].max()
top_math_student = students_df["Math"].idxmax()
top_math = {top_math_student : top_math_score}
top_math
#%% Getting top students in every subject - Method 1
top_scorers = {}
subjects = ["Math", "Science", "History", "English"]
for subject in subjects:
    top_subject_score = students_df[subject].max()
    top_subject_student = students_df[subject].idxmax()
    top_score = {top_subject_student : top_subject_score}
    top_scorers[subject] = top_score
top_scorers
#%% Getting top students in every subject - Method 2 - Better
top_scorers = {}
subjects = ["Math", "Science", "History", "English"]
for subject in subjects:
    top_subject_score = students_df[subject].max()
    top_subject_student = students_df[students_df[subject] == top_subject_score].index.to_list()
    top_scorers[subject] = {name : top_subject_score for name in top_subject_student}
top_scorers
#%% Getting top students in every subject - Method 3 - Best
top_scorers = {}
subjects = ["Math", "Science", "History", "English"]
for subject in subjects:
    top_score = students_df[subject].max()
    top_scorers[subject] = {name : score[subject] for name, score in students_df.iterrows() if score[subject] == top_score }
top_scorers


    








 
 
 
 
















