#This Program Is For The Codecademy Project (Object Oriented Programming)
import time

print("Hello! \nWelcome to the Servicedesk Portal. Before you can begin making tickets, let's create an account. Depending on your role, you can receive access to one of these types of accounts: \n\n -Servidesk User \n -Servicedesk Admin \n -Servicedesk Owner")

time.sleep(1.5)

print("\nEach type account will give you different type of access levels. Please make sure to select the appropiate account type. To begin please input your name below: (First & Last Name)")

name = input()

print("\nNice to meet you " + name + ". Now please tell us your role at Box.")

role = input()

print("\nGreat! looks like you have access to Service desk as an admin. Creating your account now. Please wait.")

time.sleep(3)

# Class Creating ServiceDesk Users, aka Objects
class servicedesk_user:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.modify_tickets = False
        self.modify_access_level = False

    def __repr__(self):
     return "You've succesfully added {name} as a Servicedesk User. They role is the following: {role}".format(name = self.name, role = self.role)

    def create_ticket(self):
        ticket_count = 0
        if ticket_count >= 0:
            ticket_count += 1
        return "You've succesfully created a new ticket. Your current ticket count is: " + str(ticket_count)
        
# Class Creating ServiceDesk Admins, aka Objects
class servicedesk_admin:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.modify_tickets = True
        self.modify_access_level = False

    def __repr__(self):
        return "You've succesfully added {name} as a Servicedesk Admin. They role is the following: {role}".format(name = self.name, role = self.role)

    def create_ticket(self):
        ticket_count = 0
        if ticket_count >= 0:
            ticket_count += 1
        return "You've succesfully created a new ticket. Your current ticket count is: " + str(ticket_count)

# Class Creating ServiceDesk Owners, aka Objects
class servicedesk_owners:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.modify_tickets = True
        self.modify_access_level = True

    def __repr__(self):
        return "You've succesfully added {name} as a Servicedesk Owner. They role is the following: {role}".format(name = self.name, role = self.role)

    def create_ticket(self):
        ticket_count = 0
        if ticket_count >= 0:
            ticket_count += 1
        return "You've succesfully created a new ticket. Your current ticket count is: " + str(ticket_count)


# Creating An Object Based On Information Inputted
account_creation = servicedesk_admin(name, role)
print(account_creation)

print("\nPlease wait a moment while we create your ticket... ... ...")
time.sleep(3)

# Creating A Ticket Using The Class Function
ticket_creation = account_creation.create_ticket()
print(ticket_creation)