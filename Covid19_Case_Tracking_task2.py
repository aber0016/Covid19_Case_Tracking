'''''

Covid19_Case_Tracking_task2

Author: Armin Berger

First created: 19/05/2020
Last edited: 08/06/2020 

OVERVIEW:
This file is the second task of the program. It reads in a list of people and their social contacts using a txt file
named 'a2_sample_set.txt'. Then it creates all unique Patient objects (which are based on the parent 'Person' class) 
possible based on the names given in the file (200 in this case). After creating this list of Patient objects the
run_simulation() function is called and given the parameters of a) the length of the simulation in days b) the meeting 
probability of individuals in the simulation and c) the health of 'patient zero' (the person that gets infected first)
the infectious disease simulation is carried out. The result of the simulation is saved as a list of integers displaying 
the number of infected individuals per day.

FEATURES:
This file for task 2 contains one class and three functions, of which each is annotate in accordance to their
purpose and role.

1.  class Patient
2.  run_simulation()
3.  remove_unwanted_characters()
4.  load_patients()
 

IMPORTED LIBRARIES: 
- math 
- matplotlib
- random

'''''

import random                       # import random library
from a2_26255367_task1 import *     # import classes and functions from a2_26255367_task1

'''''
The Patient class is one of the main classes of the program and defines the characteristics and methods of a Patient.
The Patient class is a child class of the Parent class Person, thus it inherits all of its characteristics and methods.
The Patient class contains six new methods.

1)  Method '__init__()' is the constructor method of the class which assigns all the needed variables for the
    Patient class to itself. The Patient class inherits all the the attributes of its Parent class, the Person class
    and assigns a new variable to itself, health.
2)  Method 'get_health()' returns the health status for Patient class.
3)  Method 'set_health()' assigns a new (updated) health status for Patient class.
4)  Method 'is_contagious()' returns whether a Patient object is contagious or not.
5)  Method 'infect()' infects a Patient object.
6)  Method 'sleep()' regenerates a Patient objects health by 5 points over night.
'''''
class Patient(Person):
    # constructor method of class Patient
    def __init__(self, first_name, last_name, health):
        # since we inherit the other variables from the Parent Class, Person class, we only need to assign health
        # to Patient as self.health
        super().__init__(first_name, last_name)
        self.health = health

    # method that returns the rounded health of the patient
    def get_health(self):
        return round(self.health)

    # method that sets the health of a patient to new health
    # in case health falls under 0 or over 100, it is readjusted
    def set_health(self, new_health):
        self.health = new_health
        if self.health < 0:
            self.health = 0     # set health to 0
        elif self.health > 100:
            self.health = 100   # set health to 100

    # method that checks whether a patient is contagious or not and returns Boolean
    def is_contagious(self):
        if self.health <= 49:   # if the health of a Patient is <= 49 they are contagious and can spread the virus
            contagious = True
        else:
            contagious = False
        return contagious       # return boolean

    # method that infects patient objects with a viral load and then adjusts their health
    # patients with different health statuses produce different viral loads
    def infect(self, viral_load):
        # if the health of a Patient is <= 29 they produce a lower viral load
        if self.health <= 29:
            self.set_health(self.health - (0.1 * viral_load))   # set health
        # if the health of a Patient is < 50 they produce a 'medium' viral load
        elif 29 < self.health < 50:
            self.set_health(self.health - (1.0 * viral_load))   # set health
        # if the health of a Patient is >= 50 they produced a larger viral load
        elif self.health >= 50:
            self.set_health(self.health - (2.0 * viral_load))   # set health

    # method that adds 5 health points over night due to sleep
    def sleep(self):
        self.set_health(self.health + 5)

