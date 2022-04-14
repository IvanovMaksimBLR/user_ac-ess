from function import ran, ran_pin
from pincode import check_password

data_u = {
    '12345':
        {'name': 'Joe', 'pin': 1111, 'balance': 42}
    ,
    '23456':
        {'name': 'Bill', 'pin': 2222, 'balance': 510}
    ,
    '34567':
        {'name': 'Ann', 'pin': 3333, 'balance': 1200}
    ,
    '45678':
        {'name': 'Smith', 'pin': 4444, 'balance': 100}
    ,
}
# x = input('id')
# a = data_u[x]['balance']
# print(a)


user_id = input('enter your ID')
for code, info in data_u.items():
    if user_id == code:
        check_password()
        break

# new_user_name = str(input('Let\'s create new User. Enter your Name'))
# new_user_id = str(ran())
# new_user_balance = str('0')
# new_user_pin = str(ran_pin())
#
# new_user = {
#     new_user_id:
#         {'name': new_user_name, 'pin': new_user_pin, 'balance': new_user_balance}
# }
# data_u.update(new_user)
# print(data_u)


# new_key_values_dict = {'orange': 2, 'yellow': 3}
# rainbow.update(new_key_values_dict)

# тут должна быть распоковка словаря?
# x = input('id')
# a = data_u['12345']['pin']
# print(a)
#
#
# w = {"1": {"11": 11}, "2": {"22": 22}}
# print(w["1"]["11"])
