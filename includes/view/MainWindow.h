/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#pragma once
#include <iostream>
#include <memory>
#include <gtkmm/window.h>
#include <gtkmm/box.h>
#include <gtkmm/scrolledwindow.h>
#include <gtkmm/menubar.h>
#include <gtkmm/menu.h>
#include <gtkmm/menuitem.h>
#include <gtkmm/toolbar.h>
#include <gtkmm/toolbutton.h>
#include <gtkmm/stock.h>
#include <gtkmm/notebook.h>
#include "MainPanel.h"
#include "MenuController.h"

namespace control { class MenuController; }

/**
 * Contains classes related to the application's gui following the MVC architecture.
 *
 * Classes:
 *   - @ref view::MainWindow: The main window of the application.
 */
namespace view {

    /**
     * The main window of the application.
     */
    class MainWindow : public Gtk::Window {

        public:
            /**
             * Create a MainWindow used as the main window by the application.
             */
            MainWindow();
            /**
             * Add the widgets to the window.
             */
            void addWidgets();
        private:
            /**
             * The controller of the application's menu.
             */
            std::shared_ptr<control::MenuController> menuController;
            /**
             * The main notebook of the window whxich contains all the panels.
             */
            Gtk::Notebook *notebook;
            /**
             * Create the menubar of the window.
             *
             * @return The menubar that is added to the window.
             */
            Gtk::MenuBar* createMenuBar();
            /**
             * Create the toolbar of the window.
             *
             * @return The toolbar that is added to the window.
             */
            Gtk::Toolbar* createToolBar();
            /**
             * Create the main notebook of the window.
             */
            void createNotebook();

    };

}
