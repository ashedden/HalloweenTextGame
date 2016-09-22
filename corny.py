#Allison Shedden, 9/14/16
print "\nAs Halloween has gotten closer, you decide to enter a haunted corn maze...\nIt's dusk.\n"
print "\nAre YOU ready?\n"

ready = raw_input("Press enter to begin.\n")

guesses = 0
mguessprev = ""
left = False
leftn = False
right = False
rightn = False

def spookyMan():
        print "    vvvvv "
        print "   { O o }"
        print "   _\ ^ /_ "
        print "  / /| |\ \ "
        print r" ///\| |/\\\ "
        print "     | |"
        print "    /   \ "
        print "  _|     |_\n"
        pass

def spookyBat():
        print " ____  /\_/\ ____    "
        print "/_____(' . ')____\ "
        print " Vvvvv  ^^   vvvvV\n"
        pass


for i in range(0,20):
        print "You are faced with a decision."
        print "Will you go left or right?\n"
        mguess = raw_input("> ")
        guesses = guesses + 1

        #User quits
        if mguess == "quit":
                break


        #Guess 1
        if guesses == 1:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nYou see a bunch of corn.\n"
                        left = True
                if mguess == "right":
                        print "\nSounds like someone joined you in the corn maze.\nYou hear footsteps.\n"
                        right = True

        #Guess 2
        if guesses == 2 and left == True:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nSounds like someone joined you in the corn maze.\nYou hear footsteps.\n"
                        leftn = True
                if mguess == "right":
                        print "\nYou see a bunch of corn.\n"
                        rightn = True
        if guesses == 2 and right == True:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nThe footsteps sound really close and then they stop.\nYou feel breathing on your neck.\n"
                        print "You turn around, and he is staring right back at you.\nYou die.\n"
                        spookyMan()
                        break
                if mguess == "right":
                        print "\nYou see a bunch of corn.\n"
                        rightn = True

        #Guess 3
        if guesses == 3 and leftn == True:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nYou see a bunch of corn.\n"
                        left = True
                if mguess == "right":
                        print "\nThe footsteps sound really close and then they stop.\nYou feel breathing on your neck.\n"
                        print "You turn around, and he is staring right back at you.\nYou die.\n"
                        spookyMan()
                        break
        if guesses == 3 and rightn == True:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nYou hear footsteps.\n"
                        left = True
                if mguess == "right":
                        print "\nYou see a note written in red ink that says 'Turn Left'.\n"
                        right = True
                                
        #Guess 4
        if guesses == 4 and left == True:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nYou see a bunch of corn.\n"
                        leftn = True
                if mguess == "right":
                        print "\nThe footsteps sound really close and then they stop.\nYou feel breathing on your neck.\n"
                        print "You turn around, and he is staring right back at you.\nYou die.\n"
                        spookyMan()
                        break
        if guesses == 4 and right == True:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nYou see a bunch of corn.\n"
                        leftn = True
                if mguess == "right":
                        print "\nYou hear slow footsteps.\n"
                        rightn = True

        #Guess 5
        if guesses == 5 and leftn == True:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nYou hear slow footsteps.\n"
                        left = True
                if mguess == "right":
                        print "\nYou hear footsteps behind you.\n"
                        right = True
        if guesses == 5 and rightn == True:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nThe footsteps sound really close and then they stop.\nYou feel breathing on your neck.\n"
                        print "You turn around, and he is staring right back at you.\nYou die.\n"
                        spookyMan()
                        break
                if mguess == "right":
                        print "\nYou see a bunch of corn.\n"
                        right = True

        #Guess 6
        if guesses == 6 and left == True:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nYou see a bunch of corn.\n"
                        leftn = True
                if mguess == "right":
                        print "\nThe footsteps sound really close and then they stop.\nYou feel breathing on your neck.\n"
                        print "You turn around, and he is staring right back at you.\nYou die.\n"
                        spookyMan()
                        break
        if guesses == 6 and right == True:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nThe footsteps sound like they are speeding up...\n"
                        leftn = True
                if mguess == "right":
                        print "\nYou hear footsteps.\n"
                        rightn = True
                                
        #Guess 7
        if guesses == 7 and leftn == True:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nOkay seriously, someone is running behind you!\n"
                        left = True
                if mguess == "right":
                        print "\nYou hear LOUD footsteps.\n"
                        right = True
        if guesses == 7 and rightn == True:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nThe footsteps sound really close and then they stop.\nYou feel breathing on your neck.\n"
                        print "You turn around, and he is staring right back at you.\nYou die.\n"
                        spookyMan()
                        break
                if mguess == "right":
                        print "\nYou see a bunch of corn.\n"
                        right = True

        #Guess 8
        if guesses == 8 and left == True:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nThe footsteps sound really close and then they stop.\nYou feel breathing on your neck.\n"
                        print "You turn around, and he is staring right back at you.\nYou die.\n"
                        spookyMan()
                        break
                if mguess == "right":
                        print "\nYou see the end.\nYou survived, and you'll NEVER turn back.\n"
                        spookyBat()
                        break
        if guesses == 8 and right == True:
                right = False
                left = False
                rightn = False
                leftn = False
                if mguess == "left":
                        print "\nThe footsteps sound really close and then they stop.\nYou feel breathing on your neck.\n"
                        print "You turn around, and he is staring right back at you.\nYou die.\n"
                        spookyMan()
                        break
                if mguess == "right":
                        print "\nThe footsteps sound really close and then they stop.\nYou feel breathing on your neck.\n"
                        print "You turn around, and he is staring right back at you.\nYou die.\n"
                        spookyMan()
                        break

        #User mistypes
        if mguess != "left" and mguess != "right" and mguess != "quit":
                print "\nPlease type left, right, or quit\n"
                guesses = guesses -1
                if mguessprev == "left":
                        left = True
                        leftn = True
                else:
                        right = True
                        rightn = True

##        Set previous guess
        mguessprev = mguess




