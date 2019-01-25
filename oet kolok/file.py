from operator import itemgetter
import matplotlib.pyplot as plt


class student():
	def __init__(self, ime, prezime, ind, poeni, izasao):
		self.ime = ime
		self.prezime = prezime
		self.ind = ind
		self.poeni = poeni
		self.izasao = izasao

f = open("OET.txt","r")
p = open("sort.txt","w")
stat = open("stats.txt","w")

def obrada(str):
	i = 0
	s = student('', '', '', 0, False)
	if str[0] != 'S' and i < len(str):
		while str[i] != ' ':
			i +=1
		i += 1
		
		while str[i] != ' ':
			s.ind += str[i]
			i += 1
		i += 1
			
		while str[i] != ' ':
			s.prezime += str[i]
			i += 1
		i += 1
	
		while str[i] != ' ':
			s.ime += str[i]
			i += 1
		i += 1
					
		poeni = ''
		while not poeni.isdigit():
			poeni = ''
			while str[i] != ' ' and str[i] != '\n' and i < len(str):
				poeni += str[i]
				i += 1
			poeni.replace(' ','')
			i += 1

		s.poeni = int(poeni)/2

		if i == len(str) or i > len(str):
			s.izasao = False
		else:
			s.izasao = True
	return s.ime, s.prezime, s.ind, s.poeni, s.izasao

def stats(l,max,min,period):
	ml = max - period
	md = max
	i = 0
	a = max
	j = 0
	hist = []
	indL = 0
	indD = 0
	s = []
	count = 0
	while md > min:
		while l[i][3] > ml:
			i += 1
			hist.append(l[i][3])
		indD = i

		for k in range(indL,indD):
			count += 1

	#	print(l[i])
		s.append(count)
		count = 0
		j += 1
		indL = indD
		md -= period
		ml -= period
	while i < len(l):
		count += 1
		i += 1
	s.append(count)
	return s, hist

def graph(s,hist,period):
	x = []
	y = []
	j = 0
	while j <= 30/period:
		x.append( j * period )
		y.append(s[int(30/period)-j])
		j += 1
	print(s)
	i = 0
	tx = ty = []
	while i <= 30:
		tx.append(i)
		i += period
	ty = [x * 10 for x in range(1,11)]

	m = int (30 / period)

	t = [x * period for x in range(0,m+2)]

#	plt.bar(x, y)
	plt.figure(1, figsize=(15, 5))
#	plt.plot(x, y, 'ro', x, y, 'k', linewidth = 2.0)
	plt.subplot(121)
	plt.bar(x, y, width = - (period - 0.5), align = 'edge')
	plt.ylabel('Broj Studenata')
	plt.xlabel('Broj Bodova')
	plt.grid(True)
	plt.xticks(ticks = tx, labels=None)
	plt.yticks(ticks = ty, labels=None)
	plt.axis([-5, 35, 0, max(s)+5])
#	plt.show()

	plt.subplot(122)
	plt.hist(hist, t, width = period-0.5, align = 'mid', color = 'r')
	plt.ylabel('Broj Studenata')
	plt.xlabel('Broj Bodova')
	plt.grid(True)
	plt.xticks(ticks = tx, labels=None)
	plt.yticks(ticks = ty, labels=None)
	plt.axis([-5, 35, 0, max(s)+5])
	plt.show()

def main():
	l = []
	s = student('', '', '', 0, False)

	i = 0
	while True:
		st = f.readline()
		if st == '':
			break

		s.ime, s.prezime, s.ind, s.poeni, s.izasao = obrada(st)

		if s.izasao and [s.ind, s.ime, s.prezime, s.poeni] not in l:
			l += [[s.ind, s.ime, s.prezime, s.poeni]]
			i +=1
	#	print(l,i)

	l = sorted(l, key = itemgetter(0))
	l = sorted(l, key = itemgetter(3), reverse = True)

#	l.sort(key = lambda x: (x[3], -x[0]))
#	l.reverse()

	for i in l:
		for j in i:
			p.write('%15s' %str(j))
		p.write('\n')

	max = 30.0
	min = 0.0
	period = 2.5

	s, hist = stats(l,max,min,period)
	i = 0
	c = ''
	while i < len(s)-1:
		if max - i * period < 10 and max - ( i + 1 ) * period < 10:
			c = '  '
		elif max - ( i + 1 ) * period < 10:
			c = ' '
		else:
			c = ''
		stat.write('(%.1f,%.1f] %s-- %d -- %5.2f %%\n' %( max - ( i + 1 ) * period, max - i * period, c, s[i], s[i]/len(l)*100))
		i += 1
	stat.write('0.0         -- %d -- %5.2f %%' %(s[i], s[i]/len(l)*100))
	
	print(len(l))
	print(sum(s))

	graph(s,hist,period)

	f.close()
	p.close()
	stat.close()

main()