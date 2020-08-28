#Panel functions are defined here.
import pyperclip

TEXTS = {'agree': """Yes, I agree. That sounds fine for me.""",
         'thankyou': """Thankyou for out support and cooperation.""",
         'busy': """Sorry, I am busy right now. I will talk to you later.""",
         'bday': """Happy Birthday!\nMay this year brings you all the happiness you want."""}

def help():
    print("You can Copy pre-added texts by just writing the shortform.")
    print()

def CopyText(keyphrase):
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

def CopyOption():
    keyphrase = []
    while (len(keyphrase) == 0):

        i = input('Enter shortforms with spaces to copy: ')
        keyphrase = list(i.split())

        if (len(keyphrase) == 0):
            o = input('Please enter 0 to go to menu or enter any character to continue copying: ')

            if (o == '0'):
                break

    if (len(keyphrase) > 0):
        CopyText(keyphrase)