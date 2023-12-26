/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include <gtkmm.h>

class MainWindow : public Gtk::Window {

    public:
        MainWindow() {
            this->set_title("ImageS-VD");
            this->set_default_size(400, 200);
        }

};
