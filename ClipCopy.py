#ClipCopy
#Copy multiple text/files to clipboard with just one command.
#Create your custom text to copy it whenever you like with just one word.
#Copy multiple files with ease.
#Till now it is working through command line arguments. TODO: Change it for any PC, include file copy.
#TODO: After completing above todo, delete the command line arg of this program.

import sys
import PanelFunctions

TEXTS = {'agree': """Yes, I agree. That sounds fine for me.""",
         'thankyou': """Thankyou for out support and cooperation.""",
         'busy': """Sorry, I am busy right now. I will talk to you later.""",
         'bday': """Happy Birthday!\nMay this year brings you all the happiness you want."""}

OptionsPanel = {'1': "Copy",
                '2': "Add/Edit Shortform",
                '3': "Shortform Hub",
                '4': "Help",
                '5': "About/Feedback",
                '6': "Exit"}

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
            PanelFunctions.CopyOption()
            print('')

        elif(option == '3'):
            PanelFunctions.CopyOption()
            print('')

        elif(option == '4'):
            PanelFunctions.help()

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
    PanelFunctions.CopyText(keyphrase)