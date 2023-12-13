#include <iostream>
#include <opencv2/opencv.hpp>
#include <nlohmann/json.hpp>
#include "compresser.h"

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
        compresser.compose(k);
        compresser.saveImage(argv[2]);

    } catch(exception e) {

        cout << e.what() << endl;

    }

    return 0;

}
