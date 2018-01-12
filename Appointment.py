import os
from config import *
import json

### MENU ###

menu = {}

menu['1'] = 'Add appointment'
menu['2'] = 'Delete appointment'
menu['3'] = 'Lookup appointment'
menu['4'] = 'Update appointment'
menu['0'] = 'Quit'
# more options

while True:
    conn.commit()
    cls()
    for option in menu.items():
        print('\t' + option[0] + '. ' + option[1])

    sel = input('\t>_ ')
    if sel is '1':
        patient_id = input('\tpatient_id >_ ')
        appointment_time = input('\tappointment_time >_ ')
        visit_number = input('\tvisit_number >_ ')
        payment_roll = input('\tpayment_roll >_ ')
        insurance_number = input('\tinsurance_number >_ ')
        insert(patient_id, appointment_time, visit_number, payment_roll, insurance_number)
    elif sel is '2':
        visit_number = input('\tvisit_number >_ ')
        delete(visit_number)
    elif sel is '3':
        visit_number = input('\tvisit_number >_ ')
        result = search(visit_number)
        print(result)
    elif sel is '4':
        visit_number = input('\tvisit_number >_ ')
        arg = input('\tcolumn to be updated >_ ')
        value = input('\tnew value >_ ')
        update(visit_number, arg, value)
    elif sel is '0':
        print('\tTERMINATED')
        break
    else:
        print('\tWRONG SELECTION.')

### FUNCTIONS ###

def insert(patient_id, appointment_time, visit_number, payment_roll, insurance_number):
    cur.execute('''
        INSERT INTO appointment
        VALUES ({}, {}, {}, {}, {});
    '''.format(patient_id, appointment_time, visit_number, payment_roll, insurance_number))
    cur.commit()

def delete(visit_number):
    cur.execute('''
        DELETE FROM appointment
        WHERE visit_number = '{}';
    '''.format(visit_number))

def search(visit_number):
    cur.execute('''
        SELECT * FROM appointment
        WHERE visit_number = '{}';
    '''.format(visit_number))
    result = cur.fetchone()
    return result

def update(visit_number, arg, value):
    cur.execute('''
        UPDATE appointment
        SET {} = '{}'
        WHERE visit_number = '{}';
    '''.format(arg, value, visit_number))

def insert_n(jcode):
    rows = json.loads(jcode)
    for row in rows:
        insert(row[0], row[1], row[2], row[3], row[4])
