#Panel functions are defined here.
import pyperclip,re

TEXTS = {'agree': """Yes, I agree. That sounds fine for me.""",
         'thankyou': """Thankyou for out support and cooperation.""",
         'busy': """Sorry, I am busy right now. I will talk to you later.""",
         'bday': """Happy Birthday!\nMay this year brings you all the happiness you want.""",
         'numbers':"""9979965868 99b24 426543 99245 92563 +91 99256 95864 +919924 962390 9924962390 sad9924962390 ds+919924962390 +91992496239015 kya hua 926456sfd 9409263327fdfd +919924962390 7864453123 pakau5551112224"""}

CopyOptionPanel = {'1':"""Copy Text""",
                   '2':"""Copy Phone numbers""",
                   '3':"""Copy EMail Adresses"""}

def printDict(dict):
    for key, value in dict.items():
        print(key + ' : ' + value)
    print('')

def help():
    print("You can Copy pre-added texts by just writing the shortform.")
    print()


def CopyText(keyphrase):
    ans = ''
    print('')
    for s in keyphrase:
        if s in TEXTS:
            ans = ans + "\n" + TEXTS[s]
            print("Text for " + s + " copied to clipboard.")
        else:
            print("There is no text for " + s)

    if (ans == ''):
        print('\nCopying unsuccessful. Nothing copied')
    else:
        pyperclip.copy(ans)
        print('\nCopying successful.')

def CopyPhoneNumbers(keyphrase):
    ans = ''
    phoneNumRegex = re.compile(r'(\+\d\d)?( )?(\d\d)( )?(\d\d)( )?(\d)( )?(\d\d\d\d\d)')

    for s in keyphrase:
        if s in TEXTS:
            list = phoneNumRegex.findall(TEXTS[s])
            print(list)
            for numbers in list:
                ans = ans + ''.join(numbers)
                ans.strip()
                ans = ans + "\n"

        else:
            print("There is no text for " + s)

    if (ans == ''):
        print('\nCopying unsuccessful. There are no phone numbers in these texts')
    else:
        pyperclip.copy(ans)
        print('\nCopying successful.')


def CopyOption():

    printDict(CopyOptionPanel)
    option = input('Enter your selection: ')

    keyphrase = []
    while (len(keyphrase) == 0):

        i = input('Enter shortforms with spaces to copy: ')
        keyphrase = list(i.split())

        if (len(keyphrase) == 0):
            o = input('Please enter 0 to go to menu or enter shortforms to continue copying: ')

            if (o == '0'):
                break

    if(option == '1' and len(keyphrase) > 0):
        CopyText(keyphrase)

    elif (option == '2' and len(keyphrase) > 0):
        CopyPhoneNumbers(keyphrase)

    else:
        print('Enter valid selection')


