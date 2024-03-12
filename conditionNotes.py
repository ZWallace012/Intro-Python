def entrancePasscode(passcode)
    actualPassCode ='Womp Womp'
    userCode = input('Please enter user code.')
    
    if userCode == actualPassCode:
        print('Access Granted.')
    else:
        print('Access Denied,')

        entrancePasscode()