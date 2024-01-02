/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include <iostream>
#include <gtkmm.h>
#include "MainPanel.h"

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
             * Add the widgets to the window and show it.
             *
             * @param app is the app used to run the window.
             */
            void run(Glib::RefPtr<Gtk::Application> &app);
        private:
            /**
             * Create the menubar of the window.
             *
             * @return The menubar that is added to the window.
             */
            Gtk::MenuBar* createMenuBar();
            /**
             * Create the main notebook of the window.
             *
             * @return The notebook that is added to the window.
             */
            Gtk::Notebook* createNotebook();

    };

}