'''''
The run_simulation() function takes the parameters a) the length of the simulation in days b) the meeting 
probability of individuals in the simulation and c) the health of 'patient zero' (the person that gets infected first)
and starts the infectious disease simulation using a list of all patients. At the end of simulation the method returns a
list of integers displaying the number of infected individuals per day.
'''''
def run_simulation(days, meeting_probability, patient_zero_health):
    # set every patient's health to 75
    patient_list = load_patients(75)
    # set the health of patient zero to the specified custom input
    patient_list[0].set_health(patient_zero_health)
    daily_counts = []   # list that saves the daily number of patients infected with the virus

    # iterate through the days of the simulation using a for loop
    for d in range(days):

        for p in patient_list:          # iterate through the list of patient objects using a for loop

            for f in p.get_friends():   # iterate through each friend in the friends list of a person

                random.seed(4)          # use .seed() function to maintain a 'consistent randomness'
                random_factor = random.random()     # get a random float between 0 - 1

                # decides whether a person infects a friend or not given a meeting probability and whether they are
                # infectious. The logic behind 'random_factor < meeting_probability' was adapted from stackoverflow.com
                # from user: SilentGhost https://stackoverflow.com/questions/3203099/percentage-chance-to-make-action
                # accessed on 22/05/2019
                if p.is_contagious() and random_factor <= meeting_probability:

                    # if both conditions are met create a viral load
                    viral_load = 5 + (((p.get_health() - 25) ** 2) / 62)
                    f.infect(viral_load)           # infect the friend with the calculated viral load

        # calculates how many patients are contagious
        contagious_counter = 0
        for p in patient_list:      # iterate through the list of patient objects using a for loop

            if p.is_contagious():   # if patient object is contagious  increase counter by 1

                contagious_counter += 1

            p.sleep()               # each patient sleeps at the end of a day and gains 5 health points
        # append counter for each day to the list that saves the daily number of patients infected with the virus
        daily_counts.append(contagious_counter)
    # return the list that saves the daily number of patients infected with the virus
    return daily_counts

'''''
The function remove_unwanted_characters() removes unwanted characters from a string using .replace() and then
strips the 'cleaned' word of any remaining white spaces using .strip().
'''''
def remove_unwanted_characters(word):
    characters_to_remove = [',', '.', ':', ' \n ']  # list of unwanted characters that need to be removed

    for character in characters_to_remove:          # iterate through each item in the characters_to_remove list
        new_word = word.replace(character, '')      # replace the unwanted characters in a word with '' (nothing)
    return new_word.strip()                         # return new 'cleaned' word


'''''
The function load_patients() creates Person objects based on the txt file data. The function serves the same role as
def load_people() but is used for infected patients.
'''''
def load_patients(default_health):

    patient_list = []   # list of patient objects which are created based on txt file data (contains 200 people objects)

    # read txt file input data with a try and catch block
    try:
        file_handle = open('a2_sample_set.txt')     # create file handle that reads in file date
        file_lines = file_handle.readlines()        # read line by line of file handle using readlines() function
    except FileNotFoundError:                       # throw error in case file is not found and no data could be read in
        print('Input File not Found. Exiting ...')
        exit(0)                             # exit program, user should check whether 'a2_sample_set.txt' exists

    # iterates through all file lines and creates Patient objects
    for j in range(0, len(file_lines)):             # iterate through each line of the file

        friends_group = file_lines[j].split(':')    # isolate name by splitting the first item of the list based on ':'
        person_name = friends_group[0].split()      # splitting 'first item' of friends_group based on whitespace
        friends_name = friends_group[1].split(',')  # splitting 'second  item' of friends_group based on ','

        # before creating a Patient object it needs to be checked whether there is a Patient object already existing
        # in the person list with the same name
        # this is done using the any() function and prevents the occurrence of multiple Patient objects
        # with the same name (we only want 200 Patient objects)
        if not any(p.get_name() == ' '.join(person_name) for p in patient_list):
            i = Patient(person_name[0], person_name[1], 75) # create objects using Patient class with 75 standard health
            patient_list.append(i)                          # append new Patient object to Patient list

        else:                                               # use in case Patient object with the name already exists
            i = [x for x in patient_list if x.get_name() == ' '.join(person_name)][0] # use list comprehension to search
            # through the patient list and find the matching person object

        # iterate through all the friend names in one txt line
        for friend in friends_name:

            friend = remove_unwanted_characters(friend)
            # check if friend already exists as a Patient object, if not create a new Patient object and append it
            # to the patient list

            if not any(p.get_name() == friend for p in patient_list):

                # create objects using Patient class, with 75 standard health
                friend_object = Patient(friend.split()[0], friend.split()[1], 75)
                patient_list.append(friend_object)
                i.add_friend(friend_object)

            else:  # use in case Patient object with the name already exists

                friend_object = [x for x in patient_list if x.get_name() == friend][0] # use list comprehension to
                # search through the friends list and find the matching patient object

                i.add_friend(friend_object)  # adds the existing Patient class to the friends list of a Patient

    file_handle.close()     # close txt file using .close()

    return patient_list     # return patient_list

if __name__ == '__main__':

    # This is a sample test case. Write your own testing code here.
    test_result = run_simulation(40, 1, 1)
    print(test_result)

# do not add code here (outside the main block).
