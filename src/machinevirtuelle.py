#!/usr/bin/python

#@package machine virtuelle
#Machine Virtuelle package. 

import sys, argparse, re
import logging

##################################################################################################

# configurer gedit pour que la touche tab ~ 4 espaces comme recommande ?

##################################################################################################
#### Virtual Machine class
##################################################################################################
class Virtual(object) :

	def __init__(self) :
		self.data = Stack()
		self.program = Tab([])

	def affichage(self) :
		print '\n'
		print 'Partie donnees :'
		print self.data.pile
		print 'ip =', self.data.ip, 'et pile[',self.data.ip,'] =', self.data.pile[self.data.ip]
		print 'Partie programme :'
		print self.program.po
		print 'co =', self.program.co, 'et po[',self.program.co,'] =', self.program.po[self.program.co]

	def decode(self, line):
		fields = line.split(' ')
		if fields[0] == 'debutProg':
			self.debutProg()
		elif fields[0] == 'reserver':
			self.reserver(int(fields[1]))
		elif fields[0] == 'empiler':
			self.empiler(int(fields[1]))
		elif fields[0] == 'empilerAd':
			self.empilerAd(int(fields[1]))
		elif fields[0] == 'affectation':
			self.affectation()
		elif fields[0] == 'valeurPile':
			self.valeurPile()
		elif fields[0] == 'get':
			self.get()
		elif fields[0] == 'put':
			self.put()
		elif fields[0] == 'moins':
			self.moins()
		elif fields[0] == 'sous':
			self.sous()
		elif fields[0] == 'add':
			self.add()
		elif fields[0] == 'mult':
			self.mult()
		elif fields[0] == 'div':
			self.div()
		elif fields[0] == 'egal':
			self.egal()
		elif fields[0] == 'diff':
			self.diff()
		elif fields[0] == 'inf':
			self.inf()
		elif fields[0] == 'infeg':
			self.infeg()
		elif fields[0] == 'sup':
			self.sup()
		elif fields[0] == 'supeg':
			self.supeg()
		elif fields[0] == 'et':
			self.et()
		elif fields[0] == 'ou':
			self.ou()
		elif fields[0] == 'non':
			self.non()
		elif fields[0] == 'tra':
			self.tra(int(fields[1]))
		elif fields[0] == 'tze':
			self.tze(int(fields[1]))
		elif fields[0] == 'erreur' :
			self.erreur()
		elif fields[0] == 'reserverBloc' :
			self.reserverBloc()
		elif fields[0] == 'traStat' :
			self.traStat(int(fields[1]), int(fields[2]))
		elif fields[0] == 'retourFonct' :
			self.retourFonct()
		elif fields[0] == 'retourProc' :
			self.retourProc
		elif fields[0] == 'empilerParam' :
			self.empilerParam(int(fields[1]))


	def debutProg(self) :
		self.program.next()

	#def finProg(self) :

	def reserver(self, n) :
		self.data.reserver(n)
		self.program.next()

	def empiler(self, element) :
		self.data.empiler(element)
		self.program.next()

	#def empilerAd(self, ad) :

	def affectation(self) :
		self.data.affectation()
		self.program.next()

	def valeurPile(self) :
		self.data.valeurPile()
		self.program.next()

	def get(self) :
		self.data.get()
		self.program.next()

	def put(self) :
		self.data.put()
		self.program.next()

	def moins(self) :
		self.data.moins()
		self.program.next()

	def sous(self) :
		self.data.sous()
		self.program.next()

	def add(self) :
		self.data.add()
		self.program.next()

	def mult(self) :
		self.data.mult()
		self.program.next()

	def div(self) :
		self.data.div()
		self.program.next()

	def egal(self) :
		self.data.egal()
		self.program.next()

	def diff(self) :
		self.data.diff()
		self.program.next()

	def inf(self) :
		self.data.inf()
		self.program.next()

	def infeg(self) :
		self.data.infeg()
		self.program.next()

	def sup(self) :
		self.data.sup()
		self.program.next()

	def supeg(self) :
		self.data.supeg()
		self.program.next()

	def et(self) :
		self.data.et()
		self.program.next()

	def ou(self) :
		self.data.ou()
		self.program.next()

	def non(self) :
		self.data.non()
		self.program.next()

	def tra(self, ad) :
		self.program.branch(ad)

	def tze(self, ad) :
		if self.data.element() :
			self.program.next()
		else :
			self.program.branch(ad)
		self.data.depiler()

	def erreur(self) :
		print 'erreur\n'
		#self.data.finProg()

	def reserverBloc(self) :
		self.data.reserverBloc()
		self.program.next()

	#def traStat(self, a, nbp) :

	def retourFonct(self) :
		self.data.retourFonct()
		self.program.next()

	def retourProc(self) :
		self.data.retourProc()
		self.program.next()

	def empilerParam(self, ad) :
		self.data.empilerParam(ad)
		self.program.next()



