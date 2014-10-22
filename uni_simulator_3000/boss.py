import random
import time

def your_dam():
	dam = int(energy * 0.07) + int(inteligence * 0.08) + int(social * 0.05) + random.randint(0,5)
	return dam
def player_dam(dam):
	if dam >= 9:
		print ("Woow, you made Matt blush! He lost " + str(dam) + (" patience points\n"))
	elif dam >= 7 and dam < 9:
		print ("You are doing pretty good. - " + str(dam) + " patience for Matt\n")
	elif dam <= 6 and dam >= 4:
		print ("Well that woent well... Matt lost only " + str(dam) + " points of patience\n")
	elif dam < 4 and dam >= 0:
		print ("Today is just not your day. -" + str(dam)+ " \n")
	else:
		print ("  - " + str(dam) + "\n")
def boss_battle():
	your_patience = energy * 0.5 + inteligence * 0.5 + social * 0.5
	if (you give jack to matt):
		matt_patience = 80
	else:
		matt_patience = 100
	while your_patience > 0 and matt_patience > 0:
		matt_dam = random.randint(7,11)
		dam = your_dam()

		if matt_dam == 9:
			your_patience = your_patience - 9
			print ("Matt is being ironic, you lose 9 patience points!")
			matt_patience = matt_patience - dam
			player_dam(dam)
			print ("YOUR   patience: ",your_patience)
			print ("MATTS' patience: ",matt_patience)
			print ("#################################################################################")
		elif matt_dam == 10:
			your_patience = your_patience - 10
			print ("He's giving you a lecture about..you dont even understand, but that's unbearable. -10 patience points")
			matt_patience = matt_patience - dam
			player_dam(dam)
			print ("YOUR   patience: ",your_patience)
			print ("MATTS' patience: ",matt_patience)
			print ("#################################################################################")
		elif matt_dam == 8:
			your_patience = your_patience - 8
			print ("He looks at you furiously! -8 patience points")
			matt_patience = matt_patience - dam
			player_dam(dam)
			print ("YOUR   patience: ",your_patience)
			print ("MATTS' patience: ",matt_patience)
			print ("#################################################################################")
		else:
			your_patience == your_patience - 7
			print ("Matt is shouting at you!  -7 patience")
			matt_patience = matt_patience - dam
			player_dam(dam)
			print ("YOUR   patience: ",your_patience)
			print ("MATTS' patience: ",matt_patience)
			print ("#################################################################################")
		time.sleep(4)
	if matt_patience > your_patience:
		print ("You tried your best to talk yourself out of this, but Matt is just too furiuos..")
		print ("You have been kicked out of the course. GAME OVER")
	else:
		print ("Congratulations, you have succesfuly talked yourself out of this. Matt is no longer angry")	








print ("It's 5pm. Matt is waiting for you in his office. You enter the room to take the final test...\n") 
time.sleep(3)
if inteligence < 100 or energy < 100:
	print ("Looks like you're done. You put your answer sheet on his desk.")
	time.sleep(3)
	print ("Matt checks it and then looks at you with that evil grin on his face - you know it's bad...\n")
	print ("You may still save yourself, you ")
	time.sleep(3)
	boss_battle()
elif False:
	print ("As soon as you walk into the room Matt starts shouting at you! It's about that library test, he knows that you cheated!\n")
	time.sleep(3)
	boss_battle()
else:
	print("Looks like you're done. You put your answer sheet on his desk.")
	time.sleep(3)
	print("Well well, you made the impossible! Matt is actually satisfied with your performance!")
