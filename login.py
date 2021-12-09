import time
username = 'peter'
password = 'secretpassword'

username_input = input('username: ')
password_input = input('password: ')

if username_input == username and password_input == password:
    print("access granted")
    print('please wait...')
    time.sleep(3)
    print('loading...')
    time.sleep(1)
    print('you are cleared')
elif username_input == username and password_input != password:
    print('password incorrect')
elif username_input != username and password_input == password:
    print('username incorrect')
else:
    print('you might wanna check both field...')
