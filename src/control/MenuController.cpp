/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include "MenuController.h"

control::MenuController::MenuController(view::MainWindow *_window): window(_window) {

    this->actions.emplace("open", Action([]() {

        std::cout << "Open" << std::endl;

    }, "Open", "Open a file", Gtk::Stock::OPEN));

}
void control::MenuController::registerWidget(const std::string action, Gtk::Widget *widget) {

    this->actions.at(action).registerWidget(widget);

}
