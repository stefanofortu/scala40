#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QPrinter>
#include <QtWidgets>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    //ui->;
}

int MainWindow::writeToPdf()
{
    QPrinter printer(QPrinter::PrinterResolution);
    printer.setOutputFormat(QPrinter::PdfFormat);
    printer.setPageMargins(5, 5, 5, 5, QPrinter::Millimeter);
    printer.setPaperSize(QPrinter::A4);
    printer.setOutputFileName("../test3.pdf");

    QPainter painter;
    painter.begin(&printer);

    double xscale = (printer.pageRect().width()*(double)1.0/2.0)/double(ui->centralWidget->width());
    double yscale = (printer.pageRect().height()*(double)6.0/20.0)/double(ui->centralWidget->height());


    //double xscale = (printer.pageRect().width()/2)/double(ui->centralWidget->width());
    //double yscale = (printer.pageRect().height()/3)/double(ui->centralWidget->height());
    //double scale = qMin(xscale, yscale);
    //painter.translate(printer.paperRect().x() + printer.pageRect().width()/2,
    //                  printer.paperRect().y() + printer.pageRect().height()/2);
    painter.scale(xscale, yscale);
    //painter.translate(-ui->centralWidget->width()/2, -ui->centralWidget->height()/2);
    QRect printerRect = printer.pageRect();
    QRect painterRect = painter.window();

    painter.translate(QPointF (0,printer.pageRect().height()*0/20.0));
    //painterRect = painter.window();
    ui->centralWidget->render(&painter);

    //painter.translate(QPointF (printer.pageRect().width()*3.0/2.0,0));
    //painterRect = painter.window();
    //ui->centralWidget->render(&painter);

    //painter.translate(QPointF (0,printer.pageRect().height()*.0/20.0));
    //ui->centralWidget->render(&painter);
//    painter.translate(QPointF (printer.pageRect().width()*3/2,0));
//    ui->centralWidget->render(&painter);

//    painter.translate(QPointF (0, printer.pageRect().height()*6.0/18));
//    ui->centralWidget->render(&painter);
    //painter.translate(QPointF (printer.pageRect().width()*3/2,0));
    //ui->centralWidget->render(&painter);
    return 0;
}

MainWindow::~MainWindow()
{
    delete ui;
}


