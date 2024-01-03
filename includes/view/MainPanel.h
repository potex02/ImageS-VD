/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include <gtkmm/box.h>
#include <gtkmm/label.h>
#include <gtkmm/adjustment.h>
#include <gtkmm/scale.h>

namespace view {

    /**
     * The main panel of the application used as a page of the window's notebook.
     */
    class MainPanel : public Gtk::Box {

        public:
            /**
             * Create a MainPanel.
             */
            MainPanel();
        private:
            /**
             * Thw widget used to set the singular values threshold.
             */
            Gtk::Scale *scale;

    };

}
