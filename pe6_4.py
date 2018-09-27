def new_password(new):
    'Nieuwe wachtwoord'
    if len(new) >= 6 and new!=oldpassword:
        print('Wachtwoord is aangepast')
    else:
        print('Wachtwoord voldoet niet aan de eisen.')


nieuwe=input('Wat is je nieuwe wacthwoord?')
oldpassword='Hella123'

new_password(nieuwe)
