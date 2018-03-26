import os

contact_list=[]

def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")
            

def show_help():
    clear_screen()
    print("Would you like to create a new contact?")
    print("""
Enter 'FINISHED' to save contact.
Enter 'HELP' for help.
Enter 'VIEW' to see your contact list.
Enter 'REMOVE' to delete a contact from the contact list.
""")
            
def add_to_contact(contact):
    
    if len(contact_list):
        place = input("Where should I add {}?\n"
                         "Press ENTER to add to the end of the contact\n"
                         "> ".format(contact))
    else:
        place = 0
                
    try:
        place = abs(int(place))
    except ValueError:
        place = None
    if place is not None:
        contact_list.insert(place-1, contact)
    else:
        contact_list.append(new_contact)
    
    show_contact()
            
def show_contact():
    clear_screen()
            
    print("Here's your contact:")
            

    for index, contact in enumerate(contact_list, start = 1):
        print("{}. {}".format(index, contact))
      
            
    print("!"*40)
    
def remove_from_contact(contact):
    contact = input("")
    show_contact()
    remove_contact = input("What should be removed?\n> ")
    try:
        contact_list.remove(remove_contact)
    except ValueError:
        pass
    show_contact()

show_help()
            
while True:
      new_contact = input("> ")
            
      if new_contact.upper() == 'FINISHED' or new_contact.upper() == 'QUIT':
            break
      elif new_contact.upper() == 'HELP':
            show_help()
            continue
      elif new_contact.upper() == 'VIEW':
            show_contact()
            continue
      elif new_contact.upper() == 'REMOVE':
            remove_from_contact(contact)
      else: 
          add_to_contact(new_contact)

show_contact()
            
