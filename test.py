#global variables
scores = [] #high scores list
name = []
difficulties = []

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

teacher_page()
