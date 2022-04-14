# импорт функции для создания нового клинта и пароль
# как создать и записать пароль в словарь
# через оператор if проверять наличие клиента. если клиент есть, то запросить пароль.
# если пароль верен, то вывести данные

from function import ran
from function import ran_pin
from holders import data_u
from pincode import check_password

user_id = input('enter your ID')
for code, info in data_u.items():
    if user_id == code:
        check_password()
        break
    elif user_id != code:
        new_user_name = str(input('Let\'s create new User. Enter your Name:'))
        new_user_id = str(ran())
        new_user_balance = str('0')
        new_user_pin = str(ran_pin())

        new_user = {
            new_user_id:
                {'name': new_user_name, 'pin': new_user_pin, 'balance': new_user_balance}
        }
    data_u.update(new_user)
    print(data_u)
