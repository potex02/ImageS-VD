/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include "MainWindow.h"

view::MainWindow::MainWindow() {}
void view::MainWindow::run(Glib::RefPtr<Gtk::Application> &app) {

    Gtk::Box vbox(Gtk::ORIENTATION_VERTICAL);
    Gtk::MenuBar* menubar = this->createMenuBar();
    Gtk::Notebook* notebook = this->createNotebook();

    this->set_title("ImageS-VD");
    this->set_default_size(500, 500);
    vbox.pack_start(*menubar, Gtk::PACK_SHRINK);
    vbox.pack_start(*notebook);
    this->add(vbox);
    this->show_all();
    app->run(*this);

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
Gtk::Notebook* view::MainWindow::createNotebook() {

    Gtk::Notebook* notebook = Gtk::make_managed<Gtk::Notebook>();
    Gtk::Label* label = Gtk::make_managed<Gtk::Label>("ImageS-VD");

    notebook->append_page(*label, "Page 1");
    return notebook;

}
