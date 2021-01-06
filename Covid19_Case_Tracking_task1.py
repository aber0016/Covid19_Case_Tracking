'''''

FIT9136 - Assignment 2 - TASK 1 - Armin Herman Dieter Berger, 26255367

First created: 16/05/2020
Last edited: 08/06/2020 

OVERVIEW:
This program is an infectious diseases simulation which tracks the spread of a virus over time.
Given an txt file, containing a list of people and their social contacts, as an input this program is capable of 
tracking the spread of a virus given certain parameters such as a) the length of the simulation in days b) the meeting 
probability of individuals in the simulation and c) the health of 'patient zero' (the person that gets infected first).
The spread is visualised in a cartesian plane, where the x-axis represents the number of days of the simulation and the
y-axis represents the number of infected individuals. This graph is created using the matplotlib library
(all imported libraries are listed below). 

This file is the first task of the program. It reads in a list of people and their social contacts using a txt file
named 'a2_sample_set.txt'. Then it creates all unique Person objects possible based on the names given in the file 
(200 in this case).


FEATURES:
This file for task 1 contains one class and two functions, of which each is annotate in accordance to their
purpose and role.

1.  class Person
2.  remove_unwanted_characters()
3.  load_people()

SPECIFICATIONS:
The following set of assumptions were made in accordance with the feedback of tutors,the assignment brief and were
required to guide the development of this program.
- Since we were free to decide the meeting order, I decided to create a Person object when iterating through a persons 
friends list. Later it is checked whether a person has already bin created to avoid the duplication of people. I believe
that this choice would make the dynamic of the virus spread more realistic since it mimics the natural infection
process that we observe in reality.


IMPORTED LIBRARIES: 
- math 
- matplotlib
- random

'''''

'''''
The Person class is one of the main classes of the program and defines the characteristics and methods of a Person.
It contains four methods.

1)  Method '__init__()' is the constructor method of the class which assigns all the needed variables for the
    Person class to itself. The Person class has three attributes: first_name, last_name, and friend_list.
2)  Method 'add_friend()' appends the friends of a person to their friends list. Each appended friend is a person object.
3)  Method ' get_name()' combines fist and last name and return the name of a Person object.
4)  Method 'get_friends' returns the friends list of a person.
'''''
class Person:
    # constructor method of class Person
    def __init__(self, first_name, last_name):
        self.first_name = first_name            # assign f_name to Person as self.first_name
        self.last_name = last_name             # assign l_name to Person as self.last_name
        self.friend_list = []               # create an empty list called friend_list and assign it to the Person class

    # method that appends the friends of a person to their friends list
    def add_friend(self, friend_person):        # friend_person is an object of Person type
        self.friend_list.append(friend_person)  # append each new friend object to self.friend_list

    # method that returns the full name of a Person object
    def get_name(self):
        name = self.first_name + ' ' + self.last_name   # save fist and last name as a string called 'name'
        return name                                     # return the name of Person

    #  method that returns the friends of a Person object
    def get_friends(self):
        return self.friend_list                         # returns the friends list of a person

'''''
The function remove_unwanted_characters() removes unwanted characters from a string using .replace() and then
strips the 'cleaned' word of any remaining white spaces using .strip().
'''''
def remove_unwanted_characters(word):
    characters_to_remove = [',','.',':',' \n ']     # list of unwanted characters that need to be removed

    for character in characters_to_remove:          # iterate through each item in the characters_to_remove list
        new_word = word.replace(character,'')       # replace the unwanted characters in a word with '' (nothing)
    return new_word.strip()                         # return new 'cleaned' word

'''''
The function load_people() creates Person objects based on the txt file data. 
'''''
def load_people():
    person_list = []    # list of people objects which are created based on txt file data (contains 200 people objects)

    # read txt file input data with a try and catch block
    try:
        file_handle = open('a2_sample_set.txt')     # create file handle that reads in txt file data
        file_lines = file_handle.readlines()        # read line by line of file handle using readlines() function
    except FileNotFoundError:                       # throw error in case file is not found and no data could be read in
        print('Input File not Found. Exiting ...')
        exit(0)                                     # exit program, user should check whether 'a2_sample_set.txt' exists

    # iterate through all file lines and create Person objects for each line
    for j in range(0, len(file_lines)):             # iterate through each line of the file

        friends_group = file_lines[j].split(':')    # isolate name by splitting the first item of the list based on ':'
        person_name = friends_group[0].split()      # splitting 'first item' of friends_group based on whitespace
        friends_name = friends_group[1].split(',')  # splitting 'second  item' of friends_group based on ','

        # before creating a person object it needs to be checked whether there is a Person object already existing
        # in the person list with the same name
        # this is done using the any() function and prevents the occurrence of multiple Person objects
        # with the same name (we only want 200 person objects)
        if not any(p.get_name() == ' '.join(person_name) for p in person_list):
            # if person is not in person list create new person object using Person class
            i = Person(person_name[0], person_name[1])
            person_list.append(i)           # append new Person object to person list

        else:                               # in case Person object with the name already exists
            i = [x for x in person_list if x.get_name() == ' '.join(person_name)][0] # use list comprehension to search
            # through the person list and find the matching person object

        # iterate through all the 'friend names' in the file line belonging to a certain person
        for friend in friends_name:
            friend = remove_unwanted_characters(friend)     # remove unwanted characters from the name of a friend

            # check if friend already exists as a Patient object, if not create a new Patient object and append it
            # to the patient list
            if not any(p.get_name() == friend for p in person_list):
                friend_object = Person(friend.split()[0], friend.split()[1])    # create object using Person class
                person_list.append(friend_object)                               # append Person object
                i.add_friend(friend_object)

            else:                               # use in case Person object with the name already exists
                friend_object = [x for x in person_list if x.get_name() == friend][0]   # use list comprehension to
                # search through the friends list and find the matching person object
                i.add_friend(friend_object)     # adds the existing Person class to the friends list of a person

    file_handle.close()                         # close txt file using .close()
    return person_list                          # return person_list containing only unique Person objects

# main block to check if the code is working the way you expect
if __name__ == '__main__':
    pass                    # pass in case there is no code

# do not add code here (outside the main block).
