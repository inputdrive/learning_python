import csv
compromised_users = []
compromised_passwords = []
with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
        compromised_users.append(password_row['Username'])
        compromised_passwords.append(password_row['Password'])
print(compromised_users)
print(compromised_passwords)
import json
with open('compromised_users.txt', 'w') as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user)
with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {
        'recipient': 'The Boss',
        'message': 'Mission Success'
    }
    json.dump(boss_message_dict, boss_message)
with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = '''
     _  _     ___   __  ____
    / )( \   / __) /  \(_  _)
    ) \/ (  ( (_ \(  O ) )(
    \____/   \___/ \__/ (__)
    '''
    new_passwords_obj.write(slash_null_sig)
# Path: passwords.csv
# Username,Password
# jimmy,12345
# lisa,abc123
