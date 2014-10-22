#!/usr/bin/python3
#test
from map import rooms
from player import *
from items import *
from gameparser import *
import sys
from time import sleep
from random import uniform


#Stats stored in the following order:
# Time, Social, Intelligence, Energy
stats = [0, 20, 50, 0]


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

What? An email from the bank... I spent how much on what?!?! Somehow in your drunken state you managed to sign up for a Computer Science course at Cardiff University, and you apparently start... TOMORROW.

Good Luck making it through your first day.


"""

    for x in line_1:
        print(x, end='')
        sys.stdout.flush()
        sleep(uniform(0, 0.0))


def change_value(a, b):
    return (a + b)



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





def list_of_items(items):
    # This function takes a list of items (see items.py for the definition) and returns a comma-separated list of item names (as a string).

    itemslist = []
    for i in items:
        itemslist.append((i["name"]))
    return', '.join(itemslist)


def print_room_items(room): #Shaun George
    # This function takes a room as an input and nicely displays a list of items found in this room (followed by a blank line).
    x = room['items']
   
    if list_of_items(x):
        i = "There is " + list_of_items(x) + " here."
        print(i)
        print(" ")


def print_inventory_items(items):
    # This function takes a list of inventory items and displays it nicely, in a manner similar to print_room_items().


    if not list_of_items(items):
        print("You have " + "nothing on you" + "." + "\n")
    else:
        print("You have " + list_of_items(items) + "." + "\n") 


def print_room(room): #Jamie Knowles
    # This function takes a room as an input and nicely displays its name and description.
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
    # This function takes a dictionary of exits and a direction (a particular exit taken from this dictionary). It returns the name of the room into which this exit leads.
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    # This function prints a line of a menu of exits.
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items): #Povilas Blusius
    global current_room
    # This function displays the menu of available actions to the player. The
    

    print("You can:")

    # Iterate over available exits
    for direction in exits:
    # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item in inv_items:
        x = item['name']
        if x == "Blank library test":
            print("DO TEST to complete your library test.") #Gives the option to the user to do the test
        else:
            print ("DROP " + item["id"].upper() + " to drop your " + item["name"])

    for item in room_items:
        print ("TAKE " + item["id"].upper() + " to take " + item["name"])

    try:
        for item in inv_items:
            x = item['id']
            if x == "phone":
                print("CHECK TIME on your phone")
    except:
        return

    try:
        for item in inventory:
            x = item['id']

        if "timetable" in x:
            print("READ TIMETABLE to find out what you're doing")
    except:
        pass

    if current_room['name'] == "McDonalds":
        print ("EAT to grab something to eat here")

    elif current_room['name'] == "Canteen":
        print ("EAT to grab something to eat here")
    else:
        pass

    if current_room['name'] in ["Library", "Home"]:
        print ("REVISE to study for your test later at 5.00pm")

    else:
        pass





def is_valid_exit(exits, chosen_exit):
    # This function checks, given a dictionary "exits" and returns if valid
   
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
    


def execute_take(item_id):
    # This function takes an item_id as an argument and moves this item from the list of items in the current room to the player's inventory.
    for item_dictionary in current_room["items"]:
        if item_id == item_dictionary["id"]:
            current_room["items"].remove(item_dictionary)
            inventory.append(item_dictionary)
    

def execute_drop(item_id):
    # This function takes an item_id as an argument and moves this item from the player's inventory to list of items in the current room.

    for x in inventory:  #Loops x through inventory
        i = x['id'] # i is assigned to x['name']

        if item_id == x["id"]: #checks if the input is equal to the "name" of the item.

            if "copiedtest" in item_id and (current_room["name"] == 'Library'):  #checks whether the test is copied and whether the player is in the library (can only get the test graded in library)
                inventory.remove(item_test_c) #removes test from inventory
                stats[2]
                testScore = 100 #if you cheat, you get a fixed 100% mark
                print("Your score out of a 100 is: ", testScore) #prints score

            elif "completedtest" in item_id and (current_room["name"] =='Library'):
                inventory.remove(item_test_w)
                x = stats[2] #x is assigned to the current value of intelligencepoints
                print("Your score out of a 100 is:", x) #grade depends on how much intelligence points you have

            else:
                current_room["items"].append(x) 
                inventory.remove(x)


def execute_read_timetable(items):
    # Allows the user to read timetable
    print(item_timetable["description"])


def execute_check_time(command):
    # Allows the user to check their phone for the time
    try:
        for item in inventory:
            x = item['id']
            if x == "phone":
                print("You have", stats[0], "hours until your meeting with Matt")
                break
        else:
            print ("How are you planning to check the time? You don't have your phone?")
    except:
        print ("How are you planning to check the time? You don't have your phone?")

def execute_revise():
    # Allows the user to revise for their test
    global current_room
    if current_room['name'] in ["Library", "Home"]:

        print("""While you can, you think you should revise for your test later. This is afterall what being a student is all about... You think though, it will take about an hour to revise properly.

        ###################################################################
        DO REVISION: -Social | -Energy | +Intelligence | Time -1 hour
        ###################################################################

        """)
        testInput = input("Do you really want to revise? [Yes/No]: ") #gives you the option to eat or not
        
        if testInput.lower() == "yes": #if you choose to eat

            print ("Ugh!, that was a drag... Still, you think you're becoming smarter.")
            x = stats[0]
            stats[0] = x-1 # Updating time from choice

            x = stats[1]
            stats[1] = x-10 # Updating social points

            x = stats[3] # Updating energy
            stats[3] = x-15

            x = stats[2]
            stats[2] = x+20

        elif testInput.lower() == "no":
            print ("Well, atleast you considered it! After all, it's the thought that counts!")

        else:
            print("I didn't understand that, try again.")
    else:
        print ("How are you planning to revise here? Try your home or the library")



def execute_eat():
    # Checks if the user is in a place of food, if so they eat
    global current_room
    if current_room['name'] == "McDonalds":
        print("""Looking around, still deciding if you want to eat here, you catch sight of an employee spitting in a burger, 'ugh!'. Still, looks like their new horse burger will taste good, it's got extra cheese too!

            Did you want to eat here?

        ###################################################################
        EAT AT McDONALDS: +Social | +Energy | Time -1 hour
        ###################################################################

        """)
        testInput = input("Would you like to have a burger? [Yes/No]: ") #gives you the option to eat or not
        
        if testInput.lower() == "yes": #if you choose to eat

            print ("Ah, much better! You feel slightly energised by that.")
            x = stats[0]
            stats[0] = x-1 # Updating time from choice

            x = stats[1]
            stats[1] = x+30 # Updating social points

            x = stats[3] # Updating energy
            stats[3] = x+20



        elif testInput.lower() == "no": 

            print ("Perhaps that's a good choice, afterall it would take ages to eat and you should be revising. You could also try the canteen?")

        else:
            print("I didn't understand that, try again.")

    elif current_room['name'] == "Canteen":
        print("""Right infront of you is a baguette. The bread has gone slightly gray and the ham inside looks dry, not to mention the cost of the damn thing! Still, it's better than nothing, and doesn't take long to eat.

            Did you want to eat here?

        ###################################################################
        EAT AT CANTEEN: -Social | +Energy | Time -0.5 hour
        ###################################################################

        """)
        testInput = input("Would you like to have a the roll? [Yes/No]: ") #gives you the option to eat or not
        
        if testInput.lower() == "yes": #if you choose to eat

            print ("That tasted awful, You feel slightly energised by that anyway.")
            x = stats[0]
            stats[0] = x-0.5 # Updating time from choice

            x = stats[1]
            stats[1] = x-10 # Updating social points

            x = stats[3] # Updating energy
            stats[3] = x+20



        elif testInput.lower() == "no": 

            print ("Perhaps that's a good choice, that roll would probably give you something horrific... How about McDonalds down the road?")

        else:
            print("I didn't understand that, try again.")
    else:
        print ("Eat what? There is no food here.")



    
def execute_do(item_id): # Function is only for the library test
    """This function takes an argument and does an action relevant to the item e.g. "Do test" will make the user do the test """

    for x in inventory: 
        item = (x['name'])

    if "Blank library test" in item: #checks if library test is in inventory
        print("""You look at the paper, feeling confused you glance up to see you friend. He suggests you copy his test.
            You know using your better judgement you should do it properly but at the same time, cheating is quicker.

            ###################################################################
            CHEAT THE TEST: +Social | -Intelligence | -Energy | Time -0.5 hour
            HONESTLY COMPLETE THE TEST:  +Intelligence | -Energy | Time -1 hour
            ###################################################################

            Your friend wonders why you are taking so long to answer...
            """)

        testInput = input("Would you like to cheat on the test [Yes/No]: ") #gives you the option to cheat

        if testInput.lower() == "yes": #if you cheat, your blank test will be replaced by a completed test
            inventory.remove(item_test) 
            inventory.append(item_test_c)
            x = stats[0]
            stats[0] = x-0.5 # Updating time from choice

            x = stats[1]
            stats[1] = x+10 # Updating social points

            x = stats[2] # Updating intelligance points
            stats[2] = x-10

            x = stats[3] # Updating energy
            stats[3] = x-5


        elif testInput.lower() == "no": 
            inventory.remove(item_test)
            inventory.append(item_test_w)
            x = stats[0]
            stats[0] = x-1 # Updating time from choice

            x = stats[2] # Updating intelligance points
            stats[2] = x+10

            x = stats[3] # Updating energy
            stats[3] = x-10


        else:
            print("I didn't understand that, try again.")

    else:
        print("You didn't pick up the test sheet.")

def execute_command(command):
    # This function takes a command and executes the correct function
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

    elif command[0] == "read":
        if len(command) > 1:
            execute_read_timetable(command[1])
        else:
            print("Read what?")

    elif command[0] == "check":
        if len(command) > 1:
            execute_check_time(command)
        else:
            print("Check what?")

    elif command[0] == "do": #the DO command for the DO function!
        if len(command) > 1:
            execute_do(command[1])
        else:
            print("Do what?")

    elif command[0] == "eat":
        execute_eat()

    elif command[0] == "revise":
        execute_revise()


    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    # This function, given a dictionary of possible exits from a room, and a list of items found in the room and carried by the player, prints the menu of actions using print_menu() function.

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    #This function returns the room into which the player will move.

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
    stats[0] = what_time_to_wake_up()         # Determines what time the user wants to awake (changes difficulty of game)
    stats[3] = calculateenergy(stats[0])  # Gives the user a set amount of energy depending on their wake time


    while True:
        # Display game status (room description, inventory etc.)
        print ("")
        print ("###################################################################")
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)



# The code that starts the whold thing.
if __name__ == "__main__":
    main()

