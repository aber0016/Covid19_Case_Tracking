'''''

FIT9136 - Assignment 2 - TASK 3 - Armin Herman Dieter Berger, 26255367

First created: 22/05/2020
Last edited: 08/06/2020 

OVERVIEW:
This file is the third task of the program. It plots the the daily number of patients infected with the virus.
The spread is visualised in a cartesian plane, where the x-axis represents the number of days of the simulation and the
y-axis represents the number of infected individuals. This graph is created using the matplotlib library
(all imported libraries are listed below). 


FEATURES:
This file for task 3 contains one functions: visual_curve()

EXPECTATIONS:
The following expectations are made for the three scenarios.
 
Scenario A)
In this scenario a we have the following parameters:
Number of days: 30 
Meeting probability: 0.6 
Patient zero health: 25 health points 

Since this scenario is a short simulation with a high meeting probability of individuals, you would expect the number
of cases to increase relatively quickly. However, since the patient zero health is in a ‘medium range’, patient zero
only spreads a small viral load which would lead to a decrease in the speed of transmission in the first couple of days.
As the simulation progresses and more and more people get infected that effect would diminish.

Scenario B)
In this scenario a we have the following parameters:
Number of days: 60 
Meeting probability: 0.25 
Patient zero health: 49 health points 

This scenario is a simulation of ‘medium length’ with a low meeting probability of individuals. Since the patient zero
health is high, patient zero spreads a large viral load which would lead to an increase in the speed of transmission in
the first couple of days, despite the low meeting probability. Due to the length of the simulation I would expect
everyone to get infected towards the end.

Scenario C)
In this scenario a we have the following parameters:
Number of days: 90 
Meeting probability: 0.18 
Patient zero health: 40 health points 

In this scenario the patient zero health is in a ‘medium range’ which means patient zero only spreads a small viral
load, thus decreasing in the speed of transmission in the first couple of days. Moreover, since the meeting probability
is very low, the virus would have a hard time spreading and would die out quickly. Since it dies out quickly,
regardless of the length of the simulation, not many people would be infected. 


IMPORTED LIBRARIES: 
- math 
- matplotlib
- random
'''''

import matplotlib.pyplot as plt     # import matplotlib.pyplot to sketch a graph for the case load in a cartesian plane
from a2_26255367_task1 import *     # import classes and functions from a2_26255367_task1
from a2_26255367_task2 import *     # import classes and functions from a2_26255367_task2

'''''
The function visual_curve() plots the the daily number of patients infected with the virus given three parameters 
a) the length of the simulation in days b) the meeting probability of individuals in the simulation and 
c) the health of 'patient zero' (the person that gets infected first).
The spread is visualised in a cartesian plane, where the x-axis represents the number of days of the simulation and the
y-axis represents the number of infected individuals. This graph is created using the matplotlib library.

Epectation: 
'''''
def visual_curve(days, meeting_probability, patient_zero_health):
    daily_counts = []           # list that saves the daily number of patients infected with the virus
    days_simulation = []        # list that saves the length
    daily_counts = run_simulation(days, meeting_probability, patient_zero_health)

    for i in range(0,len(daily_counts)):
        days_simulation.append(i)

    # plot the data x axis = days_simulation, y axis = daily_counts
    plt.plot(days_simulation, daily_counts)
    plt.xlabel('days')                  # label x axis
    plt.ylabel('contagious')            # label y axis
    plt.title('Virus cases over time given: \n'
              f'days: {days} | probability of meeting = {meeting_probability} |'
              f' health of patient zero = {patient_zero_health}')  # label chart
    plt.show()                          # create chart

if __name__ == '__main__':

    days = int(input('Number of days of the simulation > '))
    meeting_probability = float(input('Meeting probability of individuals > '))
    patient_zero_health = int(input('Health score of patient zero > '))
    visual_curve(days, meeting_probability, patient_zero_health)

# do not add code here (outside the main block).
