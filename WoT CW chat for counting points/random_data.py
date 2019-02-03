import random
import wotlife_scrapper as wot
import os

os.chdir("C:\\Users\\Nikola\\Desktop\\python\\CW\\data")

s = '2.2.19. '

random.seed(a=None)

l = []
i = 0
while i < 300:
	hour = random.randint(18,23)
	minute = random.randint(0,59)
	second = random.randint(0,59)
	r = str(hour) + '.' + str(minute) + '.' + str(second)
	if r not in l:
		l.append(r)
		f = open('%s%s.txt' %(s,r),'w')
		
		j = 0
		random_player_list = []

		while j < 34:
			rand_index = random.randint(0,len(wot.players)-1)
			if wot.players[rand_index] not in random_player_list:
				random_player_list.append(wot.players[rand_index])
			j += 1

		j = 0

		while j < 500:
			rand_index = random.randint(0,len(random_player_list)-1)
			hour = random.randint(18,23)
			minute = random.randint(0,59)
			second = random.randint(0,59)
			if minute < 10:
				minute_s = '0' + str(minute)
			else:
				minute_s = str(minute)
			if second < 10:
				second_s = '0' + str(second)
			else:
				second_s = str(second)
			r = str(hour) + ':' + minute_s + ':' + second_s
			blank = ' '
			f.write('%s%s(02/02/2019 %s) sample message\n' %(random_player_list[rand_index],blank,r))				#blank is not a space, but some special WG blank character
			j += 1


		i += 1
		
