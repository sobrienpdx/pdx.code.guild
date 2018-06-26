# phonebook.py

# Imports first

# Constants
phonebook = {'Beeks': {'first_name': 'Emily',
                        'last_name': "Beeks",
                        'phone_number': 4524493056},
            'Steckler': {'first_name': 'Maureen',
                        'last_name': "Steckler",
                        'phone_number': 4453859475},
            'Berry': {'first_name': 'Paul',
                        'last_name': "Berry",
                        'phone_number': 4007776666},
            'Miles': {'first_name': 'Dan',
                        'last_name': "Miles",
                        'phone_number': 4007776666},
            'Curtis': {'first_name': 'Lynn',
                        'last_name': "Curtis",
                        'phone_number': 4442229999}}



# Functions


#This function asks the user to re-enter data until it matches a contact in phonebook
def get_proper_input(corrected_contact):
    while corrected_contact not in phonebook:
        print("Contact not found.")
        corrected_contact = input("Enter the last name of the contact you would like to view: ")
    return corrected_contact

# double checks that new info is correct before adding to phonebook
def double_check_new_info(confirmation, question_to_confirm):
    while True:
        double_check = input("You have entered {}. Is that correct? Y/N ".format(confirmation))
        if double_check.lower() == "y":
            return confirmation
        elif double_check.lower() == "n":
            confirmation = input("{}: ".format(question_to_confirm))
            continue
        else:
            print("Please use y/n format.")




# create new contact
def create_contact():
    last_name_to_add = input("Enter the last name of the contact you would like to create: ")
    confirm_last_name = 'Enter the last name of the contact you would like to create '
    confirmed_last_to_add = double_check_new_info(last_name_to_add, confirm_last_name)

    first_name_to_add = input("Enter the first name of the contact you would like to create: ")
    confirm_first_name = 'Enter the first name of the contact you would like to create '
    confirmed_name_to_add = double_check_new_info(first_name_to_add, confirm_first_name)

    phone_number_to_add = input("Enter the phone number of the contact you would like to create: ")
    confirm_phone_number = 'Enter the phone number of the contact you would like to create '
    confirmed_number_to_add = double_check_new_info(phone_number_to_add, confirm_phone_number)

    phonebook[last_name_to_add]= {"first_name": confirmed_name_to_add, "last_name": confirmed_last_to_add, "phone_number": confirmed_number_to_add }
    print("Contact for {} {}, phone number {} has been created.".format(confirmed_name_to_add, confirmed_last_to_add, confirmed_number_to_add))


# Allows user to see phone number or first name of person by entering last name
def retrieve_contact():
    person_to_retrieve = input("Enter the last name of the contact you would like to view: ")
    person_to_retrieve = get_proper_input(person_to_retrieve)
    first_or_phone = input("Do you need a phone number, first name, or both? ")
    number = (phonebook[person_to_retrieve]["phone_number"])
    name = (phonebook[person_to_retrieve]["first_name"])
    if first_or_phone == "phone number":
        print("{}'s phone number is {}.".format(person_to_retrieve, number))
    elif first_or_phone == "first name":
        print("{}'s first name is {}.".format(person_to_retrieve, name))
    elif first_or_phone == "both":
        number = (phonebook[person_to_retrieve]["phone_number"])
        name = (phonebook[person_to_retrieve]["first_name"])
        print("{}'s first name is {} and their phone number is {}.".format(person_to_retrieve, name, number))

# Allows user to change either first name, phone number or both by entering last name
def update_contact():
    person_to_update = input("What is the last name of the contact you would like to update? ")
    person_to_update = get_proper_input(person_to_update)
    info_to_update = input("Do you want to change their first name, phone number, or both? ")
    if info_to_update == "phone number":
        new_number = input("What is the new phone number? ")
        question_new_number = "What is the new phone number"
        new_number = double_check_new_info(new_number, question_new_number)
        phonebook[person_to_update]["phone_number"] = new_number
        print("The phone number for {} has been changed to {}.".format(person_to_update, new_number))
    elif info_to_update == "first name":
        new_name = input("What is the new name? ")
        phonebook[person_to_update]["first_name"] = new_name
        print("The first name for {} has been changed to {}.".format(person_to_update, new_name))
    elif info_to_update == "both":
        new_number = input("What is the new phone number? ")
        phonebook[person_to_update]["phone_number"] = new_number
        new_name = input("What is the new name? ")
        phonebook[person_to_update]["first_name"] = new_name
        print("The phone number for {} has been changed to {}, and the name has been saved as {}.".format(person_to_update, new_number, new_name))

#Allows user to completely delete contact
def delete_contact():
    person_to_delete = input("Enter the last name of the contact you would like to delete: ")
    person_to_delete = get_proper_input(person_to_delete)
    del phonebook[person_to_delete]
    print("{} has been deleted from your contacts.".format(person_to_delete))

def perform_task(task):
    if task == "1":
        retrieve_contact()
    elif task == "2":
        create_contact()
    elif task == "3":
        update_contact()
    elif task == "4":
        delete_contact()

#delete_contact()
#create_contact()
#update_contact()
#retrieve_contact()

# Classes

# Setup code
task = input("Welcome to phonebook. Please choose from the following menu: \n 1 to look up a contact \n 2 to create a new contact \n 3 to update a contact \n 4 to delete a contact ")
while task not in ["1", "2", "3", "4"]:
    task = input("Invalid command entry. Please choose from the following menu: \n 1 to look up a contact \n 2 to create a new contact \n 3 to update a contact \n 4 to delete a contact ")
else:
    perform_task(task)
anything_else = input("Would you like to perform another task? y/n ")
while anything_else == "y":
    task = input("Please choose from the following menu: \n 1 to look up a contact \n 2 to create a new contact \n 3 to update a contact \n 4 to delete a contact ")
    perform_task(task)
    anything_else = input("Would you like to perform another task? y/n ")
if anything_else == "n":
    print("Ok, goodbye!")

#Paul's note:
# while True:
#     task = input("ahsdfhjkdfghjk")
#     if task in ["1", "2", "3", "4"]:
#         break
#     print("invalid")
# perform_task(task)



# Testing
