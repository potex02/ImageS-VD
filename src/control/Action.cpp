/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include "Action.h"

control::Action::Action(const std::function<void()>& _fun, const Glib::ustring& _text, const Glib::ustring& _tooltip, Gtk::BuiltinStockID _image, bool _sensitive): fun(_fun), text(_text), tooltip(_tooltip), image(_image), sensitive(_sensitive) {}
void control::Action::registerWidget(Gtk::Widget *widget) {

    if(Gtk::Button *button = dynamic_cast<Gtk::Button*>(widget); button) {

        button->set_label(this->text);
        button->signal_activate().connect(this->fun);

    }
    if(Gtk::MenuItem *menuItem = dynamic_cast<Gtk::MenuItem*>(widget); menuItem) {

        menuItem->set_label(this->text);
        menuItem->signal_activate().connect(this->fun);

    }
    if(Gtk::ToolButton *toolButton = dynamic_cast<Gtk::ToolButton*>(widget); toolButton) {

        toolButton->set_stock_id(this->image);
        toolButton->signal_clicked().connect(this->fun);

    }
    widget->set_tooltip_text(this->tooltip);
    widget->set_sensitive(this->sensitive);
    this->widgets.emplace_back(widget);

}
