/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include <iostream>
#include <vector>
#include <gtkmm.h>

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
             * Delete all widget pointers stored in the widgets vector.
             */
            ~MainWindow();
            /**
             * Add the widgets to the window and show it.
             *
             * @param app is the app used to run the window.
             */
            void run(Glib::RefPtr<Gtk::Application> &app);
        private:
            /**
             * The vector af all widget pointers in order to delete them in the destructor.
             */
            std::vector<Gtk::Widget*> widgets;
            /**
             * Create the menubar of the window.
             *
             * @return the menubar of the window.
             */
            Gtk::MenuBar createMenuBar();

    };

}
