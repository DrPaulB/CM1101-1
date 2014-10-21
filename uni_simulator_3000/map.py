from items import *
 
room_lecture = { #inside the lecture hall
 
    "name": "Lecture Hall",
 
    "description":
    """You are inside T/2.09 lecture hall, a daunting room with a slight smell of damp... Perhaps that's down to the age of the building.
    You see a timetable on the desk at the front of the room along with an assortment of junk left behind from other lectures.
    You also see a swiping device for your id card, you think to yourself 'I wonder if anyone actually uses those pointless things...'""",
 
    "exits": {"north": "Library", "east": "Commonroom", "south": "Hallway", "west": "Outside"},
 
    "items": [item_timetable] #timetable is not in items.py yet.
}
 
 
room_library = { #Library
 
    "name": "Library",
 
    "description":
    """You are in the library, you see a vast collection of books in a very complicated order. There are also some computers, but as normal these are all being used and there is no room for you.
    It is best to be quiet here as people are trying to study.
    """,
 
    "exits":  {"south": "Lecturehall"},
 
    "items": []
}
 
room_hall = { #Hallway which leads to Robs/labs/Tutoroffice
 
    "name": "Hallway",
 
    "description":
    """You are in one of the many hallways in the building. You can see that this perticular hallway leads to the computer labs
    if you go south, Robs room if you go east and the tutor room if you go west.""",
 
    "exits": {"east": "Robs", "south": "Labs", "west": "Tutor"},
 
    "items": []
}
 
 
room_robs = {
 
    "name": "Robs' room",
 
    "description":
    """You are leaning against the door of the systems managers' room. Inside you notice Rob Evans and Rob Davies. They
    ignore you. To the north is the Common Room.""",
 
    "exits":  {"north": "Commonroom"},
 
    "items": []
}
 
room_common = {
 
    "name": "Common Room",
 
    "description":
    """You are in the Common Room, you can see groups of students eating lunch, doing work
    and socialising. To the north is the Canteen.""",
 
    "exits":  {"north": "Canteen"},
 
    "items": []
}
 
room_tutor = {
 
    "name": "Your personal tutor's office",
 
    "description":
    """You are in your personal tutor's office. He intently
    stares at his huge monitor, ignoring you completely.
    On the desk you notice a cup of coffee and an empty
    pack of biscuits. The reception is to the west.""",
 
    "exits": {"east": "Hallway"},
 
    "items": []
}
 
room_canteen = {
 
    "name": "Canteen",
 
    "description":
    """You are in the canteen, you see the lunch lady waiting for you. You can also see a till where you have to 
    pay for your food.""",
 
    "exits":  {"south": "Commonroom"},
 
    "items": []
}
 
outside = {
 
    "name": "Queens building",
 
    "description":
    """You are outside the Queens bulding, you can walk home, got to McDonalds or go back inside""",
 
    "exits": {"north": "Home", "south": "Mcdonalds", "east": "Lecturehall"},
 
    "items": []
}
 
 
outside_home = { # The main spawn point - where we wake up
 
    "name" : "Your room",
 
    "description":
    """Your room in the university accommodation. You can go north to go into your flatmates room.""",
 
    "exits": {"north": "Flatmatesroom", "south": "Outside"},
 
    "items": [item_id]
 
}
 
room_flatmate = {
 
    "name" : "Your flatmate's room",
 
    "description":
    """You walk into your flatmates room, there are numerous things on their desk.""",
 
    "exits": {"south": "Home"},
 
    "items": [item_jd] #item_jd (jackdaniels) is not in items.py yet.
 
}
 
outside_mcdonalds = {
 
    "name" : "McDonalds",
 
    "description":
    """The local McDonalds, you see a lot of students here on their break. You also see a cashier looking at you expectantly. You can go north to go back outside.""",
 
    "exits": {"north": "Outside"},
 
    "items": [] #item_jd (jackdaniels) is not in items.py yet.
 
}
 
rooms = {
 
    "Lecturehall": room_lecture,
    "Library": room_library,
    "Hallway": room_hall,
    "Robs": room_robs,
    "Commonroom": room_common,
    "Tutor": room_tutor,
    "Canteen": room_canteen,
    "Outside": outside,
    "Home": outside_home,
    "Flatmatesroom": room_flatmate,
    "Mcdonalds": outside_mcdonalds,
 
}