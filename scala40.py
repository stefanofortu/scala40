import numpy as np
from random import shuffle
from random import randint


print "This is a old file"
print "Use pychar project instead"
exit()

n_giocatori=24;
N_PLAYER_EACH_TABLE=4
n_tavoli=n_giocatori/N_PLAYER_EACH_TABLE;

N_TURNI=4

turns=[]
for i in range(0,N_TURNI):
	turns.append(-1 + np.zeros((n_tavoli,N_PLAYER_EACH_TABLE),dtype=int))
listMetPlayers= {};
for i in range(0,n_giocatori):
	listMetPlayers[i]=[];

def printTurn():
	for j in range(0,n_tavoli):
		for i in range(0,N_TURNI):
			print turns[i][j],
		print ""

def printMetPlayers():
	for i in range(0,n_giocatori):
		print str(i),
		print " : ",
		print listMetPlayers[i];

listTavoli=range(0,n_tavoli)

def assignTurn(turn = 0):
	#turns[t]
	#prendi un player in modo casuale
	listPlayer=listMetPlayers.keys()
	shuffle(listPlayer)
	playerToPlace=listPlayer
	for tab in listTavoli:
		table=[-1 for i in range(0,N_PLAYER_EACH_TABLE)]
		placeAtTable=0;
		plIndex=0;
		while (placeAtTable < N_PLAYER_EACH_TABLE ):     #len(playerToPlace!=0 or
			#randint(0, len(playerToPlace))
			p=playerToPlace[plIndex];
			#if the player is not already at the table
			if (not (p in table)):
				#se non ha incontrato nessuno dei giocatori gia seduti al tavolo
				alreadyMetSomeOne=False;
				for pt in table:
					if pt in listMetPlayers[p]:
						alreadyMetSomeOne=True;

				if (alreadyMetSomeOne):
					if plIndex < 4:
						plIndex+=1; #=randint(0, len(playerToPlace))
					else:
						print "Error : plIndex > 4" 
						exit()
				else:
					#aggiungilo al tavolo
					table[placeAtTable]=p
					placeAtTable+=1;
					playerToPlace.remove(p)
					plIndex=0;
					#aggiungi 

		turns[turn][tab]=table;
		for p in table:
			tableEnemies=list(table);
			tableEnemies.remove(p)
			listMetPlayers[p].extend(tableEnemies)


printTurn()
assignTurn(0)
assignTurn(1)
printTurn()

#printMetPlayers()

#table=np.zeros((n_tavoli,N_TURNI*N_PLAYER_EACH_TABLE),dtype=int)

#print table
