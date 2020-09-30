import Operating_System_Basics

def main():

    print("----------------------------")
    print("A+ 1002 - Digital Flashcards")
    print("----------------------------")
    print("")
    print("Select Question Set: ")
    print("")
    print("1. Operating System Basics")
    print("")
    print("0. Quit")
    print("")

    user_selection = input()

    if user_selection == "1":
        Operating_System_Basics.ask_questions()
    elif user_selection == "0":
        quit

    

main()