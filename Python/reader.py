def readword():
    # Start with a word
    print("Would you like to add a word?")
    print("Enter a word, or the number 1337 to exit")
    word = input()
    if(word == '1337'):
        return
    if(word == ''):
        print("You have entered the empty string")
        print("I will assume that was unintentional")
        print("If you wish to exit, please enter \"1337\"")
    while(word != ''):
        print("did you mean to enter: " + word + "? (y/n)")
        yeah = input()
        if(yeah.lower() == 'n'):
            print("Then please input your word again")
            word = input()
        if(yeah.lower() == 'y'):
            print("Thank you. Moving on to part of speech")
            break
    print("Thank you for entering the word: " + word)
    print()
    # Part of Speech
    print("What is the word's part of speech?") 
    pos = input()
    if(pos == ''):
        print("You have entered the empty string")
        print("I will assume that was unintentional")
        print("If you wish to exit, please enter \"1337\"")
    if(word == '1337'):
        return
    while(pos != ''):
        print("did you mean to enter: " + pos + "? (y/n)")
        yeah = input()
        if(yeah.lower() == 'n'):
            print("Then please input your pos again")
            pos = input()
        if(yeah.lower() == 'y'):
            print("Thank you. Moving on to definition")
            break
    # Meaning
    print("What does " + word + " mean? (y/n)")
    meaning = input()
    if(meaning == ''):
        print("You have entered the empty string")
        print("I will assume that was unintentional")
        print("If you wish to exit, please enter \"1337\"")
    if(meaning == '1337'):
        return
    while(meaning != ''):
        print("did you mean to enter: " + meaning + "? (y/n)")
        yeah = input()
        if(yeah.lower() == 'n'):
            print("Then please input your meaning again")
            meaning = input()
        if(yeah.lower() == 'y'):
            print("Thank you. Moving on to save.")
            break
    # Saving the word
    print("You have entered the following information:")
    print("Word: " + word + ", which is a " + pos + ".")
    print("It means: " + meaning + ".")
    print("Thank you for your time")

readword()
