/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#pragma once
#include <unordered_map>
#include <functional>
#include <gtkmm/stock.h>
#include "MainWindow.h"
#include "Action.h"

namespace view { class MainWindow; }

/**
 * Contains classes related to the application's control following the MVC architecture.
 *
 * @ref control::MenuController: Contains the actions for the menu of the application.
 * @ref control::Action Contains the code to execute one action in the app and manage the widget's behaviour.
 */
namespace control {

    /**
     * Contains the actions for the menu of the application.
     */
    class MenuController {

        public:
            /**
             * Create a MenuController.
             *
             * @param _window is the pointer to the window of the application.
             */
            MenuController(view::MainWindow *_window);
            /**
             * Register a widget to an action.
             *
             * @param action is the string that identifies the action.
             * @param widget is the widget to be registered.
             */
            void registerWidget(const std::string action, Gtk::Widget *widget);
        private:
            /**
             * The pointer to the main window of the application.
             */
            view::MainWindow *window;
            /**
             * A map containing the actions of the menu.
             */
            std::unordered_map<std::string, Action> actions;

    };

}
