/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include "MainPanel.h"

view::MainPanel::MainPanel(): Gtk::Box(Gtk::ORIENTATION_VERTICAL) {

    Glib::RefPtr<Gtk::Adjustment> adjustment = Gtk::Adjustment::create(0, 0, 10);
    Gtk::Label *label = Gtk::make_managed<Gtk::Label>("Ciao");

    this->scale = Gtk::make_managed<Gtk::Scale>(adjustment);
    this->pack_start(*this->scale, Gtk::PACK_SHRINK);
    this->pack_start(*label);

}
