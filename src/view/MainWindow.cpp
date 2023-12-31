/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include "MainWindow.h"

view::MainWindow::MainWindow() {}
view::MainWindow::~MainWindow() {

    for(Gtk::Widget *i: this->widgets) {

        delete i;

    }

}
void view::MainWindow::run(Glib::RefPtr<Gtk::Application> &app) {

    Gtk::Box vbox(Gtk::ORIENTATION_VERTICAL);
    Gtk::MenuBar menubar = this->createMenuBar();
    this->set_title("ImageS-VD");
    this->set_default_size(500, 500);
    vbox.pack_start(menubar, Gtk::PACK_SHRINK);
    this->add(vbox);
    this->show_all();
    app->run(*this);

}
Gtk::MenuBar view::MainWindow::createMenuBar() {

    Gtk::MenuBar menubar;
    Gtk::Menu *file = new Gtk::Menu();
    Gtk::Menu *imageSvd = new Gtk::Menu();
    Gtk::MenuItem *fileMenu = new Gtk::MenuItem("File");
    Gtk::MenuItem *imageSvdMenu = new Gtk::MenuItem("ImageS-VD");
    Gtk::MenuItem *open = new Gtk::MenuItem("Open");
    Gtk::MenuItem *about = new Gtk::MenuItem("About");

    fileMenu->set_submenu(*file);
    file->append(*open);
    imageSvdMenu->set_submenu(*imageSvd);
    imageSvd->append(*about);
    menubar.append(*fileMenu);
    menubar.append(*imageSvdMenu);
    open->signal_activate().connect([&]() {
        std::cout << "Open" << std::endl;
    });
    about->signal_activate().connect([&]() {
        std::cout << "About" << std::endl;
    });
    this->widgets.emplace_back(file);
    this->widgets.emplace_back(imageSvd);
    this->widgets.emplace_back(fileMenu);
    this->widgets.emplace_back(imageSvdMenu);
    this->widgets.emplace_back(open);
    this->widgets.emplace_back(about);
    return menubar;

}
