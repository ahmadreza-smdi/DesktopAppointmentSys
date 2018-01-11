import psycopg2
import os
import config

# cls function

def cls():
    os.system('cls' if os.name is 'nt' else 'clear')

conn = psycopg2.connect('dbname=AppointmentSys user=postgres password=admin')
cur = conn.cursor()

### MENU ###

menu = {}

menu['1'] = 'Add appointment'
menu['2'] = 'Delete appointment'
menu['3'] = 'Lookup appointment'
menu['4'] = 'Update appointment'
menu['0'] = 'Quit'
# more options

cls()
while True:
    for option in menu.items():
        print('\t' + option[0] + '. ' + option[1])

    sel = input('\t>_ ')
    if sel is '1':
        # run add script
    elif sel is '2':
        # run delete script
    elif sel is '3':
        # run search script
    elif sel is '4':
        # run update script
    elif sel is '0':
        # Quit
    else:
        # throw exception

### FUNCTIONS ###

def insert(patient_id, appointment_time, visit_number, payment_roll, insurance_number):
    # connect to database using CONFIG

def delete(patient_id, appointment_time, visit_number, payment_roll, insurance_number):
    # connect to database using CONFIG

def search(patient_id, appointment_time, visit_number, payment_roll, insurance_number):
    # connect to database using CONFIG

def update(patient_id, appointment_time, visit_number, payment_roll, insurance_number):
    # connect to database using CONFIG
