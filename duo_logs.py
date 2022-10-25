from asyncio.windows_events import NULL
import csv

# create list of trash users from .csv file
def user_dict(source):
    users = {}
    with open(source, 'r') as f:
        user = f.readlines()
        for line in user:
            users[(line.split(',')[0])] = ''
        return users

# search through auth log and add user:[auth type] to dictionary
def auth_add(source):
    users = user_dict('C:/Users/jbackon/Repos/duo_auth/trash-users-2022-10-20.csv')
    with open(source, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
                if row[1] in user_dict('C:/Users/jbackon/Repos/duo_auth/trash-users-2022-10-20.csv'):
                    users[row[1]] += row[2] + ", " + row[0] + ', '
                    print(users[row[1]])
    
    with open('auth_log.csv', mode = 'w') as auth_file:
        auth_log = csv.writer(auth_file, delimiter = ',')
        for user in users:
            auth_log.writerow(user)
            print(user)
    return NULL

# print out dictionary as .csv file
auth_add('C:/Users/jbackon/Repos/duo_auth/authentication-log-2022-10-25.csv')

# Just need to record the system accessed. No need for a time stamp.