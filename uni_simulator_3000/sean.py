def what_time_to_wake_up():
	print ("")
	print ("")
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

hours_in_day = what_time_to_wake_up()
print (hours_in_day)