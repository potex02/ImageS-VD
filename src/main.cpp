#include <iostream>
#include <stdexcept>
#include <opencv2/opencv.hpp>
#include "Compresser.h"

using namespace std;
using namespace cv;

int main(int argc, char **argv) {

    double k;

    if(argc < 4) {

        cout << "Error. Bad arguments" << endl;
        return 1;

    }
    try {

        k = atof(argv[3]);
        Compresser compresser = Compresser(argv[1]);
        if(Compresser::isImage(argv[2])) {

            compresser.compose(k);
            compresser.saveImage(argv[2]);
            return 0;

        }
        if(Compresser::isFile(argv[2])) {

            compresser.saveChannels(argv[2]);
            return 0;

        }
        throw new std::invalid_argument("unknown extension for output file");

    } catch(exception e) {

        cout << e.what() << endl;

    }
    return 0;

}
