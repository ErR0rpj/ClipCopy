#ClipCopy
#Copy multiple text/files to clipboard with just one command.
#Create your custom text to copy it whenever you like with just one word.
#Copy multiple files with ease.
#Till now it is working through command line arguments. TODO: Change it for any PC, include file copy.
#TODO: After completing above todo, delete the command line arg of this program.

TEXTS = {'agree': """Yes, I agree. That sounds fine for me.""",
         'thankyou': """Thankyou for out support and cooperation.""",
         'busy': """Sorry, I am busy right now. I will talk to you later.""",
         'bday': """Happy Birthday!\nMay this year brings you all the happiness you want."""}

OptionsPanel = {'1': "Start Copying",
                '2': "Add/Edit Shortform",
                '3': "Shortform Hub",
                '4': "Help",
                '5': "About/Feedback",
                '6': "Exit"}

import sys,pyperclip

def printDict(dict):
    for key, value in dict.items():
        print(key + ' : ' + value)
    print('')

#Main Function starts here:
if(len(sys.argv) == 1):

    flag = 1

    while(flag):

        printDict(OptionsPanel)
        option = input('Enter your selection: ')

        if(option == '1'):

            keyphrase = []
            while(len(keyphrase) == 0):

                i = input('Enter shortforms with spaces to copy: ')
                keyphrase = list(i.split())

                if(len(keyphrase) == 0):
                    o = input('Please enter 0 to go to menu or enter any character to continue copying: ')

                    if(o == '0'):
                        break

            if(len(keyphrase) > 0):
                ans = ''
                print('')
                for s in keyphrase:
                    if s in TEXTS:
                        ans = ans + '\n' + TEXTS[s]
                        print("Text for " + s + " copied to clipboard.")
                    else:
                        print("There is no text for " + s)

                if (ans == ''):
                    print('\nCopying unsuccessful.')
                else:
                    pyperclip.copy(ans)
                    print('\nCopying successful.')
                print('')

        elif(option == '6' or option.upper() == 'E' or option.upper() == 'EXIT'):
            flag = 0
            print('Exiting....')

        else:
            print('')
            print('Invalid option selected! Please select valid option')
            print('')


elif(len(sys.argv) < 2):
    print('Type this for quick copy:python ClipCopy.py [keyphrase] [keyphrase2] [keyphrase3]')
    print('Note: You can put any number of keyphrases by putting spaces between them.')
    print('If you want to open ClipCopy (not quick copy), just type: python ClipCopy.py')
    sys.exit()

else:
    keyphrase = sys.argv[1:]

    ans = ''
    for s in keyphrase:
        if s in TEXTS:
            ans = ans + '\n' + TEXTS[s]
            print("Text for "+ s + " copied to clipboard.")
        else:
            print("There is no text for " + s)

    if(ans == ''):
        print('\nCopying unsuccessful.')
    else:
        pyperclip.copy(ans)
        print('\nCopying successful.')