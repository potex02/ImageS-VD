/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include "MainPanel.h"

view::MainPanel::MainPanel() {

    Gtk::Label *label = Gtk::make_managed<Gtk::Label>("ImageS-VD");

    this->pack_start(*label);

}
