#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 01:31:31 2026

@author: kush
"""

import numpy as np
import pandas as pd
import statistics
#%% Operations on list
numbers = [10, 20, 30, 40, 50]
nums = numbers.copy()
nums
#%% Modifying the list (add, subs, mul, div) - Method 1
nums = [x + 5 for x in nums]
nums
#%% Modifying the list (add, subs, mul, div) - Method 2
for i in range(len(nums)):
    nums[i] += 5
nums
#%% Modifying the list (add, subs, mul, div) - Method 3
nums = np.array(nums)
nums += 5
nums = nums.tolist()
nums
#%% Perform operations within a new list - Method 1
nums_op_1 = [x+5 for x in nums]
nums_op_1
#%% Perform operations within a new list - Method 2
nums_op_2 = [nums[i] + 5 for i in range(len(nums))]
nums_op_2
#%% Perform operations within a new list - Method 3
nums_op_3 = []
for x in nums:
    nums_op_3.append(x+5)
nums_op_3
#%% Working on a simple dictionary
employees_sales = {
    "John":   [12000, 13500, 12800, 14000],
    "Emma":   [15000, 14200, 15500, 16000],
    "Lucas":  [9800,  10200, 11000, 11500],
    "Sophia": [17000, 16500, 17200, 18000],
    "Daniel": [13000, 12800, 13200, 14000],
    "Mia":    [9000,  9500,  9700,  9900],
    "Oliver": [20000, 19500, 21000, 22000],
    "Lily":   [14500, 14800, 15000, 15200]
}
#%% Excess values for a key
employees_sales["Emma"]
#%% Method - 1 : Creating new dictionary for employee average
employee_avg = {name : statistics.mean(score) for name, score in employees_sales.items()}
employee_avg
#%% Method - 2 : Creating new dictionary for employee average
employees_sales_avg = {name: sum(score)/len(score) for name,score in employees_sales.items()}
employees_sales_avg
#%% Creating new dictionary for employees having avg sales > 14000
employees_sales_good = {name:score for name,score in employees_sales_avg.items() if score>14000}
employees_sales_good
#%% Sorting a dictionary
sales_sorted = sorted(employee_avg.items(), key= lambda x:x[1], reverse= True)
sales_sorted
#%% Operations on our primary simple dictionary
students_1 = {
    "Aiden": [85, 90, 88, 92],
    "Sophia": [78, 82, 80, 79],
    "Liam": [92, 94, 89, 96],
    "Isabella": [70, 75, 68, 72],
    "Ethan": [88, 85, 90, 87],
    "Maya": [95, 93, 97, 96],
    "Noah": [60, 65, 58, 62],
    "Olivia": [83, 81, 85, 80]
}
#%% Getting a new dictionary with student averages
student_avg = {name: statistics.mean(scores) for name, scores in students_1.items()}
print(student_avg)
#%% Getting top 3 average scorers
top_students = sorted(student_avg.items(), key=lambda x: x[1], reverse= True)
for name, scores in top_students[0:3]:
    print(name,"-->",scores)
#%% Forming a students_2 dictionary with subjects- Method 1
subjects = ["Maths","Science","History","English"]
students_2 = {name : {subjects[i] : score[i] for i in range(len(subjects))} for name,score in students_1.items()}
students_2
#%% Forming a students_2 dictionary - Method 2
students_3 = {}
subjects = ["Maths","Science","History","English"]
for name, scores in students_1.items():
    sc = {}
    for i in range(len(subjects)):
        sc[subjects[i]] = scores[i]
    students_3[name] = sc
students_3
#%% Operations on a nested dictionary
# students_2 = {
#     "Aiden": {"Math": 85, "Science": 90, "History": 88, "English": 92},
#     "Sophia": {"Math": 78, "Science": 82, "History": 80, "English": 79},
#     "Liam": {"Math": 92, "Science": 94, "History": 89, "English": 96},
#     "Isabella": {"Math": 70, "Science": 75, "History": 68, "English": 72},
#     "Ethan": {"Math": 88, "Science": 85, "History": 90, "English": 87},
#     "Maya": {"Math": 95, "Science": 93, "History": 97, "English": 96},
#     "Noah": {"Math": 60, "Science": 65, "History": 58, "English": 62},
#     "Olivia": {"Math": 83, "Science": 81, "History": 85, "English": 80}
# }
#%% A test to add 2 to each item in dictionary
import copy
stu = copy.deepcopy(students_2)
for scores in stu.values():
    for subject in scores.keys():
        scores[subject] += 2
stu
#%% subtract 5 from maths score
for scores in stu.values():
    scores["Maths"] -= 5
stu
#%% Excessing an item
students_2["Aiden"]["Maths"]
#%% Calculating Math avg - Method 1
math_avg = statistics.mean([score["Maths"] for score in students_2.values()])
math_avg
#%% Calculating Math avg - Method 2
math_score = 0
count_math = 0
for name, scores in students_2.items():
    math_score = math_score + scores["Maths"]
    count_math = count_math + 1
math_avg = math_score/count_math
print(math_avg)
#%% Getting each subject average - Best
subjects = ["Maths","Science","History","English"]
subject_avg = {subject : statistics.mean([score[subject] for score in students_2.values()]) for subject in subjects}
subject_avg
#%% Getting each student average - Best
student_avg_1 = {name : statistics.mean(score.values()) for name, score in students_2.items()}
student_avg_1
#%% long method 1
subjects = ["Math","Science","History","English"]
subject_avg_1 = {}
for i in range(len(subjects)):
    sc = []
    for name,subject in students_2.items():
       k = [x for x in subject.values()]
       sc.append(k[i])
    subject_avg_1[subjects[i]] = statistics.mean(sc)    
subject_avg_1
#%% long method 2
subjects = ["Math","Science","History","English"]
student_avg_2 = {}
for subject in subjects:  
   sc = []
   for score in students_2.values():
       sc.append(score[subject])
   student_avg_2[subject] = statistics.mean(sc)
student_avg_2
#%% Method 1 - Getting top Math scorer
top_math_student = {}
top_math_score = 0
for name, score in students_2.items():
    if score["Maths"] > top_math_score:
        top_math_score = score["Maths"]
        top_math_name = name
    top_math_student["Maths"] = {top_math_name : top_math_score}
top_math_student
#%% Method 2 - Getting top Math scorer
top_math_score = max(score["Maths"] for score in students_2.values())
top_math_name = [name for name, score in students_2.items() if score["Maths"] == top_math_score]
top_math = {name : top_math_score for name in top_math_name}
top_math
#%% Method 3 - Getting top Math scorer
top_name = max(students_2, key= lambda x : students_2[x]["Maths"])
top_math_student = {top_name : students_2[top_name]["Maths"]}
top_math_student
#%% Method 4 - - Getting top Math scorer
name, score = max(students_2.items(), key= lambda x : x[1]["Maths"])
top_math_student_2 = {name : score["Maths"]}
top_math_student_2
#%% Getting top scorer in every subject
subjects = ["Maths","Science","History","English"]
top_scorers = {}
for subject in subjects:
    top_subject_score = max([score[subject] for score in students_2.values()])
    top_subject_name = [name for name,score in students_2.items() if score[subject] == top_subject_score]
    top_scorers[subject] = {name : top_subject_score for name in top_subject_name}
top_scorers
#%% A Transition to DataFrames - After this you can go to Pandas-DataFrames py
students_df = pd.DataFrame(students_2).T
students_df


    
    

    
    















