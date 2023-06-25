# Star Wars Adventure Game
# by Kylor Love

# list containing names of Jedi masters
jedi_masters = ["yoda","obi won kenobi","luke skywalker","luke","obi won","mace windu"]
# list containing names of Sith lords
sith_lords = ["darth vader","emperor palpatine","count douku","darth maul","snoke"]
# input varibale to begin game
answer = input('Do you want to start the game?(yes/no) ').lower().strip()
# if statement for begining of game
if answer == "yes":
    # input variable to choose Jedi or Dark side
    print()
    answer = input('Would you like to become a Jedi or to join the Dark side? ').lower().strip()
    # nested if statements to control path for the Jedi
    if answer == "jedi":
        # display text
        print()
        print('You seem to be quite the promising young padawan. Let us begin our journey.')
        # input variable to hold players Jedi name
        name_jedi = input('What shall we call you young Jedi? ')
        print()
        # display text
        print('That is quite some name young',name_jedi+'.','Who would you')
        # input variable to hold name of chosen Jedi master from list
        name_master = input('like to have as your Jedi Master? ').lower().strip()
        print()
        # if statement to check for name from list of Jedi masters
        if name_master in jedi_masters:
            # display text
            print('Im sure master',name_master,'will be pleased to meet you very soon...')
            print('Press Enter')
            input('')
            print('Hello',name_jedi,'I am Jedi Master',name_master)
            print()
            print('it is nice to have you in this troubling time. Lord Vader and the Empire')
            print('are rapidly discovering and destroying our crucial Rebel outposts.')
            print('Together we will bring an end to these attrocities.')
            print()
            answer = input('Which outpost should we travel to first: Tattooine or Hoth? ').lower().strip()
            if answer == "tattooine":
                print('It has been a long time since I have traveled that system.')
                print('May we get there fast to warn the Rebels of the Empirial fleets formation')
            elif answer == "hoth":
                print()
                answer = input('It will be far too cold, are you sure you want to take the risk?(y/n)')
                print()
                if answer == "y":
                    print('Grab your coat',name_jedi+'.')
                    print()
                    answer = input('do you know how to fly this ship?(y/n) ')
                    if answer == "y":
                        print('Well then activate the warp drive and throw it into light speed!')
                    elif answer == "n":
                        print('well today is your lucky day hop in the pilots seat.')
                        print()
                        answer = input('First key in your destination star system. (press ENTER to continue)')
                        if answer == '':
                            print()
                            print('Now you must engage the thrusters while the warp drive')
                            answer = input('charges and we prepare to make the jump to light speed.(press ENTER)')
                            if answer == '':
                               print()
                               print('The warp drive is fully functional and we are')
                               print('now ready to make the jump to light speed!')
                               input()
                               print('We made it to planet Hoth. Good the Rebels are still here.')
                               input()
                               print('I think we should land in the hanger before the snow storm')
                               print('damages the ship.')
                                     
                            
                                  
                    
                elif answer == "n":
                    print('Tattooine it is!')
                    answer = input('How about we get some coffee?(ok/no) ')
                    print()
                    if answer == "ok":
                        print('I love good space coffee')
                    elif answer == "no":
                        print('Maybe some other time then')
             
        
    # elif statement to control path for the Dark side
    elif answer == "dark side":
        print()
        # input varibale to hold players Sith name
        name_sith = input('Welcome to the dark side what shall your name be? ')
        print()
        # displat text
        print('We can sense a great deal of power within you Lord',name_sith+'.')
        print()
        print('The disloyalty of the Republic and the Rebels must be punished. What')
        print('must we do Lord',name_sith,'to destroy the resistance? ')
        input()
        answer = input('How shall we begin; kill the jedi or build a death star? ')
        print()
        if answer == "kill the jedi":
            print('Good! Execute order 66!')
        elif answer == "build a death star":
            print('We must show the galaxy the power of the dark side')
            print('of the force.')
            input()
            print('Those peskey Jedi menace must pay for their treasonous actions.')
            input()
            print('We will set an example & make a display of our strenght by destroying a planet')
            answer = input('Which planet will we destroy Tattooine or Nabu? ').lower().strip()
            print()
            if answer == "tattooine":
                print('Shall be it Lord',name_sith)
            elif answer == "nabu":
                print('The rebelious government of Nabu will pay for their')
                print('support of those rebels.')
                input()
                print('Charge the main weapon & target the system containing')
                print('the palnet of Nabu!')
                input()
                print('We will begin the countdown on your mark')
                input()
                for numbers in range(10,0,-1):
                    print(numbers)
                    input()
                print('Fire!')
                input()
                print('What a sight of power to behold!')
                print('Where shall we position the Empirial fleet sir to protect the')
                print('Death Star from Rebel retaliation?')
                answer = input('')
                
                
    # else statement to prompt player to enter correct choice
    else:
        print('Choose either Jedi or the Dark side!')
        
        
    
    

# else statement for if player chooses not to play at begining
elif answer == "no":
    print()
    print('Maybe some other time.')
