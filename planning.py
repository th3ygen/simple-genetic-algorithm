import numpy as np
import pandas

# generate random staff planning
def generateRandomStaffPlan(n_days, n_staffs, duration):
    plan = []
    for day in range(n_days):
        day_plan = []
        for id in range(n_staffs):
            day_plan.append([id, np.random.randint(0, 23), duration])
        plan.append(day_plan)
    return plan

def calcCost(staff, staffNeeded):
    err = staff - staffNeeded
    overstaff = abs(err[err > 0].sum())
    understaff = abs(err[err < 0].sum())

    overstaff_cost = 1
    understaff_cost = 1

    cost = overstaff_cost * overstaff + understaff_cost * understaff
    return cost

# generated
""" staff_planning = [
    [[0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8]],
    [[0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8]],
    [[0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8]],
    [[0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8]],
    [[0, 0, 8], [1, 0, 8], [2, 0, 8], [3, 0, 8], [4, 0, 8], [5, 0, 8], [6, 0, 8], [7, 0, 8], [8, 0, 8], [9, 0, 8], [10, 0, 8], [11, 0, 8], [12, 0, 8], [13, 0, 8], [14, 0, 8], [15, 0, 8], [16, 0, 8], [17, 0, 8], [18, 0, 8], [19, 0, 8], [20, 0, 8], [21, 0, 8], [22, 0, 8], [23, 0, 8], [24, 0, 8], [25, 0, 8], [26, 0, 8], [27, 0, 8], [28, 0, 8], [29, 0, 8]]
] """


staff_planning = generateRandomStaffPlan(5, 30, 8)
restaurant_planning = np.array([
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

def isEmpFree(employee, time):
    return (time >= employee[1] and time < employee[1] + employee[2])

def generateHourlyPlanning(staff_planning):
    week = []
    for day in staff_planning:
        cday = []
        for employee in day:
            emps = []
            for time in range(0, 24):
                emps.append(isEmpFree(employee, time))
            cday.append(emps)
        week.append(cday)
    week = np.array(week).sum(axis = 1)
    return week

n_staff_planning = generateHourlyPlanning(staff_planning)

print(staff_planning)

""" print(n_staff_planning)
print(n_staff_planning[0].sum())
print('cost is', calcCost(n_staff_planning, restaurant_planning)) """