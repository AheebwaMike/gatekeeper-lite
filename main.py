import configparser
import json
import sys
from json import JSONDecodeError
import hashlib

from app_utils import verify_user_name, generate_password, verify_user_password, verify_dob

user_name = None
user_password = None
user_dob = None

app_configs = configparser.ConfigParser()
app_configs.read('settings.ini')

app_version = app_configs.get('app', 'version')
app_mode = app_configs.get('app', 'mode')

print(f'\t\t###===== Thanks For Joining TestApp Version {app_version}, Can we get to know your Name? =====###')
print(f'\t\t###===== Mode: {app_mode} mode =====###')

# Get and verify - user_name
while True:
    user_name = input('Please Enter Your Name:\t>> ')

    user_name_verified, name_verification_message = verify_user_name(name=user_name)

    if user_name_verified:
        if not app_configs.has_section('user'):
            app_configs.add_section('user')
        app_configs['user']['name'] = user_name

        print(name_verification_message)
        print()
        break

    else:
        print(name_verification_message)
        print('Please Try Again')
        print()

# Get and verify password
print(f'A few more steps, {user_name}...')
print('Set yourself a password, Keep your account safe!')

while True:
    auto_password_choice = input('Would You like an automatic Password (Y) or choose your self one (N)??: >>').lower()
    print()

    if auto_password_choice not in ['y', 'n']:
        print('Incorrect Choice...')
        continue

    if auto_password_choice == 'y':
        user_password = generate_password()
        print(f'Your Generated Password is {user_password}')
        print(f'You\'re almost there, {user_name}')
        print()
        break

    else:
        user_password = input('Choose A Strong Password\n'
                              'Password Should Contain 1 or more digits\n, 1 or more special Characters (!@#$%^&*():=?|)\n, '
                              '2 or more Uppercase Letters\n, 2 or more lowercase letters and a minimum of 8 Characters: >> ')
        print()
        password_verified, password_verification_message = verify_user_password(user_password)

        if not password_verified:
            print(password_verification_message)
            print('Try Again')
            print()
            continue

        else:
            print(password_verification_message)
            print(f'You\'re Almost there, {user_name}!')
            print()


# get and verify DOB
while True:
    user_dob = input('Enter your Date of Birth in this format (strictly): DD/MM/YYYY\t eg. 03/09/2005\nEnter DOB Here >> ')
    print()
    user_dob_verified, dob_verification_message, *minor = verify_dob(user_dob)

    if not user_dob_verified:
        print(dob_verification_message)

        if minor:
            sys.exit()

        print('Try Again')
        continue

    else:
        print(dob_verification_message)
        print(f'We\'re Almost Done, {user_name}')
        print()

        break


# inquire subscription
if not app_configs.has_section('payments'):
    app_configs.add_section('payments')

while True:
    user_subscription = input('Would you like to subscribe to our Premium App Version (Y/N): \t>> ').lower()
    print()

    if user_subscription not in 'yn':
        print('Invalid Choice')
        print()
        continue

    if user_subscription == 'n':
        app_configs['user']['has_premium_privileges'] = 'no'
        app_configs['payments']['is_subscribed'] = 'no'
        print('Redirecting You To our Basic App Plan.\n'
              f'You\'ve Successfully Accessed our Basic App service, {user_name}\nEnjoy!')
        break

    else:
        app_configs['user']['has_premium_privileges'] = 'yes'
        app_configs['payments']['is_subscribed'] = 'yes'

        print('You are going Premium, a place of Added Features!')
        payment_option = input('Choose a payment option: Credit Card (0) or PayPal (1)')

        if payment_option not in '01':
            print('Invalid payment option. Should be 0 (credit card) or 1 (paypal)')
            print()
            continue

        if payment_option == '0':
            app_configs['payments']['payment_option'] = 'Credit Card'
            print('Payments Will Be Made Via Credit Card.')
            print()

        else:
            app_configs['payments']['payment_option'] = 'PayPal'
            print('Payments Will Be Made Via PayPal.')
            print()

        print('Redirecting you to our premium App Plan.\n'
              f'You\'ve Successfully Accessed our Premium App Service, {user_name}\nEnjoy!')

        break


# add changes to App Configs (settings)
with open('settings.ini', 'w') as f:
    app_configs.write(f)

# add user to database
hashed_user_password = hashlib.sha256(user_password.encode()).hexdigest()
user_details = {
    'name': user_name,
    'password': hashed_user_password,
    'DOB': user_dob
}

try:
    with open('database.json', 'r') as f:
        users = json.load(f)

    users.append(user_details)

    with open('database.json', 'w') as f:
        json.dump(users, f, indent=2)

except FileNotFoundError:
    print('Database File Not Found.')

except JSONDecodeError:
    users = []
    print('Incorrect Database JSON file Format!')

user_subscription = 'Subscribed' if user_subscription == 'y' else 'Not Subscribed'
print(f"\n✅ Summary:\nName: {user_name}\nDOB: {user_dob}\nSubscription: {user_subscription}")
