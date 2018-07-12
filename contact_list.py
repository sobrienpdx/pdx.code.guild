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

contacts = {'Freely': {'first_name': 'IP', 'last_name': 'Freely', 'phone_number': '8'}, 'Care': {'first_name': 'Shirley U.', 'last_name': 'Care', 'phone_number': '8'}}
csv_style_contacts = []

# with open("contact_list.cvs", "r",) as csv_file:
#     csv_reader = csv.reader(csv_file)

# with open('contact_list.csv', 'a') as csvfile:
#     fieldnames = ['first_name', 'last_name', 'phone_number']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans', 'phone_number': '56'})

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

def return_to_comma_separated_values(contacts):
    '''
    puts dictionary back to csv format
    returns list of csv entries
    >>> return_to_comma_separated_values(contacts):
    'IP,Freely,8
    Shirley U.,Care,8'
    '''
    # with open("contacts.csv", "w") as csv_file:
    #         fieldnames = ['first_name', 'last_name', 'phone_number']
    #         csv_writer = csv.writer(contacts.csv, fieldnames=fieldnames)
    #         for key in contacts:
    #             csv_writer.writerow
    for entry in contacts:
        csv_style_line = contacts[entry]['first_name']+","+ contacts[entry]['last_name']+ ","+ contacts[entry]['phone_number']
        print(csv_style_line)
    # print(csv_style_contacts)

# populate_contact_list()
return_to_comma_separated_values(contacts)

# print(contacts)
# print(contacts['Freely']['first_name']+","+ contacts['Freely']['last_name']+ ","+ contacts['Freely']['phone_number'])
# foo = contacts['Freely']['first_name']+","+ contacts['Freely']['last_name']+ ","+ contacts['Freely']['phone_number']
# print(foo)
# def write_and_save_updated_list(contacts):
#     with open("contacts.csv", "w") as csv_file:
#         fieldnames = ['first_name', 'last_name', 'phone_number']
#         csv_writer = csv.writer(contacts.csv, fieldnames=fieldnames)
#         for key in contacts:
#             csv_writer.writerow

    # csv_writer.writeheader()
    #
    #     for line in csv_reader:
    #         csv_writer.writerow(line)



# write_and_save_updated_list(contacts)

    # with open("newcsvfile", "w") as new_file:
    #     csv_writer = csv.writer(new_file, delimiter = "-")

    # next(csv_reader)
#


    # for line in csv_reader:
        # print(line[2])


#
# def retrieve():
#     with open('contacts.csv', "r", newline='') as csvfile:
#          contactreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#          for row in contactreader:
#              print(' '.join(row))
#
#
# def user_selection():
#     while True:
#         print('What do you want to do?')
#         print('  1 Add an entry')
#         print('  2 Change an entry')
#         print('  3 Retrieve an entry')
#         print('  4 Delete an entry')
#         task = input(': ')
#         if task == '1':
#             add()
#         elif task == '2':
#             change()
#         elif task == '3':
#             retrieve()
#         elif task == '4':
#             delete()
#         else:
#             print('Entry not found.')
#             continue
#         if not yes_or_no_question('Do you want to do anything else (y/n)? '):
#             break
#     print('Goodbye then!')
#
#
# # with open('contacts.csv', 'w', newline='') as csvfile:
# #     spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# #     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
# #     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
#
# # with open('contacts.csv', newline='') as csvfile:
# #      contactreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# #      for row in contactreader:
# #          print(' '.join(row))
#
#
# with open('contacts.csv', 'a', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name', 'phone_number']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     # writer.writeheader()
#     # writer.writerow({'first_name': confirmed_last_to_add, 'last_name': confirmed_name_to_add, 'phone_number': confirmed_number_to_add})
#     add_it_all = create_contact()
#     writer.writerow(add_it_all)
#
#
# import csv
# with open('contacts.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['first_name'], row['last_name'], row['phone_number'])
#
#
# print(row)
#
# with open('contacts.csv', 'r') as file:
#     lines = file.read().split('\n')
#     print(lines)
#
#     #YOU MUST HAVE THE USER QUIT TO EXIT... CNTRL C WON'T SAVE ANY INFO!!!
#
#     #WRITE TO FILE SAVES INFO
