from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

class student():
	def __init__(self, ime, prezime, ind, prolaz):
		self.ime = ime
		self.prezime = prezime
		self.ind = ind
		self.prolaz = prolaz

def obrada(str):
	i = 0
	s = student('', '', '', 0)
	if str[0].isdigit():
		while str[i] != '\t':
			i +=1
		i += 1
		
		while str[i] != '\t':
			s.ind += str[i]
			i += 1
		i += 1
			
		while str[i] != ' ':
			s.prezime += str[i]
			i += 1
		i += 1
	
		while str[i] != '\t':
			s.ime += str[i]
			i += 1
		i += 1
					
		if str[i] == '5':
			s.prolaz = 0;
		elif str[i] != 'N':
			s.prolaz = 1
		else:
			s.prolaz = 2
	return s.ime, s.prezime, s.ind, s.prolaz

def stats(l):
	s = [0,0,0]
	for i in l:
		if i[3] == 1:
			s[1] += 1
		elif i[3] == 0:
			s[0] += 1
		else:
			s[2] += 1
	return s

def graph(s):
	x = [1,3,5]

	s[0] -= 1

	s1 = str(s[0]) + ' - ' + str(round(s[0]/(sum(s))*100,2)) + '%'
	s2 = str(s[1]) + ' - ' + str(round(s[1]/(sum(s))*100,2)) + '%'
	s3 = str(s[2]) + ' - ' + str(round(s[2]/(sum(s))*100,2)) + '%'

	t = [s3,s1,s2]

	s0 = [s[2], s[0], s[1]]

#	plt.bar(x, y)
	plt.figure(1, figsize=(10, 5))
#	plt.plot(x, y, 'ro', x, y, 'k', linewidth = 2.0)
	plt.bar(x, s0, width = 1, align = 'center')
#	plt.ylabel('Broj Studenata')
#	plt.xlabel('Rezultat')
	plt.grid(True)
	plt.xticks(ticks = x, labels = ['Prijavilo, a nije izaslo', 'Palo', 'Usmeni'])
	plt.yticks(ticks = s0, labels = t)
	plt.axis([0, 6, 0, max(s)+50])
	plt.title('Ispit iz OET-a: Januar 2019')
	plt.show()


def main():
	l = []
	s = student('', '', '', 0)

	f = open("ispit.txt","r")
	p = open("ispitsort.txt","w")
	stat = open("ispitstats.txt","w")
	
	i = 0
	while True:
		st = f.readline()
		if st == '':
			break

		s.ime, s.prezime, s.ind, s.prolaz = obrada(st)

		if [s.ind, s.ime, s.prezime, s.prolaz] not in l:
			l += [[s.ind, s.ime, s.prezime, s.prolaz]]
			i +=1
	#	print(l,i)

	l = sorted(l, key = itemgetter(0))
	l = sorted(l, key = itemgetter(3), reverse = True)

#	l.sort(key = lambda x: (x[3], -x[0]))
#	l.reverse()

	s = stats(l)
	i = 0
	c = ''
	
	for i in l:
		for j in i:
			p.write("%15s" %str(j))
		p.write("\n")
	
	graph(s)

	stat.write("True:\t%d\n" %s[1])
	stat.write("False:\t%d" %s[0])

	print(sum(s))

	f.close()
	p.close()
	stat.close()

main()