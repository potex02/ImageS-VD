/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
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

    };

}
