/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#pragma once
#include <gtkmm/window.h>
#include "MainWindow.h"

namespace view { class MainWindow; }

/**
 * Contains classes related to the application's control following the MVC architecture.
 *
 * @ref controller::MenuController: Contains the actions for the menu of the application.
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
        private:
            /**
             * The pointer to the main window of the application.
             */
            view::MainWindow *window;

    };

}
