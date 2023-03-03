from random import randint
gamecondition = True
while gamecondition:
    randomnumber = randint(1,100)
    rights = 7
    while True:
        if rights>0:
            guess = int(input("Guess the number(1-100): "))
        else:
            print("Couldn't guess the number (: {}".format(randomnumber    ))
            break
        if guess != randomnumber:
            rights -= 1
            if guess > randomnumber:
                print('Number is lower! Your  remaining rights: {}'.format(rights))
            else:
                print('Number is upper! Your  remaining rights: {}'.format(rights))
        else:
            print("Congratulations you found the number")
            break

    control = input("Wanna continue the game ? (Y/N)")
    if control == "H":
        gamecondition = True
    else:
        gamecondition = False


