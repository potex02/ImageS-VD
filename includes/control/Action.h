/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#pragma once
#include <vector>
#include <functional>
#include <gtkmm/widget.h>
#include <gtkmm/button.h>
#include <gtkmm/menuitem.h>
#include <gtkmm/toolbutton.h>
#include <gtkmm/stock.h>

namespace control {

    /**
     * Contains the code to execute one action in the app and manage the widget's behaviour.
     */
    class Action {

        public:
            /**
             * Create an Action.
             *
             * @param _fun is the code executed by the action.
             */
            Action(const std::function<void()>& _fun, const Glib::ustring& _text, const Glib::ustring& _tooltip, Gtk::BuiltinStockID _image, bool _sensitive = true);
            /**
             * Register a widget to the action.
             *
             * @param widget is the widget to be registered.
             */
            void registerWidget(Gtk::Widget *widget);
        private:
            /**
             * The code executed by the action.
             */
            std::function<void()> fun;
            /**
             * The text of the action.
             */
            Glib::ustring text;
            /**
             * The tooltip of the action.
             */
            Glib::ustring tooltip;
            /**
             * The image of the action in the toolbar.
             */
            Gtk::BuiltinStockID image;
            /**
             * Check if the action can be executed.
             */
            bool sensitive;
            /**
             * The vector of the wigets associated with the action.
             */
            std::vector<Gtk::Widget*> widgets;

    };

}
