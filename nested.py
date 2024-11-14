card='inserted'
pin=123
selection='withdraw'
atm_balance=1000

if card:
    if pin:
        print('Access Granted.please select an option.')
        if selection =='withdraw':
            if atm_balance>=1200:
                print('please take your cash')
            else:
                print('insufficient funds')
        elif selection =='deposit':
            print('your deposit have been accepted')
        elif selection =='check balance':
            print(f'your current balance is {atm_balance}.')
        else:
            print('invalid selection .Please try again')
    else:
        print('incorrect pin')
                
    

else:
    print('no card detected.please insert your card')