##################################################################################################
#### Execute Stack class
##################################################################################################
class Stack(object) :
#mettre des attributs de base ici et ensuite faire un constructeur avec parametres !

	#constructeur
	def __init__(self):
		self.pile = [0,0]
		self.ip = 1
		self.base = 0

	def reserver(self, n) :
		for i in range(0, n) :
			self.empiler(None)

	def empiler(self, element):
		self.ip += 1
		self.pile.append(element)

	def depiler(self) :
		self.pile.pop()
		self.ip -= 1

	#lecture d'un element a l'indice donne (si pas d'indice, lecture de l'element au sommet).
	def element(self, index = -1) :
		return self.pile[index]

	#def empilerAd(self, ad) :

	def affectation(self) :
		self.pile[self.element(self.ip - 1)] = self.pile[self.ip]
		self.depiler()
		self.depiler()

	def valeurPile(self) :
		self.pile[self.ip] = self.pile[self.element()]

	def get(self) :
		self.pile[self.element(self.ip)] = input()
		self.depiler()

	def put(self) :
		print self.element()
		self.depiler()

	def moins(self) :
		self.pile[self.ip] = -self.pile[self.ip]

	def sous(self) :
		self.pile[self.ip - 1] = (self.element(self.ip - 1) - self.element())
		self.depiler()

	def add(self) :
		self.pile[self.ip - 1] = (self.element(self.ip - 1) + self.element())
		self.depiler()

	def mult(self) :
		self.pile[self.ip - 1] = (self.element(self.ip - 1) * self.element())
		self.depiler()

	def div(self) :
		self.pile[self.ip - 1] = (self.element(self.ip - 1) / self.element())
		self.depiler()

	def egal(self) :
		self.pile[self.ip - 1] = int(self.element(self.ip - 1) == self.element())
		self.depiler()

	def diff(self) :
		self.pile[self.ip - 1] = int(self.element(self.ip - 1) != self.element())
		self.depiler()

	def inf(self) :
		self.pile[self.ip - 1] = int(self.element(self.ip - 1) < self.element())
		self.depiler()

	def infeg(self) :
		self.pile[self.ip - 1] = int(self.element(self.ip - 1) <= self.element())
		self.depiler()

	def sup(self) :
		self.pile[self.ip - 1] = int(self.element(self.ip - 1) > self.element())
		self.depiler()

	def supeg(self) :
		self.pile[self.ip - 1] = int(self.element(self.ip - 1) >= self.element())
		self.depiler()

	def et(self) :
		self.pile[self.ip - 1] = int(self.element(self.ip - 1) and self.element())
		self.depiler()

	def ou(self) :
		self.pile[self.ip - 1] = int(self.element(self.ip - 1) or self.element())
		self.depiler()

	def non(self) :
		self.pile[self.ip] = int(not(self.pile[self.ip]))

	#def reserverBloc(self) :

	#def traStat(self, a, nbp) :

	#def retourFonct(self) :

	#def retourProc(self) :

	def empilerParam(self, ad) :
		self.empiler(self.pile[self.base + 2 + ad])


##################################################################################################
#### Tab class
##################################################################################################
class Tab(object) :

	#constructeur
	def __init__(self, tab):
		self.po = []
		self.co = 0

	def next(self) :
		self.co += 1

	def branch(self, ad) :
		self.co = ad


##################################################################################################
#### main
##################################################################################################
def main() :
	
	f = None
	try:
		f = open('exemple.txt', 'r')
	except:
		print "Error: can\'t open input file!"
		return
		
	text = f.read()
	test = Virtual()
	test.program.po = text.split("\n")
	line = test.program.po[test.program.co]
		
	while(line.rstrip('\r\n') != 'finProg'):
		line = line.rstrip('\r\n')
		test.decode(line)
		test.affichage()
		line = test.program.po[test.program.co]
		
	f.close()

##################################################################################################

if __name__ == "__main__":
	main()


