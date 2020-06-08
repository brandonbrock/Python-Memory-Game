import random
from tkinter import *
import tkinter as tk 

#global variables
scores = []
choice = None
name = []
difficulties = []

#overall score
easy_score = 0
medium_score = 0
hard_score = 0
extreme_score = 0

                               #introduction
#--------------------------------------------------------------------------
def start():
    print("               Welcome to Maths Smash                    \n")
    print("Complete the questions the quickest to get a better score\n")
    global name
    
    #this makes sure the user can only enter characters a-z
    username = True 
    while username:
        name = input("What is your name? ")
        if not name.isalpha():#name.isalpha makes the input a-z characters only
            print("Please enter letters only")
            username = True
        else:
            print("Ok,", name, "let's begin!")
            main_menu()

                               #main menu
#--------------------------------------------------------------------------
def main_menu():
    global choice
    while choice !="0":
        print(
        """
        Maths Smash

        0 - Exit
        1 - Easy
        2 - Medium
        3 - Hard
        4 - Extreme
        5 - Teacher Login
        """
        )
        
        choice = input("Choice: ")
        print()

    #exit
        if choice == "0":
            print("Good-bye!")
            quit()
    #easy
        elif choice == "1":
            print("Easy Level")
            easy_level()
    #medium
        elif choice == "2":
            print("Medium Level")
            medium_level()
    #hard
        elif choice == "3":
            print("Hard Level")
            hard_level()
    #extreme
        elif choice == "4":
            print("Extreme Level")
            extreme_level()
    #teacher login
        elif choice == "5":
            print("Teacher Login")
            teacher_login()
    #if the users choice is not 0,1,2,3,4,5
        else:
            print("Sorry but", choice, "isn't a vaild choice.")
                            #teacher login
#--------------------------------------------------------------------------
def teacher_login():
    teacher_login = True
    while teacher_login:
        username = input("Please enter your username: ")
        password = input("Now enter your password: ")

        if username == "John Smith" and password == "teacher123":
            teacher_page()
        else:
            print("\nUsername or Password is incorrect! Please try again.\n")
            teacher_login = True
                            #teacher page
#--------------------------------------------------------------------------
def teacher_page():
    global scores, name, difficulties
    t_choice = None
    while t_choice !="0":
        print("\nWhat would you like to do?")
        print(
        """
        0 - Main Menu
        1 - Add a score
        2 - Remove a score
        3 - View highscores
        """
        )
        
        t_choice = input("Choice: ")
        print()

    #exit
        if t_choice == "0":
            main_menu()
    #add a score
        elif t_choice == "1":
            names = input("Name of the new user to add?\n")
            name.append(names)
            score = input("What did the user score?\n")
            scores.append(score)
            difficulty = input("And which difficulty did they complete it on?\n")
            difficulties.append(difficulty)
    #remove a score
        elif t_choice == "2":      
            names = input("Name of the user you want to remove?\n")
            if names in name:
                name.remove(names)          
            score = int(input("What did they score?\n"))
            if score in scores:
                scores.remove(score)
    #view highscores
        elif t_choice == "3":
            print("High Scores:")
            for score in scores:
                print(name, score, "on the difficulty ", difficulties)
    #if the t_choice does not = to 0,1,2,3
        else:
            print("Sorry but", t_choice, "isn't a vaild choice.")
                               #main
#--------------------------------------------------------------------------
#calling functions
start()

