import numpy as np
from random import shuffle
from random import randint

n_giocatori = 48
# Quando il numero di giocatori e' tale da creare un tavolo da 3,fai finta di nulla.
# calcola tutto con un giocatore in piu', come al solito, ma non stamparlo
tavoloZoppo=True;
#
N_PLAYER_EACH_TABLE = 4
n_tavoli = n_giocatori / N_PLAYER_EACH_TABLE;

N_TURNI = 4

turns = []
for i in range(0, N_TURNI):
    turns.append(-1 + np.zeros((n_tavoli, N_PLAYER_EACH_TABLE), dtype=int))
listMetPlayers = {};
for i in range(0, n_giocatori):
    listMetPlayers[i] = [];


def printTurn():
    for j in range(0, n_tavoli):
        for i in range(0, N_TURNI):
            print turns[i][j],
        print ""


def printMetPlayers():
    for i in range(0, n_giocatori):
        print str(i),
        print " : ",
        print listMetPlayers[i];


listTavoli = range(0, n_tavoli)



def assignTable(turn,listPlayer, verbose=False):
    playerToPlace=list(listPlayer)
    for tab in listTavoli:
        table = [-1 for i in range(0, N_PLAYER_EACH_TABLE)]
        placeAtTable = 0;
        plIndex = 0;
        while (placeAtTable < N_PLAYER_EACH_TABLE and len(playerToPlace) != 0):  # len(playerToPlace!=0 or
            # randint(0, len(playerToPlace))
            if (plIndex < len(playerToPlace)):
                p = playerToPlace[plIndex];
            else:
                return False;
            # if the player is not already at the table
            if (not (p in table)):
                # se non ha incontrato nessuno dei giocatori gia seduti al tavolo
                alreadyMetSomeOne = False;
                for pt in table:
                    if pt in listMetPlayers[p]:
                        alreadyMetSomeOne = True;

                if (alreadyMetSomeOne):
                    if plIndex < 4:
                        plIndex += 1;  # =randint(0, len(playerToPlace))
                    else:
                        if verbose:
                            print "Error : plIndex > 4"
                        return False
                else:
                    # aggiungilo al tavolo
                    table[placeAtTable] = p
                    placeAtTable += 1;
                    playerToPlace.remove(p)
                    plIndex = 0;
                    # aggiungi
        if verbose:
            print "Tavolo " + str(tab)  + " completato"
        turns[turn][tab] = table;
    return True;

def assignTurn(turn=0,verbose=False):
    # turns[t]
    # prendi un player in modo casuale
    stop=False;
    while (not stop):
        listPlayer = listMetPlayers.keys()
        shuffle(listPlayer)
        if verbose:
            print "Turno " + str(turn) + " iniziato"
        stop = assignTable(turn,listPlayer,verbose)
        if verbose:
            print "Turno " + str(turn) + " finito"

    #aggiorna la lista dei partecipanti incontrati
    for table in turns[turn]:
        for p in table:
            tableEnemies = list(table);
            tableEnemies.remove(p)
            listMetPlayers[p].extend(tableEnemies)

verbose=False
assignTurn(0,verbose)
printTurn()
#printMetPlayers()

assignTurn(1,verbose)
printTurn()
#printMetPlayers()
assignTurn(2)
printTurn()
# printMetPlayers()
assignTurn(3)
printTurn()

TOKEN_ZOPPO="-1"
def printCSV():
    for p in range(0,n_giocatori):
        csvString = ""
        if not tavoloZoppo:
            csvString += str(n_giocatori) + ";"
        else:
            csvString += str(n_giocatori-1) + ";"
        if tavoloZoppo and p+1==n_giocatori:
            csvString += TOKEN_ZOPPO + ";"
        else:
            csvString += str(p + 1) + ";"
        for turnIndex,turn in enumerate(turns):
            csvString += str(turnIndex + 1) + ";"
            for tabIndex, table in enumerate(turn):
                if p in table:
                    csvString += str(tabIndex+1) + ";"
                    for pl in table:
                        if tavoloZoppo and pl+1 == n_giocatori:
                            csvString += TOKEN_ZOPPO + ";"
                        else:
                            csvString += str(pl + 1) + ";"
        print csvString

def printCSVTable():
    csvString = ""
    for num in range(0,26):
        csvString += "-" + ";"
    print csvString
    #se non zoppo, stampa di nuovo
    if not tavoloZoppo:
        print csvString
    for tab in range(0,n_tavoli):
        csvString = ""
        csvString += "-" + ";"
        csvString += "-" + ";"
        for turnNum,turn in enumerate(turns):
            csvString += str(turnNum+ 1) + ";"
            csvString += str(tab+1) + ";"
            #csvString += str(tab)+ ";",
            for pl in turn[tab,:]:
                if tavoloZoppo and pl + 1 == n_giocatori:
                    csvString += TOKEN_ZOPPO + ";"
                else:
                    csvString += str(pl + 1) + ";"
        print csvString;
        #print turns[t];
        # csvString = ""
        # csvString += "-" + ";"
        # csvString += "-";
        # for pl in table:
        #     csvString += str(pl + 1) + ";"
        # print csvString
    # for j in range(0, n_tavoli):
    #     for i in range(0, N_TURNI):
    #         print turns[i][j],
    #     print ""
    #
    # for turnIndex,turn in enumerate(turns):
    #     csvString += str(turnIndex + 1) + ";"
    #     for tabIndex, table in enumerate(turn):
    #         if p in table:
    #             csvString += str(tabIndex+1) + ";"
    #             for pl in table:
    #                 csvString += str(pl+1) + ";"


#print turns
printCSV()
printCSVTable()

#printMetPlayers()
# printTurn()
# printMetPlayers()
# table=np.zeros((n_tavoli,N_TURNI*N_PLAYER_EACH_TABLE),dtype=int)
# print table
