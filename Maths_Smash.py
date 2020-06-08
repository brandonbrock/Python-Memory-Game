#Code created by Brandon Brock
#N0773065

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
    print("Complete all ten questions to get the best score possible!\n")
    start = True
    while start: #asks the user if they are a student or teacher to take them to the correct place
        user_input = input("Are you a Student or a Teacher? ")
        if user_input in ("Student", "student"):
            main()
        elif user_input in ("Teacher", "teacher"):
            teacher_login()
        else:
            print("\nIncorrect entry. Please enter if you are a Student or Teacher.\n")
            start = True
                               #main menu
#--------------------------------------------------------------------------
def main():
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
            print("                              Easy Level                                  ")
            print("--------------------------------------------------------------------------")
            easy_level()
    #medium
        elif choice == "2":
            print("                              Medium Level                                ")
            print("--------------------------------------------------------------------------")
            medium_level()
    #hard
        elif choice == "3":
            print("                                Hard Level                                ")
            print("--------------------------------------------------------------------------")
            hard_level()
    #extreme
        elif choice == "4":
            print("                              Extreme Level                               ")
            print("--------------------------------------------------------------------------")
            extreme_level()
    #teacher login
        elif choice == "5":
            print("Teacher Login")
            teacher_login()
    #if the users choice is not 0,1,2,3,4,5
        else:
            print("Sorry but", choice, "isn't a vaild choice.")
            
                               #easy level 
#--------------------------------------------------------------------------
def easy_level():
    global easy_score, name
    #this makes sure the user can only enter characters a-z
    username = True 
    while username:
        name = input("What is your name? ")
        if not name.isalpha():#name.isalpha makes the input a-z characters only
            print("Please enter letters only")
            username = True
        else:
            print("Ok,", name, "let's begin!\n")
            #easy level
            for i in range(10):
                operator_sign =""
                answer = 0
                num1 = random.randint(1,5)
                num2 = random.randint(1,5)
                operator = random.randint(1,4)
                #choosing the operator randomly
                if operator == 1:
                    operator_sign = " + "
                    answer = num1 + num2
                elif operator == 2:
                    operator_sign = " - "
                    answer = num1 - num2
                elif operator == 3:
                    operator_sign = " * "
                    answer = num1 * num2
                elif operator == 4:
                    operator_sign = " / "
                    num1 = random.randint(1,5) * num2
                    num2 = random.randint(1,5) 
                    answer = num1 // num2
                else:
                    print("That is not a vaild entry!\n")
                #outputting the questions along with working out if it's correct
                question = str(num1) + operator_sign + str(num2) + "\n"
                user_input = int(input(question))
                if user_input == answer:
                    easy_score = easy_score + 1
            #total score
            print("You scored:", str(easy_score), "out of 10")
            print("The Student Dashboard will load in just a second...\n")
            root = Tk()
            root.title("Dashboard")
            root.geometry("300x170")
            app = dashboard(root)
            root.mainloop()
                               #medium level
#--------------------------------------------------------------------------
def medium_level():
    global medium_score, name
    #this makes sure the user can only enter characters a-z
    username = True 
    while username:
        name = input("What is your name? ")
        if not name.isalpha():#name.isalpha makes the input a-z characters only
            print("Please enter letters only")
            username = True
        else:
            print("Ok,", name, "let's begin!\n")
            #easy level
            for i in range(10):#how many questions in the test
                operator_sign =""
                answer = 0
                num1 = random.randint(5,10)#ranges the maths questions
                num2 = random.randint(5,10)
                operator = random.randint(1,4)#randomises the operator
                #choosing the operator randomly
                if operator == 1:
                    operator_sign = " + "
                    answer = num1 + num2
                elif operator == 2:
                    operator_sign = " - "
                    answer = num1 - num2
                elif operator == 3:
                    operator_sign = " * "
                    answer = num1 * num2
                elif operator == 4:
                    operator_sign = " / "
                    num1 = random.randint(5,10) * num2
                    num2 = random.randint(5,10) 
                    answer = num1 // num2
                else:
                    print("That is not a vaild entry!\n")
                #outputting the questions along with working out if it's correct
                question = str(num1) + operator_sign + str(num2) + "\n"
                user_input = int(input(question))
                if user_input == answer:
                    medium_score = medium_score + 1
            #total score
            print("You scored:", str(medium_score), "out of 10")
            print("The Student Dashboard will load in just a second...\n")
            root = Tk()
            root.title("Dashboard")
            root.geometry("300x170")
            app = dashboard(root)
            root.mainloop()
                               #hard level
#-------------------------------------------------------------------------- 
def hard_level():
    global hard_score, name
    #this makes sure the user can only enter characters a-z
    username = True 
    while username:
        name = input("What is your name? ")
        if not name.isalpha():#name.isalpha makes the input a-z characters only
            print("Please enter letters only")
            username = True
        else:
            print("Ok,", name, "let's begin!\n")
            #easy level
            for i in range(10):#how many questions in the test
                operator_sign =""
                answer = 0
                num1 = random.randint(5,15)#ranges the maths questions
                num2 = random.randint(5,15)
                operator = random.randint(1,4)#randomises the operator 
            #choosing the operator randomly
                if operator == 1:
                    operator_sign = " + "
                    answer = num1 + num2
                elif operator == 2:
                    operator_sign = " - "
                    answer = num1 - num2
                elif operator == 3:
                    operator_sign = " * "
                    answer = num1 * num2
                elif operator == 4:
                    operator_sign = " / "
                    num1 = random.randint(5,15) * num2
                    num2 = random.randint(5,15) 
                    answer = num1 // num2
                else:
                    print("That is not a vaild entry!\n")
                #outputting the questions along with working out if it's correct
                question = str(num1) + operator_sign + str(num2) + "\n"
                user_input = int(input(question))
                if user_input == answer:
                    hard_core = hard_score + 1
            #total score
            print("You scored:", str(hard_score), "out of 10")
            print("The Student Dashboard will load in just a second...\n")
            root = Tk()
            root.title("Dashboard")
            root.geometry("300x170")
            app = dashboard(root)
            root.mainloop()
                               #extreme level
