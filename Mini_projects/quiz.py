#------------------------- QUIZ GAME ---------------------------------------------

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1 

    for key in questions:
        print ("--------------------------")
        print(key)
        for i in options:
            print(i)
            
#---------------------------------
def check_answer():
    pass
#---------------------------------
def display_score():
    pass
#---------------------------------
def play_again():
    pass
#---------------------------------

questions = {
    "Who created Python?: ":
    "What year was python created?: "
    "Python is tributed to which comedy group?: "
    "Is the eart round?: "
}

options =   [["A. Guido van Rossum", "B. Elon Musk ", "C. Bill Gates", "D. Mark Zuckerberg"],
            ["A. 1989" ,"B. 1991", "c. 2000", "D. 2016"],
            ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
            ["A. True", "B. False", "c. sometimes", "D. What's Eath??"]]

new_game()