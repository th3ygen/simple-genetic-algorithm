import numpy as np
import pandas as pd

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

# Genetics 1 - Create generation
def create_parent_gen(n_parents, n_days, n_staffs, duration):
    parents = []
    for x in range(n_parents):
        parent = generateRandomStaffPlan(n_days, n_staffs, duration)
        parents.append(parent)
    return parents

# Genetics 2 - Cross over / Combination
def random_combine(parents, n_offspring):
    n_parents = len(parents)
    n_periods = len(parents[0])
    n_employees = len(parents[0][0])

    offspring = []
    for x in range(n_offspring):
        random_dad = parents[np.random.randint(low = 0, high = n_parents - 1)]
        random_mom = parents[np.random.randint(low = 0, high = n_parents - 1)]

        dad_mask = np.random.randint(0, 2, size = np.array(random_dad).shape)
        mom_mask = np.logical_not(dad_mask)

        child = np.add(np.multiply(random_dad, dad_mask), np.multiply(random_mom, mom_mask))

        offspring.append(child)
    return offspring

# Genetics 3 - Mutation
def mutate_parent(parent, n_mutations, duration):
    s1 = parent.shape[0]
    s2 = parent.shape[1]

    for x in range(n_mutations):
        rnd1 = np.random.randint(0, s1)
        rnd2 = np.random.randint(0, s2)
        rnd3 = np.random.randint(1, 2)

        parent[rnd1, rnd2, rnd3] = np.random.randint(0, duration)
    return parent

def mutate_gen(parent_gen, n_mutations, duration):
    mutated = []
    for parent in parent_gen:
        mutated.append(mutate_parent(parent, n_mutations, duration = duration))
    return mutated

# Genetics 4 - Selection - Feasibility
def is_acceptable(parent, duration):
    return np.logical_not((np.array(parent)[:,:,2:] > duration).any())

def select_acceptable(parent_gen, duration):
    gen = [parent for parent in parent_gen if is_acceptable(parent, duration)]
    return gen

# Genetics 5 - Selection - Cost (inverse fitness)
def select_best(parent_gen, hourly_staff_needed, n_best, i):
    costs = []
    for idx, parent_staff_planning in enumerate(parent_gen):
        parent_hourly_planning = generateHourlyPlanning(parent_staff_planning)
        parent_cost = calcCost(parent_hourly_planning, hourly_staff_needed)
        costs.append([idx, parent_cost])
    print('{}: best gen is: {}, worst is: {}'.format(i, pd.DataFrame(costs)[1].min(), pd.DataFrame(costs)[1].max()))

    costs_tmp = pd.DataFrame(costs).sort_values(by = 1, ascending = True).reset_index(drop = True)
    selected_parents_idx = list(costs_tmp.iloc[:n_best, 0])
    selected_parents = [parent for idx, parent in enumerate(parent_gen) if idx in selected_parents_idx]

    return selected_parents

# Overall
def gen_algo(hourly_staff_needed, n_iterations, n_gen, n_days, n_staffs, duration):
    parent_gen = create_parent_gen(n_parents = n_gen, n_days = n_days, n_staffs = n_staffs, duration = duration)

    for it in range(n_iterations):
        parent_gen = select_acceptable(parent_gen, duration)
        parent_gen = select_best(parent_gen, hourly_staff_needed, n_best = 100, i = it)
        parent_gen = random_combine(parent_gen, n_offspring = n_gen)
        parent_gen = mutate_gen(parent_gen, n_mutations = 1, duration = duration)
    
    best_child = select_best(parent_gen, hourly_staff_needed, n_best = 1, i = 0)

    return best_child

