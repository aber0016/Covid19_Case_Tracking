# Covid19_Case_Tracking

This repository contains a case tracking simulation for Covid19 infections, which is split into three tasks. 
The program is an infectious diseases simulation which tracks the spread of a virus over time. Given an txt file, containing a list of people and their social contacts, as an input this program is capable of tracking the spread of a virus given certain parameters. The spread is visualised in a cartesian plane, where the x-axis represents the number of days of the simulation and the y-axis represents the number of infected individuals. This graph is created using the matplotlib library (all imported libraries are listed below).

Task 1 reads in a list of people and their social contacts using a txt file named 'a2_sample_set.txt'. Then it creates all unique Person objects possible based on the names given in the file (200 in this case).

Task 2 uses the created 200 Person objects and based on that creates a list of Patient objects. The run_simulation() function is called and given the parameters of a) the length of the simulation in days 
b) the meeting probability of individuals in the simulation and
c) the health of 'patient zero' (the person that gets infected first) 
the infectious disease simulation is carried out. The result of the simulation is saved as a list of integers displaying the number of infected individuals per day.

Task 3 plots the the daily number of patients infected with the virus. 
