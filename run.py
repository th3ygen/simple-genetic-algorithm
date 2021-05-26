import sys
import numpy as np
import planning

""" 
    Question 1
    ``````````
        Total staffs is 30 and works a total of 8 hours
        a) Find best planning
        b) Suggest two generation sizes, find best planning
"""

questionNum = '1'
questionSub = 'a'

hourlyPlanning = np.array([
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 2, 6, 6, 2, 2, 2, 6, 6, 6, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 2, 6, 6, 2, 2, 2, 6, 6, 6, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 2, 6, 6, 2, 2, 2, 6, 6, 6, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 2, 6, 6, 2, 2, 2, 6, 6, 6, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 2, 6, 6, 2, 2, 2, 6, 6, 6, 2, 2, 2, 2]
])
  

if (questionNum == '1'):
    totalStaffs = 30
    totalHours = 8
    totalDays = 5

    if (questionSub == 'a'):
        best_planning = planning.gen_algo(hourlyPlanning, 100, 500, 5, 30, 8)

        print(planning.generateHourlyPlanning(best_planning[0]))

