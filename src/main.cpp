/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include <iostream>
#include <stdexcept>
#include <gtkmm.h>
#include <opencv2/opencv.hpp>
#include "MainWindow.h"
#include "Compressor.h"

using namespace std;
using namespace Gtk;
using namespace cv;
using namespace model;
using namespace view;

bool isCliUsage(vector<string> args);
bool validAruments(vector<string> args);
void cliUsage(vector<string> args);

int main(int argc, char **argv) {

    std::vector<std::string> arguments(argv + 1, argv + argc);
    auto app = Application::create(argc, argv, "potex02.images-vd");
    MainWindow window;

    if(isCliUsage(arguments)) {

        arguments.erase(arguments.begin());
        if(!validAruments(arguments)) {

            cerr << "Bad arguments" << endl;
            return 1;

        }
        cliUsage(arguments);
        return 0;

    }
    app->run(window);
    return 0;

}
bool isCliUsage(vector<string> args) {

    return !args.empty() && args[0] == "--cli";

}
bool validAruments(vector<string> args) {

    if(args.size() < 2 || !Compressor::isValid(args[0]) || !Compressor::isValid(args[1])) {

        return false;

    }
    if(Compressor::isFile(args[1])) {

        return true;

    }
    return args.size() >= 3;

}
void cliUsage(vector<string> args) {

    try {

        Compressor compressor = Compressor(args[0]);

        if(Compressor::isImage(args[1])) {

            double k = stod(args[2]);

            compressor.compose(k);
            compressor.saveImage(args[1]);
            return;

        }
        if(Compressor::isFile(args[1])) {

            compressor.saveChannels(args[1]);
            return;

        }
        throw new std::invalid_argument("unknown extension for output file");

    } catch(exception e) {

        cout << e.what() << endl;

    }

}
