#include "mainwindow.h"
#include <QApplication>
#include <QPrinter>
//#include <QTextDocument>
//#include <QFileDialog>
#include <QtWidgets>
#include <iostream>

class Giocatore{
    std::string name1;
    std::string name2;
public: Giocatore(){
    playerId=0;
    }
unsigned int playerId;

};


class Table{
public :
    std::vector<Giocatore> players;
    unsigned int id;
    Table(int i, int numeroPlayerTavolo){
        id =i;
        for (int k=0;k<numeroPlayerTavolo; k++){
            players.push_back(Giocatore());
        }
    }
};

class Game{
    unsigned int turn;
public:
    std::vector<Table> tables;
    Game(unsigned int i)
    {
        turn=i;
    }

};

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    unsigned int numPlayer = 24;
    unsigned int numeroPlayerTavolo = 4;
    unsigned int numeroTavoli = numPlayer/numeroPlayerTavolo;
    unsigned int numeroGames=4;

    std::vector<Game> games;
    for (unsigned int j=0; j< numeroGames; j++)
        games.push_back(Game(j));

    for (unsigned int i=0; i < games.size(); i++){
        for (unsigned int j=0; j< numeroTavoli; j++)
            games[i].tables.push_back(Table(j,numeroPlayerTavolo));
    }

    for (unsigned int k=1;k< numPlayer;k++)
    {
        //Giocatore g= Giocatore(j);

        unsigned int factor = (k % numeroPlayerTavolo)+1;
        //inizializza tavolo zero
        games[0].tables[k/4].players[factor-1].playerId=k;
        games[1].tables[(k/4 + factor)%6].players[factor-1].playerId=k;
        games[2].tables[(k/4 + 2*factor)%6].players[factor-1].playerId=k;
        games[3].tables[(k/4 + 3*factor)%6].players[factor-1].playerId=k;
    }

    std::vector<std::vector<int> > playerIncontrati;
    for (unsigned int k=0;k< 1;k++){
        for (unsigned int i=0;i< numeroGames;i++){
            for (unsigned int j=0; j< numeroTavoli; j++){
                for (unsigned int z =0 ;z < numeroPlayerTavolo ; z++)
                {
                    if (games[i].tables[j].players[z].playerId==k)
                    {
                        std::vector<int> player;
                        for (unsigned int l =0 ;l < numeroPlayerTavolo ; l++)
                        {
                            if (games[i].tables[j].players[l].playerId!=k)
                                player.push_back(games[i].tables[j].players[l].playerId);
                        }
                        playerIncontrati.push_back(player);
                        break;

                    }
                }
            }
        }
    }


    for (unsigned int j=0; j< numeroTavoli; j++){
        std::cout << "table " << j << " : ";
        for (unsigned int i=0; i < games.size(); i++){
            for (unsigned int k=0; k < numeroPlayerTavolo; k++){
            std::cout << games[i].tables[j].players[k].playerId << " ";
            //std::cout << games[i].tables[j].player2.playerId << " ";
            //std::cout << games[i].tables[j].player3.playerId << " ";
            //std::cout << games[i].tables[j].player4.playerId << " ";
           }
           std::cout << "-->";
        }
        std::cout << std::endl;
    }

    //QString filename = QFileDialog::getOpenFileName();

//    QFile file("../table.html");
//     if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
//         return -1;

//    QString content = file.readAll();

//    file.close();
//    //QTextStream(stdout) << content;
//    //qDebug() << content;

//    QString html = "<h2>Hi!</h2>";

//    QTextDocument document;
//    document.setHtml(content);

    QPrinter printer(QPrinter::PrinterResolution);
    printer.setOutputFormat(QPrinter::PdfFormat);
    printer.setOutputFileName("../test3.pdf");

    //document.print(&printer);
    MainWindow w;
    w.show();
    w.writeToPdf();

    return a.exec();
}
