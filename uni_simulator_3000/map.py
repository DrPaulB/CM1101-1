from items import *
 
room_lecture = { #inside the lecture hall
 
    "name": "Lecture Hall",
 
    "description":
    """You are inside T/2.09 lecture hall, a daunting room with a slight smell of damp... Perhaps that's down to the age of the building. You see a timetable on the desk at the front of the room along with an assortment of junk left behind from other lectures. You also see a swiping device for your id card, you think to yourself 'I wonder if anyone actually uses those pointless things...'""",
 
    "exits": {"north": "Library", "east": "Canteen", "south": "Hallway", "west": "Outside"},
 
    "items": [item_timetable]
}
 
 
room_library = { #Library
 
    "name": "Library",
 
    "description":
    """You find yourself in the library, which you decide is unusual for someone as social as yourself. The walls are lined with vast collections of books towering over you and you immediately feel like you'll never begin to understand the classmark System, let alone be able to complete this simple library test! Ah yes, the library test! How did you forget? You walk up to the counter and pick up a copy of the test from the pleasent desk workers.
    """,
 
    "exits":  {"south": "Lecturehall"},
 
    "items": [item_test]
}
 
room_hall = { #Hallway which leads to Robs/labs/Tutoroffice
 
    "name": "Hallway",
 
    "description":
    """You find yourself in the hallway. To you every single hallway with its bleached white walls seems exactly the same and you realise you have no idea where you're actually going. As it's your first day you have become very disorientated and decide that the best course of action would be to ask the friendly PhD student approaching where exactly this hallway leads to!""",
 
    "exits": {"east": "Robs", "south": "Labs", "west": "Tutor", "north": "Lecturehall"},
 
    "items": []
}
 
 
room_robs = {
 
    "name": "Robs' room",
 
    "description":
    """You have arrived at Rob's room. These two Rob's have become infamous to you and you've only been here a few hours! You decide now would be the perfect time to get your laptop fixed as you've been unable to connect to the wifi until now, which is essential when it comes to your study. You knock and walk on in.""", 
    "exits":  {"north": "Canteen", "west": "Hallway"},
 
    "items": []
}
 

 
room_tutor = {
 
    "name": "Your personal tutor's office",
 
    "description":
    """It's time for your first ever meeting with your personal tutor! You wonder why you even bothered getting out of bed today, as this already seems pointless. You and your fellow peers are gathered around a table in a secluded room, and your tutor finally arrives with the pack of biscuits that he bribed you all with.""",
 
    "exits": {"east": "Hallway"},
 
    "items": []
}
 
room_canteen = {
 
    "name": "Canteen",
 
    "description":
    """You decided that you would go to the canteen for lunch! Immediately you regret this decision and wish that you had gone to McDonalds instead. You sit alone at a table for four, eating your very sorry looking baguette which you paid a fortune for! At least now you have time to revise...""",
 
    "exits":  {"south": "Robs", "west": "Lecturehall"},
 
    "items": []
}
 
outside = {
 
    "name": "Queens building",
 
    "description":
    """You have arrived at the entrance to the Queens Building! The exterior of the building seems uninviting and cold. The weather does little to contradict this... typical. You find that the only way to get to and from the building is by wading through the puddle that always seems to be there, regardless of the weather slightly improving. Good job you wore some waterproof clothing! Why wouldn't you? You did come to Wales after all..""",
 
    "exits": {"north": "Home", "south": "Mcdonalds", "east": "Lecturehall"},
 
    "items": []
}
 
 
outside_home = { # The main spawn point - where we wake up
 
    "name" : "Your room",
 
    "description":
    """You have entered your room. You flick on the light as the blinds remain shut after leaving in a bit of a rush this morning. You didn't realise until now what a mess your room had become in such a short space of time, and that it is only further emphasised by the lack of space that you have... but hey, that's the university life!""",
 
    "exits": {"north": "Flatmatesroom", "south": "Outside"},
 
    "items": [item_id, item_money, item_laptop, item_phone]
 
}
 
room_flatmate = {
 
    "name" : "Your flatmate's room",
 
    "description":
    """Just before you leave, you notice that your new flatmate has left their door unlocked. You approach their room with caution and realise that no one is in. As you go to close their door, the sunlight glistens through the window and the rays fall upon a new bottle of Jack. You would love to get your hands on that... it's so satisfying to crack the seal on a new bottle.""",
 
    "exits": {"south": "Home"},
 
    "items": [item_jd]
 
}
 
outside_mcdonalds = {
 
    "name" : "McDonalds",
 
    "description":
    """You decided that venturing to McDonalds would be a much more satisfying meal, and that it would give you enough energy to get you through your first day of university! You pull up to the window and roll down your window... A spotty faced teenager with no life goals takes your order. You shudder and think that this could be you if you don't revise hard enough. You make a mental commitment to take shorter lunch breaks in the future.""",
 
    "exits": {"north": "Outside"},
 
    "items": []
 
}

room_labs = { 
    "name": "Computer Labs",
    "description":
    """You have entered the labs and you are immediately welcomed by the sound of humming machines. You take a seat and start up the computer. You are given a sheet which details the activities that you are expected to carry out in order to solidify what you learnt previously in the day. However, you leave feeling more confused than you already were after leaving the lecture!""",
    "exits": {"north": "Hallway"},
    "items": [],
    "swipe": [swipe_machine]
}
 
rooms = {
 
    "Lecturehall": room_lecture,
    "Library": room_library,
    "Hallway": room_hall,
    "Robs": room_robs,
    "Tutor": room_tutor,
    "Canteen": room_canteen,
    "Outside": outside,
    "Home": outside_home,
    "Flatmatesroom": room_flatmate,
    "Mcdonalds": outside_mcdonalds,
    "Labs": room_labs,
 
}