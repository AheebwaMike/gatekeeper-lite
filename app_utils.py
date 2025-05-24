import string
import json
import random
import re
from datetime import datetime


def verify_user_name(name):
    if len(name) < 2:
        return False, 'User name must be at least two characters'

    special_char_present = len(set(string.punctuation) & set(name) - {'_'})

    if special_char_present:
        return False, 'User name must not contain special characters, except for _'

    with open('database.json', 'r') as f:
        users = json.load(f)

    user_names = [user['name'].lower() for user in users]

    if name.lower() in user_names:
        return False, 'Name Already Taken'

    return True, f'Good to know you, {name}'


def generate_password():
    numbers = list(random.choice(string.digits))
    upper_case = random.choices(string.ascii_uppercase, k=2)
    lower_case = random.choices(string.ascii_lowercase, k=4)
    special_chars = list(random.choice('!@#$%^&*():=?|'))

    password = numbers + upper_case + lower_case + special_chars
    random.shuffle(password)

    return ''.join(password)


def verify_user_password(password):
    # len >= 8, at least 1 digit, at least 1 special char, at least 2 uppercase, at least two lowercase.

    digits = string.digits
    lower_case_letters = string.ascii_lowercase
    upper_case_letters = string.ascii_uppercase
    special_chars = '!@#$%^&*():=?|_'

    accepted_chars = digits + lower_case_letters + upper_case_letters + special_chars

    length_cond = len(password) >= 8, '-> Password must be at least 8 characters'
    digits_cond = len(set(password) & set(digits)), '-> Password should contain al least 1 digit'
    special_char_cond = len(set(password) & set(special_chars)), '-> Password should contain at least 1 special character (!@#$%^&*():=?|)'
    upper_case_cond = len([c for c in password if c in upper_case_letters]) >= 2, '-> Password should contain at least 2 uppercase letters'
    lower_case_cond = len([c for c in password if c in lower_case_letters]) >= 2, '-> Password should contain at least 2 lowercase letters'

    wild_characters = set(password) - set(accepted_chars)
    wild_characters_present = len(wild_characters), f'-> Password should not contain unacceptable character(s): {','.join(list(wild_characters))}'

    if length_cond[0] and digits_cond[0] and special_char_cond[0] and upper_case_cond[0] and lower_case_cond[0] and not wild_characters_present[0]:
        return True, 'Password Set Successfully'

    else:
        tests = [length_cond, digits_cond, special_char_cond, upper_case_cond, lower_case_cond, (not wild_characters_present[0], wild_characters_present[1])]
        fails = [message for test, message in tests if not test]
        fail_message = 'Failed to set Password because:\n\t' + '\n\t'.join(fails)
        return False, fail_message


def verify_dob(dob):
    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    matches = re.match(pattern, dob)

    if matches:
        today = datetime.now().strftime('%d/%m/%Y')
        today, dob = datetime.strptime(today, '%d/%m/%Y'), datetime.strptime(dob, '%d/%m/%Y')
        date_difference = today - dob

        if int(date_difference.days / 365) < 18:
            return False, 'Sorry, Only Adults above 18 are allowed', True

        return True, 'DOB set Successfully!'

    return False, 'Incorrect Format for Date of Birth. Follow Convention: DD/MM/YYYY'
