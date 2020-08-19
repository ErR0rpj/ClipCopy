#ClipCopy
#Copy multiple text/files to clipboard with just one command.
#Create your custom text to copy it whenever you like with just one word. TODO: This
#Copy any file with ease.
#Till now it is working through command line arguments. TODO: Change it for any PC, include file copy.
#TODO: After completing above todo, delete the command line arg of this program.

TEXTS = {'agree':"""Yes, I agree. That sounds fine for me.""",
         'thankyou':"""Thankyou for out support and cooperation.""",
         'busy':"""Sorry, I am busy right now. I will talk to you later.""",
         'bday':"""Happy Birthday!\nMay this year brings you all the happiness you want."""}

import sys,pyperclip

if(len(sys.argv) < 2):
    print('Type this:python ClipCopy.py [keyphrase] [keyphrase2] [keyphrase3]')
    print('Note: You can put any number of keyphrases by putting spaces between them.')
    sys.exit()

keyphrase = sys.argv[1:];

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