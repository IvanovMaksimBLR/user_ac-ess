from holders import data_u


def check_password():
    x = input('input Your ID again:')
    z = int(input('Enter Your password:'))
    a = data_u[x]['pin']
    b = data_u[x]
    if a == z:
        print('password valid')
        print(b)
    else:
        print('invalid password.Try again')
   # print(a)
