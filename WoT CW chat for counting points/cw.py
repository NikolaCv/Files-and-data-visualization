import glob, os
import datetime as dt
import wotlife_scrapper as wot

def processing_the_files(files,delay,picking_time,attendance_dict,battles):
	st = ''
	blank = ' '		#it is not a space, but some special WG blank character

	for filename in files:					#going through all files
		f = open("%s" %filename, "r")		

		datetime_dict = {}					#storing every player's first message date and time 

		battle_starting_time = dt.datetime.strptime(filename,'%d.%m.%y %H.%M.%S.txt')		#files are named 'date time'
		bst = battle_starting_time - dt.timedelta(minutes=battle_starting_time.minute % 10,seconds=battle_starting_time.second)

		if bst not in battles:
			battles.append(bst)

		while True:
			st = f.readline()
			if st == '':
				break
			if '(' not in st:				#avoid all 'player left, joined and transfered' messages
				continue

			i = 0
			name = ''

			while st[i] != blank:					#reading name from the chat
				name = name + (st[i])
				i += 1
			i += 2

			datetime_of_message = dt.datetime.strptime(st[i:i+19],'%d/%m/%Y %H:%M:%S')		#datetime of message from current line
			difference = battle_starting_time - datetime_of_message

			if difference >= dt.timedelta(0) and difference <= picking_time:				 # !!!!		comment this 'if' out if you're using random_data.py (basically just for testing) 	!!!!
				if name not in datetime_dict:											#if it's player's first message add it to dictionary
					datetime_dict[name] = datetime_of_message

				if name in attendance_dict:											#if some players left the clan in the meantime it won't count them
					if bst in attendance_dict[name]:				#if this isn't player's first message
						if datetime_of_message - datetime_dict[name] >= delay and attendance_dict[name][bst] < 1:		#one message = 1 point (spam, or person is late), otherwise 2 points
							attendance_dict[name][bst] += 1	
					else:
						attendance_dict[name][bst] = 0

		for name in attendance_dict:												#filling out players that haven't showed up
			if bst not in attendance_dict[name]:
				attendance_dict[name][bst] = 0

	return attendance_dict, battles

def print_to_txt(f,attendance_dict,battles):
	f.write('\t')
	for battle in battles:
		f.write(battle.strftime("%d/%m/%Y %H:%M:%S"))
		f.write('\t')
	f.write('\n')
	for name in attendance_dict:
		f.write(name)
		f.write('\t')
		for battle in attendance_dict[name]:
			if attendance_dict[name][battle] > 0:
				f.write(str(attendance_dict[name][battle]))
				f.write('\t')
			else:
				f.write('\t')
		f.write('\n')

def main():										#add 'vs [CLAN] in battles.txt'   	#add customizable delay, picking_time, file name delimeters, input and output files, data directory, reading all info from .txt file
	spreadsheet = open('spreadsheet.txt','w')									#points by days, not by battles ?
																				#what should be done if players playing should get more points ?
	os.chdir("data")
																				
	files = [ file for file in glob.glob("*.txt") ]		#getting files from 'data' directory that end in '.txt'

	delay = dt.timedelta(seconds=0)				#delay between 2 messages to count player in as attening, to prevent spam, best delay is 1-2 mins i guess
	picking_time = dt.timedelta(days=1)			#time on counter until the beginning of the battle after which players' messages will be taken into account

	battles = []								#list of dates of battles
	attendance_dict = {}						#database of each player's attendance in CW

	for player in wot.players:					#filling out database with in-game nicknames, real-time action, since it's downloading data from wot-life when program runs
		attendance_dict[player] = {}

	attendance_dict, battles = processing_the_files(files, delay, picking_time, attendance_dict, battles)

	print_to_txt(spreadsheet, attendance_dict, battles)



main()