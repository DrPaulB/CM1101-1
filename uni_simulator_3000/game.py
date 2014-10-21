#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
import sys
from time import sleep
from random import uniform

def game_title():
    # Prints the title of the game in Askii art.
    
    print ("""

  | | | |_ __ (_)_   _____ _ __ ___(_) |_ _   _ 
  | | | | '_ \| \ \ / / _ \ '__/ __| | __| | | |
  | |_| | | | | |\ V /  __/ |  \__ \ | |_| |_| |
   \___/|_| |_|_| \_/ \___|_|  |___/_|\__|\__, |
                                          |___/ 
  ____  _                 _       _             
 / ___|(_)_ __ ___  _   _| | __ _| |_ ___  _ __ 
 \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
  ___) | | | | | | | |_| | | (_| | || (_) | |   
 |____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   



""")

def print_introduction():
    #This function prints out the starting text. Ignore the ugly formatting.
    line_1 = """You wake up, feeling highly drunk from the night before... What happened? you mutter to yourself as you pull your banging head out from the pillow.


As per normal, the first thought is to pull out your phone and check your emails, after all, you don't want to miss your daily chance to get $30,000,000,000 from that Zimbarbian prince...

What?    An email from the bank... I spent how much on what?!?! Somehow in your drunken state you managed to sign up for a Computer Science course at Cardiff University, and you apparently start... TOMORROW.

Good Luck making it through your first day.


"""
    for x in line_1:
        print(x, end='')
        sys.stdout.flush()
        sleep(uniform(0, 0.0))


def energypoints(changevalue):
    energypoints = energypoints + changevalue
    return energypoints

def timepoints(changevalue):
    timepoints = timepoints + changevalue
    return timepoints

def intelligencepoints(changevalue):
    intelligencepoints = intelligencepoints + changevalue
    return intelligencepoints

def socialpoints(changevalue):
    socialpoints = socialpoints + changevalue
    return socialpoints



def what_time_to_wake_up():
    print ("WHAT TIME TO AWAKEN?")
    print ("")
    print ("As a newly appointed Univerity Student you have the first of many hard choices to make... Like, what time to wake up.")
    print ("")
    print ("On one hand, you're really tired and would like a bit more sleep to gain some energy, but also, you would be left with less time in the day.")
    print ("")
    print ("On the other, getting up very early and springing out of bed would probably be better for your study... That is if you can stay awake.")
    print ("")
    print ("You can choose anywhere between 7.00am and 5.00pm, remember though... you have your meeting with Matt at 5.00pm, so it would be best to at least attempt to do something before then.")
    print ("")
    timeofawakening = int(input("Please type the hour you want to awaken [i.e.: 1.00pm would be '1']: "))
    while timeofawakening not in [7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5]:
        print ("That's not a suitable time... ")

        timeofawakening = int(input("Please type the hour you want to awaken [i.e.: 1.00pm would be '1']: "))
    if timeofawakening == 7:
        hours_in_day = 10
    elif timeofawakening == 8:
        hours_in_day = 9
    elif timeofawakening == 9:
        hours_in_day = 8
    elif timeofawakening == 10:
        hours_in_day = 7
    elif timeofawakening == 11:
        hours_in_day = 6
    elif timeofawakening == 12:
        hours_in_day = 5
    elif timeofawakening == 1:
        hours_in_day = 4
    elif timeofawakening == 2:
        hours_in_day = 3
    elif timeofawakening == 3:
        hours_in_day = 2
    elif timeofawakening == 4:
        hours_in_day = 1
    else:
        hours_in_day = 0
    return hours_in_day

def calculateenergy(timepoints):
    if timepoints in [0,1,2]:
        energy = 100
    elif timepoints in [3, 4, 5]:
        energy = 70
    elif timepoints in [6,7]:
        energy = 50
    else:
        energy = 20
    return energy





def list_of_items(items): #Jordan Cooke
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'
    >>> list_of_items([item_id])
    'id card'
    >>> list_of_items([])
    ''
    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'
    """

    itemslist = []
    for i in items:
        itemslist.append((i["name"]))
    return', '.join(itemslist)


def print_room_items(room): #Shaun George
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Robs"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    x = room['items']
   
    if list_of_items(x):
        i = "There is " + list_of_items(x) + " here."
        print(i)
        print(" ")

    pass


def print_inventory_items(items): #Jason Choo
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:
    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>
    """
    print("You have " + list_of_items(items) + "." + "\n")

    pass

def print_room(room): #Jamie Knowles
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Robs"])
    <BLANKLINE>
    ROBS' ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Rob Evans and Rob Davies. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    # Display items in room
    return print_room_items(room)



def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "Robs' room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "Robs' room")
    GO SOUTH to Robs' room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items): #Povilas Blusius

    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print
    "TAKE <ITEM ID> to take <item name>."
    and for each item in the inventory print
    "DROP <ITEM ID> to drop <item name>."
    For example, the menu of actions available at the Reception may look like this:
    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to Robs' room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?
    """

    print("You can:")
    # Iterate over available exits
    for direction in exits:
    # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item in inv_items:
        print ("DROP " + item["id"].upper() + " to drop your " + item["name"])

    for item in room_items:
        print ("TAKE " + item["id"].upper() + " to take " + item["name"])

        print("")
        print("What do you want to do?")

    pass


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits


def execute_go(direction): #Shaun George
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """

    global current_room

    if is_valid_exit(current_room['exits'], direction):
        x = (current_room['exits'][direction])
        current_room = rooms[x]
        return current_room
    else:
        print("You cannot go there.")
    


def execute_take(item_id): #Code not completed
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    for x in current_room['items']:
        print(x)


    for item_dictionary in current_room["items"]:
        if item_id == item_dictionary["id"]:
            current_room["items"].remove(item_dictionary)
            inventory.append(item_dictionary)
    

def execute_drop(item_id): #Code not completed
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    for item_dictionary in inventory: 
        if item_id == item_dictionary["id"]:
            current_room["items"].append(item_dictionary)
            inventory.remove(item_dictionary)
    

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Robs"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


def main():
    ####################################################################################################################
    ################################################# STARTUP SEQUENCE #################################################
    ####################################################################################################################
    # This code only runs at the beginning of the program, this declares all vairables and deals with showing the user #
    #   all non recursive commands and functions. This sequence is also where the user determines their "difficulty"   #
    ####################################################################################################################

    game_title()                                # Plays the title Askii art to the user
    print_introduction()                        # Shows introductory text explaining the story to the user
    timepoints = what_time_to_wake_up()         # Determines what time the user wants to awake (changes difficulty of game)
    intelligencepoints = 50                     # Average score, doesn't change before users gameplay
    socialpoints = 20                           # Average score, doesn't change before users gameplay
    energypoints = calculateenergy(timepoints)  # Gives the user a set amount of energy depending on their wake time


    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)



# The code that starts the whold thing.
if __name__ == "__main__":
    main()

