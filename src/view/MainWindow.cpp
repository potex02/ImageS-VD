/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include "MainWindow.h"

view::MainWindow::MainWindow() {}
void view::MainWindow::addWidgets() {

    Gtk::Box *box = Gtk::make_managed<Gtk::Box>(Gtk::ORIENTATION_VERTICAL);
    Gtk::Box *scrolledBox = Gtk::make_managed<Gtk::Box>(Gtk::ORIENTATION_VERTICAL);
    Gtk::ScrolledWindow *scrolledWindow = Gtk::make_managed<Gtk::ScrolledWindow>();
    Gtk::MenuBar* menubar = this->createMenuBar();
    Gtk::Toolbar* toolbar = this->createToolBar();

    this->createNotebook();
    this->set_title("ImageS-VD");
    this->set_default_size(500, 500);
    scrolledWindow->set_policy(Gtk::POLICY_AUTOMATIC, Gtk::POLICY_AUTOMATIC);
    scrolledBox->pack_start(*toolbar, Gtk::PACK_SHRINK);
    scrolledBox->pack_start(*this->notebook);
    scrolledWindow->add(*scrolledBox);
    box->pack_start(*menubar, Gtk::PACK_SHRINK);
    box->pack_start(*scrolledWindow);
    this->add(*box);
    this->show_all();

}
Gtk::MenuBar* view::MainWindow::createMenuBar() {

    Gtk::MenuBar *menubar = Gtk::make_managed<Gtk::MenuBar>();
    Gtk::Menu *file = Gtk::make_managed<Gtk::Menu>();
    Gtk::Menu *imageSvd = Gtk::make_managed<Gtk::Menu>();
    Gtk::MenuItem *fileMenu = Gtk::make_managed<Gtk::MenuItem>("file");
    Gtk::MenuItem *imageSvdMenu = Gtk::make_managed<Gtk::MenuItem>("ImageS-VD");
    Gtk::MenuItem *about = Gtk::make_managed<Gtk::MenuItem>("About");
    Gtk::MenuItem *open = Gtk::make_managed<Gtk::MenuItem>("Open");

    fileMenu->set_submenu(*file);
    file->append(*open);
    imageSvdMenu->set_submenu(*imageSvd);
    imageSvd->append(*about);
    menubar->append(*fileMenu);
    menubar->append(*imageSvdMenu);
    open->signal_activate().connect([&]() {
        std::cout << "Open" << std::endl;
    });
    about->signal_activate().connect([&]() {
        std::cout << "About" << std::endl;
    });
    return menubar;
}
Gtk::Toolbar* view::MainWindow::createToolBar() {

    Gtk::Toolbar *toolbar = Gtk::make_managed<Gtk::Toolbar>();
    Gtk::ToolButton *button = Gtk::make_managed<Gtk::ToolButton>(Gtk::Stock::OPEN);

    button->signal_clicked().connect([&]() {
        std::cout << "Open toolbar" << std::endl;
    });
    toolbar->append(*button);
    return toolbar;

}
void view::MainWindow::createNotebook() {

    MainPanel *panel= Gtk::make_managed<MainPanel>();

    this->notebook = Gtk::make_managed<Gtk::Notebook>();
    this->notebook->append_page(*panel, "Page 1");

}
