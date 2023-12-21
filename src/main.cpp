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

int main(int argc, char **argv) {

    double k;
    auto app = Application::create(argc, argv, "potex02.images-vd");
    MainWindow window;

    if(argc < 4) {

        app->run(window);
        return 1;

    }
    try {

        k = atof(argv[3]);
        Compressor compressor = Compressor(argv[1]);
        if(Compressor::isImage(argv[2])) {

            compressor.compose(k);
            compressor.saveImage(argv[2]);
            return 0;

        }
        if(Compressor::isFile(argv[2])) {

            compressor.saveChannels(argv[2]);
            return 0;

        }
        throw new std::invalid_argument("unknown extension for output file");

    } catch(exception e) {

        cout << e.what() << endl;

    }
    return 0;

}
