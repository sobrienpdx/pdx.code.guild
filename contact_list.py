# contact list

# first_name,last_name,phone_number
# IP,Freely,8
# Shirley U.,Care,8
# Felix,Cited,8
# Lori,Driver,8
# Stan,Dupp,8
# Frank N.,Stein,8
# Lorne,Mowers,8
# Titus,Zell,8
# Gerry,Atrick,8
# Lynn C.,Doyle,8
# Gladys,Canby,8
# Julie,Crudele,8
# Thyme,Justin,3
import csv

contacts = {}


def populate_contact_list():
    '''
    makes a dictionary out of contacts.csv
    returns list of dictionaries
    >>> populate_contact_list()
    {'Freely': {'first_name': 'IP', 'last_name': 'Freely', 'phone_number': '8'}, 'Care': {'first_name': 'Shirley U.', 'last_name': 'Care', 'phone_number': '8'}}
    '''
    with open("contacts.csv", "r",) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            temp = {'first_name': line[0], 'last_name': line[1], 'phone_number': line[2]}
            contacts[line[1]] = temp
        return contacts


def write_updated_phonebook_over_old_csv(contacts):
    '''
    puts dictionary back to csv format
    returns list of csv entries
    >>> return_to_comma_separated_values(contacts):
    'IP,Freely,8
    Shirley U.,Care,8'
    '''
    with open("contacts.csv", "w") as updated_csv_file:
        outstring = 'first_name'+","+'last_name'+","+'phone_number'+"\n"
        for entry in contacts:
            outstring +=  contacts[entry]['first_name']+","+ contacts[entry]['last_name']+ ","+ contacts[entry]['phone_number']+"\n"
        updated_csv_file.write(outstring)


def add():
    while True:
        last = input('Last name? ')
        first = input('First name? ')
        phone = input('Phone number? ')
        print('  Last name: ' + last)
        print('  First name: ' + first)
        print('  Phone number: ' + phone)
        correct_or_no = input("Is that correct? ")
        if correct_or_no.lower().strip() in ["y", "yes"]:
            contacts[last]= {'first_name': first, 'last_name': last, 'phone_number': phone}
            break
    print(contacts[last])


def change():
    while True:
        last = input('What is the last name of the person to update? ')
        if last not in contacts:
            print(f"Entry for {last} not found.")
        else:
            break
    while True:
        last = input('Last name to save? ')
        first = input('First name to save? ')
        phone = input('Phone number to save? ')
        print('  Last name: ' + last)
        print('  First name: ' + first)
        print('  Phone number: ' + phone)
        correct_or_no = input("Is that correct? ")
        if correct_or_no.lower().strip() in ["y", "yes"]:
            contacts[last]= {'first_name': first, 'last_name': last, 'phone_number': phone}
            break
        print(contacts[last])


def retrieve():
    while True:
        last = input('What is the last name of the person you would like to look up? ')
        if last not in contacts:
            print(f"Entry for {last} not found.")
        else:
            break
    entry = contacts[last]
    first = entry['first_name']
    phone = entry['phone_number']
    print('first name: ' + first)
    print('phone: ' + phone)


def delete():
    while True:
        last = input('What is the last name of the person you would like to delete? ')
        if last not in contacts:
            print(f"Entry for {last} not found.")
        else:
            break
    while True:
        print('The following entry will be deleted: ')
        print(contacts[last])
        correct_or_no = input("Is that correct? ")
        if correct_or_no.lower().strip() in ["y", "yes"]:
            break
    print(f"Entry for {last} has been deleted.")
    del contacts[last]




def user_selection():
    while True:
        print('What do you want to do?')
        print('  1 Add an entry')
        print('  2 Change an entry')
        print('  3 Retrieve an entry')
        print('  4 Delete an entry')
        task = input(': ')
        if task == '1':
            add()
            write_updated_phonebook_over_old_csv(contacts)
        elif task == '2':
            change()
            write_updated_phonebook_over_old_csv(contacts)
        elif task == '3':
            retrieve()
            write_updated_phonebook_over_old_csv(contacts)
        elif task == '4':
            delete()
            write_updated_phonebook_over_old_csv(contacts)
        else:
            print('Entry not found.')
            continue
        more = input('Do you want to do anything else (y/n)? ')
        if more.strip().lower() in ["n", "no"]:
            break
    print('Goodbye then!')

populate_contact_list()
user_selection()
write_updated_phonebook_over_old_csv(contacts)
