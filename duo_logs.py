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
                if row[1] in users:
                    if row[2] in users[row[1]]:
                        pass
                    else:
                        users[row[1]] += row[2] + ', '
                
    
    with open('auth_log.txt', 'w') as auth_file:
        auth_file.write('username, systems accessed \n')
        for i, d in users.items():
            if users[i] != '':
                auth_file.write(str(i) + ', ' + str(d)[:-2] + '\n')
            else:
                pass
    return NULL

# print out dictionary as .csv file
auth_add('C:/Users/jbackon/Repos/duo_auth/authentication-log-2022-10-25.csv')

# Just need to record the system accessed. No need for a time stamp.