#--------------------------------------------------------------------------
def extreme_level():
    global extreme_score, name
    #this makes sure the user can only enter characters a-z
    username = True 
    while username:
        name = input("What is your name? ")
        if not name.isalpha():#name.isalpha makes the input a-z characters only
            print("Please enter letters only")
            username = True
        else:
            print("Ok,", name, "let's begin!\n")
            #extreme level
            for i in range(10):#how many questions in the test
                operator_sign =""
                answer = 0
                num1 = random.randint(5,20)#ranges the maths questions
                num2 = random.randint(5,20)
                operator = random.randint(1,4)#randomises the operator
            #choosing the operator randomly
                if operator == 1:
                    operator_sign = " + "
                    answer = num1 + num2
                elif operator == 2:
                    operator_sign = " - "
                    answer = num1 - num2
                elif operator == 3:
                    operator_sign = " * "
                    answer = num1 * num2
                elif operator == 4:
                    operator_sign = " / "
                    num1 = random.randint(5,20) * num2
                    num2 = random.randint(5,20) 
                    answer = num1 // num2
                else:
                    print("That is not a vaild entry!\n")
                #outputting the questions along with working out if it's correct
                question = str(num1) + operator_sign + str(num2) + "\n"
                user_input = int(input(question))
                if user_input == answer:
                    extreme_score = extreme_score + 1
            #total score
            print("You scored:", str(extreme_score), "out of 10")
            print("The Student Dashboard will load in just a second...\n")
            root = Tk()
            root.title("Dashboard")
            root.geometry("300x170")
            app = dashboard(root)
            root.mainloop()
                            #teacher login
#--------------------------------------------------------------------------
def teacher_login():
    teacher_login = True
    while teacher_login:
        username = input("\nPlease enter your username: ")
        password = input("Now enter your password: ")

        if username == "John" and password == "1234":
            teacher_page()
        else:
            print("\nUsername or Password is incorrect! Please try again.\n")
            teacher_login = True
                            #teacher page
#--------------------------------------------------------------------------
def teacher_page():
    global scores, name, difficulties
    #these initalizes the variables as lists below instead of strings
    scores=[]
    name=[]
    difficulties=[]
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
            start()
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
            else:
                print(names, "isn't in the high scores list.\n")
            score = input("What did they score?\n")
            if score in scores:
                scores.remove(score)
            else:
                print(score, "isn't in the high scores list.\n")
            difficulty = input("And which difficulty did they complete it on?\n")
            if difficulty in difficulties:
                difficulties.remove(difficulty)
            else:
                print(difficulty, "isn't in the high scores list.\n")
    #view highscores
        elif t_choice == "3":
            print("High Scores:")
            for score in scores:
                print(name, scores, difficulties)
    #if the t_choice does not = to 0,1,2,3
        else:
            print("Sorry but", t_choice, "isn't a vaild choice.")
                               #GUI
#--------------------------------------------------------------------------
class dashboard(Frame):
    def __init__(self, master):
        super(dashboard, self).__init__(master)
        self.grid()
        self.main_menu()       
                               #student page
#--------------------------------------------------------------------------
    def main_menu(self):            
        #view highscores button
        bttn1 = Button(self, text = "Highscores",
                       command=self.view_scores, height = 2, width= 15)
        bttn1.grid()

        #print score button
        bttn2 = Button(self, text = "Save Score",
                       command=self.save_score, height = 2, width= 15)
        bttn2.grid()

        #exit button
        bttn3 = Button(self, text = "Exit",
               command=quit, height = 2, width= 15)
        bttn3.grid()        
                                #saving the score
#--------------------------------------------------------------------------       
    def save_score(self):
        global name, easy_score, medium_score, hard_score, extreme_score
        if choice == "1":
            filename = "Maths Test Score - Easy.txt" #filename of the .txt
            FILE = open(filename, "w") #creates file to local directory 'w' means if the file doesn't exist it will write one
            FILE.writelines('You scored:'+str(easy_score)) #this is what will be written into the .txt file
            print("\nScore saved to local directory.")
            FILE.close()
        elif choice == "2":
            filename = "Maths Test Score - Medium.txt"
            FILE = open(filename, "w")
            FILE.writelines('You scored:'+str(medium_score))
            print("\nScore saved to local directory.")
            FILE.close()
        elif choice == "3":
            filename = "Maths Test Score - Hard.txt"
            FILE = open(filename, "w")
            FILE.writelines('You scored:'+str(hard_score))
            print("\nScore saved to local directory.")
            FILE.close()
        elif choice == "4":
            filename = "Maths Test Score - Extreme.txt"
            FILE = open(filename, "w")
            FILE.writelines('You scored:'+str(extreme_score))
            print("\nScore saved to local directory.")
            FILE.close()
                               #viewing scores
#--------------------------------------------------------------------------
    def view_scores(self):
        global choice, name, easy_score, medium_score, hard_score, extreme_score
        print("High Scores:")
        if choice == "1":
            print(name, easy_score, "on difficulty Easy") #depending on what the user's choice was at the start of the program, 
        elif choice == "2":                                 #this will print their score out on the choice 
            print(name, medium_score, "on difficulty Medium")
        elif choice == "3":
            print(name, hard_score, "on difficulty Hard")
        elif choice == "4":
            print(name, extreme_score, "on difficulty Extreme")

                               #main
#--------------------------------------------------------------------------
#calling functions
start()

