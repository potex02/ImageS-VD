/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include "MenuController.h"

control::MenuController::MenuController(view::MainWindow *_window): window(_window) {

    this->actions["open"] = []() {

        std::cout << "Open" << std::endl;

    };

}
std::function<void()> control::MenuController::getAction(std::string action) const {

    return this->actions.at(action);

}
