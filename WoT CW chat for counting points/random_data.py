import random
import wotlife_scrapper as wot
import os

os.chdir("data")

random.seed(a=None)

l = []
i = 0
while i < 150:
	day = random.randint(1,31)
	month = 1
	year = 19
	s = str(day) + '.' + str(month) + '.' + str(year)
	hour = random.randint(18,23)
	t = random.randint(0,3)
	if t == 0:
		minute = random.randint(0,5)
	elif t == 1:
		minute = random.randint(15,20)
	elif t == 2:
		minute = random.randint(30,35)
	else:
		minute = random.randint(45,50)
	second = random.randint(0,59)
	r = str(hour) + '.' + str(minute) + '.' + str(second)
	if r not in l:
		l.append(r)
		f = open('%s %s.txt' %(s,r),'w')
		
		j = 0
		random_player_list = []
		m = minute
		while j < 33:
			rand_index = random.randint(0,len(wot.players)-1)
			if wot.players[rand_index] not in random_player_list:
				random_player_list.append(wot.players[rand_index])
			j += 1

		j = 0

		while j < 150:
			rand_index = random.randint(0,len(random_player_list)-1)
			hourp = hour
			minute = random.randint(m-15,m)
			if minute < 0:
				hourp -= 1
				minute += 60
			second = random.randint(0,59)
			if minute < 10:
				minute_s = '0' + str(minute)
			else:
				minute_s = str(minute)
			if second < 10:
				second_s = '0' + str(second)
			else:
				second_s = str(second)
			if day < 10:
				day_s = '0' + str(day)
			else:
				day_s = str(day)

			r = str(hour) + ':' + minute_s + ':' + second_s
			blank = ' '
			f.write('%s%s(%s/01/2019 %s) sample message\n' %(random_player_list[rand_index],blank,day_s,r))				#blank is not a space, but some special WG blank character
			j += 1


		i += 1
		
